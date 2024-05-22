import matplotlib.pyplot as plt
import digitsOfPi as dop
import matplotlib
matplotlib.use('TkAgg')

def plotMat(times, number_of_tests):
    x_axis = list(range(1, number_of_tests + 1))

    # Ensure y_axis doesn't exceed 100
    y_axis = [min(time, 100) for time in times]

    fig, ax = plt.subplots()
    ax.plot(x_axis, y_axis, label="Time per Test")
    ax.set_xlabel("Number of Tests")
    ax.set_ylabel("Time (seconds)")
    ax.set_title("Matrix Operations Results")
    ax.legend()

    return fig

def plotRW(results):
    operations = list(results.keys())
    times = list(results.values())

    fig, ax = plt.subplots()
    bars = ax.bar(operations, times, color=['blue', 'green', 'red', 'orange'])

    ax.set_xlabel('Operation')
    ax.set_ylabel('Time (seconds)')
    ax.set_title('Memory Read/Write Speed Test')
    ax.bar_label(bars)

    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    print(results)
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