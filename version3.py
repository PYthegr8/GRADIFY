#add entry portal and statistics portal


import tkinter as tk
from tkinter import ttk
import customtkinter
import stats 
import pylab as plt

customtkinter.set_appearance_mode("system")


def submit_data():
    # csv manipulation
    with open("student_grades.csv", "w") as fp:
        fp.write("Name,Grade\n")
        num_of_students = int(Number.get())
        student_data = {'Name': [], 'Grade': []}
        for i in range(num_of_students):
            name = name_entries[i].get()
            grade = grade_entries[i].get()
            student_data['Name'].append(name)
            student_data['Grade'].append(float(grade))
            fp.write(f"{name},{grade}\n")
    return student_data


def display_statistics():
    student_grades = submit_data()
    grades = student_grades['Grade']
    name = student_grades['Name']
    # Create a new Tkinter window for statistics display
    stats_window = tk.Tk()
    stats_window.title("Statistics Display")
    customtkinter.set_appearance_mode("system")
    course_name = Course.get()
    # Display statistics
    stats1_label = customtkinter.CTkLabel(stats_window, text=f"Grade Statistics for :{course_name}", text_color="black",font=("Lora", 20, "bold"))
    stats1_label.pack()

    stats_text = f'''
    The Average Grade was: {stats.mean(grades):.2f}
    The Lowest Grade was: {stats.min(grades)}
    The Highest Grade was: {stats.max(grades)}
    Standard Deviation: {stats.standard_dev(grades)}
    Variance: {stats.variance(grades):.2f}
    Median Score: {stats.median(grades)}
    '''
    
    stats_label = tk.Label(stats_window, text="", font=("Arial", 14))
    stats_label.config(text=stats_text)
    stats_label.pack(pady=10)

    # Create radio buttons for graph type selection
    graph_types = [ "Bar Chart", "Boxplot", "Line Chart", "Scatter Plot"]
    
    for graph_type in graph_types:
        radio_button = customtkinter.CTkRadioButton(stats_window, text=graph_type, text_color="black" ,value=graph_type, command=lambda t=graph_type: plot_selected_graph(t, grades))
        radio_button.pack(anchor="center")

    def plot_selected_graph(graph_type,grades):

        if graph_type == "Bar Chart":
            plot_bar_chart(name, grades)
          
        if graph_type == "Boxplot":
            plot_boxplot(grades)
               
        elif graph_type == "Line Chart":
            plot_line_chart(name,grades)
           
        elif graph_type == "Scatter Plot":
            plot_scatter_plot(name,grades)
            
    firstroot.destroy()
    
def plot_bar_chart(names, grades):
    # Create a bar chart using matplotlib
    plt.bar(names, grades, color='blue')
    plt.title("Bar Chart")
    plt.xlabel("Students")
    plt.ylabel("Grades")
    plt.show()

def plot_boxplot(grades):
    # Create a boxplot using matplotlib
    plt.boxplot(grades)
    plt.title("Boxplot")
    plt.ylabel("Grades")
    plt.show()

def plot_line_chart(name,grades):
    # Create a line chart using matplotlib
    plt.plot(name,grades)
    plt.title("Line Chart")
    plt.xlabel("Student")
    plt.ylabel("Grades")
    plt.show()
    
def plot_scatter_plot(name,grades):
    # Create a scatter plot using matplotlib
    plt.scatter(name,grades)
    plt.title("Scatter Plot")
    plt.xlabel("Student")
    plt.ylabel("Grades")
    plt.show()



def open_EntryPortal(firstroot):
    # Create a Toplevel window for the entry portal
    secondroot = tk.Toplevel(firstroot)
    customtkinter.set_appearance_mode("system")
    secondroot.geometry("700x400")
    secondroot.title("GradiFY Grade Portal")

    # Create a frame to hold the content
    frame = customtkinter.CTkFrame(secondroot)
    frame.pack(fill="both", expand=True)

    # Create a canvas with a vertical scrollbar
    canvas = customtkinter.CTkCanvas(frame)
    scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
    scrollable_frame = customtkinter.CTkFrame(canvas)

    # Configure the canvas
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    # Create grid for Name and Grade entries
    global name_entries
    name_entries = []
    global grade_entries
    grade_entries = []

    
    num_of_students = int(Number.get())
    UserName = Name.get()
    coursename = Course.get()

    # Grade label always at the top
    grade_label = customtkinter.CTkLabel(frame, text=f"Hi {UserName}, GradiFY {coursename} class", font=("Lora", 40, "bold"), justify="left")
    grade_label.pack(side="top", anchor="center")

    for i in range(num_of_students):
        name_entry = customtkinter.CTkEntry(scrollable_frame, placeholder_text=f"{i + 1}." + "Enter Student Name",
                                            font=("Aharoni", 12, "bold"))
        name_entry.grid(row=i + 1, column=1, padx=100, pady=5)
        name_entries.append(name_entry)

        grade_entry = customtkinter.CTkEntry(scrollable_frame, placeholder_text="Enter Student Grade")
        grade_entry.grid(row=i + 1, column=2, padx=100, pady=5)
        grade_entries.append(grade_entry)

    
    # Submit button
    submit_button = customtkinter.CTkButton(frame, hover=True,height=40, corner_radius=25, fg_color="#4cb69f",
                                             text="SUBMIT", command=lambda: [submit_data(), display_statistics()])
    submit_button.pack(side="bottom")

    # Bind the canvas to the scrollbar and configure the scrollbar
    canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")


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
customtkinter.CTkButton(master=frame, command=lambda: [ open_EntryPortal(firstroot)], hover=True,
                         corner_radius=25, fg_color="#4cb69f", text="ENTER GRADES", text_color="white",
                         font=("Aharoni", 24, "bold")).pack(expand=True, pady=(50, 300), padx=30)

firstroot.mainloop()
