import numpy as np
import matplotlib.pyplot as plt
import wave
import matplotlib.animation as manimation
from matplotlib.ticker import FuncFormatter


def kilo(x, pos):
    return '%1.fk' % (x * 1e-3)


def vidwav(wavfile, fps=25):
    FFMpegWriter = manimation.writers['ffmpeg']
    metadata = dict(title='Wav Spectrogram', artist='Matplotlib', comment='')
    writer = FFMpegWriter(fps=fps, metadata=metadata, bitrate=3500)

    wf = wave.open(wavfile, 'rb')
    fs = wf.getframerate()
    N = wf.getnframes()
    duration = N / float(fs)
    bytes_per_sample = wf.getsampwidth()
    bits_per_sample = bytes_per_sample * 8
    dtype = f'int{bits_per_sample}'
    channels = wf.getnchannels()

    audio = np.frombuffer(wf.readframes(int(duration * fs * bytes_per_sample / channels)), dtype=dtype)
    audio.shape = (int(audio.shape[0] / channels), channels)
    times = np.arange(audio.shape[0]) / float(fs)
    freqs = np.fft.fftfreq(audio[:, 0].shape[0], 1.0 / fs) / 1000.0
    max_freq_kHz = freqs.max()

    # Create a single figure for the spectrogram
    fig, ax = plt.subplots(figsize=(8, 4), facecolor='black')

    # Create the spectrogram (full figure)
    ax.specgram(audio[:, 0], Fs=fs, cmap='viridis')  # Adjust the cmap to your desired colormap
    ax.set_xlim(0, duration)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_facecolor('black')

    # Customize y-axis (frequency) labels
    formatter = FuncFormatter(kilo)
    ax.yaxis.set_major_formatter(formatter)
    ax.tick_params(axis='y', colors='white')

    # Customize the progress line to be white
    l2, = ax.plot([], [], color='white', lw=2)

    x = np.array([0., 0.])
    y1 = np.array([0, max_freq_kHz * 1000.0])

    with writer.saving(fig, "temp.mp4", 100):
        for i in range((int(duration) + 1) * fps):
            x += 1.0 / float(fps)
            l2.set_data(x, y1)
            writer.grab_frame()

    import os
    os.system(f'ffmpeg -y -i "{wavfile}" -i temp.mp4 -c:v copy -strict -2 "{wavfile.split(".")[0]}.mp4"')
    os.remove("temp.mp4")


def main():
    vidwav("t_Robin - 5.wav")


if __name__ == "__main__":
    main()
