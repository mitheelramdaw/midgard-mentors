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
    st.markdown(
        """
        <style>
        .block-container {
            display: flex;
            flex-wrap: wrap;
            justify-content: space-around;
            margin-top: 20px;
        }
        .block {
            background-color: #f9f9f9;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            padding: 20px;
            margin: 10px;
            text-align: center;
            flex: 1;
            min-width: 150px;
            max-width: 200px;
        }
        .block:hover {
            background-color: #f1f1f1;
            cursor: pointer;
        }
        </style>
        """, unsafe_allow_html=True
    )
    languages = {
        "Python": "python-icon.png",
        "Java": "java-icon.png",
        "C++": "cpp-icon.png",
        "C#": "csharp-icon.png",
        "PHP": "php-icon.png",
        "SQL": "sql-icon.png"
    }

    selected_language = None
    st.markdown('<div class="block-container">', unsafe_allow_html=True)
    cols = st.columns(len(languages))
    for idx, (lang, icon) in enumerate(languages.items()):
        with cols[idx]:
            if st.button(f"{lang}"):
                selected_language = lang
    st.markdown('</div>', unsafe_allow_html=True)

    if selected_language:
        st.session_state["language"] = selected_language
        st.experimental_rerun()

# Topic Page
def topic_page():
    st.sidebar.title(f"{st.session_state['language']} Topics")
    topics = [f"Topic {i}" for i in range(1, 7)]
    topic_choice = st.sidebar.radio("Select a Topic", topics)

    if topic_choice:
        video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"  # Replace with actual video link
        notes_path = f"Programming 631 Study Guide (Updated - 2023) (1).pdf"  # Replace with actual notes file path
        questions_path = f"Java-Interview-Questions-and-Answers-PDF-Free-Download.pdf"  # Replace with actual questions file path
        
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
