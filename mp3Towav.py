from pydub import AudioSegment


def convert_mp3_to_wav(input_mp3_path, output_wav_path):
    try:
        # Load the MP3 file
        audio = AudioSegment.from_mp3(input_mp3_path)

        # Export the audio as a WAV file
        audio.export(output_wav_path, format="wav")

        print(f"Successfully converted {input_mp3_path} to {output_wav_path}")
    except FileNotFoundError:
        print(f"Error: Input file '{input_mp3_path}' not found.")
    except Exception as e:
        print(f"Error converting MP3 to WAV: {str(e)}")

# Example usage:
convert_mp3_to_wav("data/Robin/t_Robin - 5.mp3", "t_Robin - 5.wav")
