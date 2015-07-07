"""
Graphs of user coaching relationships are generated here.

Both "classrooms" and "schools" are just lists of users. In a classroom, one
user has coaching relationships with all the others.
"""

import random

from models import User


def new_classroom(avg_num_students, variation_coeff, extra_coaching_rate=0.15):
    """
    Creates a class of new students and a teach with coaching relationships already formed
    :param avg_num_students: average number of students
    :param variation_coeff: applies to the number of students.
        Variation_coeeff * avg_num_students = standard deviation
    :param extra_coaching_rate: controls how many students have another student coach
    :return: a list of `model.User`s
    """

    class_size = int(random.gauss(avg_num_students, avg_num_students * variation_coeff))

    # Add the teacher and students
    class_list = [User() for i in range(class_size + 1)]

    teacher = class_list[-1]

    for student in class_list:
        if student is not teacher:
            student.add_coach(teacher)

    add_random_coaches(class_list, extra_coaching_rate)

    return class_list


def add_random_coaches(population, rate):
    """
    Given a population of users, adds random coaching relationships at the specified rate
    """
    for user in population:
        other_user = random.choice(population)
        if random.uniform(0, 1) < rate and user is not other_user:
            user.add_coach(other_user)