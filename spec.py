import matplotlib.pyplot as plt 
from scipy import signal
from scipy.io import wavfile

sample_rate, samples=wavfile.read('audio.wav')
frequencies,times,spectrogram=signal.spectrogram(samples,sample_rate)

plt.imshow(spectrogram)
plt.ylabel('freq(khz)')
plt.xlabel('time(sec)')
plt.show()