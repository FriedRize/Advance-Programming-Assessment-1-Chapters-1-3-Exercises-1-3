import tkinter as tk
from tkinter import messagebox
import random
import time

class WordGuessGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("🧠 Word Guess Game")
        self.geometry("500x400")
        self.configure(bg="#121212")
        self.resizable(False, False)

        # --- Game Data ---
        self.words = [
            "python", "window", "banana", "coffee", "puzzle",
            "school", "guitar", "planet", "butter", "laptop",
            "science", "friend", "football", "holiday", "mountain"
        ]
        self.score = 0
        self.current_word = ""
        self.shuffled_word = ""
        self.time_limit = 30  # seconds
        self.remaining_time = self.time_limit
        self.timer_running = False

        # --- Title ---
        tk.Label(self, text="WORD GUESS GAME", font=("Trebuchet MS", 18, "bold"),
                 fg="#00BFFF", bg="#121212").pack(pady=15)

        # --- Shuffled Word Display ---
        self.word_label = tk.Label(self, text="", font=("Courier", 22, "bold"),
                                   fg="#BB86FC", bg="#121212")
        self.word_label.pack(pady=10)

        # --- Entry for Guess ---
        self.entry = tk.Entry(self, font=("Arial", 16), justify="center", width=20,
                              bg="#1e1e1e", fg="white", insertbackground="white")
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", lambda event: self.check_guess())

        # --- Buttons ---
        button_frame = tk.Frame(self, bg="#121212")
        button_frame.pack(pady=10)

        self.check_btn = tk.Button(button_frame, text="Check", command=self.check_guess,
                                   font=("Arial", 12, "bold"), bg="#6A0DAD", fg="white",
                                   activebackground="#0077FF", relief="flat", width=10)
        self.check_btn.grid(row=0, column=0, padx=10)

        self.next_btn = tk.Button(button_frame, text="Next Word", command=self.next_word,
                                  font=("Arial", 12, "bold"), bg="#0077FF", fg="white",
                                  activebackground="#6A0DAD", relief="flat", width=10)
        self.next_btn.grid(row=0, column=1, padx=10)

        # --- Score + Timer ---
        info_frame = tk.Frame(self, bg="#121212")
        info_frame.pack(pady=10)

        self.score_label = tk.Label(info_frame, text=f"Score: {self.score}",
                                    font=("Arial", 12, "bold"), fg="#00FFAA", bg="#121212")
        self.score_label.grid(row=0, column=0, padx=20)

        self.timer_label = tk.Label(info_frame, text=f"Time Left: {self.remaining_time}s",
                                    font=("Arial", 12, "bold"), fg="#FFA500", bg="#121212")
        self.timer_label.grid(row=0, column=1, padx=20)

        # --- Feedback Label ---
        self.feedback = tk.Label(self, text="", font=("Arial", 13, "italic"),
                                 fg="#FFD700", bg="#121212")
        self.feedback.pack(pady=10)

        # --- Restart Button ---
        tk.Button(self, text="Restart Game", command=self.restart_game,
                  font=("Arial", 11, "bold"), bg="#BB86FC", fg="black",
                  activebackground="#00BFFF", relief="flat", width=12).pack(pady=10)

        self.next_word()
        self.start_timer()

    # --- Game Logic ---
    def shuffle_word(self, word):
        shuffled = list(word)
        random.shuffle(shuffled)
        return "".join(shuffled)

    def next_word(self):
        """Load next shuffled word"""
        self.entry.delete(0, tk.END)
        self.feedback.config(text="")
        self.current_word = random.choice(self.words)
        self.shuffled_word = self.shuffle_word(self.current_word)
        # ensure it’s not identical to the original
        while self.shuffled_word == self.current_word:
            self.shuffled_word = self.shuffle_word(self.current_word)
        self.word_label.config(text=self.shuffled_word)

    def check_guess(self):
        """Check user's guess"""
        guess = self.entry.get().strip().lower()
        if not guess:
            return
        if guess == self.current_word:
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
            self.feedback.config(text="✅ Correct!", fg="#00FFAA")
        else:
            self.feedback.config(text=f"❌ Wrong! It was '{self.current_word}'.", fg="#FF5555")
        self.after(1000, self.next_word)

    def restart_game(self):
        """Restart the game"""
        self.score = 0
        self.remaining_time = self.time_limit
        self.score_label.config(text=f"Score: {self.score}")
        self.feedback.config(text="")
        self.timer_label.config(text=f"Time Left: {self.remaining_time}s")
        self.next_word()
        if not self.timer_running:
            self.start_timer()

    # --- Timer Logic ---
    def start_timer(self):
        """Start countdown timer"""
        self.timer_running = True
        self.update_timer()

    def update_timer(self):
        if self.remaining_time > 0:
            self.remaining_time -= 1
            self.timer_label.config(text=f"Time Left: {self.remaining_time}s")
            self.after(1000, self.update_timer)
        else:
            self.timer_running = False
            messagebox.showinfo("Time's Up!", f"Final Score: {self.score}")
            self.word_label.config(text="Game Over!")
            self.feedback.config(text="Click Restart to play again.")
            self.entry.delete(0, tk.END)

# --- Run Game ---
if __name__ == "__main__":
    app = WordGuessGame()
    app.mainloop()