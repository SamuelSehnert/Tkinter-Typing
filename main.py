import tkinter as tk
import scrape_utils
import time



class GUI_Layout:
    def __init__(self, master):
        frame1 = tk.Frame(master)
        frame1.pack()

        self.master = master
        self.master_finish = None
        master.bind("<Return>", self.push_final) # binds the return button to return whatever is in the entry bar

        self.countdown_label = tk.Label(master)
        self.count = 3

        self.difficulty = tk.Listbox()
        self.game_difficulty = None

        # These two variables will be initalized as time.time() later in the code
        self.start = 0
        self.end = 0

        self.first_click = True
        self.sentence = ''

        self.spacer1 = tk.Label(master, text="   ") 
        spacer2 = tk.Label(master, text="   ") 
        self.spacer3v1 = tk.Label(master, text="\n\n")
        self.spacer3 = tk.Label(master, text="\n") 
        self.spacer4 = tk.Label(master, text=" \n") 

        self.initialize_introductions()
        self.initialize_difficulties(master, spacer2)

        self.entry_bar = tk.Entry(self.master, width=75)
        self.entry_bar.pack()


        self.startButton = tk.Button(master, text="START", command=self.click_countdown) #clicker begins the game
        self.startButton.pack()
        self.spacer3.pack() 

        
    def initialize_introductions(self):
        intro = "Hello, and welcome to a test of speed!\n To begin, choose your difficulty and press the start button!"
        instructions = tk.Label(self.master, text=intro, fg="red", bg="gray")
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
        self.sentence = scrape_utils.scrape_sentences(self.game_difficulty[0])
        self.sentence_label = tk.Label(master, text=self.sentence, fg="blue")
        self.sentence_label.pack()
        spacer.pack()

    def click_countdown(self):
        if self.first_click:
            self.first_click = False
            self.game_difficulty = self.difficulty.curselection()
            if len(self.game_difficulty) == 0:
                self.game_difficulty = (0,)
            self.countdown_label.pack()
            self.spacer3v1.pack()
            self.countdown(self.count)

    def push_final(self, event): # used for when enter is pressed, returns what is in the entry bar
        if not self.first_click:
            self.end = time.time()
            submission = self.entry_bar.get()
            
            correctness = calculate_score(submission, self.sentence)
            time_used = round(self.end - self.start, 2)

            self.master_finish = tk.Tk()
            self.master_finish.title("Congrats!")
            self.master_finish.geometry("250x200")

            congrats = Finish_Screen(self.master_finish, correctness, time_used)
            self.master_finish.mainloop()

    def countdown(self, count): # for the after-button timer
        self.countdown_label['text'] = count
        if count > 0:
            self.master.after(1000, self.countdown, count - 1)
        elif count <= 0:
            self.countdown_label['text'] = "GO!"
            self.start = time.time()
            self.initialize_sentence(self.master, self.spacer4)

class Finish_Screen:
    def __init__(self, master, correctness, time_used):
        self.master = master
        self.correctness = correctness
        self.time_used = time_used

        self.horray = tk.Label(master, text="CONGRATS!")
        self.horray.pack()

        self.timer = tk.Label(master, text="You took " + str(self.time_used) + " seconds!", fg="blue")
        self.timer.pack()

        self.score = tk.Label(master, text=self.correctness)
        self.score.pack()

def calculate_score(input_string, sentence):
    score = 0
    max_score = len(sentence)

    if len(input_string) > len(sentence):
        score -= len(input_string) - len(sentence)
        input_string = input_string[:len(sentence)]

    for sentence_letter, input_letter in enumerate(input_string):
        if input_letter == sentence[sentence_letter]:
            score += 1

    return str(round((score / max_score) * 100, 2)) + "%"


def main(): 
    root = tk.Tk()
    root.title("Speed Test!")
    root.geometry("1000x400")
    g = GUI_Layout(root)
    root.mainloop()


if __name__ == "__main__":
    main()
