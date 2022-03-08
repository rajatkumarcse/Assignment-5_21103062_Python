# Question ---> 2
# To create a GUI-based Calendar application using Tkinter module

# import all methods and classes from the tkinter 
from hashlib import new
from tkinter import *
# import calender module
import calendar
from tkinter import font

# Function for showing the calender of the given year
def showCal():
    # Create a GUI window
    new_gui = Tk()

    # Set background colour of GUI window
    new_gui.config(background= "white")
    # Set the name of tkinter GUI window
    new_gui.title("CALENDAR")
    # Set the configuration of GUI window
    new_gui.geometry("500x600")

    # get method returns current text as string
    fetch_year = int(year_field.get())

    # calendar method of calendar module return
    # the calendar of the given year 
    cal_content = calendar.calendar(fetch_year)

    # Create a label for showing the content of the calendar
    cal_year = Label(new_gui, text= cal_content, font="Consolas 10 bold")

    # grid method is used for placing 
    # the widgets at respective positions
    # in table like structure
    cal_year.grid(row= 5, column= 1, padx= 20)

    # start the GUI
    new_gui.mainloop()

# Driver Code for this question
if __name__ == "__main__":
    # Create a GUI window
    gui = Tk()

    # Set the background colour of GUI window
    gui.config(background= "white")
    # set the name of tkinter GUI window
    gui.title("CALENDAR")
    # set the configuration of GUI window
    gui.geometry("250x140")

    # Create a CALENDAR : Label with specified font and size 
    cal = Label(gui, text= "CALENDAR", bg= "dark gray", font= ("times", 28, "bold"))

    # Create a Enter Year : Label
    year = Label(gui, text= "Enter Year", bg= "light green")

    # Create a text entry box for filling or typing the information
    year_field = Entry(gui)

    # Create a show calendar button and attached to showCal function
    Show = Button(gui, text= "Show Calender", fg="Black", bg="Red", command= showCal) 

    # Create a Exit button and attached to exit function
    Exit = Button(gui, text= "Exit", fg= "Black", bg= "Red", command= exit)

    # grid method is used for placing the widgets at respective positions in table like structure
    cal.grid(row= 1, column= 1)
    year.grid(row= 2, column= 1)
    year_field.grid(row= 3, column= 1)
    Show.grid(row= 4, column= 1)
    Exit.grid(row= 6, column= 1)

    # start the GUI
    gui.mainloop()
