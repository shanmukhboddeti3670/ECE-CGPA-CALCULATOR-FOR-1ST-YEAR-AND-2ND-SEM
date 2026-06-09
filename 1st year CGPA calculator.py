import streamlit as st

# 1. This is your exact "nume" function logic!
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
    return grade_point * credits

# 2. Web Page Title
st.set_page_config(page_title="ECE CGPA Calculator", page_icon="🎓")
st.title("🎓 WELCOME TO CGPA CALCULATOR FOR ECE SEM-2 AND 1ST YEAR")
st.write("Enter your marks for each subject below.")
st.markdown("---")

# 3. Creating input boxes for your exact subjects
st.subheader("📚 Enter Your Semester 2 Marks (Out of 100)")

# We replace your input() lines with Streamlit number boxes
eng = st.number_input("TECHNICAL ENGLISH MARKS", min_value=0, max_value=100, value=80)
math = st.number_input("ADVANCED CALCULUS AND STATISTICS MARKS", min_value=0, max_value=100, value=80)
chem = st.number_input("CHEMISTRY MARKS", min_value=0, max_value=100, value=80)
ct = st.number_input("ELECTRICAL CIRCUIT AND NETWORK ANALYSIS MARKS", min_value=0, max_value=100, value=80)
pp = st.number_input("PYTHON PROGRAMMING MARKS", min_value=0, max_value=100, value=80)
dlc = st.number_input("DIGITAL LOGIC CIRCUITS MARKS", min_value=0, max_value=100, value=80)
chem_lab = st.number_input("CHEMISTRY LABORATORY MARKS", min_value=0, max_value=100, value=80)

st.markdown("---")
st.subheader("📈 Past Performance")
# We replace your sem_1_CGPA input line with a decimal input box
sem_1_CGPA = st.number_input("ENTER YOUR SEM-1 CGPA", min_value=0.0, max_value=10.0, value=8.0, step=0.01)

st.markdown("---")

# 4. The Clickable Calculation Button
if st.button("Calculate My CGPA", type="primary"):
    
    # Running your exact calculations behind the scenes using your credits
    num1 = calculate_points(eng, 3)
    num2 = calculate_points(math, 3)
    num3 = calculate_points(chem, 3)
    num4 = calculate_points(ct, 3)
    num5 = calculate_points(pp, 3)
    num6 = calculate_points(dlc, 4)
    num7 = calculate_points(chem_lab*2, 1)
    
    # Your exact formula for Semester 2
    sem_2 = (num1 + num2 + num3 + num4 + num5 + num6 + num7) / 17
    sem_2_CGPA = round(sem_2, 2)
    
    # Your exact formula for First Year Cumulative
    first_year_CGPA = round(((sem_1_CGPA * 19) + (sem_2_CGPA * 17)) / 36, 2)
    
    # 5. Showing your print statements as beautiful web alerts
    st.balloons() # Decorative celebration effect
    st.success(f"### YOUR SECOND SEM CGPA IS: **{sem_2_CGPA}**")
    st.success(f"### YOUR 1ST YEAR CGPA IS: **{first_year_CGPA}**")
    #st.caption("⚠️ **Disclaimer:** This tool is for quick estimation of CGPA and also the FIRST-YEAR CGPA is calculated considering that  \" You had been passed in  all subjects in sem-1 and sem-2 \" if not the first year cgpa may be vary  ")
    st.caption("⚠️ **Disclaimer:** This tool is for quick CGPA estimation. Please note that the 1st-Year CGPA calculation assumes you have **passed all subjects** in both Semester 1 and Semester 2. If you have any active backlogs, your actual final CGPA will vary.")
