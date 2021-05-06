from pandas import DataFrame


class Statistics(object):

    def __init__(self):
        self.times = []
        self.values = []

    def addValue(self, time, value):
        self.times.append(time)
        self.values.append(value)
        self.get_data_frame()

        # indexes.append(index)
        # values.append(value)
        # index += 1

    def get_data_frame(self):
        data = {'Time': self.times,
                'Values': self.values
                }

        df = DataFrame(data, columns=['Time', 'Values'])
        print(df)
