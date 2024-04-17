#------------------------------------------------------------------------
# Import
#------------------------------------------------------------------------
import streamlit as st
from PIL import Image
import random


# Streamlit page setup
icon = Image.open("MTSS.ai_Icon.png")
st.set_page_config(
    page_title="LeVesseur | Profile", 
    page_icon=icon,
    layout="centered", 
    initial_sidebar_state="auto",
    menu_items={
        'About': "### *This application was created by*  \n### LeVesseur Ph.D | MTSS.ai"
    }
)

# with open("style.css") as f:
with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#------------------------------------------------------------------------
# Header
#------------------------------------------------------------------------

# st.write('''
# # Cheyne LeVesseur, Ph.D.
# ##### *Profile* 
# ''')

st.write('''
# Cheyne LeVesseur :grey[PhD]
''')

image = Image.open('Profile.png')
st.image(image, width=350)

#------------------------------------------------------------------------
# LLM
#------------------------------------------------------------------------

# # Define a list of possible placeholder texts
# placeholders = [
#     'Example: Tell me about your graduate experience',
#     'Example: What motivates you?',
#     'Example: What is your biggest strength?',
#     'Example: Do you have hobbies outside of work?',
#     'Example: Who inspires you?',
# ]

# # Select a random placeholder from the list
# if 'placeholder' not in st.session_state:
#     st.session_state.placeholder = random.choice(placeholders)
    
# with st.form("Question",clear_on_submit=True):
#     q = st.text_input(label='Ask a Question', placeholder=st.session_state.placeholder, value='', )
#     submitted = st.form_submit_button("Submit")
    
#     st.divider()

#------------------------------------------------------------------------
# Introduction
#------------------------------------------------------------------------

st.markdown('## Introduction', unsafe_allow_html=True)
st.info('''
- PhD in Psychology, experienced in research methodology, data science, teaching, and leveraging expertise to enhance education through data-driven methods. 
- Proficient in managing data lifecycle with robust modeling and analysis; skilled in NLP, forecasting, machine learning, and survey design/validation.
- Proven ability in program evaluation and research, developing strategies for effective educational policy and MTSS implementation.
Published author and presenter, contributing substantial research to the field of education, particularly around MTSS and educational outcomes.
''')

# st.markdown(
#   "##### Connect with LinkedIn[![LinkedIn](https://upload.wikimedia.org/wikipedia/commons/8/81/LinkedIn_icon.svg)](https://www.linkedin.com/in/levesseur/)")

#------------------------------------------------------------------------
# Navigation bar
#------------------------------------------------------------------------

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-light" style="background-color: #F5F5F5;">
  <a class="navbar-brand" href="https://www.linkedin.com/in/levesseur/" target="_blank">LeVesseur</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item">
        <a class="nav-link" href="#projects">Projects</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#career">Career</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#scholarship">Scholarship</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#skills">Skills</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#connect">Connect</a>
      </li>
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">↑<span class="sr-only">(current)</span></a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

#------------------------------------------------------------------------
# Function for columns/text layout
#------------------------------------------------------------------------

# def txt(a, b):
#   col1, col2 = st.columns([4,1])
#   with col1:
#     st.markdown(a)
#   with col2:
#     st.markdown(b)

def txt(a, b):
    col1, col2 = st.columns([4, 1])
    with col1:
        st.markdown(a, unsafe_allow_html=True)  # Allow HTML tags
    with col2:
        st.markdown(b, unsafe_allow_html=True)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)
     
#------------------------------------------------------------------------
# Projects
#------------------------------------------------------------------------
##################### White space for navigation bar
st.markdown('''
<style>
.white-text {
    color: white;
}
</style>

<div class="white-text">

## Projects

</div>
''', unsafe_allow_html=True)
#####################

st.markdown('''
## Projects
''')

# st.success('- [MTSS.ai | AI Technical Assistance](http://www.MTSS.ai)') 
st.success('- [InkQA | Resource AI RAG Applications](http://www.inkqa.com)')
st.success('- [Stxtement | Alt Text + Images](http://www.stxtement.com)')
st.success('- [MTSS GPT | Conversational AI Language Model](https://mtssgpt-6204cd3bf5a6.herokuapp.com/)')
    
