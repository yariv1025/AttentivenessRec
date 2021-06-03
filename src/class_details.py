class ClassDetails(object):
    """"
    The class hold the needed value for the PDF generator.
    """

    def __init__(self, lecture_value, lecturer_value, avg_value=None, Inactivity_time=None, lecture_time=None):
        """
        Creating ClassDetails object for holding all the needed parameter for the PDF generator.
        :param lecture_value: the number of class
        :param lecturer_value: the name of lecturer
        :param avg_value: the average attention level
        :param Inactivity_time: the inactivity time of the student
        :param lecture_time: the length of the lecture
        """
        self.lecture_value = lecture_value
        self.lecturer_value = lecturer_value
        self.avg_value = avg_value
        self.Inactivity_time = Inactivity_time
        self.lecture_time = lecture_time
