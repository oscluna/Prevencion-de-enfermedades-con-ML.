import pandas as pd
import numpy as np
def transformAge(df):
    mask1 = (df['Age']>=55) 
    df.loc[mask1, 'Age'] = 70

    mask2 = (df['Age']<=55) & (df['Age']>= 45)
    df.loc[mask2, 'Age'] = 49

    mask3 = (df['Age']<=45)
    df.loc[mask3, 'Age'] = 31

def transformFBS(df):
    mask1 = (df['FastingBS'] == 1)
    df.loc[mask1, 'FastingBS'] = 79

    mask2 = (df['FastingBS'] == 0) 
    df.loc[mask2, 'FastingBS'] = 48


def transformSEX(df):
    mask1 = (df['Sex'] == 1) 
    df.loc[mask1, 'Sex'] = 63

    mask3 = (df['Sex'] == 0) 
    df.loc[mask3, 'Sex'] = 25


def transformEXA(df):
    mask1 = (df['ExerciseAngina'] == 1) 
    df.loc[mask1, 'ExerciseAngina'] = 85

    mask3 = (df['ExerciseAngina'] == 0) 
    df.loc[mask3, 'ExerciseAngina'] = 35

def transformECG(df):
    mask1 = (df['RestingECG'] == 0) 
    df.loc[mask1, 'RestingECG'] = 56
    

    mask1 = (df['RestingECG'] == 1) 
    df.loc[mask1, 'RestingECG'] = 51
   

    mask1 = (df['RestingECG'] == 2) 
    df.loc[mask1, 'RestingECG'] = 65
    

def transformST(df):
    mask1 = (df['ST_Slope'] == 0) 
    df.loc[mask1, 'ST_Slope'] = 77
    
    mask1 = (df['ST_Slope'] == 1) 
    df.loc[mask1, 'ST_Slope'] = 82
   
    mask1 = (df['ST_Slope'] == 2) 
    df.loc[mask1, 'ST_Slope'] = 19
    

def transformChest(df):
    mask1 = (df['ChestPainType'] == 0) 
    df.loc[mask1, 'ChestPainType'] = 79

    mask1 = (df['ChestPainType'] == 1) 
    df.loc[mask1, 'ChestPainType'] = 13

    mask1 = (df['ChestPainType'] == 2) 
    df.loc[mask1, 'ChestPainType'] = 35

    mask1 = (df['ChestPainType'] == 3) 
    df.loc[mask1, 'ChestPainType'] = 43

def transformMaxHr(df):
    mask1 = (df['MaxHR']>=160) 
    df.loc[mask1, 'MaxHR'] = 20 

    mask1 = (df['MaxHR']>=160) & (df["MaxHR"]<=140)
    df.loc[mask1, 'MaxHR'] = 47

    mask1 = (df['MaxHR']>=140) & (df["MaxHR"]<=120)
    df.loc[mask1, 'MaxHR'] = 63

    mask1 = (df['MaxHR']<=120) 
    df.loc[mask1, 'MaxHR'] = 76

def transformOldpeak(df):
    mask1 = (df['Oldpeak']>=3) & (df['Oldpeak']<=7)
    df.loc[mask1, 'Oldpeak'] = 91
    mask1 = (df['Oldpeak']>=2)& (df['Oldpeak']<=3)
    df.loc[mask1, 'Oldpeak'] = 85

    mask1 = (df['Oldpeak']>=0) & (df['Oldpeak']<2)
    df.loc[mask1, 'Oldpeak'] = 52

    mask1 = (df['Oldpeak']>=-6) & (df['Oldpeak']<=0.1)
    df.loc[mask1, 'Oldpeak'] = 69