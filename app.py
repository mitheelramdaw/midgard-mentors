import streamlit as st

# Function to display YouTube video
def display_video(video_url):
    st.video(video_url)

# Function to display downloadable PDF
def display_pdf(file_path, label):
    with open(file_path, "rb") as file:
        btn = st.download_button(label=label, data=file, file_name=file_path, mime="application/pdf")

# Home Page
def home():
    st.title("Learn Programming Languages")
    languages = ["Python", "JavaScript", "Java", "C++", "C#", "Ruby"]
    choice = st.selectbox("Select a Programming Language", languages)
    if choice:
        st.session_state["language"] = choice
        st.experimental_rerun()

# Topic Page
def topic_page():
    st.sidebar.title(f"{st.session_state['language']} Topics")
    topics = [f"Topic {i}" for i in range(1, 7)]
    topic_choice = st.sidebar.radio("Select a Topic", topics)

    if topic_choice:
        video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"  # Replace with actual video link
        notes_path = f"{topic_choice}_notes.pdf"  # Replace with actual notes file path
        questions_path = f"{topic_choice}_questions.pdf"  # Replace with actual questions file path
        
        st.header(topic_choice)
        st.subheader("Video Lesson")
        display_video(video_url)
        
        st.subheader("Notes")
        display_pdf(notes_path, "Download Notes")
        
        st.subheader("Practice Questions")
        display_pdf(questions_path, "Download Practice Questions")

# Main Function
def main():
    if "language" not in st.session_state:
        st.session_state["language"] = None

    if st.session_state["language"]:
        topic_page()
    else:
        home()

if __name__ == "__main__":
    main()