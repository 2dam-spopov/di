import tkinter
import tkinter.filedialog as dialog
class TextEditor:

def __init__(self, parent):

	# Framework
	self.parent = parent
	self.frame = tkinter.Frame(parent)
	self.frame.pack()
	# Text box for editing.
	self.text = tkinter.Text(parent)
	self.text.pack()
	# Menus.
	menubar = tkinter.Menu(parent)
	filemenu = tkinter.Menu(menubar)
	filemenu.add_command(label='Save', command=self.save_click)
	filemenu.add_command(label='Quit', command=self.quit_click)
	menubar.add_cascade(label='File', menu=filemenu)
	window.config(menu=menubar)
def save_click(self):

	data = self.text.get('0.0', tkinter.END)
	filename = dialog.asksaveasfilename(parent=self.parent,filetypes=[('Text', '*.txt')],title='Save as...')
	writer = open(filename, 'w')
	writer.write(data)
	writer.close()
def quit_click(self):

	self.parent.destroy()
if __name__ == '__main__':
	window = tkinter.Tk()
	app = TextEditor(window)
	window.mainloop()
