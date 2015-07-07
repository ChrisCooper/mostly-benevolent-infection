import unittest
import models

class TestUserModelBasics(unittest.TestCase):
    def setUp(self):
        self.u = models.User()

    def test_new_user_has_correct_values(self):
        self.assertTrue(len(self.u.email) > 0, msg='no email is set')
        self.assertEqual(self.u.site_version, 1)
        self.assertEqual(len(self.u.coach_set), 0)
        self.assertEqual(len(self.u.learner_set), 0)

    def test_coach_must_be_a_user(self):
        self.assertRaises(AttributeError, lambda: self.add_bad_coach(self.u))

    def add_bad_coach(self, user):
        user.add_coach('i\'m a board certified spanish tutor')

    def test_coach_relationship_works(self):
        c = models.User()
        self.u.add_coach(c)

        self.assertTrue(c in self.u.coach_set)
        self.assertTrue(self.u in c.learner_set)

    def test_site_versions_must_be_ints(self):
        self.assertRaises(TypeError, lambda: self.assign_bad_site_version(self.u))

    def assign_bad_site_version(self, user):
        user.site_version = 'bad'

if __name__ == '__main__':
    unittest.main()
