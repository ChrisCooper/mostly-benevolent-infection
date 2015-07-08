import unittest
from infection import infect
from models import User


class TestInfectionErrors(unittest.TestCase):
    def test_user_must_be_valid(self):
        self.assertRaises(ValueError, lambda: infect(None, 2))
        self.assertRaises(TypeError, lambda: infect('jokester user', 2))


class InfectionTestCase(unittest.TestCase):
    """This class adds methods to make testing infection cases much easier."""

    new_version = 2

    def expect_infection_mapping(self, users, start, infected, clean):
        infect(users[start], self.new_version)
        self.assertInfected(users, infected)
        self.assertNotInfected(users, clean)

    def assertInfected(self, user_list, indices):
        for i in indices:
            self.assertEqual(
                user_list[i].site_version, self.new_version,
                msg='user {0} not infected as expected'.format(i)
            )

    def assertNotInfected(self, user_list, indices):
        for i in indices:
            self.assertEqual(
                user_list[i].site_version, 1,
                msg='user {0} unexpectedly infected'.format(i)
            )


class TestInfectionSimpleCases(InfectionTestCase):
    def setUp(self):
        """Add one lone user, and two users with a one-way coaching relationship"""
        self.us = [User() for i in range(3)]
        self.us[1].add_coach(self.us[2])

    def test_lone_user_infects_no_one(self):
        self.expect_infection_mapping(
            self.us,
            start=0,
            infected=[0],
            clean=[1, 2]
        )

    def test_coach_infects_learner(self):
        self.expect_infection_mapping(
            self.us,
            start=2,
            infected=[2, 1],
            clean=[0]
        )

    def test_learner_infects_coaches(self):
        self.expect_infection_mapping(
            self.us,
            start=1,
            infected=[1, 2],
            clean=[0]
        )


class TestInfectionComplexCases(InfectionTestCase):
    def setUp(self):
        """A loop and a long line with some lonely items"""
        self.us = [User() for i in range(14)]

        links = [
            (1, 2), (4, 1), (2, 3), (3, 4), (1, 13), (13, 3),  # loop
            (5, 6), (7, 6), (7, 8), (9, 8), (9, 10),  # line
            (11, 12)  # lonely
        ]

        for coach, learner in links:
            self.us[learner].add_coach(self.us[coach])

    def test_loop_infected_safely(self):
        loop_indices = [1, 2, 3, 4, 13]

        for i in loop_indices:
            self.expect_infection_mapping(
                self.us,
                start=i,
                infected=loop_indices,
                clean=[0, 5, 6, 7, 8, 9, 10, 11, 12]
            )

    def test_linear_infection(self):
        line_indices = [5, 6, 7, 8, 9, 10]

        for i in line_indices:
            self.expect_infection_mapping(
                self.us,
                start=i,
                infected=line_indices,
                clean=[0, 1, 2, 3, 4, 11, 12, 13]
            )

    def test_complex_connected_case(self):
        # connect the loop and the line randomly
        self.us[4].add_coach(self.us[6])

        indices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 13]

        for i in indices:
            self.expect_infection_mapping(
                self.us,
                start=i,
                infected=indices,
                clean=[0, 11, 12]
            )


if __name__ == '__main__':
    unittest.main()
