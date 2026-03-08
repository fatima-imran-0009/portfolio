import streamlit as st
from PIL import Image

st.set_page_config(page_title="Portfolio - Fatima Imran", layout="wide")

with st.sidebar:
    try:
        profile_image = Image.open(r"C:\Users\desktop\Downloads\WhatsApp Image 2025-01-21 at 8.41.59 AM (1).jpeg")
        st.image(profile_image, width=150)
        st.markdown("<h3 style='font-weight: bold;'>FATIMA IMRAN</h3>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.error("Profile image not found. Please check the path.")

    selected_section = st.radio(
        "Go to", 
        ["Home", "About Me", "Projects", "Skills", "Contact"],
        index=0
    )

if selected_section == "Home":
    st.title("Welcome to Fatima's Portfolio")
    st.write("I’m Fatima Imran, a Data Science student at the University of Central Punjab. Currently in my 5th semester, I am passionate about learning how data can solve real-world problems. I’m constantly exploring new ways to apply data science in areas like business and technology to make a meaningful impact.")

elif selected_section == "About Me":
    st.title("About Me")
    st.write("I’m a proactive learner with an interest in data analytics and visualization. My focus is to build practical skills that contribute to solving complex problems in business and technology.")
    st.write("### Education")
    st.write("• Ongoing BS Data Science, University of Central Punjab Lahore (2022) ")
    st.write("• Intermediate, Samanabad College For Women (2020)")
    st.write("• Matriculation, The Educators")
    st.write("### Experience")
    st.write("• University Project: Worked on a project where we developed a Student Grade Management System, focusing on database management, system design, and user interface.")
    st.write("### Skills")
    st.write("• Problem solving, Time management, OOP")
    st.write("• C++, SQL, Adaptability, DSA, Teamwork")
    st.write("• HTML, Excel")

elif selected_section == "Projects":
    st.title("My Projects")
    st.subheader("Project 1: Tic Tac Toe Game")
    tic_tac_toe_image = Image.open(r"C:\Users\desktop\Desktop\tic tac toe.png")
    st.image(tic_tac_toe_image, width=200)
    st.write("Description: A simple implementation of the classic Tic Tac Toe game using C++.")
    st.write("Technologies used: C++")
    st.write("[Source Code Link](https://github.com/demo-profile/tic-tac-toe)")
    
    st.subheader("Project 2: Guess My Number Game")
    guess_my_number_image = Image.open(r"C:\Users\desktop\Desktop\New folder\Guess My Number.jpg")
    st.image(guess_my_number_image, width=200)
    st.write("Description: A number guessing game in C where the user has to guess a randomly generated number.")
    st.write("Technologies used: C")
    st.write("[Source Code Link](https://github.com/demo-profile/guess-my-number)")

    st.subheader("Project 3: Student Grade Management System")
    student_grade_image = Image.open(r"C:\Users\desktop\Desktop\New folder\student grade.png")
    st.image(student_grade_image, width=200)
    st.write("Description: A simple C++ project to manage and display student grades with options to add, remove, and display data.")
    st.write("Technologies used: C++")
    st.write("[Source Code Link](https://github.com/demo-profile/student-grade-management)")

elif selected_section == "Skills":
    st.title("Skills")
    st.write("### Technical Skills")
    st.progress(85)
    st.write("• Python: 85%")
    st.progress(75)
    st.write("• Data Analysis: 75%")
    st.progress(80)
    st.write("• Web Development: 80%")
    st.progress(70)
    st.write("• Machine Learning: 70%")
    
elif selected_section == "Contact":
    st.title("Contact Me")
    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")
        submitted = st.form_submit_button("Send Message")
        if submitted:
            st.success("Your message has been successfully sent!")
    
    st.write("### Or reach me through my professional profiles:")
    st.markdown("[LinkedIn](https://www.linkedin.com/in/demo-profile) | [GitHub](https://github.com/demo-profile)")
