# signal_processing_app.py
import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from signalnoise.utils import apply_filter, add_noise, generate_fourier_series
from signalnoise.settings_widgets import SettingsFrame


class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Signal Processing Simulation")

        # Set the theme to a dark theme
        self.set_dark_theme()

        self.noise_intensity_var = tk.DoubleVar(value=0.2)
        self.noise_type_var = tk.StringVar(value="gaussian")
        self.duration_var = tk.DoubleVar(value=10.0)
        self.sampling_rate_var = tk.DoubleVar(value=10000.0)

        self.create_widgets()

    def set_dark_theme(self):
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

        filtered = apply_filter(noisy)

        self.visualize_results(time, original, noisy, filtered)

    def visualize_results(self, time, original, noisy, filtered):
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
