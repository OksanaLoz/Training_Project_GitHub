# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 16:46:43 2023

@author: Dell
"""

from financial_functions import years

P = 1; r = 5
n = years(P, 2*P, r)

print(f'Money has doubled after {n} years')