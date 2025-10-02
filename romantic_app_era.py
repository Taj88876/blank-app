import streamlit as st
import random

# Settings
gf_name = "Era"  # <--- put her name
your_name = "Taj"

compliments = [
    f"{gf_name}, you are my sunshine ☀️",
    f"No star shines brighter than you, {gf_name} ✨",
    f"You are my one and only princess 👑",
    f"My heart beats only for you ❤️",
    f"You make my world perfect 🌍💕",
    f"Life feels magical with you in it ✨",
    f"You are my lucky charm 🍀",
    f"I fall for you more every single day 💘",
    f"You make my heart race like crazy 🔥",
    f"I can't stop smiling when I think of you 😊",
    f"You're cuter than all the kittens in the world 🐱💕",
    f"My favorite place is wherever you are 🌍💕",
    f"You're my dream come true 🌙✨",
    f"Even stars envy your sparkle ✨💫",
    f"You're sweeter than chocolate 🍫💕",
    f"You're the melody to my heart's song 🎶❤️",
]

# UI
st.set_page_config(page_title="For Era 💕", page_icon="💖", layout="centered")

# Custom CSS for better mobile experience and romantic styling
st.markdown("""
<style>
    .main {
        padding-top: 2rem;
        background: linear-gradient(135deg, #ffe0e6 0%, #fff0f5 50%, #ffe0e6 100%);
    }
    .stButton > button {
        width: 100%;
        background: linear-gradient(45deg, #ff6b9d, #ff8fab);
        border: none;
        color: white;
        font-size: 1.2rem;
        padding: 0.75rem;
        border-radius: 25px;
        margin: 1rem 0;
        box-shadow: 0 4px 15px rgba(255, 107, 157, 0.3);
    }
    .stButton > button:hover {
        background: linear-gradient(45deg, #ff8fab, #ffa8cc);
        transform: scale(1.05);
        transition: all 0.3s ease;
        box-shadow: 0 6px 20px rgba(255, 107, 157, 0.4);
    }
    .heart-container {
        text-align: center;
        font-size: 1.5rem;
        margin: 2rem 0;
        animation: heartbeat 2s infinite;
    }
    @keyframes heartbeat {
        0% { transform: scale(1); }
        50% { transform: scale(1.1); }
        100% { transform: scale(1); }
    }
    .romantic-bg {
        background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 50%, #fecfef 100%);
        padding: 2rem;
        border-radius: 20px;
        margin: 1rem 0;
        box-shadow: 0 8px 25px rgba(255, 154, 158, 0.2);
    }
    .title {
        text-align: center;
        font-size: 3rem;
        color: #d63384;
        margin-bottom: 1rem;
        text-shadow: 2px 2px 4px rgba(214, 51, 132, 0.3);
    }
    .stTextInput > div > div > input {
        border-radius: 15px;
        border: 2px solid #ff8fab;
        font-size: 1.1rem;
        padding: 0.75rem;
    }
    .floating-hearts {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        z-index: -1;
    }
    .heart {
        position: absolute;
        font-size: 20px;
        color: rgba(255, 182, 193, 0.6);
        animation: float 6s infinite ease-in-out;
    }
    @keyframes float {
        0% { transform: translateY(100vh) rotate(0deg); opacity: 0; }
        10% { opacity: 1; }
        90% { opacity: 1; }
        100% { transform: translateY(-100px) rotate(360deg); opacity: 0; }
    }
</style>
""", unsafe_allow_html=True)

# Add floating hearts background
st.markdown("""
<div class="floating-hearts">
    <div class="heart" style="left: 10%; animation-delay: 0s;">💖</div>
    <div class="heart" style="left: 20%; animation-delay: 1s;">💕</div>
    <div class="heart" style="left: 30%; animation-delay: 2s;">💗</div>
    <div class="heart" style="left: 40%; animation-delay: 3s;">💝</div>
    <div class="heart" style="left: 50%; animation-delay: 4s;">💖</div>
    <div class="heart" style="left: 60%; animation-delay: 5s;">💕</div>
    <div class="heart" style="left: 70%; animation-delay: 0.5s;">💗</div>
    <div class="heart" style="left: 80%; animation-delay: 1.5s;">💝</div>
    <div class="heart" style="left: 90%; animation-delay: 2.5s;">💖</div>
</div>
""", unsafe_allow_html=True)

st.markdown(f'<h1 class="title">For Era 💖</h1>', unsafe_allow_html=True)
st.markdown('<div class="romantic-bg">', unsafe_allow_html=True)
st.write("### Here's something special just for you 🌹")

# Heart art with animation
st.markdown(
    """
    <div class="heart-container">
    <pre style="color:#d63384; font-weight:bold; font-size:1.2rem;">
      **   **  
     **** **** 
     ********* 
      *******  
       *****   
        ***    
         *     
    </pre>
    </div>
    """, unsafe_allow_html=True
)

if st.button("Compliment Me 💕"):
    compliment = random.choice(compliments)
    st.success(compliment)
    # Add some extra visual flair
    st.markdown("### 🌟✨🌟✨🌟✨🌟")
    # Add balloons for extra romance
    st.balloons()

st.markdown("---")

answer = st.text_input("Will you be mine forever? (yes/no)", placeholder="Type 'yes' or 'no'...")

if answer.lower() == "yes":
    st.balloons()
    st.success(f"Yay! 💖 You made me the happiest person alive, Era! 😍🔥")
    st.markdown("### 🎉💕🎉💕🎉💕🎉")
    # Extra celebration
    st.snow()
elif answer.lower() == "no":
    st.warning("I'll keep loving you until you say YES 😉💘")
    st.markdown("### 💔💪💔💪💔")
elif answer and answer.lower() not in ["yes", "no"]:
    st.info("Please type 'yes' or 'no' 😊")

st.markdown('</div>', unsafe_allow_html=True)

# Footer with romantic message
st.markdown("---")
st.markdown(f"<div style='text-align: center; color: #d63384; font-size: 1.1rem;'>Made with ❤️ by Taj for his beautiful Era</div>", unsafe_allow_html=True)
st.markdown("<div style='text-align: center; color: #999; margin-top: 1rem;'>Every day with you is a blessing 🌹</div>", unsafe_allow_html=True)