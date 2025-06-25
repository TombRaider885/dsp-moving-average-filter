import numpy as np
import matplotlib.pyplot as plt

# Parameters
fs = 500          # Sampling frequency (Hz)
t = np.arange(0, 1, 1/fs)  # Time vector, 1 second duration
f = 5             # Frequency of sine wave (Hz)

# Generate clean sine wave signal
clean_signal = np.sin(2 * np.pi * f * t)

# Add random Gaussian noise
noise = np.random.normal(0, 0.5, clean_signal.shape)
noisy_signal = clean_signal + noise

# Moving average filter function
def moving_average(signal, window_size):
    return np.convolve(signal, np.ones(window_size)/window_size, mode='same')

# Apply filter with window size 10 samples
window_size = 5
filtered_signal = moving_average(noisy_signal, window_size)

# Plot the signals
plt.figure(figsize=(12,6))
plt.plot(t, clean_signal, label='Clean Signal', linewidth=2)
plt.plot(t, noisy_signal, label='Noisy Signal', alpha=0.6)
plt.plot(t, filtered_signal, label='Filtered Signal', linewidth=2)
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.title('Low-pass Filtering using Moving Average')
plt.legend()
plt.grid(True)
plt.savefig("dsp_filtered_graph.png", dpi=300)
plt.show()
