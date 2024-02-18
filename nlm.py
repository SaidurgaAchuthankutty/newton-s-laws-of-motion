import streamlit as st
import pygame
import sys

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
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

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

def main():
    st.title("Newton's Laws of Motion Simulation")
    st.sidebar.title("Learn About Newton's Laws")

    # Add explanations of Newton's laws in the sidebar
    st.sidebar.markdown("### First Law: Inertia")
    st.sidebar.write("An object in motion stays in motion and an object at rest stays at rest, unless acted upon by an external force.")

    st.sidebar.markdown("### Second Law: F = ma")
    st.sidebar.write("The acceleration of an object is directly proportional to the net force acting on it and inversely proportional to its mass.")

    st.sidebar.markdown("### Third Law: Action and Reaction")
    st.sidebar.write("For every action, there is an equal and opposite reaction.")

    # Add simulation to the main page
    st.subheader("A simple repesentation")
    simulate_newtons_laws()

if __name__ == "__main__":
    main()
