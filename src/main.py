""" main execution file """

from utils import parse_args
from audio_segment import AudioSegmentAnalyzer


def main():
    """
    main loop
    """
    args = parse_args()

    if args.verbose:
        print(args)

    asa = AudioSegmentAnalyzer(args.file)
    asa.print_attributes()


if __name__ == "__main__":
    main()
