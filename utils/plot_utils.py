import matplotlib.pyplot as plt
import numpy as np

__all__ = ['plot_hist', 'subplot_hist', "plot_embedding"]


def plot_hist(data, bins=10, density=False, label=None,
              title=None, xlabel=None, ylabel=None):
    plt.hist(data, bins, density=density, label=label)
    plt.xlabel = xlabel
    plt.ylabel = ylabel
    plt.title = title
    if label is not None:
        plt.legend()


def subplot_hist(keys, info_list):
    row = int(np.sqrt(len(keys)))
    if len(keys) > row * (row + 1):
        row += 1
    col = (len(keys) + 1) // row
    for i, key in enumerate(keys):
        data = [x[key] for x in info_list]
        plt.subplot(row, col, i + 1)
        plot_hist(data, label=key)
    plt.show()


# 绘制数据图像
def plot_embedding(data, type=None, text=None, title="", colors=None):
    if type is None:
        type = np.zeros_like(data[:, 0])
    x_min, x_max = np.min(data, 0), np.max(data, 0)
    data = (data - x_min) / (x_max - x_min)

    fig = plt.figure()
    ax = plt.subplot(111)
    for i in range(data.shape[0]):
        if text is not None:
            plt.text(data[i, 0], data[i, 1], str(text[i]),
                     color=plt.cm.Set1((type[i] + 1) / 10.) if colors is None else colors[type[i]],
                     fontdict={'weight': 'bold', 'size': 8})
        else:
            plt.scatter(data[i, 0], data[i, 1], s=3,
                        color=plt.cm.Set1((type[i] + 1) / 10.) if colors is None else colors[type[i]])
    plt.xticks([])
    plt.yticks([])
    plt.title(title)
    plt.show()
    return fig
