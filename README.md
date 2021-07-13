# Attentivness Recognition

### Attention monitoring system for students in online learning - based on [Abhishek Tandon](https://github.com/Tandon-A/emotic) project!

<p align="center">
  <img width="650" height="400" src="https://i.ibb.co/10GRLpG/Attentive-recognition.jpg">
</p>

## About The Project

___


The World Health Organization declared COVID-19 a global emergency on January 30, 2020 and an epidemic on March 11,2020.

Countries around the world responded to the epidemic by imposing restrictions on flights and gatherings and giving
directions to create distance Social, closure, curfew, cancellation of events and closure of all non-essential
institutions. As a result, the virus has had a huge impact on students, lecturers, and educational organizations around
the world. The corona plague has caused schools, colleges and universities around the world to close their doors so that
students can maintain the rules of social distance. Consequently, the transition from the frontal learning method to
online learning was necessary.

The rapid transition from one teaching method to another, together with the unpreparedness of the various institutions
are the main cause of the plethora of problems in online learning. In frontal learning the lecturer has the ability to
observe the whole class and read the facial expressions of the students during the lesson and from this to infer the
degree of listening in the class. In addition, in frontal learning, the participation and conversation that is created
among the students in the class also indicates the degree of concentration of the class, while in online learning, this
interaction is impaired.

Solving these challenges is very important, since online learning is going to be a part of our daily routine in the near
future, and we must learn and adapt to it so that we can continue to provide education in an effective and efficient way
that equals and even transcends frontal learning.

Our system has come to solve these challenges.

## Getting Started

### File structure

```
AttentivenessRec/
├── .github/                    # GitHub action configuration
│   ├── workflows
│       └── python-app.yml
├── .debug_exp/
│   ├── frames                  # Contains the last saved frame
│   │   └── frame.jpg
│   ├── models/                 # Models
│   │   └── ...
│   ├── results/                # Model training results
│   │   └── ...
│   ├── config.txt 
│   └── inference_file.txt      # Contains the frame PATH and b-box details
├── public/
│   ├── img/                    # Images of the report (The graph will update in real-time)
│   │   └── ...
│   ├── reports/                # System report
│   │   └── ...
│   └──  test_img                # Images for unit tests               
│       └── ...
├── src/
│   ├── app.py
│   ├── attention_calculator.py
│   ├── class_details.py
│   ├── emotic.py
│   ├── emotic_app.py
│   ├── emotic_dataset.py
│   ├── emotic_loop.py
│   ├── face_detector.py
│   ├── frame_provider.py
│   ├── frame_saver.py
│   ├── gui.py
│   ├── inference.py
│   ├── loss.py
│   ├── prepare_models.py
│   ├── statistics_data_loader.py
│   ├── test.py
│   └──  train.py
├── test/
│   └── unit.py                  # Currently without content   
├── venv
│   └── ...
├── .gitignore
├── README.md
└── requirements.txt
```

### Requirements

* #### We recommended using Pycharm IDE to run this project!
* #### Environments: Python 3.8 with Anaconda environment.
* #### Package manager: PIP.
* #### All `requirements.txt` dependencies installed (Will be explained later).

### Installing

###### These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

Firstly open the bash and clone this repository to your working environment by entering the command

```sh
git clone git@github.com:yariv1025/AttentivenessRec.git
```

Open the project in your IDE, integrate the system with the bash and run the pip install command listed below, for you
to be able to run this project.<br>
(This command will download locally all the packages that's needed for the running of this application.)

```sh
pip install -r requirements.txt
```

### Dev Configuration

In the run/debug configuration we will enter the following details:

```sh
Script path: "App.py PATH"
Python interpreter: "Python 3.8 with Anaconda3 environment"
Working directory: "src directory PATH"
```

In the parameters field we will enter the settings according to the desired action:

* #### Training
* #### Testing
* #### Running

###### Training Configuration

"Training configuration" for train the model.

```sh
Parameters: " --mode train --data_path PROJECT_PATH/data/emotic_pre --experiment_path PROJECT_PATH/debug_exp"
```

###### Testing Configuration

"Testing configuration" for test the model.

```sh
Parameters: "--mode test --data_path PROJECT_PATH/data/emotic_pre --experiment_path PROJECT_PATH/debug_exp"
```

###### Running Configuration

"running configuration" for running the `App.py`.

```sh
Parameters: "--mode inference --inference_file PROJECT_PATH\debug_exp\inference_file.txt --experiment_path PROJECT_PATH\debug_exp"
```

After doing so you will be able to run the app by clicking on 'Run app'

## Built With

* [Tandon-A](https://github.com/Tandon-A/emotic) -Project that uses the EMOTIC dataset and follows the methodology as
  introduced in the paper ['Context based emotion recognition using EMOTIC dataset'](https://arxiv.org/pdf/2003.13401.pdf).
* [OpenCV](https://opencv.org/) - An open source computer vision and machine learning software library with focus on
  real-time applications..
* [Pandas](https://pandas.pydata.org/) - A fast, powerful, flexible and easy to use open source data analysis and
  manipulation tool.
* [MTCNN](https://github.com/ipazc/mtcnn) - MTCNN face detection implementation for TensorFlow, as a PIP package.
* [Pytorch](https://pytorch.org/) - An open source machine learning framework that accelerates the path from research 
  prototyping to production deployment.
* [Numpy](https://numpy.org/) - Fundamental package for scientific computing with Python. 
* [Matplotlib](https://matplotlib.org/) - A comprehensive library for creating static, animated, and interactive 
  visualizations in Python.
* [tkinter](https://matplotlib.org/)  - A standard Python interface to the Tk GUI toolkit.
  

## Training, Testing & Inference
Please refer [Tandon-A](https://github.com/Tandon-A/emotic) README.md file.

## Acknowledgments & Citation
___

* [Paper](https://arxiv.org/pdf/2003.13401.pdf) - Context Based Emotion Recognition using EMOTIC Dataset.
* [Dataset Webpage](http://sunai.uoc.edu/emotic/) - EMOTions In Context, is a database of images with people in real
  environments, annotated with their apparent emotions.
* [Tandon-A](https://github.com/Tandon-A/emotic) - PyTorch implementation of Emotic CNN methodology to recognize
  emotions in images using context information.

```
R. Kosti, J.M. Álvarez, A. Recasens and A. Lapedriza, "Emotion Recognition in Context", Computer
Vision and Pattern Recognition (CVPR), 2017.
```

```
R. Kosti, J.M. Álvarez, A. Recasens and A. Lapedriza, "Context based emotion recognition using
emotic dataset", IEEE Transactions on Pattern Analysis and Machine Intelligence (PAMI), 2019.
```

## About Us
___

<p align="center">
  <img width="750" height="650" src="https://i.ibb.co/XzFVTkk/About-Us.jpg">
</p>





