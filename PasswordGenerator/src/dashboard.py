import streamlit as st
from main import pin_password_generator , random_password_generator , memorable_password_generator


st.title(':zap: Password Generator')

option = st.radio(
    'Select Your Password Generator ',
    ('Random Password' , 'Pin Password' , 'Memorable Password')
)


if option == 'Pin Password':
    length = st.slider('Select The Length Of Your Password' , 8 , 32)
    generator = pin_password_generator(length)

elif option == "Memorable Password":
    length = st.slider('Select The Number Of Words' , 1 , 20)
    capitalization = st.toggle(' Capitalization ')
    seprator = st.text_input('Enter Your Seprator', value=" * ")
    generator = memorable_password_generator(length , seprator , capitalization)

elif option == "Random Password":
    length = st.slider('Select The Length Of Your Password' , 8 , 32)
    is_symble = st.toggle('Include Symble')
    is_num = st.toggle('Include Number ')
    generator = random_password_generator(length , is_num , is_symble)


password = generator
st.write(f'Your Password Is : ```{password}```')