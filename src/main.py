import argparse
import converter
from video import analyze_video

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-vi', '--input-video',
                        required=True, help='input video filename (.rgb)', dest='v_in')
    parser.add_argument('-ai', '--input-audio',
                        required=True, help='input audio filename (.wav)', dest='a_in')
    parser.add_argument('-vo', '--output-video',
                        default='output.avi', help='output video filename (.avi)', dest='v_out')
    parser.add_argument('-ao', '--output-audio',
                        default='output.mp3', help='output audio filename (.mp3)', dest='a_out')
    parser.add_argument('-nc', '--no-conversion',
                        action='store_true', help='disable video & audio conversion', dest='no_conversion')
    parser.add_argument('-nvc', '--no-video-conversion',
                        action='store_true', help='disable video conversion', dest='no_video_conversion')
    parser.add_argument('-nac', '--no-audio-conversion',
                        action='store_true', help='disable audio conversion', dest='no_audio_conversion')
    args = parser.parse_args()

    conversion_enabled = not args.no_conversion
    video_conversion_enabled = not args.no_video_conversion
    audio_conversion_enabled = not args.no_audio_conversion

    if conversion_enabled:
        if video_conversion_enabled:
            converter.rgb2avi(args.v_in, args.v_out)
        if audio_conversion_enabled:
            converter.wav2mp3(args.a_in, args.a_out)
    
    frames = analyze_video(args.v_out)
    print("[Frames]")
    print(frames)
