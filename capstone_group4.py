''' 
* @Author: Derick.Zhengkun Du  
* @Date: 2022-03-31 20:39:41  
* @Last Modified by:   Derick.Zhengkun Du  
* @Last Modified time: 2022-03-31 20:39:41  
* @Purpose: Movie meta analysis
'''
import pandas as pd
import numpy as np
import kaggle
from kaggle.api.kaggle_api_extended import KaggleApi
import zipfile


# Check none value
def checkNone(givenlist, value):
    """
    This function Check none value in a list.
    
    arguments: list
    returns: Boolean index
    
    """
    return all([element == value for element in givenlist])


# Create profit
def prof(df, rev, bug, out):
    """
    This function Create profit to a dataframe.
    
    arguments: dataframe and corresponding variables
    returns: profit column
    
    """
    for i in range(df.shape[0]):
        if df[bug][i] == 0 or df[rev][i] == 0:
            df[out][i] = 0
        else:
            df[out][i] = df[rev][i] - df[bug][i]

    return df[out]


# Create roi
def roi(df, rev, bug, out):
    """
    This function Create ROI to a dataframe.
    
    arguments: dataframe and corresponding variables
    returns: ROI column
    
    """
    for i in range(df.shape[0]):
        if df[bug][i] == 0 or df[rev][i] == 0:
            df[out][i] = 0
        else:
            df[out][i] = (df[rev][i] - df[bug][i]) / df[bug][i]

    return df[out]


# use api to extract data from kaggle
def extData(user, key, filename):
    """
    This function use api to extract data from kaggle and read csv.
    
    arguments: api user and key, filename in the kaggle
    returns: dataframe of csv
    
    """
    token = {"username": f"{user}", "key": f"{key}"}  # Kaggle API Token
    api = KaggleApi(
        token
    )  #A Kaggle API Token is needed in C:/users ... /.kaggle/kaggle.json
    api.authenticate()
    api.dataset_download_file(
        'zhengkundu/movie', file_name=f'{filename}.csv'
    )  #Import compressed dataset from https://www.kaggle.com/datasets/zhengkundu/movie
    with zipfile.ZipFile(f'{filename}.csv.zip', 'r') as zipref:
        zipref.extractall()  #decompress data

    return pd.read_csv(f'{filename}.csv')
