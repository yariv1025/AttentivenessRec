# Attentivness Recognition

### Attention monitoring system for students in online learning



<p align="center">
  <img width="400" height="250" src="https://i.ibb.co/10GRLpG/Attentive-recognition.jpg">
</p>


## About The Project
___

> The World Health Organization declared COVID-19 a global emergency on January 30, 2020 and an epidemic on March 11, 2020.
> <br> Countries around the world responded to the epidemic by imposing restrictions on flights and gatherings and giving directions to
> <br> create distance Social, closure, curfew, cancellation of events and closure of all non-essential institutions. As a result, the virus
> <br> has had a huge impact on students, lecturers, and educational organizations around the world. The corona plague has caused
> <br> schools, colleges and universities around the world to close their doors so that students can maintain the rules of social distance.
> <br> Consequently, the transition from the frontal learning method to online learning was necessary.
>
> The rapid transition from one teaching method to another, together with the unpreparedness of the various institutions are the main cause
> <br> of the plethora of problems in online learning.
In frontal learning the lecturer has the ability to observe the whole class and read the facial
> <br> expressions of the students during the lesson and from this to infer the degree of listening in the class. In addition, in frontal learning, the
> <br> participation and conversation that is created among the students in the class also indicates the degree of concentration of the class, while
> <br> in online learning, this interaction is impaired.
>
>Solving these challenges is very important, since online learning is going to be a part of our daily routine in the near future, and we must
> <br> learn and adapt to it so that we can continue to provide education in an effective and efficient way that equals and even transcends frontal learning.
>
>Our system has come to solve these challenges.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.
<br><br>
 
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
├── docs/
│   ├── Annotations
│   │   └── ...
│   ├── emotic
│   │   └── ...
│   └──  emotic_pre
│        └── ...
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
│   ├── model_creator.py
│   ├── prepare_models.py
│   ├── statistics_data_loader.py
│   ├── test.py
│   └──  train.py
├── test/
│   ├── unit.py             # Currently without content   
│   ├── feature.py          # Currently without content
│   └── Integration.py      # Currently without content
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
___
* [OpenCV](https://opencv.org/) - An open source computer vision and machine learning software library with focus on real-time applications..
* [EMOTIC](http://sunai.uoc.edu/emotic/) -  EMOTions In Context, is a database of images with people in real environments, annotated with their apparent emotions.
* [Pandas](https://pandas.pydata.org/) - A fast, powerful, flexible and easy to use open source data analysis and manipulation tool. 
* [MTCNN](https://github.com/ipazc/mtcnn) - A fast, powerful, flexible and easy to use open source data analysis and manipulation tool. 
* [emotic](https://github.com/Tandon-A/emotic) - . 

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
```
```
```
```
```
```


## About Us
___
<table style="color: white">
	<thead>
	</thead>
	<tr>
		<td>
            <p align="center">
              <img width="250" height="250" src="https://media-exp1.licdn.com/dms/image/D4E35AQHT3pvCkLMO0Q/profile-framedphoto-shrink_800_800/0/1622721618153?e=1622815200&v=beta&t=cNbdqCszJScpmGxDvBfHIfL4A2nbkyh7FD3VJpP-94M" height="auto" width="200" style="border-radius:50%">
            </p>
		</td>
		<td>
                        <p align="center">
              <img width="250" height="250" src="https://media-exp1.licdn.com/dms/image/C4D35AQEgn6h2WEVx_A/profile-framedphoto-shrink_400_400/0/1611431372357?e=1622815200&v=beta&t=jfAKrHsPNZ14x8C1OcWeFPCiu87A5OspuxznJO39QEI" height="auto" width="200" style="border-radius:50%">
            </p>
		</td>
	</tr>
	<tr>
		<td>
            <strong>Name: <span dir="ltr">Yariv Garala</span></strong><br>
            <strong>Role: Software Engineering </strong><br>
		</td>
		<td>
            <strong>Name: <span dir="ltr">Stav Lobel</span></strong><br>
            <strong>Role: Software Engineering </strong><br>
		</td>
	</tr>
</table>


## License
---
MIT?




