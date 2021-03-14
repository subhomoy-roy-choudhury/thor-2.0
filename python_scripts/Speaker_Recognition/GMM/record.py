import sounddevice as sd
from scipy.io.wavfile import write
import predict as pd

fs = 44110  # Sample rate
seconds = 6  # Duration of recording

i = "long speech 2"

myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)

print("Speak")
sd.wait(5)  # Wait until recording is finished
write("dataset/train/subho/"+str(i)+".wav", fs, myrecording)  # Save as WAV file
print("Recorded")







