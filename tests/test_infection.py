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

    def expect_infection_mapping(self, users, start_index, infected_indices, clean_indices):
        infect(users[start_index], self.new_version)
        self.assertInfected(users, infected_indices)
        self.assertNotInfected(users, clean_indices)

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
            users=self.us,
            start_index=0,
            infected_indices=[0],
            clean_indices=[1,2]
        )

    def test_coach_infects_learner(self):
        self.expect_infection_mapping(
            users=self.us,
            start_index=2,
            infected_indices=[2,1],
            clean_indices=[0]
        )

    def test_learner_infects_coaches(self):
        self.expect_infection_mapping(
            users=self.us,
            start_index=1,
            infected_indices=[1,2],
            clean_indices=[0]
        )


if __name__ == '__main__':
    unittest.main()
