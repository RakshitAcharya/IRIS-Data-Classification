import streamlit as st
import pickle
import joblib



knn=open("knn_iris.pkl","rb")
knn_model=joblib.load(knn)


   
st.title("Streamlit Tutorial")
st.header("                      IRIS CLASSIFICATION")
sl=st.slider('Select Sepal Length', 0.0, 10.0)
sw=st.slider('Select Sepal Width', 0.0, 10.0)
pl=st.slider('Select Petal Length', 0.0, 10.0)
pw=st.slider('Select Petal Width', 0.0, 10.0)
inputs=[[sl,sw,pl,pw]]
if st.button('Classify'):
    num=(knn_model.predict(inputs))
    if num<0.5:
        st.success("Setosa")
    elif num <1.5:
        st.success('Versicolor')
    else:
        st.success('Virginica')
