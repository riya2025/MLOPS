import pandas as pd
data=pd.read_excel(r"C:\Users\LEN\Documents\PIzza.xlsx")
from sklearn.linear_model import LinearRegression
a=LinearRegression()
x=data.iloc[: , :-1]
y=data.iloc[: , -1]
a.fit(x,y)
import pickle
pickle.dump(a,open("model1.pkl","wb"))
