import streamlit as st
import cv2
import numpy as np
from PIL import Image 
st.set_page_config(page_title="канапяяя",  layout= "wide")

st.title("умное фото скачать")
st.write("розумне фото завантажити")
st.sidebar.header("фыльтр") 

uploaded_file = st.file_uploader ("оберить зображення...", type=["png", "jpeg"])
if uploaded_file is not None: 
    image = Image.open(uploaded_file)

    img_array = np.array(image)

    col1, col2 = st.columns(2)

    with col1: 
        st.subheader("оригінальне фото")
        st.image(img_array, use_container_width=True)
        
    filter_option = st.sidebar.selectbox("Виберить ефект:", 
                                     ["оріг", "інверсія", 
                                      "хорошое качество", 
                                      "яркость", "чб"])
    processed_img = img_array.copy()

    if filter_option == "чб": 
        gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)
        processed_img = cv2.cvtColor(gray, cv2.COLOR_GRAY2RGB)
    elif filter_option == "хорошое качество":
        processed_img = cv2.GaussianBlur(img_array, (15,15),0)
    elif filter_option == "яркость":
        processed_img = cv2.convertScaleAbs(img_array, alpha=1.0, beta=50)
    elif filter_option == "інверсія": 
        processed_img = 255 - img_array

    with col2:
        st.subheader("оброблене фото")
        st.image(processed_img, use_container_width=True)

        result_img = Image.fromarray(processed_img)

        import io
        buf = io.BytesIO()
        result_img.save(buf, format="JPEG")
        byte_im = buf.getvalue()

        st.download_button(
            label="скачать фотку", 
            data= byte_im,
            file_name="smart_edit.jpeg",
            mime= "image/jpeg"
        )