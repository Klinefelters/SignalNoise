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


def apply_filter(input_signal, filter_type, filter_pass):
    """
    Apply a filter to the input signal based on the specified filter type.

    Parameters:
    - input_signal (array-like): The input signal to be filtered.
    - filter_type (str): The type of filter to be applied.
    - filter_pass (str): The type of filter pass to be applied.

    Returns:
    numpy.ndarray: Filtered signal.
    """
    order = 4  # You can adjust the filter order as needed
    cutoff = 0.1  # You can adjust the cutoff frequency as needed

    if filter_type == "butterworth":
        b, a = signal.butter(order, cutoff, btype=filter_pass, analog=False)
    elif filter_type == "bessel":
        b, a = signal.bessel(order, cutoff, btype=filter_pass, analog=False)
    elif filter_type == "firwin":

        b = signal.firwin(order + 1, cutoff, fs=2.0,
                          pass_zero=filter_pass, window='hamming')
        a = 1.0
    else:
        raise ValueError("Invalid filter type")

    # Apply the filter to the input signal
    return signal.filtfilt(b, a, input_signal)
