from dataclasses import dataclass
from typing import List
from theory.notes import Note, NoteNames
from theory.interval import Interval
from theory.scaledegree import ScaleDegree
from theory.octaves import OctavesScientific


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
