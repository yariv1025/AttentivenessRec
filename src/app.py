import cv2
import keras
import time
from keras.datasets import mnist
from keras.layers import Conv2D, MaxPooling2D, Dense, Dropout, Flatten
from keras.models import Sequential

from ModelCreator import *
from src.FaceDetector import FaceDetector
from src.FrameProvider import FrameProvider
from src.draw_facebox import draw_facebox

# Images path
PATH = '../docs/ImagesForTests/'


def AttentivenessRecognition(plt=None):
    # frame providing
    fp = FrameProvider(0)

    # face detecting
    fd = FaceDetector()

    fp_counter, fd_counter = 0, 0

    while fp_counter <= 11:
        frame = fp.get_frame()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # detect faces in the image
        faces = fd.has_face(frame)

        # if has face, we will save the frame.
        if faces:
            # save frame as JPG file
            cv2.imwrite(PATH + "image" + str(fp_counter) + ".jpg", frame)
            cv2.imshow('frame', gray)

            # """
            # EDIT
            # """
            # #  TODO: Ploting our images with a face box - Fix filename!!!!
            # filename = plt.imread(PATH + "image" + str(fp_counter) + ".jpg", frame)
            #
            # # detect faces in the image
            # faceslist = FaceDetector.get_face(frame)
            #
            # # display faces on the original image
            # draw_facebox(filename, faceslist)
            # """
            # END EDIT
            # """

            print(str(faces) + "-" + str(fp_counter))
            fp_counter = fp_counter + 1

        time.sleep(5)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    fp.release()
    cv2.destroyAllWindows()

    # TODO: create train dataset from our database

    # TODO: replace this current dataset with our dataset
    model_param = ModelParametersHolder(batch_size=128, num_classes=10, epochs=12, img_rows=28, img_cols=28,
                                        dataset=mnist.load_data())

    model_param.re_shape_data(model_param.x_train, model_param.x_test)
    model_param.img_to_bin_converter(model_param.y_train, model_param.y_test)

    cnn_model = Sequential()

    # TODO: Finding the best sequence of convolution layers.
    cnn_model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(28, 28, 1)))
    cnn_model.add(Conv2D(64, (3, 3), activation='relu'))
    cnn_model.add(MaxPooling2D(pool_size=(2, 2)))
    cnn_model.add(Dropout(0.25))
    cnn_model.add(Flatten())
    cnn_model.add(Dense(128, activation='relu'))
    cnn_model.add(Dropout(0.5))
    cnn_model.add(Dense(model_param.num_classes, activation='softmax'))

    # TODO: Choosing the best optimizer.
    cnn_model.compile(loss=keras.losses.categorical_crossentropy,
                      optimizer=keras.optimizers.Adadelta(),
                      metrics=['accuracy'])

    cnn_model.fit(model_param.x_train, model_param.y_train,
                  batch_size=model_param.batch_size,
                  epochs=model_param.epochs,
                  verbose=1,
                  validation_data=(model_param.x_test, model_param.y_test))

    score = cnn_model.evaluate(model_param.x_test, model_param.y_test, verbose=0)
    print('Test loss:', score[0])
    print('Test accuracy:', score[1])


if __name__ == '__main__':
    AttentivenessRecognition()
