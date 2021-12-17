from aicapi_yw3760 import aicapi_yw3760

import pandas as pd
import numpy as np
import os
import json
import requests
from dotenv import load_dotenv
from PIL import Image
from io import BytesIO
from IPython.core.display import display, HTML

def test_art_search():
    example = 'Monet'
    actual = aicapi_yw3760.art_search(example)
    assert type(actual) == pd.DataFrame
    
def test_tour_search():
    example = 'Monet'
    actual = aicapi_yw3760.tour_search(example)
    assert type(actual) == pd.DataFrame
    
def test_product_search():
    example = ('Rainy Day','Mug')
    actual = aicapi_yw3760.product_search(example)
    expect = type(HTML())
    assert type(actual) == expect