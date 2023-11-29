import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from signalnoise.utils import apply_filter, add_noise, generate_fourier_series
from signalnoise.settings_widgets import SettingsFrame


class App:
    """
    Signal Processing Simulation Application.

    Parameters:
    - master (tk.Tk): The master widget (typically the main application window).
    """

    def __init__(self, master):
        """
        Initialize the Signal Processing Application.

        Parameters:
        - master (tk.Tk): The master widget (typically the main application window).
        """
        self.master = master
        self.master.title("Signal Processing Simulation")

        # Set the theme to a dark theme
        self.set_dark_theme()

        self.noise_intensity_var = tk.DoubleVar(value=0.2)
        self.noise_type_var = tk.StringVar(value="gaussian")
        self.filter_type_var = tk.StringVar(value="butterworth")
        self.filter_pass_var = tk.StringVar(value="low")
        self.duration_var = tk.DoubleVar(value=1)
        self.sampling_rate_var = tk.DoubleVar(value=1000)
        self.signal_noise_label = tk.StringVar(value="")

        self.create_widgets()
        self.simulate()

    def set_dark_theme(self):
        """
        Set the dark theme for the application.
        """
        style = ttk.Style()
        style.theme_use("clam")  # Use the clam theme (a simple dark theme)
        style.configure("TFrame", background="#2E2E2E")
        style.configure("TLabel", background="#2E2E2E", foreground="#FFFFFF")
        style.configure("TEntry", fieldbackground="#2E2E2E",
                        foreground="#FFFFFF")
        style.configure("TCombobox", fieldbackground="#2E2E2E",
                        foreground="#FFFFFF")
        style.configure("TButton", background="#444444", foreground="#FFFFFF")

        # Set Matplotlib style for dark theme
        plt.style.use("dark_background")

    def create_widgets(self):
        """
        Create and layout widgets for the Signal Processing Application.
        """
        # Input Settings Frame
        input_frame = SettingsFrame(self.master, self)
        input_frame.grid(row=0, column=0, padx=10, pady=10, sticky="n")

        # Graphs Frame
        graphs_frame = ttk.Frame(self.master)
        graphs_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        # Matplotlib Figure
        self.fig, self.ax = plt.subplots(
            3, 1, figsize=(8, 6), tight_layout=True)
        self.canvas = FigureCanvasTkAgg(self.fig, master=graphs_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def simulate(self):
        """
        Simulate signal processing based on user input.
        """
        duration = self.duration_var.get()
        sampling_rate = self.sampling_rate_var.get()
        time = np.linspace(0, duration, int(
            sampling_rate * duration), endpoint=False)
        frequencies = [float(freq)
                       for freq in self.frequency_entry.get().split(",")]
        amplitudes = [float(amp)
                      for amp in self.amplitude_entry.get().split(",")]
        phases = [float(phase) for phase in self.phase_entry.get().split(",")]

        original = generate_fourier_series(
            time, frequencies, amplitudes, phases)

        noisy = add_noise(original, self.noise_type_var.get(),
                          self.noise_intensity_var.get())

        filtered = apply_filter(
            noisy, self.filter_type_var.get(), self.filter_pass_var.get())
        signal_power = np.mean(original**2)

        noise_power = np.mean((filtered - original)**2)

        snr_db = 10 * np.log10(signal_power / noise_power)

        self.signal_noise_label.set(f"{snr_db} db")

        self.visualize_results(time, original, noisy, filtered)

    def visualize_results(self, time, original, noisy, filtered):
        """
        Visualize the results of signal processing.

        Parameters:
        - time (numpy.ndarray): Time values for the signals.
        - original (numpy.ndarray): Original signal.
        - noisy (numpy.ndarray): Noisy signal.
        - filtered (numpy.ndarray): Filtered signal.
        """
        self.ax[0].clear()
        self.ax[0].plot(time, original, label="Original Signal")
        self.ax[0].set_title("Original Signal")
        self.ax[0].legend()

        self.ax[1].clear()
        self.ax[1].plot(time, noisy, label="Noisy Signal", color='orange')
        self.ax[1].set_title("Noisy Signal")
        self.ax[1].legend()

        self.ax[2].clear()
        self.ax[2].plot(time, filtered, label="Filtered Signal", color='green')
        self.ax[2].set_title("Filtered Signal")
        self.ax[2].legend()

        self.canvas.draw()