#------------------------------------------------------------------------
# Education
#------------------------------------------------------------------------
##################### White space for navigation bar
st.markdown('''
<style>
.white-text {
    color: white;
}
</style>

<div class="white-text">

## Education

</div>
''', unsafe_allow_html=True)
#####################

st.markdown('''
## Education
''')

txt('**PhD**, School Psychology, <span style="color: grey;">*University of Massachusetts*, Amherst, MA</span>',
'2015')
st.markdown('''
- GPA: `4.0`
- Dissertation: `Implementing Universal Social And Emotional Learning Programs: The Development, Validation, And Inferential Findings From The Schoolwide SEL Capacity Assessment`
- Research Assistant: `Social And Emotional Learning Lab` (PI: Sara Whitcomb, Ph.D.)
''')

txt('**MA**, Education, <span style="color: grey;">*University of Massachusetts*, Amherst, MA</span>',
'2015')
st.markdown('''
- GPA: `4.0`
- Teaching Assistant: School Psychology Practicum
''') 

txt('**BA**, Psychology, <span style="color: grey;">*Oakland University*, Rochester, MI</span>',
'2008')
st.markdown('''
- GPA: `3.8`
- Cum Laude, Departmental Honors
- Research Assistant: `Psychopharmacology Lab` (PI: Keith Williams, Ph.D.)
- Research Assistant: `Emotion and Perception Lab` (PI: Dean Purcell, Ph.D.)
''')    

#------------------------------------------------------------------------
# Career
#------------------------------------------------------------------------
##################### White space for navigation bar
st.markdown('''
<style>
.white-text {
    color: white;
}
</style>

<div class="white-text">

## Career

</div>
''', unsafe_allow_html=True)
#####################

st.markdown('''
## Career
''')

st.markdown('''
#### Current
''')

txt('**Data Scientist**, <span style="color: grey;">*MiMTSS Technical Assistance Center*, Department of Education, MI</span>',
'2020-present')
# txt('**Data Scientist**, *MiMTSS Technical Assistance Center*, Department of Education, MI',
# '2020-present')
st.markdown('''
I specialize in `mixed-methods research` for Multi-Tiered System of Supports (`MTSS`) initiatives, emphasizing advanced data modeling and analysis to enhance educational strategies. I proficiently manage the data lifecycle, utilizing robust methods for collection, analysis, and interpretation. My role in `program evaluation` includes developing comprehensive plans and logic models underpinned by data-driven strategies. With expertise in statistics, NLP, forecasting, machine learning, and survey design/validation, I deliver impactful insights and informed `decision-making`. key points: 
- Manage the entire data lifecycle, employing robust data modeling and analysis methods.
- Spearhead mixed-methods research, creating advanced models and algorithms for educational data analysis.
- Refine and enhance data visualization and reporting, effectively presenting complex data insights to stakeholders with clarity and precision.
- Programming Languages: Python and SAS
- Certifications: What Works Clearinghouse (WWC) Reviewer - Group Design, PBIS and SWIS Facilitator
''')

txt('**Adjunct Professor**, <span style="color: grey;">*Grand Valley State University*, Allendale, MI</span>', '2023-present')

st.markdown('''
- Advanced `Research Methods`, undergraduate level
''')


st.markdown('''
#### Past
''')

txt('**Research and Evaluation Specialist**, <span style="color: grey;">*MiMTSS TA Center*, MDE, MI</span>',
'2018-2021')
st.markdown('''
I focused on enhancing MTSS implementation and educational outcomes. I was responsible for `designing and executing studies` to assess the effectiveness of education policies. I worked closely with stakeholders such as educators, policymakers, and community members to understand their needs and concerns and to ensure that evaluation and research efforts aligned with organizational goals and strategic plans. My duties included data analysis, identifying trends, and guiding policy decisions through program evaluations. Key points:  
- Developed program `evaluation plans`, `logic models`, and `assessment schedules`. 
- Conducted evaluations and research to measure the effectiveness of educational policies and programs.
- Utilized SAS and Excel for statistical analysis and data visualization.
- Collaborated with stakeholders to align research efforts with organizational goals.
''')

