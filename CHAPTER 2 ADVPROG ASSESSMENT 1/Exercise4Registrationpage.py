import tkinter as tk

def create_registration_gui():
    root = tk.Tk()
    root.title("Student Registration")
    # Reduced size: from 500x800 to a more compact 450x600
    root.geometry("450x600")
    root.resizable(False, False)
    root.config(bg="#f8f8f8")

    # --- Colors and Fonts (Slightly smaller for compactness) ---
    HEADER_BG = "#2c3e50"
    BUTTON_BG = "#2c3e50"
    BUTTON_FG = "white"
    TEXT_COLOR = "#333333"
    
    # Fonts reduced slightly
    LABEL_FONT = ("Arial", 9, "bold")
    TITLE_FONT = ("Arial", 14, "bold")
    SUBTITLE_FONT = ("Arial", 11, "bold")
    NORMAL_FONT = ("Arial", 9)

    # --- Top Header Frame ---
    # Height reduced from 100 to 70
    header_frame = tk.Frame(root, bg=HEADER_BG, height=70)
    header_frame.pack(fill="x")
    header_frame.pack_propagate(False)

    # Logo Text
    logo_label_bs = tk.Label(header_frame, text="BATH\nSPA", bg=HEADER_BG, fg="white", font=("Arial", 12, "bold"), justify="left")
    logo_label_bs.pack(side="left", padx=(15,3), pady=5, anchor="nw")

    separator_line = tk.Frame(header_frame, bg="white", width=2)
    separator_line.pack(side="left", fill="y", pady=5, padx=3)

    logo_label_rak = tk.Label(header_frame, text="RAK CAMPUS", bg=HEADER_BG, fg="white", font=("Arial", 14, "bold"), justify="left")
    logo_label_rak.pack(side="left", padx=5, pady=5, anchor="nw")

    # --- Main Content Frame ---
    # Reduced external padding
    content_frame = tk.Frame(root, bg="#ffffff", padx=15, pady=15, relief="flat", bd=1)
    content_frame.pack(pady=10, padx=15, fill="both", expand=False)

    # Titles (Vertical padding reduced)
    tk.Label(content_frame, text="Student Management System", font=TITLE_FONT, bg="white", fg=TEXT_COLOR).grid(row=0, column=0, columnspan=2, pady=(0, 2), sticky="w")
    tk.Label(content_frame, text="New Student Registration", font=SUBTITLE_FONT, bg="white", fg=TEXT_COLOR).grid(row=1, column=0, columnspan=2, pady=(0, 10), sticky="w")

    # --- Form Fields ---
    row_num = 2
    fields = ["Student Name", "Mobile Number", "Email Id", "Home Address"]

    # Entry fields (Vertical padding reduced)
    for field_text in fields:
        tk.Label(content_frame, text=field_text, font=LABEL_FONT, bg="white", fg=TEXT_COLOR).grid(row=row_num, column=0, sticky="w", pady=3)
        entry = tk.Entry(content_frame, width=25, relief="solid", bd=1, font=NORMAL_FONT)
        entry.grid(row=row_num, column=1, sticky="ew", pady=3)
        row_num += 1

    # Gender (Dropdown visual placeholder, vertical padding reduced)
    tk.Label(content_frame, text="Gender", font=LABEL_FONT, bg="white", fg=TEXT_COLOR).grid(row=row_num, column=0, sticky="w", pady=3)
    gender_var = tk.StringVar(value="Select Gender")
    gender_display_frame = tk.Frame(content_frame, relief="solid", bd=1, bg="white")
    gender_display_frame.grid(row=row_num, column=1, sticky="ew", pady=3)
    tk.Label(gender_display_frame, textvariable=gender_var, bg="white", fg=TEXT_COLOR, font=NORMAL_FONT).pack(side="left", padx=5, pady=1, fill="x", expand=True)
    tk.Label(gender_display_frame, text="▼", bg="white", fg=TEXT_COLOR, font=NORMAL_FONT).pack(side="right", padx=5, pady=1)
    row_num += 1

    # Course Enrolled (Radio Buttons, vertical padding reduced)
    tk.Label(content_frame, text="Course Enrolled", font=LABEL_FONT, bg="white", fg=TEXT_COLOR).grid(row=row_num, column=0, sticky="nw", pady=3)
    course_var = tk.StringVar()
    courses = ["BSc CC", "BSc CY", "BSc PSY", "BA & BM"]
    for i, course in enumerate(courses):
        rb = tk.Radiobutton(content_frame, text=course, variable=course_var, value=course, bg="white", fg=TEXT_COLOR, font=NORMAL_FONT, activebackground="white", selectcolor="white")
        rb.grid(row=row_num + i, column=1, sticky="w", pady=1)
    row_num += len(courses) # No extra row added here

    # Languages Known (Checkbuttons, vertical padding reduced)
    tk.Label(content_frame, text="Languages known", font=LABEL_FONT, bg="white", fg=TEXT_COLOR).grid(row=row_num, column=0, sticky="nw", pady=3)
    lang_vars = {lang: tk.BooleanVar() for lang in ["English", "Tagalog", "Hindi/Urdu"]}

    # Layout checkbuttons in two columns
    tk.Checkbutton(content_frame, text="English", variable=lang_vars["English"], bg="white", fg=TEXT_COLOR, font=NORMAL_FONT, activebackground="white", selectcolor="white").grid(row=row_num, column=1, sticky="w")
    tk.Checkbutton(content_frame, text="Tagalog", variable=lang_vars["Tagalog"], bg="white", fg=TEXT_COLOR, font=NORMAL_FONT, activebackground="white", selectcolor="white").grid(row=row_num, column=1, sticky="w", padx=80)
    row_num += 1
    tk.Checkbutton(content_frame, text="Hindi/Urdu", variable=lang_vars["Hindi/Urdu"], bg="white", fg=TEXT_COLOR, font=NORMAL_FONT, activebackground="white", selectcolor="white").grid(row=row_num, column=1, sticky="w")
    row_num += 1

    # Rate English Communication Skills (Scale/Slider, vertical padding reduced)
    tk.Label(content_frame, text="Rate your English communication skills", font=LABEL_FONT, bg="white", fg=TEXT_COLOR).grid(row=row_num, column=0, columnspan=2, sticky="w", pady=(10, 5))
    row_num += 1
    communication_scale = tk.Scale(content_frame, from_=0, to=10, orient="horizontal", length=300, bg="white", fg=TEXT_COLOR, highlightbackground="white", troughcolor="#c8daeb", sliderrelief="flat", sliderlength=15, bd=0)
    communication_scale.set(5)
    communication_scale.grid(row=row_num, column=0, columnspan=2, pady=(0, 10), sticky="ew")
    row_num += 1

    # --- Buttons (Vertical padding reduced) ---
    button_frame = tk.Frame(content_frame, bg="white")
    button_frame.grid(row=row_num, column=0, columnspan=2, pady=10)

    # Submit Button
    submit_button = tk.Button(button_frame, text="Submit", bg=BUTTON_BG, fg=BUTTON_FG, font=LABEL_FONT, padx=15, pady=5, relief="flat", command=lambda: print("Submit Clicked"))
    submit_button.pack(side="left", padx=10)

    # Clear Button
    clear_button = tk.Button(button_frame, text="Clear", bg=BUTTON_BG, fg=BUTTON_FG, font=LABEL_FONT, padx=15, pady=5, relief="flat", command=lambda: print("Clear Clicked"))
    clear_button.pack(side="left", padx=10)

    # Configure grid column weights for entries to expand
    content_frame.grid_columnconfigure(1, weight=1)

    root.mainloop()

if __name__ == "__main__":
    create_registration_gui()