import streamlit as st
import pygame
import sys
import matplotlib.pyplot as plt
def simulate_newtons_laws():
    # Initialize Pygame
    pygame.init()

    # Set up the screen
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Newton's Laws of Motion Simulation")

    # Colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)

    # Constants
    gravity = 0.5

    # Ball parameters
    ball_radius = 20
    ball_color = RED
    ball_x = WIDTH // 2
    ball_y = HEIGHT // 2
    ball_speed_x = 5
    ball_speed_y = 0

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Apply Newton's first law: An object in motion stays in motion
        ball_x += ball_speed_x
        ball_y += ball_speed_y

        # Apply Newton's second law: F = ma (in this case, force is gravity)
        ball_speed_y += gravity

        # Apply Newton's third law: For every action, there is an equal and opposite reaction

        # Bounce off the edges
        if ball_x <= ball_radius or ball_x >= WIDTH - ball_radius:
            ball_speed_x *= -1
        if ball_y <= ball_radius or ball_y >= HEIGHT - ball_radius:
            ball_speed_y *= -0.9

        # Clear the screen
        screen.fill(WHITE)

        # Draw the ball
        pygame.draw.circle(screen, ball_color, (int(ball_x), int(ball_y)), ball_radius)

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        pygame.time.Clock().tick(60)

    pygame.quit()

def main():
    st.title("Newton's Laws of Motion Simulation")
    st.sidebar.title("Newton's Laws of Motion")
    st.sidebar.markdown("### First Law: Inertia")
    st.sidebar.write("An object in motion stays in motion and an object at rest stays at rest, unless acted upon by an external force.")
    st.sidebar.markdown("### Second Law: F = ma")
    st.sidebar.write("The acceleration of an object is directly proportional to the net force acting on it and inversely proportional to its mass.")
    st.sidebar.markdown("### Third Law: Action and Reaction")
    st.sidebar.write("For every action, there is an equal and opposite reaction.")
    st.write("Newton's laws of motion: the original 'how-to' guide for making sense of the chaos in the universe... or at least trying to.")
    st.write("This simulation demonstrates Newton's laws of motion using a bouncing ball.")
    st.write("### Simulation Explanation")
    st.write("- **First Law (Inertia)**: The ball continues to move horizontally unless acted upon by an external force, such as gravity.")
    st.write("- **Second Law (F = ma)**: The force of gravity causes the ball to accelerate downward (increase in velocity) as it bounces off the ground.")
    st.write("- **Third Law (Action and Reaction)**: When the ball bounces off the ground, it exerts a force on the ground (action), and the ground exerts an equal and opposite force on the ball (reaction).")

    simulate_newtons_laws()

if __name__ == "__main__":
    main()
