import streamlit as st
import requests

# ---------------- CONFIGURATION ----------------

API_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="AI Career Guidance System",
    page_icon="🎓"
)

# ---------------- SIDEBAR ----------------

st.sidebar.title("Menu")
menu = ["Login", "Register", "Assessment"]
choice = st.sidebar.selectbox("Select Option", menu)

# ---------------- HOME ----------------

st.title("🎓 AI Career Guidance System")
st.write("Welcome to the AI Career Guidance System!")
st.write("This website helps students choose the right career.")

# =====================================================
# REGISTER
# =====================================================

if choice == "Register":

    st.header("Register")

    name = st.text_input("Name")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Register"):

        data = {
            "name": name,
            "email": email,
            "password": password
        }

        try:
            response = requests.post(
                f"{API_URL}/register",
                json=data
            )

            if response.status_code == 200:
                st.success(response.json()["message"])
            else:
                st.error("Registration Failed")

        except Exception as e:
            st.error(f"Cannot connect to FastAPI Server\n{e}")

# =====================================================
# LOGIN
# =====================================================

elif choice == "Login":

    st.header("Login")

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):

        data = {
            "email": email,
            "password": password
        }

        try:
            response = requests.post(
                f"{API_URL}/login",
                json=data
            )

            if response.status_code == 200:

                result = response.json()

                if result["message"] == "Login Successful":
                    st.success("Login Successful")
                else:
                    st.error(result["message"])

            else:
                st.error("Login Failed")

        except Exception as e:
            st.error(f"Cannot connect to FastAPI Server\n{e}")

# =====================================================
# ASSESSMENT
# =====================================================

elif choice == "Assessment":

    st.header("Career Assessment")

    # ---------------- Student Details ----------------

    name = st.text_input("Enter your Name")

    age = st.number_input(
        "Enter your Age",
        min_value=16,
        max_value=60
    )

    degree = st.selectbox(
        "Select your Degree",
        [
            "B.Tech",
            "B.Sc",
            "B.Com",
            "BCA",
            "M.Tech",
            "MBA",
            "Other"
        ]
    )

    year = st.selectbox(
        "Select your Year",
        [
            "1st Year",
            "2nd Year",
            "3rd Year",
            "4th Year"
        ]
    )

    # ---------------- Skills ----------------

    st.subheader("Select Your Skills")

    python_skill = st.checkbox("Python")
    sql = st.checkbox("SQL")
    excel = st.checkbox("Excel")
    powerbi = st.checkbox("Power BI")
    html = st.checkbox("HTML")
    css = st.checkbox("CSS")
    javascript = st.checkbox("JavaScript")

    # ---------------- Interests ----------------

    st.subheader("Select Your Interests")

    interests = st.multiselect(
        "Choose your Interests",
        [
            "AI",
            "Data Analysis",
            "Web Development",
            "Cyber Security",
            "Machine Learning",
            "UI/UX Design"
        ]
    )

    # ---------------- Questions ----------------

    st.subheader("Career Questions")

    answers = []

    try:

        response = requests.get(f"{API_URL}/questions")

        if response.status_code == 200:

            questions = response.json()

            for q in questions:

                score = st.radio(
                    q["question"],
                    [1, 2, 3, 4, 5],
                    horizontal=True,
                    key=q["id"]
                )

                answers.append(score)

        else:
            st.error("Unable to load questions.")

    except Exception as e:
        st.error(f"Cannot connect to FastAPI Server\n{e}")

    # ---------------- Submit Assessment ----------------

    if st.button("Submit Assessment"):

        try:

            # Recommendation API
            response = requests.post(
                f"{API_URL}/recommend",
                json={"answers": answers}
            )

            if response.status_code == 200:

                result = response.json()

                st.success("Assessment Completed!")

                # Student Details
                st.write("## Student Information")
                st.write("**Name:**", name)
                st.write("**Age:**", age)
                st.write("**Degree:**", degree)
                st.write("**Year:**", year)

                # Skills
                st.write("## Skills")

                if python_skill:
                    st.write("✅ Python")

                if sql:
                    st.write("✅ SQL")

                if excel:
                    st.write("✅ Excel")

                if powerbi:
                    st.write("✅ Power BI")

                if html:
                    st.write("✅ HTML")

                if css:
                    st.write("✅ CSS")

                if javascript:
                    st.write("✅ JavaScript")

                # Interests
                st.write("## Interests")

                if interests:
                    for item in interests:
                        st.write("✅", item)
                else:
                    st.write("No interests selected.")

                # Scores
                st.write("## Question Scores")
                st.write(answers)

                # Recommendation
                st.write("## Total Score")
                st.success(result["total_score"])

                st.write("## Recommended Career")
                st.success(result["recommended_career"])

                # Save Assessment
                save_data = {
                    "name": name,
                    "age": age,
                    "degree": degree,
                    "year": year,
                    "total_score": result["total_score"],
                    "recommended_career": result["recommended_career"]
                }

                save_response = requests.post(
                    f"{API_URL}/save-assessment",
                    json=save_data
                )

                if save_response.status_code == 200:
                    st.success("Assessment Saved Successfully!")
                else:
                    st.error("Failed to Save Assessment")

                st.balloons()

            else:
                st.error("Recommendation Failed")

        except Exception as e:
            st.error(f"Cannot connect to FastAPI Server\n{e}")