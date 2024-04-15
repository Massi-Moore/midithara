from pydub import AudioSegment
import os

# Specify the directory path
directory = 'notes/piano/5'

# Iterate over the files in the directory and its subdirectories
for root, dirs, files in os.walk(directory):
    for file in files:
        # Check if the file is a .wav file
        if file.endswith('.wav'):
            # Get the full path of the file
            file_path = os.path.join(root, file)

            # Load the .wav file
            audio = AudioSegment.from_wav(file_path)

            # If the audio is shorter than 4 seconds, loop it until it reaches 4 seconds
            while len(audio) < 3000:  # AudioSegment.length is in milliseconds
                audio += audio

            # If the audio is longer than 4 seconds, truncate it to 4 seconds
            audio = audio[:3000]

            # Save the modified audio
            audio.export(file_path, format="wav")