import tkinter as tk
from PIL import Image, ImageTk
from random import choice 

# Main window
root = tk.Tk()
root.title('Rock Paper Scissors Game')
root.configure(background='#cc66cc')

# Pictures
user_paper = ImageTk.PhotoImage(Image.open("images/user-paper.png"))
user_rock = ImageTk.PhotoImage(Image.open("images/user-rock.png"))
user_scissor = ImageTk.PhotoImage(Image.open("images/user-scissor.png"))
ai_paper = ImageTk.PhotoImage(Image.open("images/ai-paper.png"))
ai_rock = ImageTk.PhotoImage(Image.open("images/ai-rock.png"))
ai_scissor = ImageTk.PhotoImage(Image.open("images/ai-scissor.png"))

# Insert pictures
lbl_user = tk.Label(master=root, image=user_rock, bg='#cc66cc')
lbl_ai = tk.Label(master=root, image=ai_paper, bg='#cc66cc')

# Score
user_score = tk.Label(master=root, text='0', font=('Helvetica', 24), bg='#cc66cc', fg='white')
ai_score = tk.Label(master=root, text='0', font=('Helvetica', 24), bg='#cc66cc', fg='white')

lbl_user.grid(row=1, column=4)
lbl_ai.grid(row=1, column=0)

ai_score.grid(row=1, column=1)
user_score.grid(row=1, column=3)

# Update message
def update_message(user_message):
    msg_lbl['text'] = user_message

# Update user score
def update_user_score():
    score = int(user_score['text'])
    score += 1
    user_score['text'] = str(score)

# Update computer score
def update_computer_score():
    score = int(ai_score['text'])
    score += 1
    ai_score['text'] = str(score)

# Check winner
def check_winner(player, computer):
    if player == computer:
        update_message('It\'s a tie!')
    elif player == 'rock' and computer == 'scissor':
        update_message('You win!')
        update_user_score()
    elif player == 'paper' and computer == 'rock':
        update_message('You win!')
        update_user_score()
    elif player == 'scissor' and computer == 'paper':
        update_message('You win!')
        update_user_score()
    else:
        update_message('You lose!')
        update_computer_score()

# Update choice
choices = ["rock", "paper", "scissor"]

def update_choice(user_input):
    # For computer
    comp_choice = choice(choices)
    if comp_choice == 'rock':
        lbl_ai.configure(image=ai_rock)
    elif comp_choice == 'paper':
        lbl_ai.configure(image=ai_paper)
    elif comp_choice == 'scissor':
        lbl_ai.configure(image=ai_scissor)

    # For user
    if user_input == 'rock':
        lbl_user.configure(image=user_rock)
    elif user_input == 'paper':
        lbl_user.configure(image=user_paper)
    elif user_input == 'scissor':
        lbl_user.configure(image=user_scissor)

    check_winner(user_input, comp_choice)

# Buttons
rock_btn = tk.Button(master=root, width=20, height=2, text='Rock',
                     bg='#7c00ff', fg='white', command=lambda: update_choice('rock'))
rock_btn.grid(row=2, column=1)

paper_btn = tk.Button(master=root, width=20, height=2, text='Paper',
                      bg='#a640ff', fg='white', command=lambda: update_choice('paper'))
paper_btn.grid(row=2, column=2)

scissor_btn = tk.Button(master=root, width=20, height=2, text='Scissor',
                        bg='#7c00ff', fg='white', command=lambda: update_choice('scissor'))
scissor_btn.grid(row=2, column=3)

# Indicators
user_indicator = tk.Label(master=root, font=('Helvetica', 16), text='You', bg='#cc66cc', fg='white')
ai_indicator = tk.Label(master=root, font=('Helvetica', 16), text='Computer', bg='#cc66cc', fg='white')
user_indicator.grid(row=0, column=3)
ai_indicator.grid(row=0, column=1)

# Message
msg_lbl = tk.Label(master=root, font=('Helvetica', 16), bg='#cc66cc', fg='white', text='You lose')
msg_lbl.grid(row=3, column=2, pady=(20, 20))

root.mainloop()
