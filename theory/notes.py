from dataclasses import dataclass
from enum import Enum
from theory.scaledegree import ScaleDegree
from theory.interval import Interval
from theory.octaves import OctavesScientific
from typing import List



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

