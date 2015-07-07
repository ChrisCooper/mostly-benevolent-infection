import unittest
import fun
import models

class TestUserModel(unittest.TestCase):
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

class TestFunEmails(unittest.TestCase):
    def test_format_is_consistent(self):
        for i in range(10):
            email = fun.cool_email()
            self.assertRegexpMatches(email, r'\S+\.the.\S+\.\S+@example.com')

    def test_emails_are_unique(self):
        num_trials = 100
        emails_set = set()

        for i in range(num_trials):
            emails_set.add(fun.cool_email())

        self.assertEqual(len(emails_set), num_trials, msg="emails were not unique")


if __name__ == '__main__':
    unittest.main()
