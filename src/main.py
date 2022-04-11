from pydub import AudioSegment
import os.path
from utils import print_attributes, parse_args

args = parse_args()

print(args)
# load file
dirname = os.path.dirname(__file__)
samples_path = os.path.join(dirname, "../samples")

audio_segment = AudioSegment.from_file(os.path.join(samples_path, "kam_001.aac"))
print_attributes(audio_segment)
