"""
Class wrapper around pydub
"""
from pydub import AudioSegment


class AudioSegmentAnalyzer:
    """
    This class is a wrapper around pydub AudioSegment
    """

    def __init__(self, filename):
        self.filename = filename
        self.audio_segment = self.load_file(filename)

    @staticmethod
    def load_file(filename):
        """
        Load file into an AudioSegment

        Parameters: a filename
        Return: an AudioSegment
        """
        print(f"Loading file: {filename}")
        audio_segment = AudioSegment.from_file(filename)
        return audio_segment

    def print_attributes(self):
        """
        Print a recap of attribute for the given audio.

        Parameters: an AudioSegment
        Return: void
        """
        audio_segment = self.audio_segment

        print(f"Filename: {self.filename}")
        print(f"Channels: {audio_segment.channels}")
        print(f"Sample width: {audio_segment.sample_width}")
        print(f"Frame rate (sample rate): {audio_segment.frame_rate}")
        print(f"Frame width: {audio_segment.frame_width}")
        print(f"Length (ms): {len(audio_segment)}")
        print(f"Frame count: {audio_segment.frame_count()}")
        print(f"Intensity: {audio_segment.dBFS}")
        print(f"Max Intensity: {audio_segment.max_dBFS}")
        print(f"Max possible amplitude: {audio_segment.max_possible_amplitude}")
        print(f"Rms: {audio_segment.rms}")
