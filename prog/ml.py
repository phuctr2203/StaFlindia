import pandas as pd
import streamlit as st
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.preprocessing import OrdinalEncoder


df = pd.read_csv("lib//data//Clean_Dataset.csv")
df.drop(columns=['Unnamed: 0'], inplace=True)
str_columns = ['airline', 'source_city', 'stops', 'destination_city', 'class']
num_columns = ['days_left']
encoder = OrdinalEncoder().fit_transform(df[str_columns])
encoder = pd.DataFrame(encoder, columns=str_columns)

X = pd.concat([encoder, df[num_columns]], axis=1)
Y = df['price']
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.4, random_state=42)
model = LinearRegression()
model.fit(x_train, y_train)
y_pred = model.predict(x_test)
st.write(X)
st.write(Y)
st.write(y_pred)

print("r2_score: ", r2_score(y_test, y_pred))
pickle.dump(model, open('model.sav', 'wb'))