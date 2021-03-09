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
 - Look into CSP
   - https://en.wikipedia.org/wiki/Constraint_satisfaction_problem
   - https://www.cs.ubc.ca/~mack/CS322/lectures/3-CSP4.pdf
   - https://www.cs.cmu.edu/afs/cs/academic/class/15381-s07/www/slides/020107CSP.pdf
 - Write result to CSV
'''


def CSP(workouts, exercises):
    '''
    TODO:
    Depth first search through combinations of exercises in sets in splits

    Start by assigning exercise 1 in set 1 in workout 1
        - then remove all possible exercises for other exercises in sets in workouts
            - remove the exercise from possible exercises
            - remove the muscle group from the possible muscle groups of the current set

    Continue until either all exercises are filled or no possible exercises are left
        - if no possible exercise is left
            - if the current workout split is the max # of exercises seen then save
                - can be updated to be a few metrics rather than just # of EXERCISES
            - then backtrack to the previous level, ignore the last selection and pick another



    === Graph ===
    This method looks at the problem as a graph problem, the exercises are nodes
    and the lines can be constraints. Issue with this is choosing which constraint
    to connect on.

    https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/
    https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/tutorial/

    Exercises can be seen as points on a graph, sets and workouts will be constraints
    on the exercises.


    === Tree ===
    This method looks at the workouts as a tree. Each leaf can be an exercise,
    the parent of the leaves (exercises) are the sets, and the parents of the sets
    are the workouts, and the parent of the workout is the root (cycle).

    https://www.geeksforgeeks.org/dfs-traversal-of-a-tree-using-recursion/

    This representation method of the data seems the best, it allows for the best
    traversal method in terms of DFS and applying constraints.

    Implementation:
        Use the PostOrder method to look at leaves before looking at the root.

        PseduoCode:
            def DFS(node):
                if node is a list
                    workout = []
                    for item in node:
                        workout.append(DFS(item))
                    return workout
                else:
                    if possible_groups and possible_exercises not empty
                        group = random(possible_groups)
                        return random(possible_exercises)
                    else:
                        return nil

        Issues:
            - How do we check/change the possible groups
            - Current constant method does not work for the leaves of the tree
                - each exercise should have a list of groups associated with it

    ============

    Data = Cycle [Full1 [Set1 [ex1, ex2, ex3], Set2 [ex1, ex2, ex3], Set3 [ex1, ex2, ex3]], Full2 [ ], Full3 [ ] ]
    '''





def select_muscle_group(current_set_muscles, workout, exercise_lists):
    # find the first non-empty muscle group
    if not exercise_lists or not workout:
        return None
    if current_set_muscles:
        possible_groups = []
        # add all possible muscle groups to get exercises from
        for previous_muscle in current_set_muscles:
            possible_groups = possible_groups + list(
                    set(ex.SUPERSETS[previous_muscle])
                        .intersection(workout)
                        .intersection(exercise_lists.keys())
                    )
        # remove muscle groups already in set
        possible_groups = list(set(possible_groups) - set(current_set_muscles))
        # Remove muscle groups that are not compatible with muscle groups already in set
        for previous_muscle in current_set_muscles:
            possible_groups = list(
                                set(ex.SUPERSETS[previous_muscle])
                                .intersection(possible_groups)
                              )
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
        current_set_muscles.append(muscle_group)
        return select_muscle_group(current_set_muscles, workout, exercise_lists)



for i in range(len(ex.WORKOUTS)):
    workout_cycle = ex.WORKOUTS[i]
    print("\nCYCLE: " + str(i))
    exercise_lists = copy.deepcopy(ex.EXERCISES)
    for j in range(len(workout_cycle)):
        workout = copy.deepcopy(workout_cycle[j])
        print("\n" + ex.WORKOUT_NAMES[i][j] + "\n--------------")

        for set_number in range(ex.WORKOUT_SET_NUMBER[i]):
            print("Set " + str(set_number+1) + ":")
            current_set_muscles = []
            if not workout:
                break
            for exercise_number in range(ex.WORKOUT_SET_SIZE[i]):
                random.shuffle(workout)
                muscle_group = select_muscle_group(current_set_muscles, workout, exercise_lists)
                if not muscle_group:
                    break
                exercise = exercise_lists[muscle_group].pop()
                current_set_muscles.append(muscle_group)
                print(muscle_group + ": " + exercise)
        print("-----------")
