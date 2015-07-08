"""
Graphs of user coaching relationships are generated here.

Both "classrooms" and "schools" are just lists of users. In a classroom, one
user has coaching relationships with all the others.
"""

import random
import itertools

from models import User

def new_school(avg_num_classes, variation_coeff, class_gen, extra_coaching_rate=0.06):
    """
    Creates a list of students from many classes. Some inter-class relationships can be formed
    :param avg_num_classes: average number of students
    :param variation_coeff: applies to the number of classrooms
        Variation_coeeff * avg_num_classes = standard deviation
    :param class_gen: a function for generating new classrooms
    :param extra_coaching_rate: controls how many students have another
        student coach outside their class
    :return: a list of `model.User`s
    """

    num_classes = int_from_bounded_distribution(avg_num_classes, variation_coeff)

    classrooms = (class_gen() for i in range(num_classes))

    # flatten the classes iterators so all users are in one list
    school = list(itertools.chain(*classrooms))

    add_random_coaches(school, extra_coaching_rate)

    return school


def new_classroom(avg_num_students, variation_coeff=0.4, extra_coaching_rate=0.15):
    """
    Creates a class of new students and a teach with coaching relationships already formed
    :param avg_num_students: average number of students
    :param variation_coeff: applies to the number of students.
        Variation_coeeff * avg_num_students = standard deviation
    :param extra_coaching_rate: controls how many students have another student coach
    :return: a list of `model.User`s
    """

    class_size = int_from_bounded_distribution(avg_num_students, variation_coeff)

    # Add the students and 1 teacher
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

def int_from_bounded_distribution(mean, variation_coeff, minimum=1):
    """
    Returns a number from a gaussian distribution using a variation coefficient instead
    of std deviation. Also caps to a minimum value.
    """
    val = int(random.gauss(mean, mean*variation_coeff))
    return max(val, minimum)
