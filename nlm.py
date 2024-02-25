import streamlit as st
import pandas as pd
import random

def load_quiz_data(file_path):
    try:
        encodings = ['utf-8', 'latin1', 'iso-8859-1', 'cp1252']
        for encoding in encodings:
            try:
                quiz_data = pd.read_csv(file_path, encoding=encoding)
                return quiz_data
            except UnicodeDecodeError:
                continue
        st.error("Unable to decode the file using any available encoding.")
        return None
    except FileNotFoundError:
        st.error("Quiz data file not found.")
        return None


def display_question(quiz_data):
    question_index = random.randint(0, len(quiz_data) - 1)
    question_row = quiz_data.iloc[question_index]
    question = question_row['Question']
    options = question_row['Options'].split(',')
    answer = question_row['Answer']
    return question, options, answer

def main():
    st.write("## Hello there!")
    st.title("Let's learn Newton's Laws of Motion")
    st.write("You can explore more options on the sidebar")

    st.sidebar.title("Menu")
    menu_option = st.sidebar.selectbox("Choose an option:", ["Learn", "Quiz","Simulation"])
    if menu_option == "Simulation":
        st.title("Demonstration of Newton's Laws of Motion and Kinematics")

        # Introduction
        st.write("In this video, we observe the motion of a ball inside a box.")
        st.write("Let's analyze how this video demonstrates Newton's laws of motion and kinematics.")
        st.write("")
        # Display Video
        st.video("https://youtu.be/5mGuCdlCcNM?si=cwKBY9ZDMJ8kW2Ih")
        # Explanation of Newton's Laws
        st.header("Newton's Laws of Motion:")
        st.write("### 1. Newton's First Law (Law of Inertia):")
        st.write("Explanation: The video demonstrates Newton's first law by showing the logo maintaining its state of motion (constant velocity or bouncing) unless acted upon by an external force. When the logo is bouncing freely inside the box, it continues to move until it hits the walls due to inertia.")
        st.write("Example: As the logo moves around, it doesn't change its motion unless it collides with the walls of the box, which exert a force on it.")
        st.write("")

        st.write("### 2. Newton's Second Law (F = ma):")
        st.write("Explanation: Newton's second law states that the acceleration of an object is directly proportional to the force applied to it and inversely proportional to its mass. In the video, when the logo hits the wall of the box, it experiences a force from the wall (reaction force), causing it to change its velocity or direction.")
        st.write("Example: When the logo collides with the wall, the force exerted by the wall causes the ball to accelerate or decelerate, depending on the direction of the force.")
        st.write("")

        st.write("### 3. Newton's Third Law (Action and Reaction):")
        st.write("Explanation: Newton's third law states that for every action, there is an equal and opposite reaction. In the video, when the logo hits the wall of the box, it exerts a force on the wall, and the wall exerts an equal and opposite force on the logo.")
        st.write("Example: As the logo bounces off the wall, it pushes against the wall with a certain force, and in response, the wall pushes back on the ball with an equal force, causing it to bounce away.")
        st.write("")

        # Discussion on Kinematics
        st.header("Kinematics:")
        st.write("Explanation: Kinematics is the study of motion without considering its causes. In the video, kinematics can be observed by analyzing the ball's trajectory, velocity, and acceleration as it moves inside the box. Using kinematic equations, such as those for displacement, velocity, and acceleration, we can quantify and describe the logo's motion")
        st.write("Example: By tracking the position of the logo over time and measuring its velocity and acceleration, we can apply kinematics equations to predict its future motion or understand its past motion within the box.")
        st.write("")
    if menu_option == "Learn":
        # Options to choose which law to study first
        selected_law = st.sidebar.selectbox("Choose which law to study first:",
                                            ["First Law", "Second Law", "Third Law", "Kinematics Equation"])
        # Explanation and illustrations for each law
        if selected_law == "First Law":
            col1, col2= st.columns(2)
            with col1:
                st.write("## Newton's First Law: Law of Inertia")
                st.write(
                    "An object at rest stays at rest, and an object in motion stays in motion with the same speed and in the same direction unless acted upon by an unbalanced force.")
                st.write("Have you ever been so comfy on the couch that you just couldn't get up? That's Newton's first law in action! Your body is at rest and wants to stay at rest until an external force (like the impending doom of having to get up for work) comes along and nudges you into motion.")
            with col2:
                st.write("Here's a GIF to illustrate the concept:")
                st.image("inertia.gif", use_column_width=True)
        elif selected_law == "Second Law":
            col1, col2 = st.columns(2)
            with col1:
                st.write("## Newton's Second Law: F = ma")
                st.write(
                    "The acceleration of an object is directly proportional to the net force acting on it and inversely proportional to its mass.")
                st.write("Imagine you're at a buffet, trying to balance a plate piled high with food while walking to your table. Suddenly, your friend rushes past you, causing you to stumble. As you struggle to regain your balance, you realize that the force of your friend's push (the net force) caused you to accelerate (lose balance) according to Newton's Second Law. The more force your friend applies (the faster they run into you), the greater your acceleration (the harder it is to maintain balance), especially if your plate is laden with an excessive amount of food (high mass). So, next time you're at a buffet, remember Newton's Second Law – both in physics and in buffet etiquette!")
            with col2:
                st.image("sec.gif", use_column_width=True)

        elif selected_law == "Third Law":
            col1, col2 = st.columns(2)
            with col1:
                st.write("## Newton's Third Law: Action and Reaction")
                st.write("For every action, there is an equal and opposite reaction.")
                st.write("Here's a humorous example of action and reaction:")
                st.write("When you step on a banana peel and slip, it's not just the peel's revenge for being discarded; it's actually an excellent demonstration of Newton's third law! As your foot applies a force to the banana peel, according to Newton's third law, the peel applies an equal and opposite force back on your foot. This reaction force causes your foot to slip backward, leading to a comical, albeit embarrassing, fall. So, next time you encounter a banana peel, remember, it's not just a hazard; it's a physics lesson in action!")
            with col2:
                st.write("Here's a GIF to illustrate the concept:")
                st.image("reaction.gif", use_column_width=True)

        elif selected_law == "Kinematics Equation":
            (st.header
             ("Kinematics Equations"))

            st.write(
                "Let's delve into the kinematics equations, which describe the motion of objects without considering the forces causing the motion. These equations are fundamental in physics and are often used to analyze the motion of objects under various conditions.")

            st.header("Equation for displacement ($s$):")
            st.latex(r"s = ut + \frac{1}{2}at^2")
            st.write("where:")
            st.write("- $s$ is the displacement of the object.")
            st.write("- $u$ is the initial velocity of the object.")
            st.write("- $a$ is the acceleration of the object.")
            st.write("- $t$ is the time taken.")

            st.subheader("Example:")
            st.write(
                "An object is initially at rest ($u = 0$) and accelerates uniformly at $2, \text{m/s}^2$ for $5, \text{s}$. What is its displacement?")
            st.latex(r"s = (0)(5) + \frac{1}{2}(2)(5)^2 = 25 \, \text{m}")

            st.header("Equation for final velocity ($v$):")
            st.latex(r"v = u + at")
            st.write("where:")
            st.write("- $v$ is the final velocity of the object.")
            st.write("- $u$ is the initial velocity of the object.")
            st.write("- $a$ is the acceleration of the object.")
            st.write("- $t$ is the time taken.")

            st.subheader("Example:")
            st.write(
                "An object is initially at rest ($u = 0$) and accelerates uniformly at $2, \text{m/s}^2$ for $5, \text{s}$. What is its final velocity?")
            st.latex(r"v = (0) + (2)(5) = 10 \, \text{m/s}")

            st.header("Equation for displacement ($s$) with final velocity ($v$) and initial velocity ($u$):")
            st.latex(r"v^2 = u^2 + 2as")
            st.write("where:")
            st.write("- $s$ is the displacement of the object.")
            st.write("- $u$ is the initial velocity of the object.")
            st.write("- $v$ is the final velocity of the object.")
            st.write("- $u$ is the initial velocity of the object.")
            st.write("- $a$ is the acceleration of the object.")

            st.subheader("Example:")
            st.write(
                "An object accelerates from $10, \text{m/s}$ to $30, \text{m/s}$ while traveling a distance of $100, \text{m}$. What is its acceleration?")

            st.latex(r"a = \frac{v^2 - u^2}{2s} = \frac{900 - 100}{200} = 4 \, \text{m/s}^2")

    elif menu_option == "Quiz":
        quiz_data = load_quiz_data("quiz_data.csv")
        if quiz_data is not None:
            questions = []

            # Select 10 random questions from the file
            for _ in range(10):
                question, options, answer = display_question(quiz_data)
                questions.append((question, options, answer))

            # Display all questions at once
            for i, (question, options, answer) in enumerate(questions):
                st.write(f"### Question {i + 1}:")
                st.write("Question:", question)
                user_answer = st.radio(f"Select an option for question {i + 1}:", options, key=f"question_{i}")
                st.write("")

            # Submit button to evaluate answers
            if st.button("Submit", key="submit_button"):
                score = 0
                for i, (_, _, answer) in enumerate(questions):
                    user_answer = st.session_state[f"question_{i}"]
                    if user_answer == answer:
                        score += 1
                        st.write("Congratulations! You got it right!")
                    else:
                        st.write("Oops! That's not correct. The correct answer is:", answer)
                st.write(f"Your total score is: {score}/10")

if __name__ == "__main__":
    main()
