#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd

from .standard import IF, REF

def REF(DF, N):
	return DF.iloc(N)