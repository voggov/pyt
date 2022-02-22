import tkinter as tk
bomb = 100
score = 0
press_return = True
root = tk.Tk()
root.title("Game")
root.geometry("600x600+500+400")
root.iconbitmap("bomb.ico")
label = tk.Label(root, text='Press [enter] to
start the game', font=('Comic Sans MS', 12))
label.pack()
fuse_label = tk.Label(root, text=f'Fuse:
{str(bomb)}', font=('Comic Sans MS', 14))
fuse_label.pack()
score_label = tk.Label(root, text=f'Score:
{str(score)}', font=('Comic Sans MS', 14))
score_label.pack()
img_1 = tk.PhotoImage(file="1.gif")
img_2 = tk.PhotoImage(file="2.gif")
img_3 = tk.PhotoImage(file="3.gif")
img_4 = tk.PhotoImage(file="4.gif")
bomb_label = tk.Label(image=img_1)
bomb_label.pack()
def update_display():
 pass
def is_alive():
 pass
def update_bomb():
 pass
def update_score():
 pass
def start(event):
 pass
def click():
 pass