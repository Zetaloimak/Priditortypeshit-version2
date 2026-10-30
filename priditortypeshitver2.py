# made by kasidit rakphan m.2.16 no.17
# Tesaban6

lazy import os
lazy import sqlite3
lazy import time
lazy from tkinter import messagebox
lazy import PTDgui as pdg
lazy import PTDtext as pdt

# Database setup
conn = sqlite3.connect("priditor.db")
conn.commit()

title = "Pr1diT0r7typeShit"

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def opening():
    print("======  \n game studio.h\n    ======")
    time.sleep(2)
    for _ in range(4):
        time.sleep(1)
        print(".", end="", flush=True)
    clear_screen()
    time.sleep(1)

    code = input("please input the code :")
    if code == "theptd173":
        print("the code complete")
        time.sleep(0.5)
        print("please wait for the operetion")
        time.sleep(1)
        operation()
    else:
        messagebox.showerror("ERROR", "0x80070005\nERROR_ACCESS_DENIED")
        clear_screen()


def operation():
    for _ in range(4):
        time.sleep(0.5)
        print(".", end="", flush=True)
    print("\ndownload complete")
    time.sleep(5)
    clear_screen()
    pdt.user()
    start()


def luvfocus():
    print("I love focus")
    time.sleep(2)
    clear_screen()


def start():
    The_count = 0
    while True:
        clear_screen()
        thepro = input("Pr1diT0r7typeShit\n;;2569;;\n(NEW VERSION 1.5)\nwhat your service sir?\n:")

        if thepro == "openthe_user" and The_count == 1:
            pdg.devgui()
        elif thepro == "cls173":
            if The_count == 1:
                openask = messagebox.askokcancel("PDSserver", "Do you sure you wanna close server?")
                if openask == True:
                    print("see u come back")
                    messagebox.showinfo("PDSserver", "see u come back")
                    time.sleep(0.5)
                    break
            else:
                justask = messagebox.askokcancel("PDSserver", "Do you sure you wanna leave?")
                if justask == True:
                    print("see u come back")
                    messagebox.showinfo("PDSserver", "see u come back")
                    time.sleep(0.5)
                    break
        elif thepro == "Zetaluvfocus" and The_count == 1:
            luvfocus()
        elif thepro == "server,iop.sss":
            if The_count == 1:
                messagebox.showerror("PDSserver", "You aready open the server!!")
            else:
                ask = messagebox.askokcancel("PDSserver", "Do you sure you wanna open server?")
                if ask == True:
                    messagebox.showinfo("PDSserver", "Open server!!!!")
                    The_count = 1
                else:
                    messagebox.showinfo("PDSserver", "Cancel to open server")
        elif The_count == 0:
            messagebox.showerror("PDSsever", "Error, you need to open server \\server,iop.sss\\ ")

        elif The_count == 1:
            messagebox.showerror("PDSserver", "please input the correct code")


def main():
    lop = messagebox.askyesno("Warning", "Do you wanna open the program ?")
    if lop:
        opening()
    else:
        print("one time not see you")
        time.sleep(1)
        conn.close()
        exit()


if __name__ == "__main__":
    main()