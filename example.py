import greengraph

if __name__ == '__main__':
    from matplotlib import pyplot as plt
    mygraph = greengraph.Greengraph('New York','Chicago')
    data = mygraph.green_between(20)
    plt.plot(data)
    plt.show()
