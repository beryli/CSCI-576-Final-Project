import sys
import converter
from frame import Frametype
from video import analyze_video

if __name__ == '__main__':
    if len(sys.argv) < 5:
        print("Missing Arguments", file=sys.stderr)
        print("Sample Usage:", file=sys.stderr)
        print(
            "\t$ python %s <input-video>.rgb <output-video>.avi <input-audio>.wav <output-audio>.mp3"
            % (sys.argv[0]), file=sys.stderr
        )
        sys.exit()

    [v_in, v_out, a_in, a_out] = sys.argv[1:5]
    converter.rgb2avi(v_in, v_out)
    converter.wav2mp3(a_in, a_out)
    
    frames = analyze_video(v_out)
    print("[Frames]")
    print(frames)
