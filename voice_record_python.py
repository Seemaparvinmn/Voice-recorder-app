


#import sounddevice as sd
import sounddevice as sd
from scipy.io.wavfile import write
#from scipy.io.wavfile import write



def seema_recorder(seconds,file):
    print("Your recording Started.......")
    seemarecording=sd.rec(int(seconds*44100),samplerate=44100,channels=1)#4100 is the sampling rate, meaning there are 44100 samples per second.
# Multiplying it by seconds gives the total number of frames for the recording duration
    sd.wait()
    write(file,44100,seemarecording)
    print("Recording is finished")

seema_recorder(10,"Recordsave.wav1")    

