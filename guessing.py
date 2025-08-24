import tkinter as tk
import random

class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        self.root.geometry("400x300")
        self.root.config(bg="#f0f0f0")

        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0

       
        self.title_label = tk.Label(root, text="Guess the Number (1-100)", 
                                    font=("Arial", 16, "bold"), bg="#f0f0f0")
        self.title_label.pack(pady=10)

       
        self.entry = tk.Entry(root, font=("Arial", 14))
        self.entry.pack(pady=10)

        
        self.submit_button = tk.Button(root, text="Guess", font=("Arial", 12), 
                                       bg="#4CAF50", fg="white", command=self.check_guess)
        self.submit_button.pack(pady=5)

        
        self.result_label = tk.Label(root, text="", font=("Arial", 14), bg="#f0f0f0")
        self.result_label.pack(pady=10)

        
        self.reset_button = tk.Button(root, text="Reset Game", font=("Arial", 12), 
                                      bg="#2196F3", fg="white", command=self.reset_game)
        self.reset_button.pack(pady=5)

    def check_guess(self):
        try:
            guess = int(self.entry.get())
            self.attempts += 1

            if guess < self.number_to_guess:
                self.result_label.config(text=f"Too Low! Try again. Attempts: {self.attempts}", fg="red")
            elif guess > self.number_to_guess:
                self.result_label.config(text=f"Too High! Try again. Attempts: {self.attempts}", fg="red")
            else:
                self.result_label.config(text=f"🎉 Correct! You guessed it in {self.attempts} attempts!", fg="green")
        except ValueError:
            self.result_label.config(text="⚠ Please enter a valid number!", fg="orange")

    def reset_game(self):
        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0
        self.entry.delete(0, tk.END)
        self.result_label.config(text="Game Reset! Start guessing again.", fg="blue")



if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()
