# Attention and concentration monitoring system for students in online learning
(Facial Emotion Recognition by Machine Learning)

<p align="center">
  <img width="250" height="50" src="https://imagehost.imageupload.net/2020/04/27/injection.jpg">
</p>


## About The Project
___

> The World Health Organization declared COVID-19 a global emergency on January 30, 2020 and an epidemic on March 11, 2020.
> Countries around the world responded to the epidemic by imposing restrictions on flights and gatherings and giving directions to
> create distance Social, closure, curfew, cancellation of events and closure of all non-essential institutions. As a result, the virus
> has had a huge impact on students, lecturers, and educational organizations around the world. The corona plague has caused
> schools, colleges and universities around the world to close their doors so that students can maintain the rules of social distance.
> Consequently, the transition from the frontal learning method to online learning was necessary.
>
> The rapid transition from one teaching method to another, together with the unpreparedness of the various institutions are the main cause
> of the plethora of problems in online learning. In frontal learning the lecturer has the ability to observe the whole class and read the facial
> expressions of the students during the lesson and from this to infer the degree of listening in the class. In addition, in frontal learning, the
> participation and conversation that is created among the students in the class also indicates the degree of concentration of the class, while
> in online learning, this interaction is impaired.
>
> Solving these challenges is very important, since online learning is going to be a part of our daily routine in the near future, and we must
> learn and adapt to it so that we can continue to provide education in an effective and efficient way that equals and even transcends frontal learning.
>
>Our system has come to solve these challenges.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.
<br><br>
 
###### File structure
```
AttentivenessRec/
├── .github
│   ├── workflows
│       └── python-app.yml
├── .debug_exp
│   ├── frames
│   │   └── frame.jpg
│   └── logs
│      ├── train
│      └── val
├── docs
│   ├── Annotations
│   │   └── ...
│   ├── emotic
│   │   └── ...
│   └──  emotic_pre
│        └── ...
├── src/
│   ├── 
│   ├── 
│   ├── 
│   ├── 
│   ├── 
│   ├── 
│   ├── 
│   ├── 
│   ├── 
│   └──  
├── test/
│   ├── unit.js 
│   └── test.js
├── venv
│   └── ...
├── .gitignore
├── =4.2b1        # Check this file
├── Dockerfile    # Try to implement
├── README.md
└──requirements.txt

```
###### Requirements
* ####Environments: Python 3.8 with Anaconda environment.
* ####All `requirements.txt` dependencies installed (Will be explained later).

###### Prerequisites
We recommended using Pycharm IDE to run this project!
<br>
Firstly open the bash and clone this repository to your working environment by entering the command

```sh
git clone git@github.com:yariv1025/AttentivenessRec.git
```

###### Installing
run the pip install command for you to be able to run this project.
(This command will download locally all the packages that's needed for the developing and running of this application.)

```sh
pip install -r requirements.txt
```

###### Running Configuration
Add "running configuration" to running the `App.py`.

```sh
Script path: "App.py PATH"
Parameters: "experiment_path ..\debug_exp PATH"
Python interpreter: "Python 3.8 with Anaconda3 environment"
Working directory: "src directory PATH"
```
 
After doing so you will be able to run the app by clicking on 'Run app'

## Built With
___
* [OpenCV](https://opencv.org/) - OpenCV (Open Source Computer Vision Library) is an open source computer vision and machine learning software library.
* [ÝOLO](https://github.com/ultralytics/yolov3) -  Future object detection methods.
* [EMOTIC Datadet](http://sunai.uoc.edu/emotic/) -  EMOTions In Context, is a database of images with people in real environments, annotated with their apparent emotions.

## Training
___


## Testing
___


## Inference
___
`App.py` runs on a video streaming sources, performs analysis of the frames and presents conclusions.
<p align="center">
  <img width="250" height="50" src="https://imagehost.imageupload.net/2020/04/27/injection.jpg">
</p>

The conclusions are saved in the `inference_list.txt` file.
```sh
...\AttentivenessRec\debug_exp\frames\frame.jpg Anticipation Confidence Disconnection Engagement Excitement Happiness 5.9682 5.2205 6.6595
```

## Citation
___

## About Us
___

## License
---
MIT?




