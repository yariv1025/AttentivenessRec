from tensorflow import keras

"""
The keras library helps us build our convolutional neural network.
We import a sequential model which is a pre-built keras model where you can just add the layers.
We import the convolution and pooling layers.
We also import dense layers as they are used to predict the labels.
The dropout layer reduces overfitting and the flatten layer expands a three-dimensional vector into a one-dimensional vector.
Finally, we import numpy for matrix operations.

We reshape x_train and x_test because our CNN accepts only a four-dimensional vector.
The value 60000 represents the number of images in the training data,
28 represents the image size and 1 represents the number of channels.
The number of channels is set to 1 if the image is in grayscale.
If the image is in RGB format, the number of channels is set to 3

We build a sequential model and add convolutional layers and max pooling layers to it.
We also add dropout layers in between, dropout randomly switches off some neurons in the network which forces the data
to find new paths. Therefore, this reduces overfitting.
We add dense layers at the end which are used for class prediction(0–9).

Compiling the model with a categorical cross entropy loss function,
Adadelta optimizer and an accuracy metric. We then fit the dataset to the model,
i.e we train the model for 12 epochs. After training the model,
we evaluate the loss and accuracy of the model on the test data and print it.
"""

# TODO : check if that correct to create a class to holding parameters
class ModelParametersHolder:
    def __init__(self, batch_size, num_classes, epochs, img_rows, img_cols, dataset):
        """
        Initialize needed parameters for CNN model.
        :param batch_size:
        :param num_classes: amount of matrix of binary classes.
        :param epochs: number of epochs.
        :param img_rows: rows image dimension.
        :param img_cols: columns image dimension.
        :param dataset: our dataset.
        """
        self.batch_size = batch_size
        self.num_classes = num_classes
        self.epochs = epochs

        # input image dimensions
        self.img_rows = img_rows
        self.img_cols = img_cols

        # load desire dataset
        (self.x_train, self.y_train), (self.x_test, self.y_test) = dataset

    def re_shape_data(self, x_train, x_test):
        """
        Reshape x_train and x_test because our
        CNN accepts only a four-dimensional vector.
        :param x_train:
        :param x_test:
        """
        self.x_train = x_train.reshape(60000, 28, 28, 1)
        self.x_test = x_test.reshape(10000, 28, 28, 1)

        print('x_train shape:', x_train.shape)
        print(x_train.shape[0], 'train samples')
        print(x_test.shape[0], 'test samples')

    def img_to_bin_converter(self, y_train, y_test):
        """
        Convert class vectors to binary class matrices
        :param y_train:
        :param y_test:
        """
        self.y_train = keras.utils.to_categorical(y_train, self.num_classes)
        self.y_test = keras.utils.to_categorical(y_test, self.num_classes)
