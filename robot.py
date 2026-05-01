from lesson_header import *

# Variables
number_of_obstacles = 4
obstacle_count = 0
warning_distance = 15
eye_colours = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
direction = 0

# Function ideas
def show_progress():
    if obstacle_count < 4:
        eyes.set_both(255, 0, 0)
        print("---Obstacle Number {}---".format(obstacle_count))
    elif obstacle_count >= 4:
        eyes.set_both(0, 255, 0)
        print("----Finished----")

def choose_move():
    global distance
    global warning_distance
    global direction
    global obstacle_count
    distance = sonar.get_distance_cm(filtered=True)
    print("Distance is {}cm".format(distance))
    if distance > warning_distance:
        eyes.set_both(0, 0, 255)
        moves.forward(0.5)
    else:
        obstacle_count += 1
        show_progress()
        if direction == 0:
            moves.move_right(1.6)
            direction += 1
        else:
            moves.move_left(1.6)
            direction -= 1
        

while obstacle_count < number_of_obstacles:
    choose_move()

# Finish safely when you are done.
stop_project_robot()
