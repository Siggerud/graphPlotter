import matplotlib.pyplot as plt
import numpy as np

class Plotter:
    def __init__(self, f, x_range, functionText):
        self.f = f
        self.x_range = x_range
        self.functionText = functionText
        self.x = self.setUpXValues()
        self.y = 0

    # sets up the array with x values
    def setUpXValues(self):
        x_range = self.x_range

        x_start = x_range[0]
        x_end = x_range[1]

        time_points = int((x_end - x_start)) * 50

        x = np.linspace(x_start, x_end, time_points)

        return x


    # returns the derivative at point x
    def diff(self, x):
        f = self.f
        h = 1e-7

        return (f(x+h) - f(x))/h


    # plots function specified by user
    def plot_function(self, minMax, funcEqual0, dydx="No"):
        x = self.x
        if dydx == "Yes":
            y = self.diff(x)
        else:
            y = self.f(x)
        plt.clf() # don't plot over any existing plots

        plt.plot(x, y, label=f"{self.functionText}")

        self.setUpAxes(y)


        if minMax == "Yes":
            self.addMinAndMax(x, y)

        if funcEqual0 == "Yes":
            self.addFuncEqual0(x, y)

        plt.legend(bbox_to_anchor=(1, 1.1))
        plt.savefig("functionPlot.png")


    # adds the min and max values on the graph
    def addMinAndMax(self, x, y):
        maxValueIndices = np.where(y == np.amax(y))
        minValueIndices = np.where(y == np.amin(y))

        if len(maxValueIndices[0] > 1):
            for index, i in enumerate(maxValueIndices[0]):
                if index == 0:
                    plt.text(x[i], y[i], f"max\n({round(x[i], 2)}, {round(y[i], 2)})", verticalalignment="bottom", horizontalalignment="center")
                    plt.plot(x[i], y[i], marker="o")
                    continue
                # avoid two max values on the "same" point
                if maxValueIndices[0][index] != maxValueIndices[0][index - 1] + 1:
                    plt.text(x[i], y[i], f"max\n({round(x[i], 2)}, {round(y[i], 2)})", verticalalignment="bottom", horizontalalignment="center")
                    plt.plot(x[i], y[i], marker="o")

        else:
            i = maxValueIndices[0]
            plt.text(x[i], y[i], f"max\n({round(x[i], 2)}, {round(y[i], 2)})", verticalalignment="bottom", horizontalalignment="center")
            plt.plot(x[i], y[i], marker="o")

        if len(minValueIndices[0] > 1):
            for index, i in enumerate(minValueIndices[0]):
                if index == 0:
                    plt.text(x[i], y[i], f"min\n({round(x[i], 2)}, {round(y[i], 2)})", verticalalignment="top", horizontalalignment="center")
                    plt.plot(x[i], y[i], marker="o")
                    continue
                # avoid two min values on the "same" point
                if minValueIndices[0][index] != minValueIndices[0][index-1]+1:
                    plt.text(x[i], y[i], f"min\n({round(x[i], 2)}, {round(y[i], 2)})", verticalalignment="top", horizontalalignment="center")
                    plt.plot(x[i], y[i], marker="o")

        else:
            i = minValueIndices[0]
            plt.text(x[i], y[i], f"min\n({round(x[i], 2)}, {round(y[i], 2)})", verticalalignment="bottom", horizontalalignment="center")
            plt.plot(x[i], y[i], marker="o")


    # adds the points where f=0 on the graph
    def addFuncEqual0(self, x, y):
        funcEqual0Indices = []

        for i in range(len(y)):
            if i == 0:
                if y[i] == 0:
                    funcEqual0Indices.append(i)
                    continue

            # check if there is a sign change
            if y[i-1] * y[i] < 0:
                funcEqual0Indices.append(i)

        for i in funcEqual0Indices:
            plt.text(x[i], y[i], f"({round(x[i], 2)}, 0)")
            plt.plot(x[i], y[i], marker="o")


    # adds more space (10%) for potential min/max markers
    def setUpAxes(self, y):
        minY = min(y) - abs(min(y)) * 0.1
        maxY = max(y) + abs(max(y)) * 0.1

        plt.axis([self.x_range[0], self.x_range[1], minY, maxY])


