from dataclasses import dataclass
from theory.scales import Note, NoteNames, OctavesScientific
from typing import List
from enum import Enum


class ChordVersion(Enum):
    STANDARD = 0


@dataclass()
class Chord:
    name: str
    version: ChordVersion = ChordVersion.STANDARD
    notes: List[Note] or None = None

    def __post_init__(self):
        if self.notes is not None:
            return
        if self.name.lower() == 'C Major'.lower():
            if self.version == ChordVersion.STANDARD:
                self.notes = [
                    Note(name=NoteNames.C, degree=None, octave=OctavesScientific.FOUR),
                    Note(name=NoteNames.E, degree=None, octave=OctavesScientific.FOUR),
                    Note(name=NoteNames.G, degree=None, octave=OctavesScientific.FOUR),
                ]
