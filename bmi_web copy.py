import streamlit as st

# Set page config
st.set_page_config(
    page_title="BMI Calculator",
    page_icon="🧮",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Dark theme via Streamlit config is recommended
st.markdown("<h1 style='text-align: center; color: #00FFAB;'>💪 BMI Calculator</h1>", unsafe_allow_html=True)
st.markdown("---")

with st.form("bmi_form"):
    age = st.text_input("Enter your age")
    weight = st.number_input("Enter your weight (kg)", min_value=1.0, format="%.2f")
    height_cm = st.number_input("Enter your height (cm)", min_value=1.0, format="%.2f")

    submitted = st.form_submit_button("Calculate BMI")
    if submitted:
        height_m = height_cm / 100
        bmi = weight / (height_m ** 2)
        bmi = round(bmi, 2)

        if bmi <= 18:
            msg = "🍽️ **BMI is very low. Eat something healthy!**"
        elif 18 <= bmi < 25:
            msg = "✅ **BMI is normal. Keep it up!**"
        elif 25 <= bmi < 30:
            msg = "⚠️ **BMI is high. Consider regular exercise.**"
        else:
            msg = "🚨 **Obese! Time to hit the gym!**"

        st.markdown("---")
        st.success(f"**Age:** {age}  \n**BMI:** {bmi}  \n{msg}")

if st.button("🔄 Clear"):
    st.experimental_rerun()

