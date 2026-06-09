import streamlit as st

# grade-point
def calculate_points(marks, credits):
    if marks >= 90 and marks <= 100:
        grade_point = 10
    elif marks >= 80 and marks <= 89:
        grade_point = 9
    elif marks >= 70 and marks <= 79:
        grade_point = 8
    elif marks >= 60 and marks <= 69:
        grade_point = 7
    elif marks >= 50 and marks <= 59:
        grade_point = 6
    else:
        grade_point = 0
    return grade_point*credits

# Streamlit Page Setup (No emojis in title to avoid '??' encoding errors)
st.set_page_config(page_title="ECE CGPA Calculator", page_icon="🎓")
st.title("WELCOME TO CGPA CALCULATOR FOR ECE SEM-2 AND 1ST YEAR")
st.write("Enter your marks for each subject below to calculate your performance.")
st.markdown("---")

st.subheader("Enter Your Semester 2 Marks *(Out of 100)")

# Interactive Number Input Boxes for Sem 2
eng = st.number_input("TECHNICAL ENGLISH MARKS", min_value=0, max_value=100, value=None,step=1)
math = st.number_input("ADVANCED CALCULUS AND STATISTICS MARKS", min_value=0, max_value=100, value=None, step=1)
chem = st.number_input("CHEMISTRY MARKS", min_value=0, max_value=100, value=None, step=1)
ct = st.number_input("ELECTRICAL CIRCUIT AND NETWORK ANALYSIS MARKS", min_value=0, max_value=100, value=None, step=1)
pp = st.number_input("PYTHON PROGRAMMING MARKS", min_value=0, max_value=100, value=None, step=1)
dlc = st.number_input("DIGITAL LOGIC CIRCUITS MARKS", min_value=0, max_value=100, value=None, step=1)
chem_lab = st.number_input("CHEMISTRY LABORATORY MARKS(OUT OF 50)", min_value=0, max_value=50, value=None, step=1)

st.markdown("---")
st.subheader("Past Performance")

# Decimal Number Box for Sem 1 CGPA (Fixed the input bug here)
sem_1_CGPA = st.number_input("ENTER YOUR SEM-1 CGPA", min_value=0.0, max_value=10.0, value=None, step=0.01)

st.markdown("---")

# The Action Button
if st.button("Calculate My CGPA", type="primary"):
    
    # Run calculations using your subject credits
    num1 = calculate_points(eng,3)
    num2 = calculate_points(math,3)
    num3 = calculate_points(chem,3)
    num4 = calculate_points(ct,3)
    num5 = calculate_points(pp,3)
    num6 = calculate_points(dlc,4)
    num7 = calculate_points((chem_lab*2),1)
    
    # Sem 2 total credits = 20
    sem_2 = (num1 + num2 + num3 + num4 + num5 + num6 + num7)/20
    sem_2_CGPA = round(sem_2, 2)
    
    # First Year total credits = 39 (Sem 1: 19 + Sem 2: 20)
    first_year_CGPA = round(((sem_1_CGPA * 19) + (sem_2_CGPA * 20)) / 39, 2)
    
    #Output Results
    st.success(f"### YOUR SECOND SEM CGPA IS: **{sem_2_CGPA}**")
    st.success(f"### YOUR 1ST YEAR CGPA IS: **{first_year_CGPA}**")
   
    st.caption("⚠️ **Disclaimer:** This tool is for quick CGPA estimation. Please note that the 1st-Year CGPA calculation assumes you have **passed all subjects** in both Semester 1 and Semester 2. If you have any active backlogs, your actual final CGPA will vary.")
    st.caption("*May vary")
