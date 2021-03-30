import os

import torch
from emotic_app import emotic


def create_model():
    emotic()
    print("Model Created.")


def get_model():
    print(emotic())

