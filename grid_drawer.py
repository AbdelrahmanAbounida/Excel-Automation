# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 19:06:41 2022
@author: ozanogunc
Modified by: Semih Ahıshali
"""
# %% ---------- Library ---------- #%%
import numpy as np
import tkinter as tk
import openseespy.opensees as op

# %% ---------- Algorithm Open ---------- #%%
np.set_printoptions(3, suppress=True)
window = tk.Tk()
# %% ---------- Step 1 ---------- #%%
sw = window.winfo_screenwidth()
sh = window.winfo_screenheight()
ww = int(5 * sw / 6)
wh = int(5 * sh / 6)
who = int(1 * (sh - wh) / 3)
wwo = int((sw - ww) / 2)
window.minsize(800, 400)
winsize = str(ww) + 'x' + str(wh) + '+' + str(wwo) + '+' + str(who)
window.geometry(winsize)
# %% ---------- Step 2 ---------- #%%
window.columnconfigure([0, 1], weight=1)
window.rowconfigure(1, weight=1)
titleframe = tk.Frame(window, bg='gray')
titleframe = tk.Frame(window, bg='gray')
guiframe = tk.Frame(window, bg='gray')
graphframe = tk.Frame(window, bg='white')
titleframe.grid(row=0, column=0, columnspan=2, sticky='nsew')
guiframe.grid(row=1, column=0, sticky='nsew')
graphframe.grid(row=1, column=1, sticky='nsew')
# %% ---------- Step 3 ---------- #%%
titleframe.columnconfigure(0, weight=1)
guiframe.columnconfigure(0, weight=1)
guiframe.rowconfigure(0, weight=1)
guiframe.grid_propagate(0)
guicanvs = tk.Canvas(guiframe, bg='gray', highlightthickness=0)
guivscrol = tk.Scrollbar(guiframe, orient='vertical', command=guicanvs.yview)
guihscrol = tk.Scrollbar(guiframe, orient='horizontal', command=guicanvs.xview)
guicanvs.grid(row=0, column=0, sticky='nsew')
guivscrol.grid(row=0, column=1, rowspan=2, sticky='nsew')
guihscrol.grid(row=1, column=0, sticky='nsew')
guicanvs.columnconfigure(0, weight=1)
guicanvs.rowconfigure(0, weight=1)
# %% ---------- Step 4 ---------- #%%
containerframe = tk.Frame(guicanvs, bg='gray')
containerframe.grid(row=0, column=0, sticky='nsew')
# %% ---------- Step 5 ---------- #%%
guicanvs.create_window((0, 0), width=ww / 2 - 17,
                       window=containerframe,
                       anchor='nw', tags=('canwin'))

containerframe.bind('<Configure>',
                    lambda e: guicanvs.configure(scrollregion=guicanvs.bbox('all')))

guicanvs.configure(yscrollcommand=guivscrol.set,
                   xscrollcommand=guihscrol.set)

containerframe.columnconfigure([0, 1, 2], weight=1)
graphframe.grid_propagate(0)
graphframe.columnconfigure(0, weight=1)
graphframe.rowconfigure(0, weight=1)
plotcanvs = tk.Canvas(graphframe,
                      bg='white',
                      highlightthickness=0,
                      width=ww / 2)
plotcanvs.grid(row=0, column=0, sticky='nsew')
# %% ---------- Step 6 ---------- #%%
cor_x = tk.Label(containerframe, text='X')
cor_x.grid(row=0, column=1, sticky='nsew')
cor_y = tk.Label(containerframe, text='Y')
cor_y.grid(row=0, column=2, sticky='nsew')

tnlbl = tk.Label(containerframe, text='Number of Gridlines : ')
tnlbl.grid(row=1, column=0, sticky='nsew')

tnetx = tk.Entry(containerframe)
tnetx.grid(row=1, column=1, sticky='nsew')
tnety = tk.Entry(containerframe)
tnety.grid(row=1, column=2, sticky='nsew')

telbl = tk.Label(containerframe, text='Grid Spacing : ')
telbl.grid(row=2, column=0, sticky='nsew')

teetx = tk.Entry(containerframe)
teetx.grid(row=2, column=1, sticky='nsew')

teety = tk.Entry(containerframe)
teety.grid(row=2, column=2, sticky='nsew')
# %% ---------- Important 1 ---------- #%%
# to handle all corner coordinates, create a main list
entire_corners_list = []


# %% ---------- Input GUI Function ---------- #%%
def general():
    class Node:
        def __init__(self, row, col):
            self.row = row
            self.col = col
            return

    def generatGrid(nrows, ncols):
        grid = []
        for r in range(nrows):
            row = [Node(r, c) for c in range(ncols)]
            grid.append(row)
        return grid

    def drawNode(canvas, node):
        x1 = int(teetx.get()) * node.col
        y1 = int(teety.get()) * node.row
        x2 = x1 + int(teetx.get())
        y2 = y1 + int(teety.get())

        # create list includes sub-dicts to keep coordinates of all corners of new rectangle
        new_rectangle_corners_list = [{"x": x1, "y": y1}, {"x": x2, "y": y1}, {"x": x1, "y": y2}, {"x": x2, "y": y2}]

        # put these new corners into entire_corners_list if not exist
        for corner in new_rectangle_corners_list:
            if corner not in entire_corners_list:
                entire_corners_list.append(corner)

        del new_rectangle_corners_list

        plotcanvs.create_rectangle(x1, y1, x2, y2)
        # canvas.place(x = 400, y = 300)
        return

    def drawGrid(canvas, grid):
        for row in grid:
            for node in row:
                drawNode(canvas, node)
        return

    grid = generatGrid(int(tnetx.get()), int(tnety.get()))
    drawGrid(plotcanvs, grid)


# %% ---------- Step 7 ---------- #%%
btn1 = tk.Button(containerframe, text='OK', command=general)
btn1.grid(row=3, column=1, columnspan=2, sticky='nsew')

# click distance to corner and corner circle oval radius variables in pixels
click_distance_to_corner_value = 10
click_circle_r_value = 10
# %% ---------- Step 8 ---------- #%%


# Material Properties
E = 2 * 10 ** 8  # kPa
a_tot = 120 * 70 * 10 ** -6  # m2
a_hollow = 50 * 100 * 10 ** -6  # m2
A = a_tot - a_hollow  # m2

F = -10  # kN

# remove existing model
op.wipe()

# set modelbuilder
op.model('basic', '-ndm', 2, '-ndf', 2)

# define materials
op.uniaxialMaterial("Elastic", 1, E)

# variable to handle op.no number
count_of_op_nodes = 1


def mouse_left_click_on_plotcanvs(event):
    global count_of_op_nodes
    click_coord_dict = {"x": event.x, "y": event.y}

    for corner in entire_corners_list:
        if (click_coord_dict["x"] - click_distance_to_corner_value <= corner["x"] <= click_coord_dict[
            "x"] + click_distance_to_corner_value) and \
                (click_coord_dict["y"] - click_distance_to_corner_value <= corner["y"] <= click_coord_dict[
                    "y"] + click_distance_to_corner_value):
            plotcanvs.create_oval(corner["x"] - click_circle_r_value, corner["y"] - click_circle_r_value, corner["x"]
                                  + click_circle_r_value, corner["y"] + click_circle_r_value, fill="blue",
                                  outline='blue')

            # create op.node on each mouse click on corner
            op.node(count_of_op_nodes, float(corner["x"]), float(corner["y"]))
            # print number of op.nodes created to screen
            print(f"No: {count_of_op_nodes} op.node created")
            print(float(corner["x"]))
            # increment op.node number
            count_of_op_nodes += 1
            break

    del click_coord_dict


# %% ---------- Step 9 ---------- #%%
# mouse click event binded to def created above
plotcanvs.bind("<Button-1>", mouse_left_click_on_plotcanvs)
# %% ---------- Step 10 ---------- #%%

# %% ---------- Algorithm Close ---------- #%%
window.mainloop()

