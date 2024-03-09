from dataclasses import dataclass
from enum import Enum
from typing import List


class OctavesScientific(Enum):
    MINUS_ONE = -1
    ZERO = 0
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9


@dataclass()
class NoteDetails:
    name: str
    short: str
    interval: int


class NoteNames(Enum):
    C: NoteDetails = NoteDetails(name='C major', short='C', interval=0)
    Cs: NoteDetails = NoteDetails(name='C sharp', short='C#', interval=1)
    Df: NoteDetails = NoteDetails(name='D flat', short='Db', interval=1)
    D: NoteDetails = NoteDetails(name='D major', short='D', interval=2)
    Ds: NoteDetails = NoteDetails(name='D sharp', short='D#', interval=3)
    Ef: NoteDetails = NoteDetails(name='E flat', short='Eb', interval=3)
    E: NoteDetails = NoteDetails(name='E major', short='E', interval=4)
    F: NoteDetails = NoteDetails(name='F major', short='F', interval=5)
    Fs: NoteDetails = NoteDetails(name='F sharp', short='F#', interval=6)
    Gf: NoteDetails = NoteDetails(name='G flat', short='Gb', interval=6)
    G: NoteDetails = NoteDetails(name='G major', short='G', interval=7)
    Gs: NoteDetails = NoteDetails(name='G sharp', short='C#', interval=8)
    Af: NoteDetails = NoteDetails(name='A flat', short='Ab', interval=8)
    A: NoteDetails = NoteDetails(name='A major', short='A', interval=9)
    As: NoteDetails = NoteDetails(name='A sharp', short='A#', interval=10)
    Bf: NoteDetails = NoteDetails(name='B flat', short='Bb', interval=10)
    B: NoteDetails = NoteDetails(name='B major', short='B', interval=11)

    @classmethod
    def by_interval(cls, interval: int):
        selection = [_n for _n in cls if _n.value.interval == interval]
        return selection[0] if selection else None

    @classmethod
    def use_alternative_name(cls, orig):
        selection = [_n for _n in cls if _n.value.interval == orig.value.interval]
        other = [_n for _n in selection if _n != orig]
        return other[0] if other else orig


class ScaleDegree(Enum):
    TONIC = 1
    SUPERTONIC = 2
    MEDIANT = 3
    SUBDOMINANT = 4
    DOMINANT = 5
    SUBMEDIANT = 6
    SUBTONIC = 7
    LEADING_TONE = 7
    TONIC_OCTAVE = 8


class Interval(Enum):
    HALF = 1
    WHOLE = 2

    @classmethod
    def major(cls):
        steps = [
            Interval.WHOLE,
            Interval.WHOLE,
            Interval.HALF,
            Interval.WHOLE,
            Interval.WHOLE,
            Interval.WHOLE,
            Interval.HALF
        ]
        degrees = [
            # ScaleDegree.TONIC,
            ScaleDegree.SUPERTONIC,
            ScaleDegree.MEDIANT,
            ScaleDegree.SUBDOMINANT,
            ScaleDegree.DOMINANT,
            ScaleDegree.SUBMEDIANT,
            ScaleDegree.LEADING_TONE,
            ScaleDegree.TONIC_OCTAVE,
        ]
        return steps, degrees

    @classmethod
    def minor(cls):
        """whole, half, whole, whole, half, whole, whole"""
        steps = [
            Interval.WHOLE,
            Interval.HALF,
            Interval.WHOLE,
            Interval.WHOLE,
            Interval.HALF,
            Interval.WHOLE,
            Interval.WHOLE
        ]
        degrees = [
            # ScaleDegree.TONIC,
            ScaleDegree.SUPERTONIC,
            ScaleDegree.MEDIANT,
            ScaleDegree.SUBDOMINANT,
            ScaleDegree.DOMINANT,
            ScaleDegree.SUBMEDIANT,
            ScaleDegree.SUBTONIC,
            ScaleDegree.TONIC_OCTAVE,
        ]
        return steps, degrees


@dataclass()
class Note:
    name: NoteNames
    degree: ScaleDegree or None
    octave: OctavesScientific or None

    def up_half_tones(self, half_tones: int):
        nc = max([_n.value.interval for _n in NoteNames]) + 1
        offset = int((self.name.value.interval + half_tones) / nc)
        half_tones = half_tones - nc * offset

        new_octave = self.octave
        if new_octave is not None:
            if offset:
                if offset + self.octave.value > OctavesScientific.NINE.value:
                    new_octave = None
                else:
                    new_octave = OctavesScientific(self.octave.value + offset)
        name = NoteNames.by_interval(self.name.value.interval + half_tones)
        note = Note(name=name, degree=None, octave=new_octave)
        return note

    def up_steps(self, steps: List[Interval], degree: ScaleDegree):
        if steps:
            half_tones = sum([1 if step == Interval.HALF else 2 for step in steps])
            note = self.up_half_tones(half_tones=half_tones)
            note.degree = degree
        else:
            note = self
        return note

    def __str__(self) -> str:
        return '{}{}'.format(self.name.name, '' if self.octave is None else self.octave.value)

    @property
    def info(self) -> str:
        info = '{:>2}{:<3} - {}'.format(
            self.name.value.short,
            '' if self.octave is None else self.octave.value,
            '' if self.degree is None else self.degree.name
        )
        return info


@dataclass()
class Scale:
    name: str
    root: Note
    steps: List[Interval]
    degrees: List[ScaleDegree] or None

    @property
    def notes(self) -> List[Note]:
        _notes = self.__build_scale_notes__(root=self.root, steps=self.steps, degrees=self.degrees)
        return _notes

    @staticmethod
    def __build_scale_notes__(root: Note, steps: List[Interval], degrees: List[ScaleDegree]) -> List[Note]:
        notes = list()
        notes.append(root)
        _names = list()
        for i in range(len(steps)):
            note = root.up_steps(steps=steps[:i + 1], degree=degrees[i] if degrees is not None else None)
            if note.degree is not None:
                note.degree = ScaleDegree.TONIC if degrees[i] == ScaleDegree.TONIC_OCTAVE else note.degree
            if note.name.name[0] in _names:
                note.name = NoteNames.use_alternative_name(note.name)
            notes.append(note)
            _names.append(note.name.name[0])
        return notes

    @classmethod
    def major_scale(cls, root: Note):
        steps, degrees = Interval.major()
        return Scale(name='{} Major'.format(root.name.name), root=root, steps=steps, degrees=degrees)

    @classmethod
    def minor_scale(cls, root: Note):
        steps, degrees = Interval.minor()
        return Scale(name='{} Minor'.format(root.name.name), root=root, steps=steps, degrees=degrees)

    def __str__(self) -> str:
        return 'Scale(name={}, notes={})'.format(self.name, [str(note) for note in self.notes])

    def show(self, cmd_output: bool = True) -> None or List[str]:
        print_string = '{:20}: {}'

        info = list()
        info.append(print_string.format('Name', self.name))
        info.append(print_string.format('Steps', [step.name for step in self.steps if step is not None]))
        info.append('Notes:')
        for note in self.notes:
            info.append('  {}'.format(note.info))
        info.append('')

        if cmd_output:
            for line in info:
                print(line)
        else:
            return info


if __name__ == '__main__':
    root_note = Note(name=NoteNames.C, octave=OctavesScientific.FOUR, degree=ScaleDegree.TONIC)
    Scale.major_scale(root=root_note).show(True)
    Scale.minor_scale(root=root_note).show(True)
