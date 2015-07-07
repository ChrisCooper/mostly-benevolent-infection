import unittest
import fun

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
