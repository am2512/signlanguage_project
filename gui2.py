import Tkinter as tk
from PIL import ImageTk, Image

path = '/home/ahalyamandana/sign_language_project/tf_files/sign_photos/Y.jpg'

root = tk.Tk()
img = ImageTk.PhotoImage(Image.open(path))
panel = tk.Label(root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")
root.mainloop()