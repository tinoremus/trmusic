from dataclasses import dataclass
from guitar.guitarstring import GuitarString
from theory.scales import Note, NoteNames, OctavesScientific, Interval, Scale
from theory.chord import Chord
from typing import List


@dataclass()
class FretBoard6String:
    name: str
    strings: List[GuitarString]
    frets: int

    @property
    def intervals(self) -> List[Interval]:
        return self.frets * [Interval.HALF]

    def __post_init__(self):
        for string in self.strings:
            string.intervals = self.intervals

    def get_layout(self, note_filter: List[Note] or None = None) -> List[str]:
        if not self.strings:
            return []
        layout = []
        for string in self.strings[::-1]:
            if note_filter is None:
                names = [note.name.value.short for note in string.notes]
            else:
                names = [note.name.value.short if note.name in [n.name for n in note_filter]
                         else '' for note in string.notes]
            layout.append('| '.join(['{:3}'.format(name) for name in names]))
        layout.insert(0, '-' * len(layout[0]))
        layout.insert(0, '| '.join(['{:<3}'.format(f) for f in range(self.frets + 1)]))
        layout.append('-' * len(layout[1]))
        return layout

    def show_layout(self, cmd_output: True, chord: Chord or None = None):
        layout = self.get_layout(note_filter=chord.notes if chord is not None else None)
        if cmd_output:
            for line in layout:
                print(line)
        else:
            return layout

    def show(self, cmd_output: True):
        print_string = '{:20}: {}'

        info = list()
        info.append(print_string.format('Name', self.name))
        info.append(print_string.format('Frets', self.frets))
        info.append('')

        if cmd_output:
            for line in info:
                print(line)
        else:
            return info


if __name__ == '__main__':
    fb16 = FretBoard6String(
        name='6 String Std. Fretboard 16 frets',
        strings=[
            GuitarString(root=Note(name=NoteNames.E, octave=OctavesScientific.FOUR, degree=None)),
            GuitarString(root=Note(name=NoteNames.A, octave=OctavesScientific.FOUR, degree=None)),
            GuitarString(root=Note(name=NoteNames.D, octave=OctavesScientific.FOUR, degree=None)),
            GuitarString(root=Note(name=NoteNames.G, octave=OctavesScientific.FOUR, degree=None)),
            GuitarString(root=Note(name=NoteNames.B, octave=OctavesScientific.FOUR, degree=None)),
            GuitarString(root=Note(name=NoteNames.E, octave=OctavesScientific.FOUR, degree=None)),
        ],
        frets=16
    )
    fb16.show(True)
    test_chord = Chord(name='C Major')
    fb16.show_layout(True, chord=test_chord)
    # c_major = Chord(name='C Major')
    # fb16.print_chord(chord=c_major)
