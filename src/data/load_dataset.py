# -*- coding: utf-8 -*-
import logging
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



class LoadDataset:

    def __init__(self):
        """ TODO Doc """
        self.logger = logging.getLogger(__name__)


    def read_raw_data(self):
        """ TODO Doc """
        train_values = pd.read_csv('../data/raw/train_values.csv')
        train_labels = pd.read_csv('../data/raw/train_labels.csv')
        test_values = pd.read_csv('../data/raw/test_values.csv')
        return train_values, train_labels, test_values



