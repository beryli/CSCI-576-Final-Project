# This is an example of converting .rgb video file to .avi file
import sys
import video

if len(sys.argv) < 4:
    print("Missing Arguments", file=sys.stderr)
    print("Sample Usage:", file=sys.stderr)
    print("\t$ python %s <input-video> <input-audio> <output-video>" % (sys.argv[0]), file=sys.stderr)
    sys.exit()

[v_in, a_in, v_out] = sys.argv[1:4]
video.rgb2avi(v_in, a_in, v_out)