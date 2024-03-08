from dataclasses import dataclass
from guitar.notes import Note


@dataclass()
class GuitarString:
    root: Note

    def note_at_fret(self, fret: int) -> Note:
        nc = max([_n.value for _n in Note]) + 1
        offset = int((self.root.value + fret) / nc)
        pos = self.root.value + fret - nc * offset
        note = [_n for _n in Note if _n.value == pos].pop()
        return note


if __name__ == '__main__':
    s = GuitarString(root=Note.E)
    for i in range(20):
        n = s.note_at_fret(i)
        print(i, n)

