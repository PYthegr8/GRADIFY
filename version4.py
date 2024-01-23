#USE OOP
import tkinter as tk
from tkinter import ttk
import customtkinter
import stats
import pylab as plt

class GradiFYApp:
    def __init__(self, root):
        self.root = root
        self.setup_ui()

    def setup_ui(self):
        self.root.geometry("700x500")
        self.root.title("GradiFY")
        customtkinter.set_appearance_mode("system")

        self.frame = customtkinter.CTkFrame(master=self.root, width=700, height=700)
        self.frame.grid(row=1, column=1)
        customtkinter.CTkLabel(master=self.frame, text="Welcome to GradiFY", font=("Lora", 50, "bold"),
                                justify="left").pack(expand=True, pady=(75, 50))
        self.Name = customtkinter.CTkEntry(master=self.frame, placeholder_text="Enter your Name", width=400)
        self.Name.pack(expand=True, pady=15, padx=150)
        self.Course = customtkinter.CTkEntry(master=self.frame, placeholder_text="Enter your Course Name", width=400)
        self.Course.pack(expand=True, pady=15, padx=20)
        self.Number = customtkinter.CTkEntry(master=self.frame, placeholder_text="Enter Number of students", width=400)
        self.Number.pack(expand=True, pady=15, padx=20)
        customtkinter.CTkButton(master=self.frame, command=self.open_entry_portal, hover=True,
                                corner_radius=25, fg_color="#4cb69f", text="ENTER GRADES", text_color="white",
                                font=("Aharoni", 24, "bold")).pack(expand=True, pady=(50, 300), padx=30)

    def open_entry_portal(self):
        second_root = tk.Toplevel(self.root)
        customtkinter.set_appearance_mode("system")
        second_root.geometry("700x400")
        second_root.title("GradiFY Grade Portal")

        frame = customtkinter.CTkFrame(second_root)
        frame.pack(fill="both", expand=True)

        canvas = customtkinter.CTkCanvas(frame)
        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
        scrollable_frame = customtkinter.CTkFrame(canvas)

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        num_of_students = int(self.Number.get())
        user_name = self.Name.get()
        course_name = self.Course.get()

        grade_label = customtkinter.CTkLabel(frame, text=f"Hi {user_name}, GradiFY {course_name} class",
                                             font=("Lora", 40, "bold"), justify="left")
        grade_label.pack(side="top", anchor="center")

        self.name_entries = []
        self.grade_entries = []

        for i in range(num_of_students):
            name_entry = customtkinter.CTkEntry(scrollable_frame, placeholder_text=f"{i + 1}." + "Enter Student Name",
                                                font=("Aharoni", 12, "bold"))
            name_entry.grid(row=i + 1, column=1, padx=100, pady=5)
            self.name_entries.append(name_entry)

            grade_entry = customtkinter.CTkEntry(scrollable_frame, placeholder_text="Enter Student Grade")
            grade_entry.grid(row=i + 1, column=2, padx=100, pady=5)
            self.grade_entries.append(grade_entry)

        submit_button = customtkinter.CTkButton(frame, hover=True, height=40, corner_radius=25, fg_color="#4cb69f",
                                                 text="SUBMIT", command=lambda: [self.submit_data(), self.display_statistics()])
        submit_button.pack(side="bottom")

        canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    def submit_data(self):
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
        student_grades = self.submit_data()
        grades = student_grades['Grade']
        name = student_grades['Name']

        stats_window = tk.Tk()
        stats_window.title("Statistics Display")
        customtkinter.set_appearance_mode("system")
        course_name = self.Course.get()

        stats1_label = customtkinter.CTkLabel(stats_window, text=f"Grade Statistics for :{course_name}", text_color="black", font=("Lora", 20, "bold"))
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

        graph_types = ["Bar Chart", "Boxplot", "Line Chart", "Scatter Plot"]

        for graph_type in graph_types:
            radio_button = customtkinter.CTkRadioButton(stats_window, text=graph_type, text_color="black", value=graph_type, command=lambda t=graph_type: self.plot_selected_graph(t, grades))
            radio_button.pack(anchor="center")

        self.root.destroy()

    def plot_selected_graph(self, graph_type, grades):
        
        if graph_type == "Bar Chart":
            self.plot_bar_chart(grades)

        if graph_type == "Boxplot":
            self.plot_boxplot(grades)

        elif graph_type == "Line Chart":
            self.plot_line_chart(grades)

        elif graph_type == "Scatter Plot":
            self.plot_scatter_plot(grades)

    def plot_bar_chart(self, grades):
        # Create a bar chart using matplotlib
        names = [name.get() for name in self.name_entries]
        plt.bar(names, grades, color='blue')
        plt.xticks(rotation=45, ha='right')
        plt.title("Bar Chart")
        plt.xlabel("Students")
        plt.ylabel("Grades")
        plt.show()

    def plot_line_chart(self, grades):
        # Create a line chart using matplotlib
        names = [name.get() for name in self.name_entries]
        plt.plot(names, grades, marker='o')
        plt.xticks(rotation=45, ha='right')
        plt.title("Line Chart")
        plt.xlabel("Student")
        plt.ylabel("Grades")
        plt.show()

    def plot_scatter_plot(self, grades):
        # Create a scatter plot using matplotlib
        names = [name.get() for name in self.name_entries]
        plt.scatter(names, grades)
        plt.xticks(rotation=45, ha='right')
        plt.title("Scatter Plot")
        plt.xlabel("Student")
        plt.ylabel("Grades")
        plt.show()


def main():
    root = tk.Tk()
    app = GradiFYApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
