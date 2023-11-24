import numpy as np
from scipy import signal


def generate_signal(time, frequency, amplitude):
    """
    Generate a sinusoidal signal.

    Parameters:
    - time (array-like): Time values for the signal.
    - frequency (float): Frequency of the signal in Hertz.
    - amplitude (float): Amplitude of the signal.

    Returns:
    numpy.ndarray: Sinusoidal signal.
    """

    original_signal = amplitude * np.cos(2 * np.pi * frequency * time)
    return original_signal


def generate_fourier_series(time, frequencies, amplitudes, phases):
    """
    Generate a Fourier series signal.

    Parameters:
    - time (array-like): Time values for the signal.
    - frequencies (list): List of frequencies for each component.
    - amplitudes (list): List of amplitudes for each component.
    - phases (list): List of phases for each component.

    Returns:
    numpy.ndarray: Fourier series signal.
    """

    signal_wave = np.zeros_like(time)

    for freq, amp, phase in zip(frequencies, amplitudes, phases):
        signal_wave += amp * np.sin(2 * np.pi * freq * time + phase)

    return signal_wave


def add_noise(signal_wave, noise_type, noise_intensity):
    """
    Add noise to a signal.

    Parameters:
    - signal_wave (array-like): The original signal.
    - noise_type (str): Type of noise ("gaussian", "impulse", or "random").
    - noise_intensity (float): Intensity of the noise.

    Returns:
    numpy.ndarray: Signal with added noise.
    """

    if noise_type == "gaussian":
        noise = np.random.normal(0, noise_intensity, len(signal_wave))
    elif noise_type == "impulse":
        noise = np.random.choice([0, 1], size=len(signal_wave), p=[
                                 1 - noise_intensity, noise_intensity])
    elif noise_type == "random":
        noise = noise_intensity * np.random.rand(len(signal_wave))
    else:
        raise ValueError("Invalid noise type")

    return signal_wave + noise


def apply_filter(input_signal):
    """
    Apply a low-pass Butterworth filter to the input signal.

    Parameters:
    - input_signal (array-like): The input signal to be filtered.

    Returns:
    numpy.ndarray: Filtered signal.
    """

    b, a = signal.butter(4, 0.1, btype='low', analog=False)
    return signal.filtfilt(b, a, input_signal)
