import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

class gui_main_window:
    def __init__(self, master):
        self.kanji_rtk_dictionary = {} 
        self.rtk_kanji_dictionary = {} 
        self.output = []

        self.master = master
        self.frame = ttk.Frame(master)
        self.frame.grid(row=0, column=0, sticky='nesw')

        self.btn_kanji_rtk = ttk.Button(self.frame, text='Kanji -> RTK', command=self.kanji_rtk)
        self.btn_rtk_kanji = ttk.Button(self.frame, text='RTK -> Kanji', command=self.rtk_kanji)
        self.btn_exit = ttk.Button(self.frame, text='Exit', command=self.exit)

        self.btn_kanji_rtk.grid(column=0, row=0)
        self.btn_rtk_kanji.grid(column=0, row=1)
        self.btn_exit.grid(column=0, row=3)

        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)

        self.frame.columnconfigure(1, weight=1)
        self.frame.rowconfigure(1, weight=1)

    def kanji_rtk(self):
        # create dictionary
        with open("rtk_list.csv","r", encoding="utf-8") as rtk_list:
            for line in rtk_list:
                definition = line.split(",")
                self.kanji_rtk_dictionary[definition[0]] = definition[1][:-1]
        
        # get kanji from csv file
        user_kanji_list = []
        user_file = filedialog.askopenfile(mode="r")
        for lines in user_file:
            line = lines.split(",")
            characters = [x for x in line[0]]
            for cha in characters:
                user_kanji_list.append(cha)
        
        # get rtk 
        self.output = []
        for kanji in user_kanji_list:
            if kanji in self.kanji_rtk_dictionary:
                self.output.append([kanji, self.kanji_rtk_dictionary[kanji]])
        
        # write to csv
        self.csv_write()

        return

    def rtk_kanji(self):
        # create dictionary
        with open("rtk_list.csv","r", encoding="utf-8") as rtk_list:
            for line in rtk_list:
                definition = line.split(",")
                self.rtk_kanji_dictionary[definition[1][:-1]] = definition[0]

        # get rtk from csv file
        user_rtk_list = []
        user_file = filedialog.askopenfile(mode="r")
        for lines in user_file:
            line = lines.split(",")
            user_rtk_list.append(line[0][:-1])
        user_rtk_list = user_rtk_list[1:]

        # get kanji
        self.output = []
        failed_list = []
        print(user_rtk_list)
        for rtk in user_rtk_list:
            if rtk in self.rtk_kanji_dictionary:
                self.output.append([self.rtk_kanji_dictionary[rtk], rtk])
            else:
                failed_list.append(rtk)

        # popup window for failed rtk
        tk.Tk().withdraw()
        title = "RTK Error"
        message = "Failed to find kanji for the following RTK definitions: "
        for failed in failed_list:
            message += "\n" + failed
        messagebox.showerror(title, message)

        # write to csv
        self.csv_write()

        return

    def csv_write(self):
        f = filedialog.asksaveasfilename(defaultextension="csv")
        with open(f, "w") as csvfile:
            for line in self.output:
                csvfile.write(line[0] + "," + line[1] + "\n")
        return

    def exit(self):
        self.master.destroy()


root = tk.Tk()
root.title('Kanji Scraper')
window = gui_main_window(root)
root.mainloop()

