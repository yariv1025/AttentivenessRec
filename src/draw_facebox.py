def draw_facebox(self, filename, result_list, plt=None):
    # TODO: complete docs
    """
    Creates / draws a rectangle around the face identified in the image.
    :param filename:
    :param result_list:
    :param plt:
    :return:
    """
    # load the image
    data = plt.imread(filename)
    # plot the image
    plt.imshow(data)
    # get the context for drawing boxes
    ax = plt.gca()
    # plot each box
    for result in result_list:
        # get coordinates
        x, y, width, height = result['box']
        # create the shape
        rect = plt.Rectangle((x, y), width, height, fill=False, color='green')
        # draw the box
        ax.add_patch(rect)
        # show the plot
        plt.show()
