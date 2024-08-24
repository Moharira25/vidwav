import os
import warnings

# Suppress warnings
warnings.filterwarnings("ignore")

from pydub import AudioSegment


def trim_audio(input_path, output_path, start_time=0, duration=5, amplification_db=10):
    try:
        audio = AudioSegment.from_wav(input_path)
        #audio = AudioSegment.from_mp3(input_path)
        trimmed_audio = audio[start_time * 1000:(start_time + duration) * 1000]
        trimmed_audio = trimmed_audio.set_channels(1)  # Convert to mono

        # Amplify the audio by the specified number of decibels
        amplified_audio = trimmed_audio + amplification_db

        amplified_audio.export(output_path, format="wav")
        #amplified_audio.export(output_path, format="mp3")
        print(f"Trimmed and amplified audio saved as {output_path}")
    except FileNotFoundError:
        print(f"Error: Input file '{input_path}' not found.")
    except Exception as e:
        print(f"Error trimming and amplifying audio: {str(e)}")


def main():
    # Paths to the audio files
    input_audio_path = 'Robin\\Robin - 5.wav'  # Replace with your input file path
    output_audio_path = 't_Robin - 5.wav'

    # Check if input file exists
    if not os.path.exists(input_audio_path):
        print(f"Error: Input file '{input_audio_path}' not found.")
        return

    # Trim the audio to 5 seconds and save it
    trim_audio(input_audio_path, output_audio_path, start_time=3, duration=3)



if __name__ == "__main__":
    main()