import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="ClassPulse",
    page_icon="📊",
    layout="wide"
)

# -----------------------------
# Student Data
# -----------------------------
if "students" not in st.session_state:
    st.session_state.students = [
        {"Roll No": 101, "Name": "Rahul", "Marks": 85, "Attendance": 92},
        {"Roll No": 102, "Name": "Priya", "Marks": 78, "Attendance": 88},
        {"Roll No": 103, "Name": "Aman", "Marks": 91, "Attendance": 95},
        {"Roll No": 104, "Name": "Neha", "Marks": 67, "Attendance": 75},
        {"Roll No": 105, "Name": "Rohit", "Marks": 54, "Attendance": 68},
    ]


def get_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"


def get_dataframe():
    df = pd.DataFrame(st.session_state.students)
    df["Grade"] = df["Marks"].apply(get_grade)
    return df


# -----------------------------
# Header
# -----------------------------
st.title("📊 ClassPulse")
st.subheader("Student Performance Analytics System")

st.write(
    "A Python-based system to manage student marks, attendance "
    "and academic performance."
)

# -----------------------------
# Dashboard
# -----------------------------
df = get_dataframe()

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("👨‍🎓 Total Students", len(df))

with col2:
    st.metric("📈 Average Marks", f"{df['Marks'].mean():.2f}")

with col3:
    st.metric("📝 Average Attendance", f"{df['Attendance'].mean():.2f}%")

with col4:
    st.metric("🏆 Highest Marks", df["Marks"].max())

st.divider()

# -----------------------------
# Navigation
# -----------------------------
menu = st.sidebar.selectbox(
    "📌 Select Option",
    [
        "Dashboard",
        "All Students",
        "Top Students",
        "Search Student",
        "Low Attendance",
        "Add Student"
    ]
)

# -----------------------------
# Dashboard
# -----------------------------
if menu == "Dashboard":

    st.header("📊 Performance Dashboard")

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

    st.subheader("📈 Marks Overview")

    chart_data = df[["Name", "Marks"]].set_index("Name")
    st.bar_chart(chart_data)


# -----------------------------
# All Students
# -----------------------------
elif menu == "All Students":

    st.header("👨‍🎓 All Students")

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )


# -----------------------------
# Top Students
# -----------------------------
elif menu == "Top Students":

    st.header("🏆 Top 5 Students")

    top = df.sort_values(
        by="Marks",
        ascending=False
    ).head(5)

    st.dataframe(
        top,
        use_container_width=True,
        hide_index=True
    )


# -----------------------------
# Search Student
# -----------------------------
elif menu == "Search Student":

    st.header("🔍 Search Student")

    search = st.text_input(
        "Enter student name"
    )

    if search:
        result = df[
            df["Name"].str.contains(
                search,
                case=False,
                na=False
            )
        ]

        if len(result) > 0:
            st.dataframe(
                result,
                use_container_width=True,
                hide_index=True
            )
        else:
            st.warning("Student not found.")


# -----------------------------
# Low Attendance
# -----------------------------
elif menu == "Low Attendance":

    st.header("⚠️ Low Attendance Students")

    limit = st.slider(
        "Attendance limit",
        min_value=50,
        max_value=90,
        value=75
    )

    low = df[df["Attendance"] < limit]

    if len(low) > 0:
        st.dataframe(
            low,
            use_container_width=True,
            hide_index=True
        )
    else:
        st.success("No students have low attendance.")


# -----------------------------
# Add Student
# -----------------------------
elif menu == "Add Student":

    st.header("➕ Add New Student")

    with st.form("student_form"):

        roll = st.number_input(
            "Roll Number",
            min_value=1,
            step=1
        )

        name = st.text_input(
            "Student Name"
        )

        marks = st.number_input(
            "Marks",
            min_value=0,
            max_value=100,
            step=1
        )

        attendance = st.number_input(
            "Attendance (%)",
            min_value=0,
            max_value=100,
            step=1
        )

        submitted = st.form_submit_button(
            "Add Student"
        )

        if submitted:

            if name.strip() == "":
                st.error("Please enter student name.")

            else:
                st.session_state.students.append(
                    {
                        "Roll No": roll,
                        "Name": name,
                        "Marks": marks,
                        "Attendance": attendance
                    }
                )

                st.success(
                    f"{name} added successfully! 🎉"
                )

                st.rerun()


st.sidebar.divider()

st.sidebar.info(
    "ClassPulse Project\n\n"
    "Student Performance Analytics System\n\n"
    "Developed using Python & Streamlit"
)
