import subprocess

def rgb2avi(f_in, f_audio, f_out = 'OutputVideo.avi', fps_in = 30, fps_out = 30, w_in = 480, h_in = 270, w_out = 480, h_out = 270):
    cmd = "ffmpeg -f rawvideo -pix_fmt rgb24 -s:v {0}x{1} -r {2} -i {3} -i {4} -s:v {5}x{6} -r {7} -c:v rawvideo -pix_fmt yuv420p -c:a copy {8}".format(
        w_in, h_in, fps_in, f_in, f_audio, w_out, h_out, fps_out, f_out
    )
    subprocess.call(cmd)