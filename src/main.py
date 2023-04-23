# This is an example of converting .rgb video to .avi file and .wav audio to .mp3 file
import sys
import converter

if len(sys.argv) < 5:
    print("Missing Arguments", file=sys.stderr)
    print("Sample Usage:", file=sys.stderr)
    print("\t$ python %s <input-video> <output-video> <input-audio> <output-audio>" % (sys.argv[0]), file=sys.stderr)
    sys.exit()

[v_in, v_out, a_in, a_out] = sys.argv[1:5]
converter.rgb2avi(v_in, v_out)
converter.wav2mp3(a_in, a_out)
