import streamlit as st

# Function to display YouTube video
def display_video(video_url):
    st.video(video_url)

# Function to display downloadable PDFs
def display_pdfs(file_paths, labels):
    for file_path, label in zip(file_paths, labels):
        if st.button(label):
            st.markdown(f"Downloading {file_path}...")
            st.download_button(label=label, data=file_path, file_name=file_path, mime="application/pdf")

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

    st.markdown('<div class="block-container">', unsafe_allow_html=True)
    cols = st.columns(len(languages))
    for idx, (lang, icon) in enumerate(languages.items()):
        with cols[idx]:
            if st.button(f"{lang}", key=lang):
                st.session_state["language"] = lang
            st.markdown(
                f"""
                <div class="block">
                    <img src="{icon}" alt="{lang} logo"/>
                    <h3>{lang}</h3>
                </div>
                """, unsafe_allow_html=True
            )
    st.markdown('</div>', unsafe_allow_html=True)

# Language Home Page
def language_home(language):
    st.title(f"Learn {language}")
    
    # Replace with actual data based on language
    if language == "Python":
        video_urls = [
            ["https://www.youtube.com/watch?v=dQw4w9WgXcQ"],  # Topic 1 videos
            ["https://www.youtube.com/watch?v=dQw4w9WgXcQ"]   # Topic 2 videos
        ]
        notes_paths = [
            [
                "Python Topic 1 Notes.pdf",
                "Python Topic 1 Additional Notes.pdf"
            ],
            [
                "Python Topic 2 Notes.pdf",
                "Python Topic 2 Additional Notes.pdf"
            ]
        ]
        questions_paths = [
            [
                "Python Topic 1 Practice Questions.pdf",
                "Python Topic 1 Additional Questions.pdf"
            ],
            [
                "Python Topic 2 Practice Questions.pdf",
                "Python Topic 2 Additional Questions.pdf"
            ]
        ]
        topics = [f"Python Topic {i}" for i in range(1, 3)]  # Replace with actual topics

    elif language == "Java":
        video_urls = [
            ["https://www.youtube.com/watch?v=jNQXAC9IVRw"],  # Topic 1 videos
            ["https://www.youtube.com/watch?v=jNQXAC9IVRw"]   # Topic 2 videos
        ]
        notes_paths = [
            [
                "Java Topic 1 Notes.pdf",
                "Java Topic 1 Additional Notes.pdf"
            ],
            [
                "Java Topic 2 Notes.pdf",
                "Java Topic 2 Additional Notes.pdf"
            ]
        ]
        questions_paths = [
            [
                "Java Topic 1 Practice Questions.pdf",
                "Java Topic 1 Additional Questions.pdf"
            ],
            [
                "Java Topic 2 Practice Questions.pdf",
                "Java Topic 2 Additional Questions.pdf"
            ]
        ]
        topics = [f"Java Topic {i}" for i in range(1, 3)]  # Replace with actual topics

    elif language == "C++":
        video_urls = [
            ["https://www.youtube.com/watch?v=oxbWdCwD9Ts"],  # Topic 1 videos
            ["https://www.youtube.com/watch?v=oxbWdCwD9Ts"]   # Topic 2 videos
        ]
        notes_paths = [
            [
                "C++ Topic 1 Notes.pdf",
                "C++ Topic 1 Additional Notes.pdf"
            ],
            [
                "C++ Topic 2 Notes.pdf",
                "C++ Topic 2 Additional Notes.pdf"
            ]
        ]
        questions_paths = [
            [
                "C++ Topic 1 Practice Questions.pdf",
                "C++ Topic 1 Additional Questions.pdf"
            ],
            [
                "C++ Topic 2 Practice Questions.pdf",
                "C++ Topic 2 Additional Questions.pdf"
            ]
        ]
        topics = [f"C++ Topic {i}" for i in range(1, 3)]  # Replace with actual topics

    elif language == "C#":
        video_urls = [
            ["https://www.youtube.com/watch?v=-5jH5mf6mSs"],  # Topic 1 videos
            ["https://www.youtube.com/watch?v=-5jH5mf6mSs"]   # Topic 2 videos
        ]
        notes_paths = [
            [
                "C# Topic 1 Notes.pdf",
                "C# Topic 1 Additional Notes.pdf"
            ],
            [
                "C# Topic 2 Notes.pdf",
                "C# Topic 2 Additional Notes.pdf"
            ]
        ]
        questions_paths = [
            [
                "C# Topic 1 Practice Questions.pdf",
                "C# Topic 1 Additional Questions.pdf"
            ],
            [
                "C# Topic 2 Practice Questions.pdf",
                "C# Topic 2 Additional Questions.pdf"
            ]
        ]
        topics = [f"C# Topic {i}" for i in range(1, 3)]  # Replace with actual topics

    elif language == "PHP":
        video_urls = [
            ["https://www.youtube.com/watch?v=7TF00hJI78Y"],  # Topic 1 videos
            ["https://www.youtube.com/watch?v=7TF00hJI78Y"]   # Topic 2 videos
        ]
        notes_paths = [
            [
                "PHP Topic 1 Notes.pdf",
                "PHP Topic 1 Additional Notes.pdf"
            ],
            [
                "PHP Topic 2 Notes.pdf",
                "PHP Topic 2 Additional Notes.pdf"
            ]
        ]
        questions_paths = [
            [
                "PHP Topic 1 Practice Questions.pdf",
                "PHP Topic 1 Additional Questions.pdf"
            ],
            [
                "PHP Topic 2 Practice Questions.pdf",
                "PHP Topic 2 Additional Questions.pdf"
            ]
        ]
        topics = [f"PHP Topic {i}" for i in range(1, 3)]  # Replace with actual topics

    elif language == "SQL":
        video_urls = [
            ["https://www.youtube.com/watch?v=27axs9dO7AE"],  # Topic 1 videos
            ["https://www.youtube.com/watch?v=27axs9dO7AE"]   # Topic 2 videos
        ]
        notes_paths = [
            [
                "SQL Topic 1 Notes.pdf",
                "SQL Topic 1 Additional Notes.pdf"
            ],
            [
                "SQL Topic 2 Notes.pdf",
                "SQL Topic 2 Additional Notes.pdf"
            ]
        ]
        questions_paths = [
            [
                "SQL Topic 1 Practice Questions.pdf",
                "SQL Topic 1 Additional Questions.pdf"
            ],
            [
                "SQL Topic 2 Practice Questions.pdf",
                "SQL Topic 2 Additional Questions.pdf"
            ]
        ]
        topics = [f"SQL Topic {i}" for i in range(1, 3)]  # Replace with actual topics

    # Sidebar for selecting topic
    st.sidebar.title(f"{language} Topics")
    topic_choice = st.sidebar.selectbox("Select a Topic", topics, index=0)

    # Define the selected topic and display the materials
    if topic_choice:
        topic_index = topics.index(topic_choice)
        st.header(f"{language}: {topic_choice}")
        st.subheader("Video Tutorials")
        st.markdown("Here are some video tutorials to help you learn:")

        for i, video_url in enumerate(video_urls[topic_index]):
            st.video(video_url, start_time=0)

        st.subheader("Notes")
        display_pdfs(notes_paths[topic_index], [f"Download {topic_choice} Notes {i+1}" for i in range(len(notes_paths[topic_index]))])

        st.subheader("Practice Questions")
        display_pdfs(questions_paths[topic_index], [f"Download {topic_choice} Practice Questions {i+1}" for i in range(len(questions_paths[topic_index]))])

        # Add a back button to return to the home page
        if st.button("Back to Language Selection"):
            st.session_state["language"] = None

# Main function
def main():
    if "language" not in st.session_state:
        st.session_state["language"] = None

    if st.session_state["language"]:
        language_home(st.session_state["language"])
    else:
        home()

if __name__ == "__main__":
    main()

