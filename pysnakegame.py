# from tkinter import *
# import random

# GAME_WIDTH = 700
# GAME_HEIGHT = 700
# SPEED = 50
# SPACE_SIZE = 50
# BODY_PARTS = 3
# SNAKE_COLOR = "#BLUE"
# FOOD_COLOR = "#RED"
# BACKGROUND_COLOR = "#000000"



# class snake :
#     pass

# class Food:
#     pass


# def next_turn():
#     pass

# def change_direction():(new_direction):
# pass

# def check_collisions():
#     pass

# def game_over():
#     pass

# window = Tk()
# window.title("Snake game")
# window.resizable(False, False)

# score = 0
# direction = 'down'

# Label =Label(window, text="score:{}".format(score), font=('consplas', 40))
# Label.pack()

# Canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
# Canvas.pack()



# window.mainloop()


# import tkinter as tk
# import random

# # Constants for the game
# GAME_WIDTH = 700
# GAME_HEIGHT = 700
# SPEED = 100
# SPACE_SIZE = 50
# BODY_PARTS = 3
# SNAKE_COLOR = "#00FF00"  # Green
# FOOD_COLOR = "#FF0000"   # Red
# BACKGROUND_COLOR = "#000000"

# # Initialize game variables
# score = 0
# direction = 'down'
# snake_body = [(100, 100), (50, 100), (0, 100)]  # Snake's initial body
# food_position = None
# food_spawned = False


# class Snake:
#     def __init__(self):
#         self.body = snake_body
#         self.direction = direction

#     def move(self):
#         head_x, head_y = self.body[0]

#         if self.direction == 'up':
#             new_head = (head_x, head_y - SPACE_SIZE)
#         elif self.direction == 'down':
#             new_head = (head_x, head_y + SPACE_SIZE)
#         elif self.direction == 'left':
#             new_head = (head_x - SPACE_SIZE, head_y)
#         elif self.direction == 'right':
#             new_head = (head_x + SPACE_SIZE, head_y)

#         self.body = [new_head] + self.body[:-1]  # Move the snake forward

#     def grow(self):
#         """ Add a new body part to the snake. """
#         tail_x, tail_y = self.body[-1]
#         self.body.append((tail_x, tail_y))


# class Food:
#     def __init__(self):
#         self.position = None
#         self.spawn()

#     def spawn(self):
#         """ Randomly place the food on the board. """
#         self.position = (random.randint(0, (GAME_WIDTH / SPACE_SIZE) - 1) * SPACE_SIZE,
#                          random.randint(0, (GAME_HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE)


# def draw_objects():
#     """ Draw the snake and food on the canvas. """
#     global food_spawned

#     canvas.delete("all")

#     # Draw the snake
#     for segment in snake.body:
#         canvas.create_rectangle(segment[0], segment[1], segment[0] + SPACE_SIZE, segment[1] + SPACE_SIZE, fill=SNAKE_COLOR)

#     # Draw the food
#     if not food_spawned:
#         food.spawn()
#         food_spawned = True

#     canvas.create_rectangle(food.position[0], food.position[1], food.position[0] + SPACE_SIZE, food.position[1] + SPACE_SIZE, fill=FOOD_COLOR)

#     # Update the score
#     score_label.config(text="Score: {}".format(score))


# def next_turn():
#     """ This function moves the snake forward and checks for collisions. """
#     snake.move()
#     check_collisions()
#     draw_objects()
#     window.after(SPEED, next_turn)


# def change_direction(new_direction):
#     """ Change the snake's direction based on key press. """
#     global direction
#     if new_direction == 'up' and direction != 'down':
#         direction = 'up'
#     elif new_direction == 'down' and direction != 'up':
#         direction = 'down'
#     elif new_direction == 'left' and direction != 'right':
#         direction = 'left'
#     elif new_direction == 'right' and direction != 'left':
#         direction = 'right'


# def check_collisions():
#     """ Check for collisions with food, walls, or the snake itself. """
#     global score, food_spawned

#     # Check for collision with the food
#     if snake.body[0] == food.position:`11`1
#         score += 10
#         food_spawned = False
#         snake.grow()

#     # Check for collision with walls
#     head_x, head_y = snake.body[0]
#     if head_x < 0 or head_x >= GAME_WIDTH or head_y < 0 or head_y >= GAME_HEIGHT:
#         game_over()

#     # Check for collision with itself
#     if len(snake.body) != len(set(snake.body)):
#         game_over()


# def game_over():
#     """ Handle the end of the game. """
#     canvas.delete("all")
#     canvas.create_text(GAME_WIDTH / 2, GAME_HEIGHT / 2, text="GAME OVER", fill="white", font=('consplas', 40))
#     canvas.create_text(GAME_WIDTH / 2, GAME_HEIGHT / 2 + 50, text="Final Score: {}".format(score), fill="white", font=('consplas', 20))


# # Set up the window
# window = tk.Tk()
# window.title("Snake Game")
# window.resizable(False, False)

# # Create a label for the score
# score_label = tk.Label(window, text="Score: {}".format(score), font=('consplas', 40))
# score_label.pack()

