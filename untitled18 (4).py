# -*- coding: utf-8 -*-
"""Untitled18.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ro4nI9YXI7MdMjgPDOHw-9ODZFuFLfyJ
"""

import pandas as pd

baza = [{'Country': 'Germaniya', "WHO COVID-19 cases": 100}]


db = pd.DataFrame(baza)
print(db)

filtr = db[db["Country"] == "Germaniya"]
print(filtr)