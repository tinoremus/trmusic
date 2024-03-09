from dataclasses import dataclass
from theory.scales import Note, NoteNames, OctavesScientific


@dataclass()
class GuitarString:
    root: Note


if __name__ == '__main__':
    root_note = Note(name=NoteNames.C, octave=OctavesScientific.FOUR, degree=None)
    s = GuitarString(root=root_note)
    

