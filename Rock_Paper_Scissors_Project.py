#Project:  [Rock, Paper, Scissors]
# from ctypes import windll

#Rule:
     #Rock wins against Scissors
     #Scissors win against Paper
     #Paper win against Rock


#cases:
   #0-Rock:
           # Rock - Rock = tie
           # Rock - Paper = paper wine
           # rock - scissors = rock wine


   # 1- Paper:
         # paper - paper = tie
         # paper - rock = paper wine
         #paper - scissors = scissors win

  # 2- Scissors:
        # scissors - scissors = tie
        # scissors - rock = rock wine
        # scissors - paper = scissor win





# Rock_Paper_Scissors_
import streamlit as st
import random

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Rock Paper Scissors 🎮",
    page_icon="🪨📄✂️",
    layout="centered"
)

# --- CUSTOM CSS FOR COLORFUL DASHBOARD ---
st.markdown(
    """
    <style>
    /* Background gradient */
    .stApp {
        background:  linear-gradient(135deg, #FFB6C1, #87CEFA); 
    }

    /* Center title */
    h1 {
        text-align: center;
        color: #6a0dad;
        font-size: 50px;
    }

    h4 {
        text-align: center;
        color: #1E90FF;
    }

    /* Scoreboard boxes */
    .scorebox {
        background: #FFD700;
        padding: 15px;
        border-radius: 15px;
        text-align: center;
        font-size: 25px;
        font-weight: bold;
        color: #000000;
    }

    /* Buttons */
    div.stButton > button:first-child {
        background-color: #FF69B4;
        color: white;
        height: 50px;
        width: 200px;
        border-radius: 10px;
        font-size: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- SESSION STATE FOR SCORES ---
if "user_score" not in st.session_state:
    st.session_state.user_score = 0
if "computer_score" not in st.session_state:
    st.session_state.computer_score = 0
if "ties" not in st.session_state:
    st.session_state.ties = 0

# --- TITLE ---
st.markdown("<h1>🎮 Rock · Paper · Scissors</h1>", unsafe_allow_html=True)
st.markdown("<h4>🪨 Rock beats ✂️ · ✂️ Scissors beats 📄 · 📄 Paper beats 🪨</h4>", unsafe_allow_html=True)
st.write("---")

# --- GAME OPTIONS ---
choices = ["🪨 Rock", "📄 Paper", "✂️ Scissors"]

# --- SCOREBOARD ---
st.markdown("### 📊 Scoreboard")
col1, col2, col3 = st.columns(3)
col1.markdown(f"<div class='scorebox'>🧍 You<br>{st.session_state.user_score}</div>", unsafe_allow_html=True)
col2.markdown(f"<div class='scorebox'>💻 Computer<br>{st.session_state.computer_score}</div>", unsafe_allow_html=True)
col3.markdown(f"<div class='scorebox'>🤝 Ties<br>{st.session_state.ties}</div>", unsafe_allow_html=True)
st.write("---")

# --- USER SELECTION ---
user_choice = st.radio("👉 Choose your move:", choices, horizontal=True)

# --- PLAY BUTTON ---
if st.button("🎯 Play Now"):
    user_index = choices.index(user_choice)
    computer_index = random.randint(0, 2)
    computer_choice = choices[computer_index]

    st.markdown(f"### 🧍 You chose: {user_choice}")
    st.markdown(f"### 💻 Computer chose: {computer_choice}")

    # --- RESULT LOGIC ---
    if user_index == computer_index:
        st.info("🤝 It's a Tie!")
        st.session_state.ties += 1
    elif (user_index == 0 and computer_index == 2) or \
         (user_index == 1 and computer_index == 0) or \
         (user_index == 2 and computer_index == 1):
        st.success("🎉 You Win!")
        st.session_state.user_score += 1
        st.balloons()
    else:
        st.error("😞 You Lose...")
        st.session_state.computer_score += 1

# --- RESET BUTTON ---
if st.button("🔄 Reset Score"):
    st.session_state.user_score = 0
    st.session_state.computer_score = 0
    st.session_state.ties = 0
    st.success("✅ Scores have been reset!")

# --- FOOTER ---
st.markdown("---")
st.markdown(
    "<p style='text-align:center; color:gray;'>Built by Indra Jaiswal<b>❤️</b></p>",
    unsafe_allow_html=True,
)










