--------------------------------------------
Author : Jake Isaac Harvey / JackInDaBean
--------------------------------------------

Copyright (C) Jake Isaac Harvey 2025

---------------------------------
CSV Employee Timesheet Calculator:
---------------------------------
The goal of this program is to be able to open a CSV file, iterate through the different employee names from within; collect and add up their hours worked whislt subtracting the break times for each employee, outputting a file that has the employee name and their hours worked.

---------------------------------
Reason for creation:
---------------------------------
This was a request from my boss at a restaurant so I wrote this to improve the efficieny of the accounting each week, this saves him roughly 15-30 minutes of admin work, I sold him this software and it is still in active use.

-------------
How It's Made:
-------------
Tech used: Python, Tkinter, Pandas, sys

-------------
Optimisations:
-------------
Used the groupby() method within pandas to cut down a 30 line algorithm to a 4 line module - Most of the pandas libray is responsible for the optimisations using methods such as groupby(), sum().

---------------
Lessons Learned:
---------------
Learnt to read the documentation regarding a library before attempting to use it - spent a week writing a long algorithm to sort through two columns simultaneously and grab data from both which was completely unnecessary as already pandas contains a function that does said task.

Learnt how to use Tkinter to create an incredibly basic GUI window, with buttons - also learnt to use openfile and askfilesavename dialogues to get the user to open and save files through a mouse click as opposed to a command line input.

Learnt how to setup a class for GUI and call it in a seperate module.

Learnt how to sucessefully read in and write out to files of CSV and TXT types.

Learnt how to setup modules and call them into eachother, with a few lines of code in main so that it cannot be called.
