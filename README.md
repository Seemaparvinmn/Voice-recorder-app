# Voice-recorder-app
Voice Recorder in Python This project is a simple Voice Recorder built using Python. It allows users to record audio from their microphone for a specified duration and save it as a .wav file. The program uses the sounddevice library for audio recording and the scipy library to handle file saving

Features
Records audio from the system's default microphone.
Allows the user to specify the recording duration.
Saves the recording as a .wav file in CD-quality (44.1 kHz sampling rate).
Mono-channel recording for compact file size.


Technologies Used
Python:
Easy-to-use programming language for building simple yet powerful tools.
sounddevice:
A library for capturing and playing audio data.
scipy.io.wavfile:
A module from the scipy library for handling .wav files.
Setup and Installation
Clone the repository:

bash
Copy code
git clone https://github.com/your-username/voice-recorder.git
cd voice-recorder
Install the required dependencies:

bash
Copy code
pip install sounddevice scipy
Run the script:

bash
Copy code
python voice_record.py
Usage
Specify the duration of the recording and the filename in the script:

python
Copy code
seema_recorder(10, "output.wav")
10: Duration of the recording in seconds.
"output.wav": Name of the file where the recording will be saved.
Run the program, and the recording will start. Once finished, it will save the recording in the current directory.


Code Snippet
python
Copy code
import sounddevice as sd
from scipy.io.wavfile import write

def seema_recorder(seconds, file):
    print("Your recording Started.......")
    seemarecording = sd.rec(int(seconds * 44100), samplerate=44100, channels=1)
    sd.wait()
    write(file, 44100, seemarecording)
    print("Recording is finished")
    

# Example usage:
seema_recorder(10, "Recordsave.wav")
Requirements
Python 3.6 or higher
sounddevice library
scipy library
Future Improvements
Add GUI support for easier interaction (e.g., using Tkinter or PyQt).
Enable stereo recording (optional).
Allow users to select the microphone device and adjust settings like sample rate.

