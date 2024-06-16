import pygame
import time



# Initialize Pygame
pygame.init()

# Initialize the joystick module
pygame.joystick.init()
time.sleep(2)

# Check if there is any joystick connected
if pygame.joystick.get_count() > 0:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    print(f"Joystick Name: {joystick.get_name()}")

    # Main loop
    try:
        while True:
            # Event handling loop
            for event in pygame.event.get():
                if event.type == pygame.JOYAXISMOTION:
                    x_axis01 = joystick.get_axis(0)
                    y_axis01 = joystick.get_axis(1)
                    # x_axis02 = joystick.get_axis(2)
                    # y_axis02 = joystick.get_axis(3)
                    print(f"X Axis: {x_axis01}, Y Axis: {y_axis01}")
                    # print(f"X Axis: {x_axis02}, Y Axis: {y_axis02}")
                elif event.type == pygame.JOYBUTTONDOWN:
                    print(f"Button {event.button} pressed")
                elif event.type == pygame.JOYBUTTONUP:
                    print(f"Button {event.button} released")

            time.sleep(0.1)
    except KeyboardInterrupt:
        print("Exiting...")
else:
    print("No joystick found.")

# Quit Pygame
pygame.quit()
