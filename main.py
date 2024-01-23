"""
    Papa Yaw Owusu Nti
    CS152B
    PROJECT 10
    7th December 2023
    GradiFY - Student Score Management and Analysis Tool

    This program provides a graphical user interface (GUI) for entering student grade scores,
    displaying statistics, and plotting various graphs based on the data.
    
    Instructions:
    
   - Run the script to launch GradiFY. Input your name, course, and student count.
   - Click "ENTER GRADES."
   - In the new window, add student names and grades. Click "SUBMIT" when done.
   - See score statistics instantly.
   - Choose Bar, Box, Line, or Scatter plots to explore different graphs
   - Close the window to exit.
Enjoy using GradiFY!

"""

import tkinter as tk
from tkinter import ttk
import customtkinter
import stats
import pylab as plt

class GradiFYApp:
    """Class for the main GradiFY application."""
    def __init__(self, root):
        """Initialize GradiFYApp instance."""
        self.root = root
        self.setup_ui()

    def setup_ui(self):
        """Set up the user interface for the GradiFY application."""
        self.root.geometry("700x500")
        self.root.title("GradiFY")
        customtkinter.set_appearance_mode("system")
        

        # Create the main frame
        self.frame = customtkinter.CTkFrame(master=self.root, width=700, height=700)
        self.frame.grid(row=1, column=1)
        customtkinter.CTkLabel(master=self.frame, text="Welcome to GradiFY", font=("Lora", 50, "bold"),
                                justify="left").pack(expand=True, pady=(75, 50))
        
        
        # Add welcome label and entry widgets
        self.Name = customtkinter.CTkEntry(master=self.frame, placeholder_text="Enter your Name", width=400)
        self.Name.pack(expand=True, pady=15, padx=150)
        self.Course = customtkinter.CTkEntry(master=self.frame, placeholder_text="Enter your Course Name", width=400)
        self.Course.pack(expand=True, pady=15, padx=20)
        self.Number = customtkinter.CTkEntry(master=self.frame, placeholder_text="Enter Number of students", width=400)
        self.Number.pack(expand=True, pady=15, padx=20)
        
        
        # Add button for entering grades
        customtkinter.CTkButton(master=self.frame, command=self.open_entry_portal, hover=True,
                                corner_radius=25, fg_color="#4cb69f", text="ENTER GRADES", text_color="white",
                                font=("Aharoni", 24, "bold")).pack(expand=True, pady=(50, 300), padx=30)

    def open_entry_portal(self):
        """Open a new window to enter student grades."""
        
        # Create a new top-level window 
        second_root = tk.Toplevel(self.root)
        customtkinter.set_appearance_mode("system")
        second_root.geometry("700x400")
        second_root.title("GradiFY Grade Portal")
        
        # Create a frame
        frame = customtkinter.CTkFrame(second_root)
        frame.pack(fill="both", expand=True)

        # Create a canvas to allow scrolling
        canvas = customtkinter.CTkCanvas(frame)
        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
        scrollable_frame = customtkinter.CTkFrame(canvas)

        # Configure the canvas and frame 
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        #Retrieve user information
        num_of_students = int(self.Number.get())
        user_name = self.Name.get()
        course_name = self.Course.get()


        # Display a personalized greeting label
        grade_label = customtkinter.CTkLabel(frame, text=f"Hi {user_name}, GradiFY {course_name} class",
                                             font=("Lora", 40, "bold"), justify="left")
        grade_label.pack(side="top", anchor="center")

        # Initialize lists to store name and grade entry
        self.name_entries = []
        self.grade_entries = []
        
        # Create entry widgets for each student
        for i in range(num_of_students):
            name_entry = customtkinter.CTkEntry(scrollable_frame, placeholder_text=f"{i + 1}." + "Enter Student Name",
                                                font=("Aharoni", 12, "bold"))
            name_entry.grid(row=i + 1, column=1, padx=100, pady=5)
            self.name_entries.append(name_entry)

            grade_entry = customtkinter.CTkEntry(scrollable_frame, placeholder_text="Enter Student Grade")
            grade_entry.grid(row=i + 1, column=2, padx=100, pady=5)
            self.grade_entries.append(grade_entry)
            
        # Create a submit button 
        submit_button = customtkinter.CTkButton(frame, hover=True, height=40, corner_radius=25, fg_color="#4cb69f",
                                                 text="SUBMIT", command=lambda: [self.submit_data(), self.display_statistics()])
        submit_button.pack(side="bottom")

        #pack configured scrollbar in window
        canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    def submit_data(self):
        """Submit entered student data and save it to a CSV file."""
        with open("student_grades.csv", "w") as fp:
            fp.write("Name,Grade\n")
            num_of_students = int(self.Number.get())
            student_data = {'Name': [], 'Grade': []}
            for i in range(num_of_students):
                name = self.name_entries[i].get()
                grade = self.grade_entries[i].get()
                student_data['Name'].append(name)
                student_data['Grade'].append(float(grade))
                fp.write(f"{name},{grade}\n")
        return student_data

    def display_statistics(self):
        """Display statistics for entered student grades."""
        stats_display = StatisticsDisplayApp(self.root, self.Course.get(), self.name_entries, self.grade_entries)
        stats_display.display()


