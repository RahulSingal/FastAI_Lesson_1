# ------------------------------------------------------------------------------------------------------------
# | Programmer: Rahul Singal
# | File Name: library.py
# | Date Created: 10/16/2024 
# | Date Last Modified: 10/26/2024
# | Description: This will initialize and import all required libraries in one plce and initialize global variables
# ------------------------------------------------------------------------------------------------------------

# Installing FastAI required library with Python - may not need this
# !pip install -Uqq fastai duckduckgo_search

# Installing and importing required libraries
from fastcore.all import *              # Fast.AI library for Python ML
from duckduckgo_search import DDGS      # To search web images using duck duck go search engine
from fastdownload import download_url   # Simplifies downloading and caching data from URLS
from fastai.vision.all import *         # Fast.AI tool for deep learning computer vision models
import os                               # Provides functions for interacting with the OS (e.g. file management)
import numpy as np                      # Linear algebra
import pandas as pd                     # Data processing, CSV file I/O (e.g. pd.read_csv)
from fastcore.all import *              # Fast.AI tool for accelerating Python development
from time import sleep                  # Allows you to pause program execution
from pathlib import Path                # Provides an object-oriented interface for working with file system paths
from PIL import Image                   # Import Image from PIL
from IPython.display import display     # Import display function from IPython (let's me see image displayed inside a function)

