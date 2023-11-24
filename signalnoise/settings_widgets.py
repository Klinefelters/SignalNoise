# settings_widgets.py
import tkinter as tk
from tkinter import ttk

class SettingsFrame(ttk.Frame):
    def __init__(self, master, app):
        super().__init__(master, padding=10)
        self.app = app
        self.create_widgets()

    def create_widgets(self):
        # Frequency
        ttk.Label(self, text="Frequencies:").grid(row=0, column=0, sticky="w")
        self.app.frequency_entry = ttk.Entry(self)
        self.app.frequency_entry.grid(row=0, column=1)
        self.app.frequency_entry.insert(0, "2, 5, 10")  # Default values

        # Amplitude
        ttk.Label(self, text="Amplitudes:").grid(row=1, column=0, sticky="w")
        self.app.amplitude_entry = ttk.Entry(self)
        self.app.amplitude_entry.grid(row=1, column=1)
        self.app.amplitude_entry.insert(0, "1, 0.5, 0.2")  # Default values

        # Phases
        ttk.Label(self, text="Phases:").grid(row=2, column=0, sticky="w")
        self.app.phase_entry = ttk.Entry(self)
        self.app.phase_entry.grid(row=2, column=1)
        self.app.phase_entry.insert(0, "0, 1.5708, 3.1416")  # Default values

        # Duration
        ttk.Label(self, text="Duration:").grid(row=3, column=0, sticky="w")
        self.app.duration_entry = ttk.Entry(self, textvariable=self.app.duration_var)
        self.app.duration_entry.grid(row=3, column=1)

        # Sampling Rate
        ttk.Label(self, text="Sampling Rate:").grid(row=4, column=0, sticky="w")
        self.app.sampling_rate_entry = ttk.Entry(self, textvariable=self.app.sampling_rate_var)
        self.app.sampling_rate_entry.grid(row=4, column=1)

        # Noise Intensity
        ttk.Label(self, text="Noise Intensity:").grid(row=5, column=0, sticky="w")
        self.app.noise_intensity_entry = ttk.Entry(self, textvariable=self.app.noise_intensity_var)
        self.app.noise_intensity_entry.grid(row=5, column=1)

        # Noise Type
        ttk.Label(self, text="Noise Type:").grid(row=6, column=0, sticky="w")
        self.app.noise_type_combobox = ttk.Combobox(self, textvariable=self.app.noise_type_var, values=["gaussian", "impulse", "random"])
        self.app.noise_type_combobox.grid(row=6, column=1)

        # Simulate Button
        simulate_button = ttk.Button(self, text="Simulate", command=self.app.simulate)
        simulate_button.grid(row=7, column=0, columnspan=2, pady=10)
