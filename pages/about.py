import streamlit as st

def content():
    st.title('About me')
    st.write(
"""I am a French PhD candidate in oceanography and machine learning, 
currently completing my doctoral research with a planned defense in November 2026. 
My work focuses on understanding and predicting ocean–climate interactions by integrating physical 
and biogeochemical ocean observations through deep learning approaches. 
Ocean variables such as sea surface temperature, salinity, sea surface height, and phytoplankton pigments 
are strongly interconnected, yet are often observed through heterogeneous and incomplete datasets. 
My research explores how data-driven models can leverage these cross-variable dependencies 
while remaining consistent with established physical and biogeochemical knowledge.
During my PhD, I develop and evaluate deep learning methods for ocean prediction, reconstruction, 
and spatial completion, including forecasting sea surface height from temperature fields, 
reconstructing long-term phytoplankton variability from physical drivers, and improving ocean-colour gap filling 
using autoencoders and diffusion-based models. 
Beyond methodological development, my work aims to establish validation strategies ensuring that AI models 
remain physically meaningful when applied to climate science.

I am particularly interested in collaborations at the interface between oceanography, 
climate science, and machine learning, and I am currently seeking postdoctoral opportunities within research groups 
focusing on deep learning for Earth system applications.""")
        
    st.write("You can find my github [here](https://github.com/Sma6500)")
