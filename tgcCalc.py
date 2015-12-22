from tkinter import *
from tkinter import ttk

def calculate(*args):
	try:
		if elevud.get() == 'u':
			elev = float(elevation.get()) / 3
			dist = float(distance.get()) + elev
		else:
			elev = float(elevation.get()) / 3
			dist = float(distance.get()) - elev
		if windfb.get() == 'f':
			w = float(wind.get()) * 1.75
			dist = dist + w
		else:
			w = float(wind.get()) * 0.75
			dist = dist - w
		newDistance.set(dist)
				
	except ValueError:
		pass


root = Tk()
root.title("TGC Disctance Calculator")

mainframe = ttk.Frame(root, padding = "3 3 12 12")
mainframe.grid(column = 0, row = 0, sticky = (N, W, E, S))
mainframe.columnconfigure(0, weight = 1)
mainframe.rowconfigure(0, weight = 1)

distance = StringVar()
elevation = StringVar()
elevud = StringVar()
wind = StringVar()
windfb = StringVar()
newDistance = StringVar()

distance_entry = ttk.Entry(mainframe, width = 7, textvariable = distance)
distance_entry.grid(column = 2, row = 1, sticky = (W, E))
elevation_entry = ttk.Entry(mainframe, width = 7, textvariable = elevation)
elevation_entry.grid(column = 2, row = 2, sticky = (W, E))
elevud_entry = ttk.Entry(mainframe, width = 7, textvariable = elevud)
elevud_entry.grid(column = 2, row = 3, sticky = (W, E))
wind_entry = ttk.Entry(mainframe, width = 7, textvariable = wind)
wind_entry.grid(column = 2, row = 4, sticky = (W, E))
windfb_entry = ttk.Entry(mainframe, width = 7, textvariable = windfb)
windfb_entry.grid(column = 2, row = 5, sticky = (W, E))

#ttk.Label(mainframe, textvariable = meters).grid(column = 2, row = 2, sticky = (W, E))
ttk.Label(mainframe, text = "Distance").grid(column = 1, row = 1, sticky = W)
ttk.Label(mainframe, text = "Elevation").grid(column = 1, row = 2, sticky = W)
ttk.Label(mainframe, text = "Up or Down [u/d]").grid(column = 1, row = 3, sticky = W)
ttk.Label(mainframe, text = "Wind Speed").grid(column = 1, row = 4, sticky = W)
ttk.Label(mainframe, text = "Wind Direction [f/b]").grid(column = 1, row = 5, sticky = W)
ttk.Button(mainframe, text = "Calculate", command = calculate).grid(column = 2, row = 6, sticky = W)
ttk.Label(mainframe, text = "Corrected Distance ").grid(column = 1, row = 7, sticky = W)
ttk.Label(mainframe, textvariable = newDistance).grid(column = 2, row = 7, sticky = E)

for child in mainframe.winfo_children():  child.grid_configure(padx = 5, pady = 5)

distance_entry.focus()
root.bind('<Return>', calculate)

root.mainloop()

