# signal_simulator.py
import numpy as np
from scipy import signal


def generate_signal(time, frequency, amplitude):
    original_signal = amplitude * np.cos(2 * np.pi * frequency * time)
    return original_signal


def generate_fourier_series(time, frequencies, amplitudes, phases):
    signal_wave = np.zeros_like(time)

    for freq, amp, phase in zip(frequencies, amplitudes, phases):
        signal_wave += amp * np.sin(2 * np.pi * freq * time + phase)

    return signal_wave


def add_noise(signal_wave, noise_type, noise_intensity):
    if noise_type == "gaussian":
        noise = np.random.normal(
            0, noise_intensity, len(signal_wave))
    elif noise_type == "impulse":
        noise = np.random.choice([0, 1], size=len(signal_wave), p=[
            1 - noise_intensity, noise_intensity])
    elif noise_type == "random":
        noise = noise_intensity * np.random.rand(len(signal_wave))
    else:
        raise ValueError("Invalid noise type")

    return signal_wave + noise


def apply_filter(input_signal):
    b, a = signal.butter(4, 0.1, btype='low', analog=False)
    return signal.filtfilt(b, a, input_signal)
