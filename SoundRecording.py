import sounddevice as sd
import time
from scipy.io.wavfile import write
fs=44100
seconds=int(input('Enter the duration buffer'))
for x in range(2):
    myrecording=sd.rec(int(seconds*fs), samplerate=fs, channels=2)
    sd.wait()
    write('recording.wav',fs,myrecording)
