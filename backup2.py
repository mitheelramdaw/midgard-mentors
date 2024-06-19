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
            border-radius: 15px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
            padding: 30px;
            margin: 20px;
            text-align: center;
            flex: 1;
            min-width: 200px;
            max-width: 250px;
            transition: background-color 0.3s ease, transform 0.3s ease;
        }
        .block:hover {
            background-color: #e9e9e9;
            transform: translateY(-10px);
            cursor: pointer;
        }
        .block img {
            width: 60px;
            height: 60px;
            margin-bottom: 10px;
        }
        </style>
        """, unsafe_allow_html=True
    )
    languages = {
        "Python": "https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg",
        "Java": "https://upload.wikimedia.org/wikipedia/en/3/30/Java_programming_language_logo.svg",
        "C++": "https://upload.wikimedia.org/wikipedia/commons/1/18/ISO_C%2B%2B_Logo.svg",
        "C#": "https://upload.wikimedia.org/wikipedia/commons/4/4f/Csharp_Logo.png",
        "PHP": "https://upload.wikimedia.org/wikipedia/commons/2/27/PHP-logo.svg",
        "SQL": "https://upload.wikimedia.org/wikipedia/commons/8/87/Sql_data_base_with_logo.png"
    }

    selected_language = None
    st.markdown('<div class="block-container">', unsafe_allow_html=True)
    cols = st.columns(len(languages))
    for idx, (lang, icon) in enumerate(languages.items()):
        with cols[idx]:
            st.markdown(
                f"""
                <div class="block" onclick="document.getElementById('{lang}').click()">
                    <img src="{icon}" alt="{lang} logo"/>
                    <h3>{lang}</h3>
                </div>
                """, unsafe_allow_html=True
            )
            if st.button(f"{lang}", key=lang, on_click=lambda lang=lang: set_language(lang)):
                selected_language = lang
    st.markdown('</div>', unsafe_allow_html=True)

def set_language(lang):
    st.session_state["language"] = lang
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
