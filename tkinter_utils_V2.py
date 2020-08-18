import tkinter as tk
import scrape_utils
import time

root = tk.Tk()
root.title("Speed Test!")
root.geometry("400x400")


class GUI_Layout:
    def __init__(self, master):
        frame1 = tk.Frame(master)
        frame1.pack()

        self.master = master
        master.bind("<Return>", self.push_final) # binds the return button to return whatever is in the entry bar

        spacer1 = tk.Label(master, text="   ") 
        spacer2 = tk.Label(master, text="   ") 
        spacer3 = tk.Label(master, text="\n \n \n \n") 
        self.spacer4 = tk.Label(master, text="\n \n \n \n") 

        self.initialize_introductions(master, spacer1)
        self.initialize_difficulties(master, spacer2)

        self.startButton = tk.Button(master, text="START", command=self.clicker)
        self.startButton.pack()
        spacer3.pack() 

        
    def initialize_introductions(self, master, spacer):
        intro = "Hello, and welcome to a test of speed!\n To begin, choose your difficulty and press the start button!"
        instructions = tk.Label(master, text=intro, fg="red")
        instructions.config(anchor="center")
        instructions.pack()
        spacer.pack()
    
    def initialize_difficulties(self, master, spacer):
        difficulty_choices = ["EASY", "MEDIUM", "HARD"]
        difficulty = tk.Listbox(master, height=3)
        for i in difficulty_choices:
            difficulty.insert(tk.END, i)
        difficulty.pack()
        spacer.pack()

    def initialize_sentence(self, master, spacer):
        sentence = scrape_utils.push_final_sentence()
        sentence_label = tk.Label(master, text=sentence, fg="blue")
        sentence_label.pack()
        spacer.pack()

    def clicker(self):
        three = tk.Label(self.master, text="3", fg="green")
        three.pack()
        time.sleep(1)
        three.pack_forget()

        two = tk.Label(self.master, text="2", fg="yellow")
        two.pack()
        time.sleep(1)
        two.pack_forget()

        one = tk.Label(self.master, text="1", fg="red")
        one.pack()
        time.sleep(1)
        one.pack_forget()

        self.initialize_sentence(self.master, self.spacer4)
        
        self.entry_bar = tk.Entry(self.master)
        self.entry_bar.pack()


    def push_final(self, event): # used for when enter is pressed, returns what is in the entry bar
        submission = self.entry_bar.get()
        print(submission)
        if len(submission) > 3:
            print("nice!!!!")


g = GUI_Layout(root)
root.mainloop()
