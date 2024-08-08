import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import Binarizer
header= ['preg','plas','pres','skin','test','mass','pedi','age','class']
data = pd.read_csv('./data/pima-indians-diabetes.data.csv',
                   names=header)
array = data.values
X = array[:,0:8]
Y = array[:,8]
# scaler=MinMaxScaler(feature_range=(0,1))
# rescaled_X=scaler.fit_transform(X)
# print(rescaled_X)
# -------------------------------------딥러닝을 하기 위해 데이터를 변환시켜 주는 거임=중요이거만 쓰면됨
# 어떤걸 사용하든 상관없음
# scaler=StandardScaler()
# rescaled_X=scaler.fit_transform(X)
# print(rescaled_X)
# -------------------------------------------------------------
scaler = Binarizer(threshold=0.5)
rescaled_X=scaler.fit_transform(X)
print(rescaled_X)
# ------------------0,1로 변환
