"""
Shimsha's Vocabulary
"""


from tkinter import *
from random import randint
import time


# Initialize the index list and index value
index_list = []
index = -1

while True:

    # Get the total number of line in the vocab.txt (In the sense number of words with meaning)
    num_lines = sum(1 for line in open('C:\\Users\\Shimsha\\Documents\\Python Materials\\My projects\\vocabulary\\vocab.txt'))

    # If you have iterated all the words in the file, re initialize index list
    if len(index_list) == num_lines:
        index_list = []

    # Get the index value using randint (You will not get the word and meaning in an order, it will always be shuffled)
    index = randint(0, num_lines - 1)

    # If the random index you get i.e you have already come across the word before, it will be skipped
    if index in index_list:
        index = randint(0, num_lines - 1)
        continue
    else:
        index_list.append(index)

    # Open the file and read the lines one after the other
    file = open('C:\\Users\\Shimsha\\Documents\\Python Materials\\My projects\\vocabulary\\vocab.txt')

    line = file.readlines()

    # Get the line corresponding to the index
    res = line[index]
    res_list = res.split(',')

    # Get the Word and Meaning
    word = res_list[0]
    meaning = res_list[1]

    # Initialize Tkinter Window
    window = Tk()

    window.wm_title("Shimsha's Vocabulary")
    window.geometry("300x100+1230+730")

    # Program the Label for Word and Meaning
    l1 = Label(window, text=word, fg="red", font=("Helvetica", 10)).pack(pady=10)

    l1 = Label(window, text=meaning, fg="green", font=("Arial", 8)).pack(pady=10)

    # Window closes after 10 seconds
    window.after(10000, lambda: window.destroy())
    window.mainloop()

    # Repeat after 30 minutes
    time.sleep(1800)
