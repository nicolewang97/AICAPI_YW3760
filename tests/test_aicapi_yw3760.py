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
    actual2 = aicapi_yw3760.art_search(example)
    assert type(actual2) == pd.DataFrame
    
def test_tour_search():
    example = 'Monet'
    actual3 = aicapi_yw3760.tour_search(example)
    assert type(actual3) == pd.DataFrame
    
def test_pic_search():
    actual = aicapi_yw3760.pic_search('Water Lillies','Monet')
    assert actual is not None
    
def test_product_search():
    actual4 = aicapi_yw3760.product_search('Rainy Day','Monet')
    assert actual4 is not None