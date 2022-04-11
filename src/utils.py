from pydub import AudioSegment
import argparse


def parse_args():
    """
    Parses args

    Parameters: void
    Returns: args
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", action="store_true", help="Verbose Output")
    parser.add_argument('--source',
                    dest='sources',
                    help='sources',
                    type=int,
                    nargs='+'
                    )

    return parser.parse_args()


def print_attributes(audio_segment):
    """
    Print a recap of attribute for the given audio.

    Parameters: an AudioSegment
    Return: void
    """
    print(f"Channels: {audio_segment.channels}")
    print(f"Sample width: {audio_segment.sample_width}")
    print(f"Frame rate (sample rate): {audio_segment.frame_rate}")
    print(f"Frame width: {audio_segment.frame_width}")
    print(f"Length (ms): {len(audio_segment)}")
    print(f"Frame count: {audio_segment.frame_count()}")
    print(f"Intensity: {audio_segment.dBFS}")
