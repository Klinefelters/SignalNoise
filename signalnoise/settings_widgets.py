import tkinter as tk
from tkinter import ttk


class SettingsFrame(ttk.Frame):
    """
    A frame containing widgets for configuring signal simulation settings.

    Parameters:
    - master (tk.Tk): The master widget (typically the main application window).
    - app (Application): An instance of the main application.

    Attributes:
    - app (Application): An instance of the main application.
    """

    def __init__(self, master, app):
        """
        Initialize the SettingsFrame.

        Parameters:
        - master (tk.Tk): The master widget (typically the main application window).
        - app (Application): An instance of the main application.
        """
        super().__init__(master, padding=10)
        self.app = app
        self.create_widgets()

    def create_widgets(self):
        """
        Create and layout widgets for configuring signal simulation settings.
        """
        self.configure(style="TFrame")
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
        self.app.duration_entry = ttk.Entry(
            self, textvariable=self.app.duration_var)
        self.app.duration_entry.grid(row=3, column=1)

        # Sampling Rate
        ttk.Label(self, text="Sampling Rate:").grid(
            row=4, column=0, sticky="w")
        self.app.sampling_rate_entry = ttk.Entry(
            self, textvariable=self.app.sampling_rate_var)
        self.app.sampling_rate_entry.grid(row=4, column=1)

        # Noise Intensity
        ttk.Label(self, text="Noise Intensity:").grid(
            row=5, column=0, sticky="w")
        self.app.noise_intensity_entry = ttk.Entry(
            self, textvariable=self.app.noise_intensity_var)
        self.app.noise_intensity_entry.grid(row=5, column=1)

        # Noise Type
        ttk.Label(self, text="Noise Type:").grid(row=6, column=0, sticky="w")
        self.app.noise_type_combobox = ttk.Combobox(
            self, textvariable=self.app.noise_type_var, values=["gaussian", "impulse", "random"])
        self.app.noise_type_combobox.grid(row=6, column=1)

        # Filter Type
        ttk.Label(self, text="Filter Type:").grid(row=7, column=0, sticky="w")
        self.app.filter_type_combobox = ttk.Combobox(
            self, textvariable=self.app.filter_type_var, values=["butterworth", "bessel", "firwin"])
        self.app.filter_type_combobox.grid(row=7, column=1)

        # Filter Type
        ttk.Label(self, text="Filter Pass:").grid(row=8, column=0, sticky="w")
        self.app.filter_pass_combobox = ttk.Combobox(
            self, textvariable=self.app.filter_pass_var, values=["lowpass", "highpass"])
        self.app.filter_pass_combobox.grid(row=8, column=1)

        # Simulate Button
        simulate_button = ttk.Button(
            self, text="Simulate", command=self.app.simulate)
        simulate_button.grid(row=9, column=0, columnspan=2, pady=10)

        # Signal to noise Ratio
        ttk.Label(self, text="Noisy Noise Ratio:").grid(
            row=10, column=0, sticky="w")
        ttk.Label(self, textvariable=self.app.noisey_noise_label).grid(
            row=10, column=1, sticky="w")

        # Signal to noise Ratio
        ttk.Label(self, text="Filtered Noise Ratio:").grid(
            row=11, column=0, sticky="w")
        ttk.Label(self, textvariable=self.app.signal_noise_label).grid(
            row=11, column=1, sticky="w")