txt('**Adjunct Professor**, <span style="color: grey;">*Western Michigan University*, Kalamazoo, MI</span>',
'2016-2019')
st.markdown('''
- `Research Methods`, graduate level
''')

txt('**School Climate Transformation Specialist**, <span style="color: grey;">*MiMTSS TA Center*, MDE, MI</span>',
'2015-2018')
st.markdown('''
I guided and supported the implementation of MTSS frameworks in educational systems. My role involved `developing content` and deliverying `professional learning` on Positive Behavioral Interventions and Supports (PBIS) for district teams. I coordinated and led technical assistance for PBIS Coordinators and trainers, focusing on local professional development activities. I provided professional development, created instructional content, and facilitated knowledge transfer. Key points:
- Provided direction, guidance, and support to Intermediate School District and Local School District implementation planning teams for developing multiple levels of competency within the educational system to implement, with fidelity, a durable multi-tiered behavioral framework.
- Provided professional development, developed instructional content, and facilitated knowledge transfer.
''')

txt('**Lecturer**, <span style="color: grey;">*Lansing Community College*, Lansing, MI</span>',
'2015-2017')
st.markdown('''
- Introduction to Psychology, undergraduate level
''')

txt('**School Psychologist & MTSS Coordinator**, <span style="color: grey;">*West Ottawa School District*, Holland, MI</span>',
'2014-2015')
st.markdown('''
I focused on `conducting psychological assessments and evaluations`. I developed and executed `interventions` for behavioral and academic challenges and played a key role in creating individualized education plans. Additionally, my role as an MTSS Coordinator involved leading the implementation and management of an MTSS framework, enhancing educational strategies and outcomes across various student tiers. Key Points:
- Conducted psychological assessments and evaluations and collaborated on IEPs.
- Developed behavioral and academic interventions.
- Led MTSS implementation and management.
''')

#------------------------------------------------------------------------
# Scholarship
#------------------------------------------------------------------------
##################### White space for navigation bar
st.markdown('''
<style>
.white-text {
    color: white;
}
</style>

<div class="white-text">

## Scholarship

</div>
''', unsafe_allow_html=True)
#####################

st.markdown('''
## Scholarship
''')

st.markdown('''
#### Research Publications
''')

txt4('2023', 'Bohanon, H., **LeVesseur, C.**, Harms, A., & Meng-Jia, W. (2023). *A Preliminary Study Connecting School Improvement and MTSS with Student Outcomes.* Australasian Journal of Special and Inclusive Education.', 'https://www.cambridge.org/core/journals/australasian-journal-of-special-and-inclusive-education/article/preliminary-study-connecting-school-improvement-and-mtss-with-student-outcomes/44D3798F6A68AD7F1005AFDCADADA2DC#')
txt4('2022', 'Morrison, J. Q., **LeVesseur, C. A.**, Harms, A. L., & Zhang, J. (2022). *Statewide recognition system for promoting implementation fidelity of multi-tiered system of supports.* Research and Practice in the Schools, 9(1), 63-78.', 'https://www.txasp.org/assets/docs/tasp-journal/Vol_9_Issue_1_Complete%20Issue.pdf')
txt4('2022', "**LeVesseur, C.**, Morrison, J., Melissa N. (2022). *Educators' Preferences for Professional Learning Formats by Learning Objective.* Journal of Education and Training Studies.",'https://redfame.com/journal/index.php/jets/article/view/5495')
txt4('2021', 'Bohanon, H., Wu, H., Kushki, A., **LeVesseur, C.**, Harms, A., Vera, E., Carlson-Sanei, J., & Shriberg, D. (2021). *The Role of School Improvement Planning in the Implementation of MTSS in Secondary Schools.* Preventing School Failure.', 'https://eric.ed.gov/?id=EJ1295725')
txt4('2021', '[**LeVesseur, C.**] MiMTSS Technical Assistance Center (2021). *Michigan Evaluation Brief: How are Schools Using the School-wide Reading/PBIS Fidelity Inventory/District Capacity Assessment?* Michigan Department of Education.','https://mimtsstac.org/evaluation-research/results/evaluation-briefs')
txt4('2015', 'Russell, C., Ward, c., Harms, A., St. Martin, K., Cusumano, D., Fixsen, D., Levy, R., & **LeVesseur, C.** (2015). *District Capacity Assessment Technical Manual.* National Implementation Research Network, University of North Carolina at Chapel Hill.', 'https://files.eric.ed.gov/fulltext/ED606132.pdf')
txt4('2015', '**LeVesseur, C.**, (2015) *Implementing Universal Social and Emotional Learning Programs: The Development, Validation, and Inferential Findings from the Schoolwide SEL Capacity Assessment.* Doctoral Dissertations', 'https://scholarworks.umass.edu/cgi/viewcontent.cgi?article=1459&context=dissertations_2')
txt4('2013', 'Whitcomb, S.A., & **LeVesseur, C.** (2012). *Promoting student strengths and assets.* In. S.E. Brock, P.J. Lazarus, & S.R. Jimerson (Eds.), Best practices in crisis prevention and intervention (2nd edition), (pp. 97-114). Bethesda, MD: National Association of School Psychologists.', 'https://www.nasponline.org/books-and-products/products/books/titles/best-practices-in-school-crisis-prevention-and-intervention')