class StatisticsDisplayApp(GradiFYApp):
    """Class for displaying statistics and plotting graphs based on student grades."""

    def __init__(self, root, course_name, name_entries, grade_entries):
        """Initialize StatisticsDisplayApp instance."""
        super().__init__(root)
        self.course_name = course_name
        self.name_entries = name_entries
        self.grade_entries = grade_entries

    def display(self):
        """Display statistics and provide options for graph plotting."""
        stats_window = tk.Tk()
        stats_window.title("Statistics Display")
        customtkinter.set_appearance_mode("system")

        stats1_label = customtkinter.CTkLabel(stats_window, text=f"Grade Statistics for :{self.course_name}",
                                              text_color="black", font=("Lora", 20, "bold"))
        stats1_label.pack()

        
        grades = [float(grade.get()) for grade in self.grade_entries]
        name = [name.get() for name in self.name_entries]
        

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

        graph_types = ["Bar Chart", "Boxplot", "Line Chart", "Scatter Plot"]

        for graph_type in graph_types:
            radio_button = customtkinter.CTkRadioButton(stats_window, text=graph_type, text_color="black",
                                                        value=graph_type, command=lambda t=graph_type: self.plot_selected_graph(t,name, grades))
            radio_button.pack(anchor="center")

        self.root.destroy()
    
   
    def plot_selected_graph(self, graph_type, name_entries, grades):
        """Plot the selected graph type."""
        self.name_entries = name_entries
        
        if graph_type == "Bar Chart":
            self.plot_bar_chart(self.name_entries,grades)

        if graph_type == "Boxplot":
            self.plot_boxplot(grades)

        elif graph_type == "Line Chart":
            self.plot_line_chart(self.name_entries,grades)

        elif graph_type == "Scatter Plot":
            self.plot_scatter_plot(self.name_entries,grades)

    def plot_bar_chart(self,name, grades):
        """Plot a bar chart based on student names and grades."""
        plt.bar(name, grades, color='blue')
        plt.title("Bar Chart")
        plt.xlabel("Students")
        plt.ylabel("Grades")
        plt.show()

    def plot_boxplot(self, grades):
        """Plot a boxplot based on student grades."""
        plt.boxplot(grades)
        plt.title("Boxplot")
        plt.ylabel("Grades")
        plt.show()

    def plot_line_chart(self,name, grades):
        """Plot a line chart based on student names and grades."""
        plt.plot(name, grades)
        plt.title("Line Chart")
        plt.xlabel("Student")
        plt.ylabel("Grades")
        plt.show()

    def plot_scatter_plot(self,name, grades):
        """Plot a scatter plot based on student names and grades."""
        plt.scatter(name, grades)
        plt.title("Scatter Plot")
        plt.xlabel("Student")
        plt.ylabel("Grades")
        plt.show()


def main():
    """Main function to run the GradiFY application."""
    root = tk.Tk()
    app = GradiFYApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
