from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
import pyqtgraph as pg
import sys


class Plot2D:
    def __init__(self):
        self.traces = {}

        self.app = QtGui.QApplication([])

        self.window = pg.GraphicsWindow(title="Sine Plot")
        self.window.resize(1000, 600)
        self.window.setWindowTitle("Interactive Sine Plot")

        pg.setConfigOptions(antialias=True)

        self.canvas = self.window.addPlot(title="Sine")

    def start(self):
        if (sys.flags.interactive != 1) or not hasattr(QtCore, "PYQT_VERSION"):
            QtGui.QApplication.instance().exec_()
        self.app.instance().exec_()

    def trace(self, name, dataset_x, dataset_y):
        if name in self.traces:
            self.traces[name].setData(dataset_x, dataset_y)
        else:
            self.traces[name] = self.canvas.plot(pen="y")


if __name__ == "__main__":
    plot = Plot2D()
    i = 0

    def update():
        global plot, i
        time = np.arange(0, 5.0, 0.01)
        sinus = np.sin(np.pi * time + i)
        plot.trace("sinus", time, sinus)
        i += 0.1

    timer = QtCore.QTimer()
    timer.timeout.connect(update)
    timer.start(50)

    plot.start()
