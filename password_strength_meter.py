import streamlit as st

# Page configuration
st.set_page_config(page_title="Password Strength Meter", page_icon="🔒", layout="centered")

# Custom CSS for styling
st.markdown(
    """
    <style>
    .stTextInput>div>div>input {
        font-size: 18px;
        padding: 10px;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-size: 16px;
        padding: 10px 24px;
        border-radius: 8px;
        border: none;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .stMarkdown h2 {
        color: #4CAF50;
    }
    .strength-weak {
        color: red;
        font-size: 20px;
    }
    .strength-medium {
        color: orange;
        font-size: 20px;
    }
    .strength-strong {
        color: green;
        font-size: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Title and description
st.title("🔒 Password Strength Meter")
st.write("Check how strong your password is!")

# Function to check password strength
def check_password_strength(password):
    strength = 0
    feedback = []

    # Check length
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Check for uppercase letters
    if any(char.isupper() for char in password):
        strength += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    # Check for lowercase letters
    if any(char.islower() for char in password):
        strength += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    # Check for numbers
    if any(char.isdigit() for char in password):
        strength += 1
    else:
        feedback.append("Add at least one number.")

    # Check for special characters
    if any(not char.isalnum() for char in password):
        strength += 1
    else:
        feedback.append("Add at least one special character.")

    # Determine strength level
    if strength == 5:
        return "Strong 💪", "strength-strong", feedback
    elif strength >= 3:
        return "Medium 😐", "strength-medium", feedback
    else:
        return "Weak 😟", "strength-weak", feedback

# Password input
password = st.text_input("Enter your password:", type="password")

# Check password strength
if st.button("Check Strength"):
    if password:
        strength_level, strength_class, feedback = check_password_strength(password)
        st.markdown(f"<p class='{strength_class}'>Password Strength: {strength_level}</p>", unsafe_allow_html=True)
        
        if feedback:
            st.write("Suggestions to improve your password:")
            for suggestion in feedback:
                st.write(f"- {suggestion}")
    else:
        st.error("Please enter a password to check its strength.")

# Footer
st.markdown("---")
st.write("Created with ❤️ by **Naseem Ahmed Detho**")