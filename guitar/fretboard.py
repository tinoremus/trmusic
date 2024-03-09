from dataclasses import dataclass
from guitar.guitarstring import GuitarString
from theory.scales import Note, NoteNames, OctavesScientific, Interval, Scale
from theory.chord import Chord
from typing import List


@dataclass()
class FretBoard6String:
    name: str
    string1: GuitarString
    string2: GuitarString
    string3: GuitarString
    string4: GuitarString
    string5: GuitarString
    string6: GuitarString
    frets: int

    @property
    def intervals(self) -> List[Interval]:
        return (self.frets + 1) * [Interval.HALF]

    @property
    def layout(self) -> List[str]:
        s1 = Scale(name='Sting 1', root=self.string1.root, steps=self.intervals, degrees=None)
        s2 = Scale(name='Sting 2', root=self.string2.root, steps=self.intervals, degrees=None)
        s3 = Scale(name='Sting 3', root=self.string3.root, steps=self.intervals, degrees=None)
        s4 = Scale(name='Sting 4', root=self.string4.root, steps=self.intervals, degrees=None)
        s5 = Scale(name='Sting 5', root=self.string5.root, steps=self.intervals, degrees=None)
        s6 = Scale(name='Sting 6', root=self.string6.root, steps=self.intervals, degrees=None)

        layout = list()
        for f, n1, n2, n3, n4, n5, n6 in (
                zip(range(self.frets + 1), s1.notes, s2.notes, s3.notes, s4.notes, s5.notes, s6.notes)):
            line = '{:>3}    {:<2}  {:<2}  {:<2}  {:<2}  {:<2}  {:<2}  '.format(
                f,
                n1.name.value.short,
                n2.name.value.short,
                n3.name.value.short,
                n4.name.value.short,
                n5.name.value.short,
                n6.name.value.short)
            layout.append(line)
            if f == 0:
                layout.append('       ' + '=' * 22)
            else:
                layout.append('       |   |   |   |   |   |   ')
        return layout

    def show_layout(self, cmd_output: True, chord: Chord or None = None):
        if cmd_output:
            for line in self.layout:
                print(line)
        else:
            return self.layout

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
        string1=GuitarString(root=Note(name=NoteNames.E, octave=OctavesScientific.FOUR, degree=None)),
        string2=GuitarString(root=Note(name=NoteNames.A, octave=OctavesScientific.FOUR, degree=None)),
        string3=GuitarString(root=Note(name=NoteNames.D, octave=OctavesScientific.FOUR, degree=None)),
        string4=GuitarString(root=Note(name=NoteNames.G, octave=OctavesScientific.FOUR, degree=None)),
        string5=GuitarString(root=Note(name=NoteNames.B, octave=OctavesScientific.FOUR, degree=None)),
        string6=GuitarString(root=Note(name=NoteNames.E, octave=OctavesScientific.FOUR, degree=None)),
        frets=16
    )
    fb16.show(True)
    lo = fb16.layout
    test_chord = Chord(name='C Major')
    fb16.show_layout(True, chord=test_chord)
    # c_major = Chord(name='C Major')
    # fb16.print_chord(chord=c_major)
