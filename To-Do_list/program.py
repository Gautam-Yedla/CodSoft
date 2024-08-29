import tkinter as tk
from tkinter import *

root = Tk()
root.title("TO-DO-LIST")



root.geometry("400x650+400+100")
root.resizable(True,True)

task_list = []

def addTask():
  
  task = task_entry.get()
  task_entry.delete(0, END)
  
  if task:
    with open("tasklist.txt", 'a') as taskfile:
      taskfile.write(f"\n{task}")
    task_list.append(task)
    listbox.insert( END, task)
    
    

def deleteTask():
  global task_list
  task = str(listbox.get(ANCHOR))
  if task in task_list:
    with open("tasklist.txt", 'w') as taskfile:
      for task in task_list:
        taskfile.write(task+"\n")
        
    listbox.delete( ANCHOR)
          
   

def openTaskFile():
  
  try:
    
      global task_list
      with open("tasklist.txt", "r") as taskfile:
        tasks = taskfile.readlines()
    
      for task in tasks:
          if task != '\n':
            task_list.append(task)
            listbox.insert(END, task)
    
  except:
    file = open('tasklist.txt', 'w')
    file.close()



""" <<<<<<<<<........... ICON .............>>>>>>>>>>>>>>>> """

img_icon = PhotoImage(file="pics/task.png")
root.iconphoto(True,img_icon)


""" <<<<<<<<<........... TOP_BAR .............>>>>>>>>>>>>>>>> """

top_img = PhotoImage(file="pics/topbar.png")
Label(root,image=top_img).pack()

dock_img = PhotoImage(file="pics/dock.png")
Label(root,image=dock_img,bg="#32405b").place(x=30,y=25)

note_img = PhotoImage(file="pics/task.png")
Label(root,image=note_img,bg="#32405b").place(x=340,y=25)

heading = Label(root,text="ALL TASKS",font = "arial 20 bold", fg = "white", bg = "#32405b")
heading.place(x = 130, y = 20)



""" <<<<<<<<<........... MAIN .............>>>>>>>>>>>>>>>> """

frame = Frame(root, width = 400, height = 50, bg = "white")
frame.place(x = 0, y = 180)

task = StringVar()
task_entry = Entry(frame, width = 18, font = "arial 20 ", bg = "white")
task_entry.place(x = 10, y = 7)
task_entry.focus()

button = Button(frame, text = "ADD", font = "arial 20 bold", width =6, bg = "#5a95ff", fg = "#fff", bd = 0, command = addTask)
button.place(x = 300, y = 0)


""" <<<<<<<<<........... LIST_BOX .............>>>>>>>>>>>>>>>> """

frame1 = Frame(root, bd = 3, width = 700, height = 280, bg = "#32405b")
frame1.pack(pady = (160,0))

listbox = Listbox(frame1,font = ('arial', 12), width = 40, height = 16, bg = "#32405b", fg = "white", cursor = "hand2", selectbackground = "#5a95ff")
listbox.pack(side = LEFT, fill = BOTH, padx = 2)
scrollbar = Scrollbar(frame1)
scrollbar.pack(side = RIGHT, fill = BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command = listbox.yview)


openTaskFile()

""" <<<<<<<<<........... DELETE .............>>>>>>>>>>>>>>>> """

delete_icon = PhotoImage(file = "pics/delete.png")
Button(root, image = delete_icon, bd = 0, command=deleteTask).pack(side = BOTTOM, pady = 13)



root.mainloop()