
"""Main module for Cartesian to Polar Coordinate Converter project."""

import tkinter as tk
from tkinter import ttk

from utils import cartesian_to_polar
from utils import radians_to_degrees

## AI generated code for the dialog box and UI

def on_go():
    """This is AI generated code handling the dialog box in Tk inter. It retrieves the input values, calls the conversion function, and updates the output."""
    try:
        x = float(entry_x.get())
        y = float(entry_y.get())
        r, theta = cartesian_to_polar(x, y)
        degrees = radians_to_degrees(theta)
        result = f"Polar coordinates:\nr = {r:.2f}\ntheta = {theta:.2f} radians\ntheta = {degrees:.1f} degrees"
    except ValueError:
        result = "Invalid input. Please enter numeric values."
    output_var.set(result)

root = tk.Tk()
root.title("Cartesian to Polar Coordinate Converter")
root.geometry("600x340")

mainframe = ttk.Frame(root, padding="10 10 10 10")
mainframe.grid(row=0, column=0, sticky=("N", "W", "E", "S"))

ttk.Label(mainframe, text="X coordinate:").grid(row=0, column=0, sticky="W")
entry_x = ttk.Entry(mainframe, width=10)
entry_x.grid(row=0, column=1, sticky="W")

ttk.Label(mainframe, text="Y coordinate:").grid(row=1, column=0, sticky="W")
entry_y = ttk.Entry(mainframe, width=10)
entry_y.grid(row=1, column=1, sticky="W")

button_frame = ttk.Frame(mainframe)
button_frame.grid(row=2, column=0, columnspan=2, pady=5)

go_button = ttk.Button(button_frame, text="Go", command=on_go)
go_button.pack(side="left", padx=(0, 10))

quit_button = ttk.Button(button_frame, text="Quit", command=root.destroy)
quit_button.pack(side="left")

output_var = tk.StringVar()
output_label = ttk.Label(mainframe, textvariable=output_var, background="white", relief="sunken", anchor="w", width=40)
output_label.grid(row=3, column=0, columnspan=2, sticky="WE", pady=5)
output_var.set("Enter the X,Y coordinates of a point\nClick Go\nThe application returns the\nresult as Polar coordinates.")

root.mainloop()
