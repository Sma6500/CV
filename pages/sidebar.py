import streamlit as st
import base64
from typing import List


def get_base64_from_png(png_path: str) -> str:
    with open(png_path, "rb") as image_file:
        return base64.b64encode(image_file.read())

def image_link(link: str, png_path: str) -> str:
    image_base64 = get_base64_from_png(png_path)
    html = f"<a href={link}><img src='data:image/png;base64,{image_base64.decode()}'></a>"
    return html


def sidebar(pages: List[str]) -> st.radio:
    st.sidebar.image("img/me_min.png", use_column_width=True)
    st.sidebar.subheader('Luther Ollier')
    st.sidebar.markdown("Research engineer at LOCEAN.")
    left_column, right_column = st.sidebar.beta_columns([2,2])
    html = image_link('https://github.com/Sma6500', "./img/github_min.png")
    left_column.markdown(html, unsafe_allow_html=True)
    html = image_link('https://www.linkedin.com/in/luther-ollier', "./img/linkedin_min.png")
    right_column.markdown(html, unsafe_allow_html=True)
    selection = st.sidebar.radio("Go to", pages)
    return selection
