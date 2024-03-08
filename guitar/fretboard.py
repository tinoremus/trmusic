from dataclasses import dataclass
from guitar.guitarstring import GuitarString
from guitar.notes import Note
from guitar.chord import Chord


@dataclass()
class FretBoard6String:
    string1: GuitarString
    string2: GuitarString
    string3: GuitarString
    string4: GuitarString
    string5: GuitarString
    string6: GuitarString
    frets: int

    def print(self, cmd_output=True):
        fret_board = list()
        fret_board.append('   ===========================')
        for f in range(self.frets + 1):
            line = '{:>2} | {:3} {:3} {:3} {:3} {:3} {:3} |'.format(
                f,
                self.string1.note_at_fret(f).name,
                self.string2.note_at_fret(f).name,
                self.string3.note_at_fret(f).name,
                self.string4.note_at_fret(f).name,
                self.string5.note_at_fret(f).name,
                self.string6.note_at_fret(f).name,
            )
            fret_board.append(line)
            # fret_board.append('   |  |   |   |   |   |   |  |')

        if cmd_output:
            for line in fret_board:
                print(line)
        else:
            return fret_board

    def print_chord(self, chord: Chord, cmd_output=True):
        fret_board = list()
        fret_board.append('Chord: {}'.format(chord))
        fret_board.append('   ===========================')
        for f in range(self.frets + 1):
            line = '{:>2} | {:3} {:3} {:3} {:3} {:3} {:3} |'.format(
                f,
                self.string1.note_at_fret(f).name if self.string1.note_at_fret(f) in chord.notes else '',
                self.string2.note_at_fret(f).name if self.string2.note_at_fret(f) in chord.notes else '',
                self.string3.note_at_fret(f).name if self.string3.note_at_fret(f) in chord.notes else '',
                self.string4.note_at_fret(f).name if self.string4.note_at_fret(f) in chord.notes else '',
                self.string5.note_at_fret(f).name if self.string5.note_at_fret(f) in chord.notes else '',
                self.string6.note_at_fret(f).name if self.string6.note_at_fret(f) in chord.notes else '',
            )
            fret_board.append(line)
            # fret_board.append('   |  |   |   |   |   |   |  |')

        if cmd_output:
            for line in fret_board:
                print(line)
        else:
            return fret_board


if __name__ == '__main__':
    fb16 = FretBoard6String(
        string1=GuitarString(root=Note.E),
        string2=GuitarString(root=Note.A),
        string3=GuitarString(root=Note.D),
        string4=GuitarString(root=Note.G),
        string5=GuitarString(root=Note.B),
        string6=GuitarString(root=Note.E),
        frets=12
    )
    test_chord = Chord(name='Test', notes=[Note.E, Note.A, Note.G])
    c_major = Chord(name='C Major')
    fb16.print_chord(chord=c_major)
