from tkinter import *
from tkinter import filedialog as fd, filedialog
from tkinter import messagebox as ms
#Import asksaveasfilename and asksaveasfile module to open save name and file window 
from tkinter.filedialog import asksaveasfilename, asksaveasfile
#Import PIL
from PIL import ImageTk, Image

#  Build A Image Viewer Now
from imageio import save


class Image_Viewer:

    def __init__(self, master):
        self.savefile = None
        self.master = master
        self.c_size = (700, 500)
        self.setup_gui(self.c_size)
        self.img = None

    def setup_gui(self, s):
        Label(self.master, text='Image Viewer', pady=5, bg='white', font=('Arial', 30)).pack()
        self.canvas = Canvas(self.master, height=s[1], width=s[0], bg='Black', bd=10, relief='ridge')
        self.canvas.pack()
        txt = '''
                                                       By Prashant More 

                                '''
        self.wt = self.canvas.create_text(s[0] / 2 - 270, s[1] / 2, text=txt, font=('', 30), fill='white')
        g = Frame(self.master, bg='white', padx=10, pady=10)
        Button(g, text='Save Image', bd=2, fg='white', bg='green', font=('', 15), command=self.save).pack(
            side=LEFT)
        g.pack()
       

    def save(self):

        File = fd.askopenfilename()
        self.pilImage = Image.open(File)
        files = [('All Files', '*.*'),
                 ('jpg', '*.jpg'),
                 ('png ', '*.png')]
        file = asksaveasfile(filetypes=files, defaultextension=files)

    def make_image(self):

        try:
            File = fd.askopenfilename()
            self.pilImage = Image.open(File)
            re = self.pilImage.resize((700, 500), Image.ANTIALIAS)
            self.img = ImageTk.PhotoImage(re)
            self.canvas.delete(ALL)
            self.canvas.create_image(self.c_size[0] / 2 + 10, self.c_size[1] / 2 + 10, anchor=CENTER, image=self.img)
            self.status['text'] = 'Current Image:' + File

        except:
            ms.showerror('Error!', 'File type is unsupported.')


root = Tk()
root.configure(bg='white')
root.title('Image Viewer')
Image_Viewer(root)
root.resizable(True, True)
root.mainloop()
