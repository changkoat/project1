from tkinter import *
from tkinter import messagebox
import random

# Word list
word_list = [
    "apple", "brave", "charm", "dream", "eagle",
    "fancy", "ghost", "happy", "ivory", "jewel",
    "koala", "lemon", "mango", "night", "ocean",
    "panda", "queen", "river", "sugar", "tiger",
    "unity", "value", "wheat", "xerox", "yacht",
    "zebra", "agile", "blush", "crisp", "delve",
    "ember", "flint", "grace", "hover", "ideal",
    "jolly", "knack", "light", "merge", "notch",
    "orbit", "pluck", "query", "rally", "slope"
]

# Select a random word
word = random.choice(word_list).lower()

# Initialize Tkinter window
window = Tk()
window.title('WORDLE')

# Color
green = '#32a852'
yellow = '#fffb14'
grey = '#262622'
black = '#080808'
white = '#f2f3f5'

# Window configuration
window.config(bg=black)
app_title = Label(window, text = 'WORDLE', font = ('Arial Bold', 30), bg = black, fg = white)
app_title.grid(row = 0, column = 0, columnspan = 5, padx = 15, pady = 15)


user_input = Entry(window)
user_input.grid(row = 100, column = 0, padx = 15, pady = 15, columnspan = 3)


round_num = 1


def Guess():
    global word, round_num
    user_guess = user_input.get().lower()

    if round_num <= 5:
        if len(user_guess) == 5 and user_guess.isalpha():
            if user_guess == word:
                for i, guessLetter in enumerate(user_guess):
                    guessLabel = Label(window, text=guessLetter.upper())
                    guessLabel.grid(row=round_num, column=i, padx=15, pady=15)
                    guessLabel.config(bg=green, fg=grey)

                messagebox.showinfo('CONGRATS', f'YOU GUESSED THE WORD IN {round_num} TRIES!')
                window.quit()
            else:
                for i, guessLetter in enumerate(user_guess):
                    guessLabel = Label(window, text=guessLetter.upper())
                    guessLabel.grid(row = round_num, column = i, padx = 15, pady = 15)

                    if guessLetter == word[i]:
                        guessLabel.config(bg = green, fg = grey)
                    elif guessLetter in word:
                        guessLabel.config(bg = yellow, fg = grey)
                    else:
                        guessLabel.config(bg = white, fg = grey)
        else:
            messagebox.showinfo('ERROR', 'TYPE IN WORDS WITH 5 ALPHABETIC CHARACTERS')

        round_num += 1
        user_input.delete(0, END)

    elif round_num == 6:
        messagebox.showinfo('YOU LOSE', f'THE WORD WAS: {word}')
        window.quit()

# Guess button
user_guessButton = Button(window, text='GUESS', command=Guess)
user_guessButton.grid(row=100, column=3, columnspan=2)

# Main loop
window.mainloop()