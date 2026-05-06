from lesson_header import *

# Variables
number_of_obstacles = 4
obstacle_count = 0
warning_distance = 18
eye_colours = [
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255)
]
direction = 0

# Function ideas
def show_progress():
    if obstacle_count < 4:
        eyes.set_both(*eye_colours[0])
        print("---Obstacle Number {}---".format(obstacle_count))
       
def choose_move():
    global distance
    global warning_distance
    global direction
    global obstacle_count
    distance = sonar.get_distance_cm(filtered=True)
    print("Distance is {}cm".format(distance))
    if distance > warning_distance:
        eyes.set_both(*eye_colours[2])
        moves.forward(0.5)
    else:
        obstacle_count += 1
        show_progress()
        if direction == 0:
            print("Direction = {}, moving right".format(direction))
            moves.move_right(1.6)
            direction += 1
        else:
            print("Direction = {}, moving left".format(direction))
            moves.move_left(1.6)
            direction -= 1
        

while obstacle_count < number_of_obstacles:
    choose_move()
print("----Finished----")
eyes.set_both(*eye_colours[1])
time.sleep(0.4)
eyes.set_both(*eye_colours[2])
time.sleep(0.4)
eyes.set_both(*eye_colours[1])
# Finish safely when you are done.
stop_project_robot()
