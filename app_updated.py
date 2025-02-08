import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 🔹 Initialize DataFrame (with session state to persist changes)
if "df" not in st.session_state:
    data = {
        'Employee': ['John Doe', 'Jane Smith', 'Ali Khan', 'Sarah Lee'],
        'Role': ['Developer', 'Artist', 'UI Designer', 'Support Staff'],
        'Technical Mastery': [8, 7, 9, 6],
        'Innovation & Impact': [7, 8, 6, 7],
        'Leadership & Mentorship': [6, 7, 8, 5],
        'Collaboration & Culture': [9, 8, 7, 9],
        'Performance Score': [80, 85, 78, 75]
    }
    df = pd.DataFrame(data)

    # 🔹 Fix data types (prevents Arrow errors)
    df = df.astype({
        'Employee': 'string',
        'Role': 'string',
        'Technical Mastery': 'int32',
        'Innovation & Impact': 'int32',
        'Leadership & Mentorship': 'int32',
        'Collaboration & Culture': 'int32',
        'Performance Score': 'int32'
    })

    st.session_state.df = df  # Store DataFrame in session state

# 🔹 Load DataFrame from session state
df = st.session_state.df  

# Streamlit UI
st.title("Game District Meritocracy Dashboard")
st.write("Tracking employee performance, growth, and cultural impact.")

# Show Data
st.dataframe(df)

# 🔹 Performance Visualization (Updates in Real-Time)
st.subheader("Performance Breakdown")
fig, ax = plt.subplots(figsize=(8, 5))
df.set_index("Employee")[['Technical Mastery', 'Innovation & Impact', 'Leadership & Mentorship', 'Collaboration & Culture']].plot(kind='bar', ax=ax)
plt.xticks(rotation=45)
st.pyplot(fig)

# 🔹 Employee Detail View (Updates in Real-Time)
st.subheader("Employee Performance Review")
selected_employee = st.selectbox("Select an Employee", df['Employee'])
emp_data = df[df['Employee'] == selected_employee].T
st.write(emp_data)

# 🔹 Update Employee Performance
st.subheader("Update Employee Performance")
emp_name = st.selectbox("Select Employee to Update", df['Employee'], key="update_emp")
metric = st.selectbox("Metric", ['Technical Mastery', 'Innovation & Impact', 'Leadership & Mentorship', 'Collaboration & Culture'])
new_value = st.slider("New Score (0-10)", 0, 10, 5)

# 🔹 Button to update the score and refresh session state
if st.button("Update Score"):
    st.session_state.df.loc[df['Employee'] == emp_name, metric] = new_value
    st.success(f"Updated {metric} for {emp_name} to {new_value}")
    st.rerun()  # 🔄 Refresh the app to reflect changes immediately
