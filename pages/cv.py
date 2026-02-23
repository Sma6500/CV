import streamlit as st

def research_experiences():
    research_experiences = st.expander("Research experience")
    research_experiences.markdown(
            """__2023-2026__: PHD student at LOG and LOCEAN supervized by Gregory Beaugrand, Roy El Hourany and Marina Levy  
            __Subject__ : Integrating Physical and Biogeochemical Ocean Data with Deep Learning: Toward Multivariable Understanding of Ocean Behavior  
            My PhD focuses on developing deep learning approaches to better
            understand and predict ocean–climate interactions by integrating
            physical and biogeochemical variables (SSH, SST, salinity, and
            phytoplankton pigments). I apply data-driven methods to ocean
            prediction, reconstruction, and spatial completion, including SSH
            forecasting, phytoplankton variability reconstruction, and
            ocean-colour gap filling. My focus is to produce physically consistent AI models and validation
            strategies for reliable climate applications.""") 
    research_experiences.markdown(
            """__Publications__ :  
            - Success and Limits of Reconstructing Phytoplankton Pigment Temporal Variations from Simultaneous Surface Ocean Physics with a Unet model (Preprint in preparation, 2026)  
            - Bridging gaps in daily global ocean-colour products using physical fields and neural networks (Submitted to Climate Informatics 2026)  
            - North-South asymmetry in subtropical phytoplankton response to recent warming. Second author.  (Submitted to Nature Communication)""")
    research_experiences.markdown(
            """__Internship supervision__ :  
            - 2024 : Artificial Intelligence for Environment: Generative deep learning models for filling gaps in Sea Surface Phytoplankton Ratios  
            - 2024 : Machine Learning Algorithm for the Prediction of Ocean Currents Estimated from Sea Surface Height Anomaly (SLA), Sea Surface Temperature (SST) and Sea Surface Salinity (SSS) time series  
            - 2025 : Down-scaling of Sea Surface Salinity (SSS) Using Deep Learning Techniques (associated publication submitted to Ocean Modeling)  
            - 2025 : Physically Consistent Sampling For Ocean Model Initialization (accepted publication in [Neurips Tackling Climate Change with Machine Learning](https://neurips.cc/virtual/2025/loc/san-diego/poster/126936))""")
    research_experiences.markdown(
            """__Conferences__ :   
            - EGU 2024 : Linking Satellite and physics-informed Data with Phytoplankton communities Using Deep Learning. [DOI](https://doi.org/10.5194/egusphere-egu24-18663)  
            - EGU 2025 : Deep learning algorithm to uncover links between satellite-derived physical drivers and biological fields. [DOI](https://doi.org/10.5194/egusphere-egu25-6755)  
            - LPS 2025 : Reconstructing Phytoplankton Community Dynamics from Ocean Physics with Deep Learning [Oral](https://lps25.esa.int/lps25-presentations/presentations/906/)
            - OSM 2026 : Integrating Physical and Biogeochemical Ocean Data with Deep Learning: Toward Multivariable Understanding of Ocean Behavior (Oral and Poster)""")    
    
    research_experiences.markdown(
        """__2022-2023__: Research engineer at LOCEAN  
        __Subject__ : Data driven strategies to improve multivariate climate data""")
    research_experiences.markdown(    
        """__Publications__ :  
        - Neural Network Approaches for Sea Surface Height Predictability Using Sea Surface Temperature. [DOI](https://doi.org/10.1017/eds.2024.33)  
        - Interhemispheric Temperature Gradient and Equatorial Pacific SSTs Drive Sahel Monsoon Uncertainties under Global Warming [DOI](https://doi.org/10.1175/JCLI-D-23-0162.1)  
        __Conferences__ :  
        - Colloquium Machine learning and data analysis in oceanography Liège 2023 : Neural network approaches for Sea Surface Height predictability using Sea Surface Temperature [Oral](https://ocean-colloquium.fsc.uliege.be/PresentationManager/colloquium/2023/abstracts/2023-01-26_19:01:30_IP_134.157.16.213.pdf)""")    

