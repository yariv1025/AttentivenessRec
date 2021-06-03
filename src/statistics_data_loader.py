from datetime import datetime
from pandas import DataFrame
import matplotlib.pyplot as plt
from fpdf import Template


class Statistics(object):
    """
    A class for storing the attention values of the subject.
    """

    def __init__(self, class_data, fd):
        """
        Creating a new Statistics object.
        """
        self.times = []
        self.values = []
        self.class_data = class_data
        self.fd = fd

    def add_value(self, time, value):
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
                'Attention levels': self.values
                }
        df = DataFrame(data, columns=['Time', 'Attention levels']).groupby('Time').sum()
        return df

    def save_to_pdf(self):
        """
        PDF report generator.

        Configuration details:
        ---------------------
        # Layout    ('P', 'L')
        # Unit      ('mm', 'cm', 'in')
        # format    ('A3', 'A4'(default), 'À5', 'letter', 'legal', (100,150))
        # fonts     ('times', 'courier', 'helvetica', 'symbol')
        # 'B' (bold), 'U' (underline), 'I' (italics)
        # w = width, h = height
        """

        df = self.get_data_frame()
        fig, ax = plt.subplots(figsize=(12, 4))
        ax.axis('tight')
        ax.axis('off')
        the_table = ax.table(cellText=df.values, colLabels=df.columns, loc='center')
        date = datetime.now()

        # This will define the ELEMENTS that will compose the template.
        elements = [
            {
                'name': 'box', 'type': 'B', 'x1': 15.0, 'y1': 15.0, 'x2': 195.0, 'y2': 280.0, 'font': 'helvetica',
                'size': 0.0,
                'bold': 0, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': None,
                'priority': 0,
            },
            {
                'name': 'company_logo', 'type': 'I', 'x1': 20.0, 'y1': 17.0, 'x2': 50.0, 'y2': 30.0, 'font': None,
                'size': 0.0,
                'bold': 0, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': 'logo',
                'priority': 2,
            },
            {
                'name': 'github_barcode', 'type': 'I', 'x1': 179.0, 'y1': 17.0, 'x2': 192.0, 'y2': 28.0, 'font': None,
                'size': 0.0,
                'bold': 0, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': 'logo',
                'priority': 2,
            },
            {
                'name': 'company_header', 'type': 'T', 'x1': 75.0, 'y1': 35.5, 'x2': 120.0, 'y2': 42.5,
                'font': 'helvetica',
                'size': 16.0, 'bold': 2, 'italic': 0, 'underline': 10, 'foreground': 0, 'background': 0, 'align': 'I',
                'text': '', 'priority': 2,
            },
            {
                'name': 'lecture', 'type': 'T', 'x1': 30.0, 'y1': 45.5, 'x2': 120.0, 'y2': 50.5, 'font': 'helvetica',
                'size': 10.0, 'bold': 1, 'italic': 0, 'underline': 5, 'foreground': 0, 'background': 0, 'align': 'I',
                'text': '', 'priority': 2,
            },
            {
                'name': 'lecture_value', 'type': 'T', 'x1': 42.0, 'y1': 45.5, 'x2': 120.0, 'y2': 50.5,
                'font': 'helvetica',
                'size': 10.0, 'bold': 1, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I',
                'text': '', 'priority': 2,
            },
            {
                'name': 'lecturer', 'type': 'T', 'x1': 30.0, 'y1': 50.5, 'x2': 120.0, 'y2': 55.5, 'font': 'helvetica',
                'size': 10.0, 'bold': 1, 'italic': 0, 'underline': 5, 'foreground': 0, 'background': 0, 'align': 'I',
                'text': '', 'priority': 2,
            },
            {
                'name': 'lecturer_value', 'type': 'T', 'x1': 47.0, 'y1': 50.5, 'x2': 120.0, 'y2': 55.5,
                'font': 'helvetica',
                'size': 10.0, 'bold': 1, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I',
                'text': '', 'priority': 2,
            },
            {
                'name': 'line_1', 'type': 'T', 'x1': 30.0, 'y1': 60.5, 'x2': 80.0, 'y2': 65.5, 'font': 'helvetica',
                'size': 10.0, 'bold': 0, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I',
                'text': '', 'priority': 2,
            },
            {
                'name': 'line_2', 'type': 'T', 'x1': 30.0, 'y1': 65.5, 'x2': 120.0, 'y2': 70.5, 'font': 'helvetica',
                'size': 10.0, 'bold': 0, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I',
                'text': '', 'priority': 2,
            },
            {
                'name': 'avg', 'type': 'T', 'x1': 30.0, 'y1': 75.5, 'x2': 120.0, 'y2': 80.5, 'font': 'helvetica',
                'size': 10.0, 'bold': 1, 'italic': 0, 'underline': 5, 'foreground': 0, 'background': 0, 'align': 'I',
                'text': '', 'priority': 2,
            },
            {
                'name': 'avg_value', 'type': 'T', 'x1': 75.0, 'y1': 75.5, 'x2': 120.0, 'y2': 80.5, 'font': 'helvetica',
                'size': 10.0, 'bold': 1, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I',
                'text': '', 'priority': 2,
            },
            {
                'name': 'Inactivity_time', 'type': 'T', 'x1': 30.0, 'y1': 80.5, 'x2': 120.0, 'y2': 85.5,
                'font': 'helvetica', 'size': 10.0, 'bold': 1, 'italic': 0, 'underline': 5, 'foreground': 0,
                'background': 0,
                'align': 'I', 'text': '', 'priority': 2,
            },
            {
                'name': 'Inactivity_time_value', 'type': 'T', 'x1': 60.0, 'y1': 80.5, 'x2': 120.0, 'y2': 85.5,
                'font': 'helvetica', 'size': 10.0, 'bold': 1, 'italic': 0, 'underline': 0, 'foreground': 0,
                'background': 0,
                'align': 'I', 'text': '', 'priority': 2,
            },
            {
                'name': 'lecture_time', 'type': 'T', 'x1': 30.0, 'y1': 90.5, 'x2': 120.0, 'y2': 85.5,
                'font': 'helvetica', 'size': 10.0, 'bold': 1, 'italic': 0, 'underline': 5, 'foreground': 0,
                'background': 0,
                'align': 'I', 'text': '', 'priority': 2,
            },
            {
                'name': 'lecture_time_value', 'type': 'T', 'x1': 70.0, 'y1': 90.5, 'x2': 120.0, 'y2': 85.5,
                'font': 'helvetica', 'size': 10.0, 'bold': 1, 'italic': 0, 'underline': 0, 'foreground': 0,
                'background': 0,
                'align': 'I', 'text': '', 'priority': 2,
            },
            {
                'name': 'graph_header', 'type': 'T', 'x1': 30.0, 'y1': 165.5, 'x2': 120.0, 'y2': 170.5,
                'font': 'helvetica', 'size': 10.0, 'bold': 1, 'italic': 0, 'underline': 5, 'foreground': 0,
                'background': 0,
                'align': 'I', 'text': '', 'priority': 2,
            },
            {
                'name': 'graph', 'type': 'I', 'x1': 65.0, 'y1': 170.0, 'x2': 150.0, 'y2': 250.0, 'font': None,
                'size': 0.0, 'bold': 0, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I',
                'text': 'logo', 'priority': 2,
            },
            {
                'name': 'rights', 'type': 'T', 'x1': 75.0, 'y1': 285.5, 'x2': 150.0, 'y2': 290.5,
                'font': 'helvetica', 'size': 7.0, 'bold': 1, 'italic': 0, 'underline': 0, 'foreground': 0,
                'background': 0, 'align': 'I', 'text': '', 'priority': 2,
            },
            # {
            #     'name': 'line1', 'type': 'L', 'x1': 100.0, 'y1': 25.0, 'x2': 100.0, 'y2': 57.0, 'font': 'helvetica',
            #     'size': 0,
            #     'bold': 0, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': None,
            #     'priority': 3,
            # },
            # {
            #     'name': 'barcode', 'type': 'BC', 'x1': 20.0, 'y1': 266.5, 'x2': 140.0, 'y2': 274.0,
            #     'font': 'Interleaved 2of5 NT', 'size': 0.75, 'bold': 0, 'italic': 0, 'underline': 0, 'foreground': 0,
            #     'background': 0, 'align': 'I', 'text': '200000000001000159053338016581200810081', 'priority': 3,
            # },
        ]

        # Here we instantiate the template and define the HEADER
        pdf_file = Template(format="A4", elements=elements, title="Sample Invoice")
        pdf_file.add_page()

        # We FILL some of the fields of the template with the information we want
        # Note we access the elements treating the template instance as a "dict"

        # Header:
        pdf_file["company_logo"] = "../public/img/SCE_logo.png"
        pdf_file["github_barcode"] = "../public/img/github.png"
        pdf_file["company_header"] = "AttentivenessRec Report"

        # Lecture and lecturer details:
        pdf_file["lecture"] = "Class:"
        pdf_file["lecture_value"] = self.class_data.lecture_value
        pdf_file["lecturer"] = "Lecturer:"
        pdf_file["lecturer_value"] = self.class_data.lecturer_value

        # Template of text:
        pdf_file["line_1"] = "AttentiveRec system collected attention data during the lecture, " \
                             "performed the statistical analysis,"
        pdf_file["line_2"] = "and reached the following results:"

        # Statistic details:
        total_time = self.times[len(self.times) - 1]

        pdf_file["avg"] = "Average attention level:"
        pdf_file["avg_value"] = str(round(df['Attention levels'].mean() * 10, 2)) + '%'

        pdf_file["Inactivity_time"] = "Inactivity time:"
        pdf_file["Inactivity_time_value"] = str(round((self.fd.no_face_time / total_time) * 100, 2)) + '%'

        pdf_file["lecture_time"] = "Length of the lecture:"
        pdf_file["lecture_time_value"] = str(round(self.times[len(self.times) - 1] / 60, 2)) + ' minutes'

        # Graph:
        pdf_file["graph_header"] = "Graph:"
        pdf_file["graph"] = "../public/img/graph.png"

        # Rights
        pdf_file["rights"] = "© 2021 Yariv Garala & Stav Lobel. All rights reserved."

        # PDF generation - render the page
        try:
            {
                pdf_file.render(
                    "../public/reports/Report_{}_{}_{}_{}.pdf".format(self.class_data.lecture_value, date.day,
                                                                      date.month, date.year))
            }
        except Exception as e:
            print("An exception occurred: ", e)
