import streamlit as st

import pickle

# import os 

# print("-------------------------------------------")
# print(os.getcwd())

pickle_in = open("./myFolder/Regressor.pkl","rb")

regressor = pickle.load(pickle_in)


def prediction(cylinders,displacement,horsepower,weight,acceleration,modelyear,origin):
    prediction = regressor.predict([[cylinders,displacement,horsepower,weight,acceleration,modelyear,origin]])
    print(prediction)
    return prediction
    
    
def main():
    
    #st.write("## streamlit Fuel consumption ML WEBApp ")
    
    html_temp = """
    <div style = "background-color:lightblue;padding:13px">
    <h1 style = "color:black;text-align:center;">streamlit Fuel consumption ML WEBApp</h1>
    </div>
    """
    
    st.markdown(html_temp,unsafe_allow_html=True)
    
    cylinders = st.text_input("Cylinders")
    displacement = st.text_input("Displacement")
    horsepower = st.text_input("Horsepower")
    weight = st.text_input("Weight")
    acceleration = st.text_input("Acceleration")
    modelyear = st.text_input("modelyear")
    origin = st.text_input("origin")
    result = "" 
    
    if st.button('Predict'):
        result = prediction(cylinders,displacement,horsepower,weight,acceleration,modelyear,origin)
    st.success("The Output is {}".format(result))
    
       
if __name__=="__main__":
    main()
