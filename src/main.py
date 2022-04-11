from pydub import AudioSegment
from utils import print_attributes, parse_args, load_file

args = parse_args()

if args.verbose:
    print(args)

audio_segment = load_file(args.file)
print_attributes(audio_segment)
