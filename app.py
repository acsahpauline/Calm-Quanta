import streamlit as st
from PIL import Image
import base64

import base64

def set_bg_from_local(image_file):
    with open(image_file, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Set page config at the top
# Header
st.markdown('''
    <div class="header">CALMQUANTA - WHERE CALM MEETS CLARITY</div>
    <hr style="border: 1px solid white; width: 100%;">
''', unsafe_allow_html=True)

set_bg_from_local("backgrounds/serene_forest.jpg")

# Load feature icons
mood_image = Image.open("icons/mood.png")
bar_chart_image = Image.open("icons/bar_chart.png")
calendar_image = Image.open("icons/calendar.png")
line_chart_image = Image.open("icons/line_chart.png")
journal_image = Image.open("icons/journal.png")
breath_image = Image.open("icons/breath.png")
sound_image = Image.open("icons/sound.png")
forest_image = Image.open("icons/forest.png")
quotes_image = Image.open("icons/quotes.png")
ai_image = Image.open("icons/ai.png")
stats_image = Image.open("icons/stats.png")
report_image = Image.open("icons/report.png")
meditation_image = Image.open("icons/meditation.png")
target_image = Image.open("icons/target.png")

# Inject custom CSS
st.markdown("""
    <style>
    body {
        background-color: black;
        color: white;
        font-family: 'Times New Roman', Times, serif;
    }
    .header {
        text-align: center;
        font-size: 48px;
        font-weight: bold;
        margin-top: 20px;
        color: white;
    }
    .subtext {
        font-style: italic;
        font-size: 18px;
        margin: 40px 100px;
        text-align: justify;
    }
    .feature-grid {
        display: flex;
        flex-wrap: wrap;
        justify-content: space-around;
        margin: 50px 30px;
    }
    .feature-block {
        width: 250px;
        text-align: center;
        margin: 20px;
        cursor: pointer;
    }
    .feature-block img {
        width: 80px;
        height: 80px;
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Subtext
st.markdown("""
<div class="subtext">
An AI-inspired mental health tracker uses advanced algorithms and machine learning models to monitor and assess an individual's emotional well-being over time.
By analyzing data from mood logs, activity patterns, sleep patterns, and even speech or text inputs, it can offer personalized insights, track changes in mental health,
and detect early signs of stress, anxiety, or depression. This proactive approach helps individuals better understand their emotional states, identify potential triggers,
and implement strategies for improving their mental health.
</div>
""", unsafe_allow_html=True)

# Feature selector
selected_feature = st.radio(
    "🧠 Choose a feature to explore:",
    (
        "Select Current Mood", "Mood Frequency Bar Chart", "Mood Calendar View", "Mood Trend Line Chart",
        "Mindful Journaling", "Breathing Exercise", "Ambient Sounds", "VR Forest Mode",
        "Daily Quotes", "AI Suggestions", "Emotion Analytics", "Weekly Mood Report",
        "Guided Meditation Sessions", "Daily Intention Setting"
    ),
    horizontal=True
)

# Display feature image based on selection
if selected_feature == "Select Current Mood":
    st.image(mood_image, width=100)
    st.header("Select Your Current Mood")
    mood = st.selectbox("How are you feeling?", ["Happy", "Sad", "Angry", "Anxious", "Calm", "Stressed"])

elif selected_feature == "Mood Frequency Bar Chart":
    st.image(bar_chart_image, width=100)
    st.header("Mood Frequency Bar Chart")
    st.bar_chart([10, 15, 7, 3, 12, 8])  # Replace with real data

elif selected_feature == "Mood Calendar View":
    st.image(calendar_image, width=100)
    st.header("Mood Calendar View")
    st.write("Calendar view coming soon!")

elif selected_feature == "Mood Trend Line Chart":
    st.image(line_chart_image, width=100)
    st.header("Mood Trend Line Chart")
    st.line_chart([10, 12, 9, 7, 11, 13, 8])  # Sample data

elif selected_feature == "Mindful Journaling":
    st.image(journal_image, width=100)
    st.header("Mindful Journaling")
    st.text_area("📝 Start writing your thoughts here...")

elif selected_feature == "Breathing Exercise":
    st.image(breath_image, width=100)
    st.header("Breathing Exercise")
    st.write("Try box breathing: Inhale (4s), Hold (4s), Exhale (4s), Hold (4s).")

elif selected_feature == "Ambient Sounds":
    sound_files = [
        "birds.mp3",
        "forest_birds.mp3",
        "gentle_rain.mp3",
        "ocean_waves.mp3",
        "tree.mp3",
        "water.mp3",
        "wind.mp3"
        ]
    # Path to the ambient sounds folder
    sound_folder = "ambient_sounds/"

    # Header and instructions
    st.header("Ambient Sounds")
    st.write("Choose a soothing sound to relax and play:")

    # Create a dropdown (selectbox) for sound selection
    sound_choice = st.selectbox("Select Sound:", sound_files)

    # Construct the file path based on user choice
    audio_path = sound_folder + sound_choice

    # Display the selected sound
    st.audio(audio_path)
    
elif selected_feature == "VR Forest Mode":
    st.image(forest_image, width=100)
    st.header("VR Forest Mode")
    st.write("Immerse yourself in nature. (VR simulation coming soon!)")

elif selected_feature == "Daily Quotes":
    st.image(quotes_image, width=100)
    st.header("Daily Quotes")
    st.success("“You don’t have to control your thoughts. You just have to stop letting them control you.” — Dan Millman")

elif selected_feature == "AI Suggestions":
    st.image(ai_image, width=100)
    st.header("AI Suggestions")
    st.write("Based on your mood, we suggest a 10-minute meditation today.")

elif selected_feature == "Emotion Analytics":
    st.image(stats_image, width=100)
    st.header("Emotion Analytics")
    st.write("See emotional patterns and behavior insights.")

elif selected_feature == "Weekly Mood Report":
    st.image(report_image, width=100)
    st.header("Weekly Mood Report")
    st.write("📊 Your average mood this week: Calm\nMost common mood: Happy")

elif selected_feature == "Guided Meditation Sessions":
    st.image(meditation_image, width=100)
    st.header("Guided Meditation Sessions")
    st.video("https://www.youtube.com/watch?v=inpok4MKVLM")  # Replace with real content

elif selected_feature == "Daily Intention Setting":
    st.image(target_image, width=100)
    st.header("Daily Intention Setting")
    intention = st.text_input("🌟 Set your intention for today:")
    if intention:
        st.success(f"Your intention for today is: **{intention}**")

# Theme toggle
st.sidebar.title("🌓 Theme Toggle")
theme = st.sidebar.radio("Choose mode", ["Dark", "Bright"])
st.sidebar.info(f"Current mode: {theme}")