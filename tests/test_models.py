import unittest
import models

class TestUserModelBasics(unittest.TestCase):
    def test_new_user_has_correct_values(self):
        u = models.User()
        self.assertTrue(len(u.email) > 0, msg='no email is set')
        self.assertEqual(u.site_version, 1)
        self.assertEqual(len(u.coach_set), 0)
        self.assertEqual(len(u.learner_set), 0)

    def test_coach_relationship_works(self):
        u = models.User()
        c = models.User()
        u.add_coach(c)

        self.assertTrue(c in u.coach_set)
        self.assertTrue(u in c.learner_set)

    def test_site_versions_must_be_ints(self):
        u = models.User()

        self.assertRaises(TypeError, lambda: self.assign_bad_site_version(u))

    def assign_bad_site_version(self, user):
        user.site_version = 'bad'

if __name__ == '__main__':
    unittest.main()
