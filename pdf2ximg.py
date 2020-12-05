#conda install -c conda-forge poppler
#pip install pdf2image
import streamlit as st 
from pdf2image import convert_from_path
import os

st.title("Convert PDF into Multiple Images")
pdf_file = st.selectbox('Select a file', os.listdir('.'))

if st.button("Convert PDF to Images"):
    images = convert_from_path(pdf_file)
    for i, image in enumerate(images):
        fname = "image" + str(i) + ".png"
        image.save(fname, "PNG")
        st.write('Created: '+fname)