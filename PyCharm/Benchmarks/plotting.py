import matplotlib.pyplot as plt
import digitsOfPi as dop

def plotMat(times, number_of_tests):

    x_axis = []
    y_axis = []
    for x_value in range(1, number_of_tests + 1):
        x_axis.append(x_value)
    for y_value in times:
        y_axis.append(y_value)

    x_axis = list(range(1, number_of_tests + 1))
    y_axis = times

    fig, ax = plt.subplots()
    ax.plot(x_axis, y_axis, label="Time per Test")
    ax.set_xlabel("Number of Tests")
    ax.set_ylabel("Time (seconds)")
    ax.set_title("Matrix Operations Results")
    ax.legend()

    return fig

def plotPi(times):
        x_axis = []
        y_axis = []

        for iteration in range(1, dop.repeat_benchmark + 1):
            x_axis.append(iteration)
        for time in times:
            y_axis.append(time)

        fig, ax = plt.subplots()
        ax.plot(x_axis, y_axis, label="Time per Test")
        ax.set_xlabel("Number of Tests")
        ax.set_ylabel("Time (seconds)")
        ax.set_title("Powers of Pi Results")
        ax.legend()

        return fig