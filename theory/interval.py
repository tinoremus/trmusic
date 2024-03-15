from enum import Enum
from theory.scaledegree import ScaleDegree


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
