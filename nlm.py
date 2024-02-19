import streamlit as st

def joke_on_newton():
    st.write("## Welcome to Newton's Laws of Motion Simulator!")
    st.write("Why did the apple fall on Newton's head? Because it couldn't resist his gravity!")

def main():
    # Display joke on Newton
    joke_on_newton()

    # Options to choose which law to study first
    selected_law = st.sidebar.selectbox("Choose which law to study first:", ["First Law", "Second Law", "Third Law", "Kinematics Equation"])

    # Explanation and illustrations for each law
    if selected_law == "First Law":
        st.write("## Newton's First Law: Law of Inertia")
        st.write("An object at rest stays at rest, and an object in motion stays in motion with the same speed and in the same direction unless acted upon by an unbalanced force.")
        st.write("Here's a GIF to illustrate the concept:")
        st.image("inertia.gif", use_column_width=True)
        st.write("Imagine a cat lounging on a couch all day... that's inertia in action!")
        st.write("Now, let's move on to a numerical question:")

        # Mind-boggling numerical question
        numerical_answer = st.write("What is the value of inertia of an object with mass 5 kg?", min_value=0)
        inertia_answer= st.radio("Inertia would be",['10kg','5kg','20kg'])
        if st.button("Submit"):
            if inertia_answer == '5kg':
                st.write("Congratulations! You got it right!")
            else:
                st.write("Oops! That's not correct. The correct answer is 5 kg.")

    elif selected_law == "Second Law":
        st.write("## Newton's Second Law: F = ma")
        st.write("The acceleration of an object is directly proportional to the net force acting on it and inversely proportional to its mass.")
        st.image("sec.gif", use_column_width=True)

        st.write("And now, let's solve a numerical question:")

        # Mind-boggling numerical question
        numerical_answer = st.write("What force is required to accelerate an object with mass 10 kg at 5 m/s^2?", min_value=0)
        force_answer = st.radio("The force would be",['10N','35N','50N'])
        if st.button("Submit"):
            if force_answer == '50N':
                st.write("Congratulations! You got it right!")
            else:
                st.write("Oops! That's not correct. The correct answer is 50 N.")

    elif selected_law == "Third Law":
        st.write("## Newton's Third Law: Action and Reaction")
        st.write("For every action, there is an equal and opposite reaction.")
        st.write("Here's a humorous example of action and reaction:")

        # Include a sarcastic example
        st.write("Imagine trying to push a door open and ending up getting pushed back instead!")
        st.write("Here's a GIF to illustrate the concept:")
        st.image("reaction.gif", use_column_width=True)
        st.write("Now, let's tackle a numerical question:")

        # Mind-boggling numerical question
        numerical_answer = st.write("If object A exerts a force of 10 N on object B, what force does object B exert on object A?", min_value=0)
        t_answer = st.radio("The answer is",['10N','20N','30N'])
        if st.button("Submit"):
            if t_answer == '10N':
                st.write("Congratulations! You got it right!")
            else:
                st.write("Oops! That's not correct. The correct answer is 10 N in the opposite direction.")

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
            "An object is initially at rest ($u = 0$) and accelerates uniformly at $2 \, \text{m/s}^2$ for $5 \, \text{s}$. What is its displacement?")
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
            "An object is initially at rest ($u = 0$) and accelerates uniformly at $2 \, \text{m/s}^2$ for $5 \, \text{s}$. What is its final velocity?")
        st.latex(r"v = (0) + (2)(5) = 10 \, \text{m/s}")

        st.header("Equation for displacement ($s$) with final velocity ($v$) and initial velocity ($u$):")
        st.latex(r"v^2 = u^2 + 2as")
        st.write("where:")
        st.write("- $s$ is the displacement of the object.")
        st.write("- $u$ is the initial velocity of the object.")
        st.write("- $v$ is the final velocity of the object.")
        st.write("- $a$ is the acceleration of the object.")

        st.subheader("Example:")
        st.write(
            "An object accelerates from $10 \, \text{m/s}$ to $30 \, \text{m/s}$ while traveling a distance of $100 \, \text{m}$. What is its acceleration?")
        st.latex(r"a = \frac{v^2 - u^2}{2s} = \frac{900 - 100}{200} = 4 \, \text{m/s}^2")

        st.write("Now, let's solve numerical question:")

        # Mind-boggling numerical question
        numerical_answer = st.write("What is the final velocity of an object with initial velocity 5 m/s and acceleration 2 m/s^2 after 3 seconds?", min_value=0)
        velocity_answer = st.radio("The final velocity is",['49m/s','32m/s','11 m/s'])
        if st.button("Submit"):
            if velocity_answer == '11m/s':
                st.write("Congratulations! You got it right!")
            else:
                st.write("Oops! That's not correct. The correct answer is 11 m/s.")

if __name__ == "__main__":
    main()