def experiences():
    experiences = st.expander("Experiences")
    experiences.markdown(
        "__2021__: Deep-learning project -LATIM, laboratory of medical information processing  \n"
        "Subject : Regularized directional representations for medical image registration applied with VoxelMorph. \
        Implementation of the following concepts : 3D Pytorch Pipeline, Preprocessing on 3D Volumes           (Vector field \
convolution), Voxelmorph from the paper ‘VoxelMorph: A Learning Framework for Deformable Medical Image \
Registration.")
    
    experiences.markdown(
        " __2020__: Data Science Internship at Direct Assurance \n"
        "-French insurance company, part of Axa Group    \n"
        "In charge of statistical studies in the Data department, I am monitoring the KPI's evolution \
        and presenting weekly reports to the board. I am crunching data to answer board of \
        Directors business requests, and then automatig these data analysis with python, SQL and HTML dashboards.\
        I help predictiong competitors advertising investment by building \
        a machine-learning algorithm (a Gradient Boosted Regression Trees) based on the company data.\
        I am also in charge of exploring new data bought to a survey company (Yougov).\
        I made hypothesis and created new KPI to straighten the global understanding of the company business, \
        with a focus on the Covid period.")
    
    experiences.markdown(
        "__2020__: [DataChallenge](https://datachallenge.sfrnet.org/) for the French Radiology Society Congress. Subject: \
        Automatic assessment of severity of coronary artery disease through AI assisted \
        coronary artery calcium score computation.    \n"
        "Main concepts implemented:    \n"
        "   - 3D Pytorch Pipeline    \n"
        "   - Preprocessing on 3D volumes (scans and segmentation masks).    \n"
        "   - DeepLab  v3+ 3D from the paper 'Encoder-Decoder with Atrous Separable Convolution for Semantic Image Segmentation'.")
    
    experiences.markdown(
        "__2019__ : Machine learning company project \n"
        "-ZF Autocruise, part of ZF Friedrichshafen an outfitter car company \n"
        "Classification method applied to error process (Data processing, machine-learning with Python). \
        Managing a team of 5 students coming from different countries (China, Tunisia and Brazil) to classify error from a chain of production. \
        Automatization of hand process in order to help the company to operate its digital transformation. \
        The result was a program that with the data of the defective part (radar parts) sort the error in one of the 37 different default type.")
    
    experiences.markdown(
        "__2019__: Internship at Zodiac Aerospace \n"
        "-French aerospace company, part of Safran Group \n"
        "Managed and optimized the packing and dispatching processing of spare parts returns.\
        New processes implemented did result in a increase of 10% in productivity (nb of parts dispatched / day) \
        and a decrease of 3% in dispatching errors.")
    
    experiences.markdown(
        "__2019__: Chairman at Student Union official, \n"
        "IMT Atlantique  \n"
        "Managed the merger of a variety of groups within the school (change & people management), \
        defined and wrote the new association status with lawyer.\
        Managed and controlled the association budget (150 000€ / year).\
        Event manager (integration’s weekend, regional sport competition, ...).")

    experiences.markdown(
        "__2020__: Student Bar Renovation, \n"
        "IMT Atlantique \n"
        "Built and managed the whole project, from inception to achievement, \
        including finding funding (50 000 €), sponsors (AB Inbev) and negotiation with all stakeholders.\
        Project successfully achieved in 10 months and on budget.")
    
    experiences.markdown(
        "__2016__: Internship at La Banque Postale \n"
        "Bank arm of the French Postal Group \n"
        "Managing an Incentive on Northeast post stations to straighten the economic implantation of the company.\
        Rewarding post offices that get the best progression during the incentive. \
        Built an excel-based analysis and Data Mining tool in order to define what’s progression regardless of sales revenue.")
        
def education():
    education = st.expander("Educational Background")
    education.subheader("2018 - 2022: National Graduate Engineering School")
    education.write(
        "IMT Atlantique (ex Telecom Bretagne), from the national competitive examination \
        Mines-Ponts.    \n"
        "2nd year major: Machine Learning & digital innovation.    \n"
        "3rd year major: Health & deep-learning.")
    education.subheader("2016 - 2018: Preparatory Classes")
    education.write(
        "Lycée Condorcet, Paris    \n"
        "Undergraduate intensive courses in mathematics, physics, and computer sciences \
        to prepare for the french 'Grandes Ecoles' national competitive examination.")
    education.subheader("2016: Scientific Baccalauréat")
    education.write(
        "Major in mathematics.    \n")

def skills():
    skills = st.expander("Skills")
    skills.markdown(
        "__IT – Programming__ : \n"
        "Linux : Ubuntu, CentOS7, comfortable with bash"
        "Python: I've an advanced knowledge of Python, including object oriented programming\n"
        "Data processing : Proficient with netcdf files"
        "R, SQL, (proficient) \
        Java, Julia (informal) \
        Proficient in MS Office tools \
        Basic Front-end knowledge (JavaScript, HTML) \
            ")
    skills.markdown(
        "__Machine-learning__ : \n"
        "Machine-learning algorithms (from linear regression to SOM), Data Science basics, Statistics, Markov Chain")
    skills.markdown(
        "__Deep-learning__ : \n"
        "Deep-learning architectures (CNN, RNN, Transformers, VAE, GAN, Diffusion..), proficient in pytorch, informal in Tensorflow and Jax"
        "To see examples of my code you can check my [github](https://github.com/Sma6500)")
    skills.markdown(
        "__Digital innovation__ : \n"
        "new economic model, business strategies, digital tools (Gant), finance basic knowledge (pricing algorithms).")
    skills.markdown(
        "__Languages__ : \n" 
        "– French (mother tongue), English (fluent), German (basics)")
    

def hobbies():
    hobbies = st.expander("Hobbies")
    hobbies.write("I like climbing, I also love reading and playing chess. \
        Obviously a lot more could be said here but that's most likely not why you're here.")

def content():
    st.title('Curriculum vitæ')
    research_experiences()
    experiences()
    education()
    skills()
    hobbies()



