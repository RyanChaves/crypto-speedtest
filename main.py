#use crypto api that takes descriptions from cryptos and makes user to key speed test on them

#have a gui that says "Begin once clicked, start time and show text, once user is done enterer, he hits done, program checks if correct then takes currenttime-timeofstart

#for every letter user types, change text color the script

#calculate words per minute, take script, count words divide by time taken?
from tkinter import *
from tkinter import messagebox

import time


YELLOW = "#40A2B9"
RED="#CC6E6E"
FONT_NAME = "Courier"
FONT_SIZE= 20


root = Tk()
root.title("Crypto Typing Speed Test")
root.config(padx=100, pady=50,bg=YELLOW)
root.geometry("700x500")

root.minsize(700,500)
root.maxsize(700,500)

start_time=""
script = "Bitcoin is a peer-to-peer online currency."
split_script = script.split()


current_word = ""
#String -> whenever corret char is entered, append that to user_correct_input, when user_correct_input == current_word, move on to next word.
user_correct_input = ""
letter_count= 0
word_count=0
script_label = Text(root, height=1, width=20,  font=(FONT_NAME, FONT_SIZE, "bold"), bg=YELLOW, bd=0)
script_label.tag_configure("center", justify='center')
text_entry = Text(root, font=(FONT_NAME, FONT_SIZE, "bold"), height=1, width=20)




#change to only show one word at a time (every time a key is entered, highlight part of text green)
def begin_game():
    global current_word, start_time
    start_btn.place_forget()

    title_label = Label(root, text="Crypto",bg=YELLOW,font=(FONT_NAME, FONT_SIZE, "bold"), justify='center')
    title_label.place(relx=0.5, rely=.2,anchor= CENTER)

    #begin with first word in split_script
    script_label.insert(1.0,f"{split_script[0]}")
    script_label.place(relx=0.5, rely=0.5, anchor=CENTER)
    #script_label.tag_add("center", "1.0", "end")

    current_word=split_script[0]

    text_entry.bind("<KeyRelease>", check_key)
    text_entry.place(relx=0.5, rely=.9,anchor= CENTER)
    text_entry.focus()

    start_time = time.time()


    #current_word = split_script[word_count]

def check_key(key_pressed):
    global user_correct_input, letter_count, script_label, current_word, word_count, text_entry
    #time.sleep(0.3)
    user_correct_input=text_entry.get(1.0,END).strip('\n')
    #print(user_correct_input)
    if key_pressed.char == current_word[letter_count]:
        #user_correct_input += key_pressed.char
        #create tag to highlight entered text
        script_label.tag_add("highlight","1.0", f"1.{letter_count+1}")
        script_label.tag_config("highlight", background=RED)

        #check if word complete by comparing what is in text_entry
        print(f"{current_word}{user_correct_input}1")
        #print(user_correct_input)
        if current_word == user_correct_input:
            word_count += 1

            # check if we are done script
            if word_count == len(split_script):
                print(f"done, that took: {time.time()-start_time}")
                #show dialog box to typing speed
                messagebox.showinfo("Results", f"You typed {len(split_script)} words in {time.time()-start_time} seconds. WPM: {(len(split_script)*60)/(time.time()-start_time)}")
            else:
                user_correct_input=""
                current_word=split_script[word_count]
                script_label.delete(1.0,END)
                script_label.insert(INSERT,f"{current_word}")
                letter_count=0
                #delete users input
                text_entry.delete(1.0, END)



        else:

            letter_count+=1
    else:
        #the letter that was entered is incorrect
        text_entry.delete(f"1.{letter_count}",END)

start_btn = Button(root, text="Start!",font=(FONT_NAME, FONT_SIZE, "bold"),command=begin_game)
start_btn.place(relx=.5, rely=.5,anchor= CENTER)



root.mainloop()