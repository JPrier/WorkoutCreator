import exercises as ex
import random
import copy


##### Workout Creator #####
#
# This script creates workouts given muscle groups.
# Each workout is maxed to 3 super or circuit sets with 2-3 exercises each.
# Order of muscle groups is random for each variation.
# There is enough variations for all exercises to be covered in a single cycle.
#
# Workouts are written to a csv to be read easily in a spreadsheet.
#
##### --------------- #####

'''
TODO:
 - Set previous_muscle to a list of all previous muscles in the set
 - Need to fix recursive logic
    - Gets stuck on path of muscle groups that have no exercises

'''
def select_muscle_group(previous_muscle, workout, exercise_lists):
    # find the first non-empty muscle group
    if not exercise_lists or not workout:
        return None
    if previous_muscle:
        possible_groups = list(set(ex.SUPERSETS[previous_muscle]).intersection(workout).intersection(exercise_lists.keys()))
        if not possible_groups:
            return None
        random.shuffle(possible_groups)
        muscle_group = possible_groups[0]
    else:
        random.shuffle(workout)
        muscle_group = workout[0]
    if muscle_group in exercise_lists and exercise_lists[muscle_group]:
        workout.remove(muscle_group)
        return muscle_group
    else:
        exercise_lists = {k: v for k, v in exercise_lists.items() if v}
        exercise_lists.pop(muscle_group, None)
        return select_muscle_group(muscle_group, workout, exercise_lists)



for i in range(len(ex.WORKOUTS)):
    workout_cycle = ex.WORKOUTS[i]
    print("\nCYCLE: " + str(i))
    exercise_lists = copy.deepcopy(ex.EXERCISES)
    for j in range(len(workout_cycle)):
        workout = copy.deepcopy(workout_cycle[j])
        print("\n" + ex.WORKOUT_NAMES[i][j] + "\n--------------")

        for set_number in range(ex.WORKOUT_SET_NUMBER[i]):
            print("Set " + str(set_number+1) + ":")
            previous_muscle = ""
            if not workout:
                break
            for exercise_number in range(ex.WORKOUT_SET_SIZE[i]):
                random.shuffle(workout)
                muscle_group = select_muscle_group(previous_muscle, workout, exercise_lists)
                if not muscle_group:
                    break
                exercise = exercise_lists[muscle_group].pop()
                previous_muscle = muscle_group
                print(muscle_group + ": " + exercise)
        print("-----------")
