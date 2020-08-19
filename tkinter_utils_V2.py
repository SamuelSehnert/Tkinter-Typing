import tkinter as tk
import scrape_utils

root = tk.Tk()
root.title("Speed Test!")
root.geometry("400x400")


class GUI_Layout:
    def __init__(self, master):
        frame1 = tk.Frame(master)
        frame1.pack()

        self.master = master
        master.bind("<Return>", self.push_final) # binds the return button to return whatever is in the entry bar

        self.countdown_label = tk.Label(master)
        self.count = 3

        self.difficulty = tk.Listbox()
        self.game_difficulty = None

        self.spacer1 = tk.Label(master, text="   ") 
        spacer2 = tk.Label(master, text="   ") 
        self.spacer3v1 = tk.Label(master, text="\n\n")
        self.spacer3 = tk.Label(master, text="\n") 
        self.spacer4 = tk.Label(master, text=" \n") 

        self.initialize_introductions()
        self.initialize_difficulties(master, spacer2)

        self.startButton = tk.Button(master, text="START", command=self.click_countdown) #clicker begins the game
        self.startButton.pack()
        self.spacer3.pack() 

        
    def initialize_introductions(self):
        intro = "Hello, and welcome to a test of speed!\n To begin, choose your difficulty and press the start button!"
        instructions = tk.Label(self.master, text=intro, fg="red")
        instructions.config(anchor="center")
        instructions.pack()
        self.spacer1.pack()
    
    def initialize_difficulties(self, master, spacer):
        """
        (0,) = Easy
        (1,) = Medium
        (2,) = Hard
        """
        difficulty_choices = ["EASY", "MEDIUM", "HARD"]
        self.difficulty = tk.Listbox(master, height=3)
        for i in difficulty_choices:
            self.difficulty.insert(tk.END, i)
        self.difficulty.pack()
        spacer.pack()

    def initialize_sentence(self, master, spacer):
        sentence = scrape_utils.push_final_sentence()
        sentence_label = tk.Label(master, text=sentence, fg="blue")
        sentence_label.pack()
        spacer.pack()

    def click_countdown(self):
        self.game_difficulty = self.difficulty.curselection()
        self.countdown_label.pack()
        self.spacer3v1.pack()
        self.countdown(self.count)

    def clicker(self):
        self.initialize_sentence(self.master, self.spacer4)
        
        self.entry_bar = tk.Entry(self.master)
        self.entry_bar.pack()

    def push_final(self, event): # used for when enter is pressed, returns what is in the entry bar
        submission = self.entry_bar.get()
        print(submission)

    def countdown(self, count): # for the after-button timer
        self.countdown_label['text'] = count
        if count > 0:
            self.master.after(1000, self.countdown, count - 1)
        elif count <= 0:
            self.countdown_label['text'] = "GO!"
            self.clicker()

g = GUI_Layout(root)
root.mainloop()
