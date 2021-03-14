import sounddevice as sd
from scipy.io.wavfile import write
import predict as pd

fs = 44110  # Sample rate
seconds = 5  # Duration of recording

i = 1

myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)

print("Speak")
sd.wait(5)  # Wait until recording is finished
a=str(i)+".wav"
write(str(a), fs, myrecording)  # Save as WAV file
print("Recorded")

num = pd.predict(str(a))
print(num)




