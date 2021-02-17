##### Exercises #####
#
# This file is a set of constants that contain exercises.
# The exercises are grouped by muscle group.
# Each muscle group is then assigned super, and circuit opposites
# Workouts are also set using the muscle groups
#
##### --------- #####

##### --------------------------------- #####
#     Exercises grouped by muscle group     #
##### --------------------------------- #####

# Upper body
CHEST = ['Push-ups', 'Incline Bench Press', 'Bench Press']
BICEPS = ['Narrow grip chin ups', 'Curls', 'Cross Body Hammer Curls', 'Hammer curls', 'Reverse Grip curl']
TRICEPS = ['Reverse Grip bench press', 'Floor Press', 'Incline Overhead Tricep extension', 'One-arm overhead tricep extension']
SHOULDERS = ['Standing Overhead Press', 'Front Raise', 'Single arm overhead press',
             'Lateral Raise', 'Chest Supported rear Delt Raise',
             'Single Arm bent-over rear Delt Raise']
FOREARMS = ['Pinch Grip rows', 'Heavy Carries', 'Wrist Curls']
BACK = ['One-arm support row', 'Bent-over row', 'Pull-ups', 'Chin-ups']
ABS = ['Plank', 'pallof press', 'Reverse Crunch', 'Hanging leg lifts', 'Leg Lifts',
       'Russian Twist', 'Side plank lifts', 'Side Bends', 'Crunches']
# Lower Body
HAMSTRINGS = ['DeadLift', 'Lying Leg Curls', 'Glute ham raise']
CALVES = ['Single Leg paused calf raise', 'Calf Raise', 'Seated Calf Raise']
QUADS = ['Squat', 'Split Squats', 'Bulgarian Split Squats', 'Box Squat']
GLUTES = ['Hip Thrusts', 'Glute Bridges', 'Romanian Deadlifts']

# Dict of all muscle groups
EXERCISES = {
    "chest": CHEST,
    "biceps": BICEPS,
    "triceps": TRICEPS,
    "shoulders": SHOULDERS,
    "forearms": FOREARMS,
    "back": BACK,
    "abs": ABS,
    "hamstrings": HAMSTRINGS,
    "calves": CALVES,
    "quads": QUADS,
    "glutes": GLUTES
}

# dict of muscles groups and their compatible super set groups
SUPERSETS = {
    "chest": ["back", "forearms", "hamstrings", "quads", "calves", "glutes", "abs"],
    "biceps": ["triceps", "shoulders", "hamstrings", "quads", "calves", "glutes", "abs"],
    "triceps": ["biceps", "forearms", "hamstrings", "quads", "calves", "glutes", "abs"],
    "shoulders": ["biceps", "forearms", "hamstrings", "quads", "calves", "glutes", "abs", "triceps"],
    "forearms": ["chest", "biceps", "triceps", "shoulders", "back", "hamstrings", "quads", "calves", "glutes", "abs"],
    "back": ["chest", "forearms", "quads", "calves"],
    "abs": ["chest", "biceps", "triceps", "shoulders", "back", "hamstrings", "quads", "calves", "glutes", "forearms"],
    "hamstrings": ["quads", "calves", "chest", "biceps", "triceps", "shoulders"],
    "calves": ["chest", "biceps", "triceps", "shoulders", "back", "hamstrings", "quads", "forearms", "glutes", "abs"],
    "quads": ["hamstrings", "calves", "chest", "biceps", "triceps", "shoulders"],
    "glutes": ["calves", "quads", "chest", "biceps", "triceps", "shoulders"]
}

##### -------- #####
#     Workouts     #
##### -------- #####

#####
# Workouts contain lists of muscle groups
# For each time a muscle group is in a workout list there will be 1 exercise of that group.
# If chest could/should be hit twice in a single workout, it should be in the workout list twice
#####


# Push/Pull
PUSH_PP = ["quads", "quads", "chest", "chest", "shoulders", "shoulders", "triceps", "triceps", "calves"]
PULL_PP = ["back", "back", "hamstrings", "hamstrings", "biceps", "biceps", "glutes", "glutes", "abs", "forearms"]
# Push/Pull/Legs
PUSH = ["chest", "chest", "chest", "shoulders", "shoulders", "shoulders", "triceps", "triceps", "triceps"]
PULL = ["back", "back", "back", "biceps", "biceps", "biceps", "abs", "abs", "forearms"]
LEGS = ["quads", "quads", "quads", "quads", "hamstrings", "hamstrings", "hamstrings", "hamstrings",
        "calves", "calves", "glutes", "glutes", "glutes"]
# Full Body
FULLBODY = ["chest", "chest", "biceps", "biceps", "triceps", "triceps",
            "shoulders", "shoulders", "forearms", "back", "back", "abs",
            "hamstrings", "hamstrings", "calves", "quads", "quads", "glutes", "glutes"]
# Bro Split
BACK_BICEPS = ["back", "back", "back", "back", "back",
               "biceps", "biceps", "biceps", "biceps", "forearms"]
CHEST_TRICEPS = ["chest", "chest", "chest", "chest", "chest",
                 "triceps", "triceps", "triceps", "triceps", "triceps"]
SHOULDERS_ABS = ["shoulders", "shoulders", "shoulders", "shoulders", "shoulders", "shoulders",
                 "abs", "abs", "abs", "abs", "abs"]
# Other
# MURPHY = ["Pull-ups", "Push-ups", "Squats"]
CARDIO_ABS = ["abs", "abs", "abs", "abs", "abs", "abs", "abs", "abs", "abs",]

# Each of the splits and other workouts grouped into their cycles
WORKOUTS = [
    [PUSH_PP, PULL_PP, PUSH_PP, PULL_PP, PUSH_PP, PULL_PP],
    # [PUSH, PULL, LEGS, PUSH, PULL, LEGS],
    # [FULLBODY, FULLBODY, FULLBODY, FULLBODY],
    # [BACK_BICEPS, CHEST_TRICEPS, SHOULDERS_ABS, LEGS],
    # [CARDIO_ABS]
]

WORKOUT_NAMES = [
    ["Push", "Pull", "Push", "Pull", "Push", "Pull"],
    ["Push", "Pull", "Legs", "Push", "Pull", "Legs"],
    ["FullBody", "FullBody", "FullBody", "FullBody"],
    ["Back and Biceps", "Chest And Triceps", "Shoulders and Abs", "Legs"],
    ["Cardio and Abs"]
]
# SET Sizes
WORKOUT_SET_SIZE = [3, 2, 3, 3, 1]
WORKOUT_SET_NUMBER = [3, 3, 3, 3, 6]

# What style workout 0=Superset, 1=Compound
# SuperSet => Each workout in a set is from a different muscle group
# Compound => Each workout in a set can be from the same muscle group
WORKOUT_STYLE = [0, 0, 0, 1, 1]
