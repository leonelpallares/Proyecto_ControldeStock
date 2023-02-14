from app_vista import Vista
from tkinter import Tk


class Controller:

    def __init__(self, root):
        self.root = root
        self.obj1 = Vista(self.root)


if __name__ == "__main__":
    principal = Tk()
    obj = Controller(principal)
    principal.mainloop()