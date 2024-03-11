from dataclasses import dataclass
from typing import List
from theory.scales import Note, NoteNames, OctavesScientific
from theory.scales import Interval, Scale


@dataclass()
class GuitarString:
    root: Note
    intervals: List[Interval] or None = None

    @property
    def notes(self) -> List[Note]:
        s = Scale(name='Sting 1', root=self.root, steps=self.intervals, degrees=None)
        return s.notes


if __name__ == '__main__':
    root_note = Note(name=NoteNames.C, octave=OctavesScientific.FOUR, degree=None)
    s = GuitarString(root=root_note)
    

