import streamlit as st
import pickle



lin_model=pickle.load(open('lin_model.pkl','rb'))
knn_model=pickle.load(open("knn_iris.pkl","rb"))

def classify(num):
    if num<0.5:
        return 'Setosa'
    elif num <1.5:
        return 'Versicolor'
    else:
        return 'Virginica'
def main():
   
    st.title("Streamlit Tutorial")
    st.header("                      IRIS CLASSIFICATION")
    sl=st.slider('Select Sepal Length', 0.0, 10.0)
    sw=st.slider('Select Sepal Width', 0.0, 10.0)
    pl=st.slider('Select Petal Length', 0.0, 10.0)
    pw=st.slider('Select Petal Width', 0.0, 10.0)
    inputs=[[sl,sw,pl,pw]]
    if st.button('Classify'):
        st.success(classify(knn_model.predict(inputs)))
    
   


if __name__=='__main__':
    main()
