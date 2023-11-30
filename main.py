# main.py
import tkinter as tk
from signalnoise import App


def main() -> None:
    root = tk.Tk()
    app = App(root)
    root.mainloop()


if __name__ == "__main__":
    main()
