# graphPlotterGUI is an app for graphing functions and its derivatives

import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from plotter import Plotter
from numpy import cos, sin # import for user input use

root = tk.Tk()
root.geometry("500x650")
root.title("Graph plotter")

# define functions

# plots function given by user
def plotFunction(key):
    x0, x1 = float(xRangeLowerValue.get()), float(xRangeUpperValue.get())
    functionText = functionValue.get()

    f = lambda x: eval(functionText)

    plotter = Plotter(f, [x0, x1], functionText)

    minMax = minMaxValue.get()
    funcEqual0 = functionEqualZeroValue.get()

    if key=="function":
        plotter.plot_function(minMax, funcEqual0)
    elif key=="derivative":
        plotter.plot_function(minMax, funcEqual0, dydx="Yes")

    insertImage("functionPlot.png")


# inserts image/graph
def insertImage(imageName):
    newMmage = Image.open(imageName)
    resized_newImage = newMmage.resize((400, 400))
    imageFileNew = ImageTk.PhotoImage(resized_newImage)

    # change image in widget
    imageLabel.config(image=imageFileNew)
    imageLabel.image = imageFileNew

# define layout
font= "Helvetiva"

promptFunctionLabel = tk.Label(root, text="Input function:", font=font)
promptFunctionLabel.grid(row=1, column=0, sticky="w")

functionValue = tk.StringVar()
functionEntry = ttk.Entry(root, textvariable=functionValue)
functionEntry.grid(row=2, column=0, sticky="w")

xRangeLabel = tk.Label(root, text="Input lower and upper bound for x", font=font)
xRangeLabel.grid(row=3, column=0, columnspan=3, sticky="w")

f1 = tk.Frame(root)
f1.grid(row=4, column=0, sticky="w")

xRangeLowerValue = tk.StringVar()
xRangeLowerEntry = ttk.Entry(f1, textvariable=xRangeLowerValue, width=5)
xRangeLowerEntry.grid(row=0, column=0, padx=20)

xRangeUpperValue = tk.StringVar()
xRangeUpperEntry = ttk.Entry(f1, textvariable=xRangeUpperValue, width=5)
xRangeUpperEntry.grid(row=0, column=1)

minMaxLabel = tk.Label(root, text="Mark min/max values?", font=font)
minMaxLabel.grid(row=5, column=0, sticky="w")

f2 = tk.Frame(root)
f2.grid(row=6, column=0, sticky="w")

minMaxValue = tk.StringVar(value="Yes")
R1 = tk.Radiobutton(f2, text="Yes", variable=minMaxValue, value="Yes")
R1.grid(row=0, column=0)

R2 = tk.Radiobutton(f2, text="No", variable=minMaxValue, value="No")
R2.grid(row=0, column=1)

functionEqualZeroLabel = tk.Label(root, text="Mark where function equal 0?", font=font)
functionEqualZeroLabel.grid(row=7, column=0, columnspan=3, sticky="w")

f3 = tk.Frame(root)
f3.grid(row=8, column=0, sticky="w")

functionEqualZeroValue = tk.StringVar(value="No")
R3 = tk.Radiobutton(f3, text="Yes", variable=functionEqualZeroValue, value="Yes")
R3.grid(row=0, column=0)

R4 = tk.Radiobutton(f3, text="No", variable=functionEqualZeroValue, value="No")
R4.grid(row=0, column=1)

plotGraphButt = tk.Button(root, text="Plot function", fg="green", command=lambda: plotFunction("function"))
plotGraphButt.grid(row=9, column=0)

plotDerivativeButt = tk.Button(root, text="Plot dy/dx", fg="green", command=lambda: plotFunction("derivative"))
plotDerivativeButt.grid(row=9, column=1)

# startup picture is an empty graph
image = Image.open("emptyGraph.png")
resized_image = image.resize((400, 400))
imageFile = ImageTk.PhotoImage(resized_image)
imageLabel = tk.Label(root, image=imageFile)
imageLabel.grid(row=10, column=0, columnspan=4, )


root.mainloop()