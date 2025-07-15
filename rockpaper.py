import tkinter as tk
import random

# Game logic
choices = ["Rock", "Paper", "Scissors"]

def determine_winner(user, computer):
    if user == computer:
        return "Tie"
    elif (user == "Rock" and computer == "Scissors") or \
         (user == "Scissors" and computer == "Paper") or \
         (user == "Paper" and computer == "Rock"):
        return "You Win!"
    else:
        return "Computer Wins!"

# Main action
def play(user_choice):
    global user_score, computer_score

    computer_choice = random.choice(choices)
    result = determine_winner(user_choice, computer_choice)

    user_choice_label.config(text="Your_choice: " + user_choice)
    computer_choice_label.config(text="Computer_choice: " + computer_choice)
    result_label.config(text="Result: " + result)

    if result == "You Win!":
        user_score += 1
    elif result == "Computer Wins!":
        computer_score += 1

    score_label.config(text=f"Score - You: {user_score} | Computer: {computer_score}")

# Reset Game
def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    user_choice_label.config(text="Your_choice:")
    computer_choice_label.config(text="Computer_choice:")
    result_label.config(text="Result:")
    score_label.config(text="Score - You: 0 | Computer: 0")

# Window setup
window = tk.Tk()
window.title("Rock-Paper-Scissors")
window.geometry("400x400")
window.config(bg="#f0f0f0")

user_score = 0
computer_score = 0

title = tk.Label(window, text="Rock-Paper-Scissors Game", font=("Arial", 16, "bold"), bg="#f0f0f0")
title.pack(pady=10)

user_choice_label = tk.Label(window, text="Your_choice:", font=("Arial", 12), bg="#f0f0f0")
user_choice_label.pack()

computer_choice_label = tk.Label(window, text="Computer_choice:", font=("Arial", 12), bg="#f0f0f0")
computer_choice_label.pack()

result_label = tk.Label(window, text="Result:", font=("Arial", 12, "bold"), bg="#f0f0f0")
result_label.pack(pady=10)

score_label = tk.Label(window, text="Score - You: 0 | Computer: 0", font=("Arial", 12), bg="#f0f0f0")
score_label.pack(pady=10)

button_frame = tk.Frame(window, bg="#f0f0f0")
button_frame.pack()

rock_btn = tk.Button(button_frame, text="Rock", width=10, command=lambda: play("Rock"))
rock_btn.grid(row=0, column=0, padx=5, pady=5)

paper_btn = tk.Button(button_frame, text="Paper", width=10, command=lambda: play("Paper"))
paper_btn.grid(row=0, column=1, padx=5, pady=5)

scissors_btn = tk.Button(button_frame, text="Scissors", width=10, command=lambda: play("Scissors"))
scissors_btn.grid(row=0, column=2, padx=5, pady=5)

reset_btn = tk.Button(window, text="Reset Game", command=reset_game)
reset_btn.pack(pady=10)

exit_btn = tk.Button(window, text="Exit", command=window.destroy)
exit_btn.pack(pady=5)

window.mainloop()
