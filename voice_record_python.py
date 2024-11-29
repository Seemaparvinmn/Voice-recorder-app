#


# import sounddevice
# from scipy.io.wavfile import write


# def sharadvoice_recorder(seconds,file):
#     print("Your Recording Started.....")
#     sharadrecording=sounddevice.rec((seconds*44100),samplerate=44100,channels=2)
#     sounddevice.wait()
#     write(file,44100,sharadrecording)
#     print(" Recordin is finished")


# sharadvoice_recorder(10," Recordsave.wav")



import sounddevice as sd
from scipy.io.wavfile import write

def seema_recorder(seconds,file):
    print("Your recording Started.......")
    seemarecording=sd.rec(int(seconds*44100),samplerate=44100,channels=1)
    sd.wait()
    write(file,44100,seemarecording)
    print("Recording is finished")

seema_recorder(10,"Recordsave.wav1")    

