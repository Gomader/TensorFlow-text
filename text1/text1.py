import tensorflow as tf
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

data = pd.read_csv('./泰坦尼克数据集/test.csv')

plt.scatter(data.Age,data.SibSp)