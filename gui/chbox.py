from tkinter import Tk, Frame, Checkbutton, Button, BooleanVar

class MyFrame(Frame):

    def __init__(self, parent):

        Frame.__init__(self, parent)
        self.parent = parent
        self.test01 = BooleanVar()
        checkbutton = Checkbutton(parent, text='check it',
        variable=self.test01, command=self.testcheck)

        checkbutton.pack()

        testbutton = Button(parent, text='check test', command=self.testcheck)
        testbutton.pack()
        self.parent.title('Checkbutton test')


    def testcheck(self):
        print('Check test: ' + str(self.test01.get()))

def main():

    root = Tk()
    app = MyFrame(root)
    root.mainloop()

if __name__ == '__main__':
    main()
