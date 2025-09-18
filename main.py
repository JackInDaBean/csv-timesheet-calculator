from modules import gui_module as gui
from modules import csv_operations as csvcalc

if __name__ == "__main__":

    programWindow = gui.programGUI("CSV Calculator", 200, 150)
    programWindow.run()

    finalStaffHours = csvcalc.calculate_csv_data(gui.csv_file_path, 'staff', 'shift time ex. break (hr)') # Send the CSV file path to the iteration module.
    gui.save_text_file(str(finalStaffHours))