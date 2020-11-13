import streamlit as st


def experiences():
    experiences = st.beta_expander("Experiences")
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
    education = st.beta_expander("Educational Background")
    education.subheader("2018 - 2022: National Graduate Engineering School")
    education.write(
        "IMT Atlantique (ex Telecom Bretagne), from the national competitive examination \
        Mines-Ponts.    \n"
        "2nd year major: Machine Learning & digital innovation.    \n"
        "3rd year major: Mathematical engineering & deep-learning.")
    education.subheader("2016 - 2018: Preparatory Classes")
    education.write(
        "Lycée Condorcet, Paris    \n"
        "Undergraduate intensive courses in mathematics, physics, and computer sciences \
        to prepare for the french 'Grandes Ecoles' national competitive examination.")
    education.subheader("2016: Scientific Baccalauréat")
    education.write(
        "Major in mathematics.    \n")

def skills():
    skills.markdown(
        "__IT – Programming__ : \n"
        "Python: I've an advanced knowledge of Python, including object oriented programming\n"
        "R, SQL, (proficient) \
        Java, Julia (informal) \
        Proficient in MS Office tools \
        Basic Front-end knowledge (JavaScript, Visual Studio) \
            ")
    skills.markdown(
        "__Machine-learning__ : \n"
        "Machine-learning algorithms (sklearn, pytorch), Data Science basics, Statistics, Markov Chain")
    skills.markdown(
        "__Digital innovation__ : \n"
        "new economic model, business strategies, new digital tools, finance basic knowledge (pricing algorithms).")
    skills.markdown(
        "__Languages__ : \n" 
        "– French (mother tongue), English (fluent), German (advanced)")
    

def hobbies():
    hobbies = st.beta_expander("Hobbies")
    hobbies.write("I play the piano. I also love reading and playing chess. \
        Obviously a lot more could be said here but that's most likely not why you're here.")

def content():
    st.title('Curriculum vitæ')
    experiences()
    education()
    skills()
    hobbies()
    


