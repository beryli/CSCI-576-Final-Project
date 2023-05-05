import subprocess

# Video
def rgb2avi(f_in, f_out, fps_in = 30, fps_out = 30, w_in = 480, h_in = 270, w_out = 480, h_out = 270):
    cmd = "ffmpeg -f rawvideo -pix_fmt rgb24 -s:v {0}x{1} -r {2} -i {3} -s:v {4}x{5} -r {6} -c:v rawvideo -pix_fmt yuv420p {7}".format(
        w_in, h_in, fps_in, f_in, w_out, h_out, fps_out, f_out
    )
    subprocess.call(cmd)

# Audio
def wav2mp3(f_in, f_out, sampling_freq = 44100, channel = 2, bit_rate = "192k"):
    cmd = "ffmpeg -i %s -vn -ar %d -ac %d -b:a %s %s" % (
        f_in, sampling_freq, channel, bit_rate, f_out
    )
    subprocess.run(cmd)
