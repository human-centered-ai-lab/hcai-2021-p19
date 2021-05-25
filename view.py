import tkinter
import tkinter.filedialog as tkFile
import tkinter.ttk
import tkinter as tk
import matplotlib.figure
import matplotlib.backends.backend_tkagg
import numpy


class View:

    btn_width = 10

    def __init__(self):

        self.selected_node_index = None

        self.root = tk.Tk()
        self.root.title("Project 19")
        self.root.geometry("800x600")

        # IDs of eventhandle, needed to be unregistered on new plot
        self.hoover_cid = None
        self.click_cid = None

        # Input
        self.containerInput = tk.Frame(master=self.root, width=150)

        # file loading elements
        self.txtFileName = tk.Label(master=self.containerInput, text="File Name")
        self.btnLoadFile = tk.Button(master=self.containerInput,
                                     text="Load File",
                                     width=self.btn_width)
        self.btnLoadFile.pack()
        self.txtFileName.pack()

        # Aggregation Dropdown
        self.aggregationPopupValue = tk.StringVar(self.containerInput)
        # Dictionary with options
        choices = {'Lukasiewicz', 'MinMax', 'TnormTconorm'}
        self.aggregationPopupValue.set('Lukasiewicz')  # set the default option

        self.aggregationPopup = tk.OptionMenu(self.containerInput, self.aggregationPopupValue, *choices)
        self.txtAggregationLabel = tk.Label(master=self.containerInput, text="Aggregation Function")
        self.txtAggregationLabel.pack()
        self.aggregationPopup.pack()

        # lambda and r
        self.gridLambdaR = tk.Frame(master=self.containerInput)
        tk.Label(master=self.gridLambdaR, text="l: ").grid(row=0, column=0)
        tk.Label(master=self.gridLambdaR, text="r: ").grid(row=1, column=0)
        tk.Label(master=self.gridLambdaR, text="mean error l: ").grid(row=2, column=0)
        tk.Label(master=self.gridLambdaR, text="mean error r: ").grid(row=3, column=0)
        self.entK = tk.Entry(master=self.gridLambdaR, width=6)
        self.entK.insert(0, 1.0)
        self.entK.grid(row=0, column=1)
        self.entR = tk.Entry(master=self.gridLambdaR, width=6)
        self.entR.insert(0, 1.0)
        self.entR.grid(row=1, column=1)
        self.entErrorL = tk.Entry(master=self.gridLambdaR, width=6)
        self.entErrorL.insert(0, 0.0)
        self.entErrorL.grid(row=2, column=1)
        self.entErrorR = tk.Entry(master=self.gridLambdaR, width=6)
        self.entErrorR.insert(0, 0.0)
        self.entErrorR.grid(row=3, column=1)
        self.gridLambdaR.pack()

        # calc lambda and r
        self.btnCalcLR = tk.Button(master=self.containerInput,
                                   text="calc l r",
                                   width=self.btn_width)
        self.btnCalcLR.pack()

        # plotting trigger button
        self.btnPlot = tk.Button(master=self.containerInput,
                                 text="Plot",
                                 width=self.btn_width)
        self.btnPlot.pack()

        # clear data trigger button
        self.btnClear = tk.Button(master=self.containerInput,
                                  text="Clear",
                                  width=self.btn_width)
        self.btnClear.pack()

        # inverting checkboxes
        self.invertX = tkinter.BooleanVar()
        self.cbInvertX = tk.Checkbutton(master=self.containerInput, text="X Inverted", variable=self.invertX)
        self.invertY = tkinter.BooleanVar()
        self.cbInvertY = tk.Checkbutton(master=self.containerInput, text="Y Inverted", variable=self.invertY)
        self.cbInvertX.pack()
        self.cbInvertY.pack()

        # user input for points
        self.gridInput = tk.Frame(master=self.containerInput)
        self.txtInputX = tk.Label(master=self.gridInput, text="X")
        self.txtInputY = tk.Label(master=self.gridInput, text="Y")
        self.txtInputSol = tk.Label(master=self.gridInput, text="Sol")
        self.entInputX = tk.Entry(master=self.gridInput, width=6)
        self.entInputY = tk.Entry(master=self.gridInput, width=6)
        self.entInputSol = tk.Entry(master=self.gridInput, width=6)
        self.txtInputX.grid(row=0, column=0)
        self.txtInputY.grid(row=1, column=0)
        self.txtInputSol.grid(row=2, column=0)
        self.entInputX.grid(row=0, column=1)
        self.entInputY.grid(row=1, column=1)
        self.entInputSol.grid(row=2, column=1)
        self.gridInput.pack(fill=tk.X, anchor=tk.NW)

        self.btnAddValue = tk.Button(master=self.containerInput,
                                     text="Add",
                                     width=self.btn_width)

        self.btnChangeValue = tk.Button(master=self.containerInput,
                                        text="Change",
                                        width=self.btn_width)
        self.btnAddValue.pack()
        self.btnChangeValue.pack()

        # sum of all nodes
        self.gridSum = tk.Frame(master=self.containerInput)
        tk.Label(master=self.gridSum, text="Sum: ").grid(row=0, column=0)
        self.txtSumValue = tk.StringVar()
        self.txtSumValue.set(0)
        lblSumValue = tk.Label(master=self.gridSum, textvariable=self.txtSumValue)
        lblSumValue.grid(row=0, column=1)
        self.gridSum.pack(fill=tk.X, anchor=tk.NW)

        self.containerInput.pack(fill=tk.Y, side=tk.LEFT)
        self.containerInput.pack_propagate(0)

        # Plot
        self.containerPlot = tk.Frame(master=self.root)
        self.containerPlot.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

        self.i = tk.Label(master=self.containerPlot, text="The Plot:")
        self.i.pack()

        self.figurePlot = matplotlib.figure.Figure(figsize=(5, 4), dpi=100)
        self.targetSubPlot = self.figurePlot.add_subplot(111)
        self.targetSubPlot.set_xticks(numpy.arange(0, 1.1, 0.1))
        self.targetSubPlot.set_yticks(numpy.arange(0, 1.1, 0.1))

        self.canvasPlot = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(self.figurePlot, master=self.containerPlot)
        self.canvasPlot.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def run(self):
        self.root.mainloop()