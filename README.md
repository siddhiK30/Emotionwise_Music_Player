Problem Statement:

A person’s mood is mainly affected by the surrounding atmosphere and the type of company they keep around them. Our aim is to create a system that recognizes the significant influence of a person's surroundings and social interactions on their mood, impacting both their personal and professional life. This system will recommend suitable songs to users based on their current mood.



Installation Steps:

    1. Clone the repository.
    2. Navigate to the project directory.
    3. Create and activate a virtual environment (optional but recommended).
    4. Install Django.
    6. Install other required dependencies(django, streamlit, numpy , cv2, mediapipe, tensorflow, keras, streamlit_webrtc).
    7. Before running the code, make sure to modify the file path according to your system's directory structure.
    8. Run the Django server ----> 'python manage.py  runserver'
    9. Open your web browser and go to http://localhost:8000 to access the website.
    

                     
Features:

    Utilize emotion recognition for personalized playlists matching user’s moods.
    Home page displaying login and sign up options
    Analyze song emotions to align with users' current mood.
    Backend with authentication and linking of webpages.
    Songs to be recommended according to language, singer and emotion preference.
    Feature mood-specific playlists and trending songs.



How to Use the Project:

    1. Register and log in to the website.
    2. Click on the songs button to get redirected to the streamlit page.
    3. Enter your preferred language and singer.
    4. A webcam will be opened and scan your face and capture the emotion.
    5. Then click on recommend me songs you will be redirected to a youtube page with your preferred songs.



Sources:
    Frontend: Bootstrap
    Backend: YouTube tutorials.
    Machine Learning: 
        -Machine Learning in Action(textbook)
        -Supporting Diverse ML Systems at Netflix(link)
        -Youtube tutorials
    Streamlit: Official documentation for integration.


Conclusion:- 
This endeavor sharpened planning and execution abilities, offering practical insights into both web development and machine learning. It emphasized the value of incorporating buffer periods between project phases and provided a glimpse into the synergy between web development and machine learning.
