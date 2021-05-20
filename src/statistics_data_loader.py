from pandas import DataFrame


class Statistics(object):
    """
    A class for storing the attention values of the subject.
    """

    def __init__(self):
        """
        Creating a new Statistics object.
        """
        self.times = []
        self.values = []

    def addValue(self, time, value):
        """
        A function for adding a new row for the attention level table.

        :param time: the time which the attention level has been recorded.
        :param value: the attention level.
        """
        self.times.append(time)
        self.values.append(value)

    def get_data_frame(self):
        """
        A function for recieving the attention levels that has been recorded as a DataFrame object.

        :return: Dataframe object of the attention levels.
        """
        data = {'Time': self.times,
                'Emotion levels': self.values
                }
        df = DataFrame(data, columns=['Time', 'Emotion levels']).groupby('Time').sum()
        return df
