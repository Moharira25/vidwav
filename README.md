# Wav to Video Spectrogram

## Overview

This Python script converts a WAV audio file into a video that displays a spectrogram of the audio. It uses `numpy`, `matplotlib`, and `wave` to process the audio data and generate a spectrogram. The resulting video is created using `FFmpeg` for better integration and output.

## Features

- **Spectrogram Visualization**: Generates a visual representation of the audio's frequency spectrum over time.
- **Video Creation**: Converts the spectrogram into an MP4 video file.
- **Customizable Frame Rate**: Allows you to set the frames per second (FPS) for the video.

## Prerequisites

Before running the script, make sure you have the following installed:

- **Python 3.x**: The script is compatible with Python 3.
- **Required Python Libraries**:
  - `numpy`
  - `matplotlib`
  - `wave`

- **FFmpeg**: Ensure `ffmpeg` is installed on your system. It is used to handle video encoding.

You can install the required Python libraries using pip:

```bash
pip install numpy matplotlib
```

## Usage
Prepare Your Audio File: Ensure you have a WAV file ready to be converted. For example, t_Robin - 5.wav.

Run the Script:

```bash
python your_script_name.py
```
Replace your_script_name.py with the name of your Python file.

Check the Output: After running the script, an MP4 video file will be created with the same name as the input WAV file but with the .mp4 extension. For example, if your input file is t_Robin - 5.wav, the output file will be t_Robin - 5.mp4.

Script Details
kilo(x, pos): Custom formatter to convert frequency values to kilohertz (kHz) for the y-axis of the spectrogram.

## Functions

### `vidwav(wavfile, fps=25)`

Main function that:
- Reads the WAV file.
- Generates a spectrogram.
- Creates a video of the spectrogram.
- Uses FFmpeg to combine the audio and video into a single MP4 file.

### `main()`

Calls the `vidwav` function with a sample WAV file `t_Robin - 5.wav`. You can replace this with your own file.

## Notes

- **Customization**: You can adjust the frame rate by changing the `fps` parameter in the `vidwav` function.
- **Colormap**: The spectrogram uses the `'viridis'` colormap. You can change it to other available colormaps in matplotlib.

## Contributing
If you would like to contribute to this project, please fork the repository and submit a pull request with your changes.

## Contact

For any questions or issues, you can reach out to [Moharira25](https://github.com/Moharira25).

## License

This project is licensed under the MIT License. See the LICENSE file for details.
