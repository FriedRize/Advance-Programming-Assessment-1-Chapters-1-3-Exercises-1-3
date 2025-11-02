import tkinter as tk

def create_gui():
    root = tk.Tk()
    root.title("GUI Pack Example")
    root.minsize(400, 300)

    DARK_COLOR = "#1f2937"
    LIGHT_COLOR = "#f3f4f6"
    LABEL_FONT = ("Inter", 24)

    # Left Frame (A & B)
    left_frame = tk.Frame(root, bd=5, relief="solid")
    left_frame.pack(side="left", expand=True, fill="both")

    # Right Frame (C & D)
    right_frame = tk.Frame(root, bd=5, relief="solid")
    right_frame.pack(side="left", expand=True, fill="both")

    # Labels A and B
    tk.Label(left_frame, text="A", bg=DARK_COLOR, fg="white", font=LABEL_FONT).pack(side="top", expand=True, fill="both")
    tk.Label(left_frame, text="B", bg=LIGHT_COLOR, fg="black", font=LABEL_FONT).pack(side="bottom", expand=True, fill="both")

    # Labels C and D
    tk.Label(right_frame, text="C", bg=LIGHT_COLOR, fg="black", font=LABEL_FONT).pack(side="top", expand=True, fill="both")
    tk.Label(right_frame, text="D", bg=DARK_COLOR, fg="white", font=LABEL_FONT).pack(side="bottom", expand=True, fill="both")

    root.mainloop()

if __name__ == "__main__":
    create_gui()