# # Create the canvas
# canvas = tk.Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
# canvas.pack()

# # Initialize snake and food
# snake = Snake()
# food = Food()

# # Set up keyboard bindings
# window.bind("<Up>", lambda event: change_direction('up'))
# window.bind("<Down>", lambda event: change_direction('down'))
# window.bind("<Left>", lambda event: change_direction('left'))
# window.bind("<Right>", lambda event: change_direction('right'))

# # Start the game loop
# next_turn()

# # Run the window
# window.mainloop()



import tkinter as tk
import random

# Constants for the game
GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 200  # Adjusted speed
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#00FF00"  # Green
FOOD_COLOR = "#FF0000"   # Red
BACKGROUND_COLOR = "#000000"

# Initialize game variables
score = 0
direction = 'down'
snake_body = [(100, 100), (50, 100), (0, 100)]  # Snake's initial body
food_position = None
food_spawned = False
game_running = True

class Snake:
    def __init__(self):
        self.body = snake_body
        self.direction = direction

    def move(self):
        head_x, head_y = self.body[0]

        if self.direction == 'up':
            new_head = (head_x, head_y - SPACE_SIZE)
        elif self.direction == 'down':
            new_head = (head_x, head_y + SPACE_SIZE)
        elif self.direction == 'left':
            new_head = (head_x - SPACE_SIZE, head_y)
        elif self.direction == 'right':
            new_head = (head_x + SPACE_SIZE, head_y)

        self.body = [new_head] + self.body[:-1]  # Move the snake forward

    def grow(self):
        """ Add a new body part to the snake. """
        tail_x, tail_y = self.body[-1]
        self.body.append((tail_x, tail_y))


class Food:
    def __init__(self):
        self.position = None
        self.spawn()

    def spawn(self):
        """ Randomly place the food on the board. """
        self.position = (random.randint(0, (GAME_WIDTH // SPACE_SIZE) - 1) * SPACE_SIZE,
                         random.randint(0, (GAME_HEIGHT // SPACE_SIZE) - 1) * SPACE_SIZE)
        print("Food position:", self.position)  # Debugging line


def draw_objects():
    """ Draw the snake and food on the canvas. """
    global food_spawned

    canvas.delete("all")

    # Draw the snake
    for segment in snake.body:
        canvas.create_rectangle(segment[0], segment[1], segment[0] + SPACE_SIZE, segment[1] + SPACE_SIZE, fill=SNAKE_COLOR)

    # Draw the food if not already spawned
    if not food_spawned:
        food.spawn()
        food_spawned = True

    canvas.create_rectangle(food.position[0], food.position[1], food.position[0] + SPACE_SIZE, food.position[1] + SPACE_SIZE, fill=FOOD_COLOR)

    # Update the score
    score_label.config(text="Score: {}".format(score))


def next_turn():
    """ This function moves the snake forward and checks for collisions. """
    snake.move()
    check_collisions()
    if game_running:
        draw_objects()
        window.after(SPEED, next_turn)


def change_direction(new_direction):
    """ Change the snake's direction based on key press. """
    global direction
    if new_direction == 'up' and direction != 'down':
        direction = 'up'
    elif new_direction == 'down' and direction != 'up':
        direction = 'down'
    elif new_direction == 'left' and direction != 'right':
        direction = 'left'
    elif new_direction == 'right' and direction != 'left':
        direction = 'right'


def check_collisions():
    """ Check for collisions with food, walls, or the snake itself. """
    global score, food_spawned, game_running

    # Check for collision with the food
    if snake.body[0] == food.position:
        score += 10
        food_spawned = False
        snake.grow()

    # Check for collision with walls
    head_x, head_y = snake.body[0]
    if head_x < 0 or head_x >= GAME_WIDTH or head_y < 0 or head_y >= GAME_HEIGHT:
        game_over()

    # Check for collision with itself
    if len(snake.body) != len(set(snake.body)):
        game_over()


def game_over():
    """ Handle the end of the game. """
    global game_running
    game_running = False
    canvas.delete("all")
    canvas.create_text(GAME_WIDTH / 2, GAME_HEIGHT / 2, text="GAME OVER", fill="white", font=('Arial', 40))
    canvas.create_text(GAME_WIDTH / 2, GAME_HEIGHT / 2 + 50, text="Final Score: {}".format(score), fill="white", font=('Arial', 20))


# Set up the window
window = tk.Tk()
window.title("Snake Game")
window.resizable(False, False)

# Create a label for the score
score_label = tk.Label(window, text="Score: {}".format(score), font=('Arial', 40))
score_label.pack()

# Create the canvas
canvas = tk.Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

# Initialize snake and food
snake = Snake()
food = Food()

# Set up keyboard bindings
window.bind("<Up>", lambda event: change_direction('up'))
window.bind("<Down>", lambda event: change_direction('down'))
window.bind("<Left>", lambda event: change_direction('left'))
window.bind("<Right>", lambda event: change_direction('right'))

# Start the game loop
next_turn()

# Run the window
window.mainloop()
