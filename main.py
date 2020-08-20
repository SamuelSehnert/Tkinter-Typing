import tkinter as tk
import scrape_utils
import time


class Game_Screen:
    def __init__(self, master):

        self.master = master
        self.master_endgame = None # Will be used to initialize the win screen
        master.bind("<Return>", self.push_final) 

        self.countdown_label = tk.Label(master, font=("Courier", 20))
        self.count = 3 # Countdown after start has been pressed

        self.game_difficulty = None

        self.first_click = True # User isn't allowed to click start twice

        self.spacer1 = tk.Label(master) 
        self.spacer2 = tk.Label(master) 
        self.spacer3v1 = tk.Label(master, text="\n\n")
        self.spacer3 = tk.Label(master, text="\n") 
        self.spacer4 = tk.Label(master, text=" \n") 

        self.initialize_introductions()
        self.initialize_difficulties()

        self.entry_bar = tk.Entry(self.master, width=75)
        self.entry_bar.pack()


        self.startButton = tk.Button(self.master, 
                                    text="START", 
                                    command=self.click_countdown)
        self.startButton.pack()
        self.spacer3.pack() 

        
    def initialize_introductions(self):
        intro = "Hello, and welcome to a test of speed!\n To begin, choose your difficulty and press the start button!\n"
        intro_2 = "Simply select a difficulty and press start.\nGood Luck!!"
        instructions = tk.Label(self.master, 
                                text=intro + intro_2, 
                                fg="orange", 
                                bg="blue", 
                                font=("Courier", 20))
        instructions.config(anchor="center")
        instructions.pack()
        self.spacer1.pack()
    
    def initialize_difficulties(self):
        """
        (0,) = Easy
        (1,) = Medium
        (2,) = Hard
        """
        difficulty_choices = ["EASY", "MEDIUM", "HARD"]
        self.difficulty = tk.Listbox(self.master, height=3)
        for i in difficulty_choices:
            self.difficulty.insert(tk.END, i)
        self.difficulty.pack()
        self.spacer2.pack()

    def click_countdown(self):
        if self.first_click:
            self.first_click = False
            self.game_difficulty = self.difficulty.curselection()
            if len(self.game_difficulty) == 0:
                self.game_difficulty = (0,)
            self.sentence = scrape_utils.scrape_sentences(self.game_difficulty[0])
            self.countdown_label.pack()
            self.spacer3v1.pack()
            self.countdown(self.count)

    def countdown(self, count): 
        self.countdown_label['text'] = count
        if count > 0:
            self.master.after(1000, self.countdown, count - 1)
        elif count <= 0:
            self.countdown_label['text'] = "GO!"
            self.start = time.time()
            self.display_random_sentences()


    def display_random_sentences(self):
        self.sentence_label = tk.Label(self.master, 
                                       text=self.sentence, 
                                       fg="blue", 
                                       font=("Courier", 20), 
                                       wraplength=1000)
        self.sentence_label.pack()
        self.spacer4.pack()


    def push_final(self, event): # used for when enter is pressed, returns what is in the entry bar
        if not self.first_click:
            self.end = time.time()
            submission = self.entry_bar.get()
            
            score = calculate_score(submission, self.sentence)
            time_used = round(self.end - self.start, 2)

            self.master_endgame = tk.Tk()
            self.master_endgame.title("Congrats!")
            self.master_endgame.geometry("250x200")

            congrats = Finish_Screen(self.master_endgame, score, time_used)
            self.master_endgame.mainloop()



class Finish_Screen:
    def __init__(self, master, score, time_used):
        self.master = master
        self.score = score
        self.time_used = time_used

        self.spacer1 = tk.Label(self.master)
        self.spacer2 = tk.Label(self.master, text="\n")

        self.horray = tk.Label(self.master, text="CONGRATS!")
        self.horray.pack()
        self.spacer1.pack()

        self.timer = tk.Label(self.master,
                              text="You took " + str(self.time_used) + " seconds!", 
                              fg="blue")
        self.timer.pack()
        self.spacer2.pack()

        self.score = tk.Label(self.master, text=self.score, font=("Courier", 20))
        self.score.pack()



def calculate_score(input_string, sentence):
    score = 0
    max_score = len(sentence)
    missing_letter = False

    if len(input_string) < len(sentence):
        input_string = list(input_string)
        sentence = list(sentence)
        for sentence_letter, input_letter in enumerate(input_string):
            if sentence_letter > len(input_string) or input_string[sentence_letter] != input_letter:
                input_string.insert(sentence_letter, "0")
            elif input_string[sentence_letter] == input_letter:
                score += 1
        return str(round((score / max_score) * 100, 2)) + "%"

    
    else:
        if len(input_string) > len(sentence):
            score -= (len(input_string) - len(sentence))
            input_string = input_string[:len(sentence)]


        for sentence_letter, input_letter in enumerate(input_string):
            if input_letter == sentence[sentence_letter]:
                score += 1

        return str(round((score / max_score) * 100, 2)) + "%"



def main(): 
    root = tk.Tk()
    root.title("Speed Test!")
    root.geometry("1000x600")
    Game_Screen(root)
    root.mainloop()


if __name__ == "__main__":
    main()
