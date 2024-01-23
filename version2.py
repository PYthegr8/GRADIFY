#use functional programming then convert later
#add subject
#create the tkinter window


import tkinter as tk
from tkinter import ttk
import customtkinter
import stats

customtkinter.set_appearance_mode("system")

def open_EntryPortal():
    # Create a Toplevel window for the entry portal
    secondroot = tk.Toplevel(firstroot)
    customtkinter.set_appearance_mode("system")
    secondroot.geometry("700x400")
    secondroot.title("GradiFY Grade Portal")

    # firstroot.destroy()
    user_name, user_course, num_of_students = getUserInfo()

    def submit_data():
        # csv manipulation
        with open("student_grades.csv", "w") as fp:
            fp.write("Name,Grade\n")
            student_data = {'Name': [], 'Grade': []}
            for i in range(num_of_students):
                name = name_entries[i].get()
                grade = grade_entries[i].get()
                student_data['Name'].append(name)
                student_data['Grade'].append(grade)
                fp.write(f"{name},{grade}\n")

    
    # Create a frame to hold the content
    frame = customtkinter.CTkFrame(secondroot)
    frame.pack(fill="both", expand=True)


    # Create a canvas with a vertical scrollbar
    canvas = customtkinter.CTkCanvas(frame)
    scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
    scrollable_frame = customtkinter.CTkFrame(canvas,bg_color="black")
    # scrollable_frame = ttk.Frame(canvas)
    
    
    

    # Configure the canvas
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    # Create grid for Name and Grade entries
    name_entries = []
    grade_entries = []

    for i in range(int(num_of_students)):
        grade_label = customtkinter.CTkLabel(scrollable_frame, text="GradiFY", font=("Lora", 40, "bold"),
                                             justify="left")
        grade_label.grid(row=0, column=2, padx=40, pady=5)

        name_entry = customtkinter.CTkEntry(scrollable_frame, placeholder_text=f"{i + 1}." + "Enter Student Name",
                                            font=("Aharoni", 12, "bold"))
        name_entry.grid(row=i + 1, column=1, padx=40, pady=5)
        name_entries.append(name_entry)

        grade_entry = customtkinter.CTkEntry(scrollable_frame, placeholder_text="Enter Student Grade")
        grade_entry.grid(row=i + 1, column=3, padx=40, pady=5)
        grade_entries.append(grade_entry)

    # Submit button
    submit_button = customtkinter.CTkButton(scrollable_frame, hover=True, corner_radius=25, fg_color="#4cb69f",
                                             text="SUBMIT", command=submit_data)
    submit_button.grid(row=num_of_students + 1, column=2, padx=10, pady=10)

    # Bind the canvas to the scrollbar and configure the scrollbar
    canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
    
    
    

def getUserInfo():
    UserName = Name.get()
    UserCourse = Course.get()
    Num_of_students = int( Number.get())
    return UserName, UserCourse, Num_of_students

firstroot = tk.Tk()  # create the Tk window
firstroot.geometry("700x500")
firstroot.title("GradiFY")
customtkinter.set_appearance_mode("system")

frame = customtkinter.CTkFrame(master=firstroot, width=700, height=700)
frame.grid(row=1, column=1)
customtkinter.CTkLabel(master=frame, text="Welcome to GradiFY", font=("Lora", 50, "bold"),
                        justify="left").pack(expand=True, pady=(75, 50))
Name = customtkinter.CTkEntry(master=frame, placeholder_text="Enter your Name", width=400)
Name.pack(expand=True, pady=15, padx=150)
Course = customtkinter.CTkEntry(master=frame, placeholder_text="Enter your Course Name", width=400)
Course.pack(expand=True, pady=15, padx=20)
Number = customtkinter.CTkEntry(master=frame, placeholder_text="Enter Number of students", width=400)
Number.pack(expand=True, pady=15, padx=20)
customtkinter.CTkButton(master=frame, command=lambda: [getUserInfo(), open_EntryPortal()], hover=True,
                         corner_radius=25, fg_color="#4cb69f", text="ENTER GRADES", text_color="white",
                         font=("Aharoni", 24, "bold")).pack(expand=True, pady=(50, 300), padx=30)

firstroot.mainloop()