#------------------------------------------------------------------------
# Skills
#------------------------------------------------------------------------
##################### White space for navigation bar
st.markdown('''
<style>
.white-text {
    color: white;
}
</style>

<div class="white-text">

## Skills

</div>
''', unsafe_allow_html=True)
#####################

st.markdown('''
## Skills
''')
txt3('Programming', '`Python`, `SAS`')
txt3('Data processing/wrangling', '`pandas`, `numpy`')
txt3('Data visualization', '`matplotlib`, `seaborn`, `plotly`, `folium`')
txt3('Artificial Intelligence (AI)', '`Langchain`, `AI APIs`')
# txt3('Machine Learning', '`scikit-learn`')
# txt3('Deep Learning', '`TensorFlow`')
txt3('Web development', '`HTML`')
txt3('Model deployment', '`streamlit`, `Heroku`, `Hugging Face`')

#------------------------------------------------------------------------
# Connect
#------------------------------------------------------------------------
##################### White space for navigation bar
st.markdown('''
<style>
.white-text {
    color: white;
}
</style>

<div class="white-text">

## Connect

</div>
''', unsafe_allow_html=True)
#####################

st.markdown('''
## Connect
''')

# Start with your email (2nd line of code), a reply will provide a random-like string to replace so your email is not visible <form target="_blank" action="https://formsubmit.co/your@email.com" method="POST">
st.markdown("""
<div class="container">

  <form target="_blank" action="https://formsubmit.co/561dfd935804a0a7c24778d592d02ded" method="POST">
    <div class="form-group">
      <div class="form-row">
        <div class="col">
          <input type="text" name="name" class="form-control" placeholder="Full Name" required>
        </div>
        <div class="col">
          <input type="email" name="email" class="form-control" placeholder="Email Address" required>
        </div>
      </div>
    </div>
    <div class="form-group">
      <textarea placeholder="Your Message" class="form-control" name="message" rows="10" required></textarea>
    </div>
    <button type="submit" class="btn btn-lg btn-dark btn-block">Submit Form</button>
  </form>
</div>
""", unsafe_allow_html=True)

txt2(" ", " ")
txt2('LinkedIn', 'https://www.linkedin.com/in/levesseur/')
txt2('GitHub', 'https://github.com/ProfessorLeVesseur/')
txt2('Hugging Face', 'https://huggingface.co/')
txt2('ORCID', 'https://orcid.org/0009-0007-9274-0426')
txt2('ResearchGate', 'https://www.researchgate.net/profile/Cheyne-Levesseur')
