# Wav to Video Spectrogram

## Overview

This Python project includes a set of scripts to convert audio files into videos that display a spectrogram of the audio. The process involves trimming and converting audio files if needed and generating a video with a spectrogram using `numpy`, `matplotlib`, and `wave`. The resulting video is created using `FFmpeg` for better integration and output.

## Features

- **Spectrogram Visualization**: Generates a visual representation of the audio's frequency spectrum over time.
- **Video Creation**: Converts the spectrogram into an MP4 video file.
- **Customizable Frame Rate**: Allows you to set the frames per second (FPS) for the video.
- **Audio Conversion and Trimming**: Includes tools to convert MP3 files to WAV and trim audio files.

## Prerequisites

Before running the scripts, make sure you have the following installed:

- **Python 3.x**: The scripts are compatible with Python 3.
- **Required Python Libraries**:
  - `numpy`
  - `matplotlib`
  - `wave`
  - `pydub`

- **FFmpeg**: Ensure `ffmpeg` is installed on your system. It is used to handle video encoding.

You can install the required Python libraries using pip:

```bash
pip install numpy matplotlib pydub
```

## Usage
1. Trim and Amplify Audio
Use the audio_trimmer.py script to trim and amplify your audio. This is useful if you want to generate the spectrogram for a specific portion of the original audio.

```bash
python audio_trimmer.py
```
Update the file paths and parameters in audio_trimmer.py as needed. For example, it trims the audio file to 3 seconds starting at the 3-second mark and saves it.

2. Convert MP3 to WAV
If your audio file is in MP3 format, use the mp3ToWav.py script to convert it to WAV format.

```bash
python mp3ToWav.py
```
Update the file paths in mp3ToWav.py to match your input MP3 file and desired output WAV file.

3. Generate Spectrogram Video
Once you have your WAV file ready, use the vidwav.py script to generate a video of the spectrogram.

```bash
python vidwav.py
```
Ensure the vidwav.py script references your WAV file correctly. The script will generate an MP4 video with the spectrogram visualization.

## Contributing
If you would like to contribute to this project, please fork the repository and submit a pull request with your changes.

## Contact

For any questions or issues, you can reach out to [Moharira25](https://github.com/Moharira25).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
