import unittest
import numpy
import fun
import graph_generation


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


class TestClassroomGeneration(unittest.TestCase):
    """
    These tests are rough and incomplete, since the spec is pretty flexible.
    Tests for the classrooms depend on randomness, so testing the distribution etc.
    is one way to make unit tests "work". Possibly overkill for this part of the
    program though.
    """

    def test_size_distribution(self):
        """
        This test may fail 1 out of 10,000 times because it tests a sample
        mean against a population
        """

        pop_avg = 100
        pop_std_dev = 10
        z_for_99_point_99_confidence = 3.8906
        n = 20

        classrooms = [
            graph_generation.new_classroom(
                avg_num_students=pop_avg,
                variation_coeff=pop_std_dev * 1.0 / pop_avg
            )
            for c in range(n)
            ]

        mean_users = numpy.mean([len(c) for c in classrooms])

        # We generate the 99.99% confidence interval for this sample mean
        max_distance = z_for_99_point_99_confidence * pop_std_dev / numpy.sqrt(n)

        self.assertTrue(numpy.abs(mean_users - pop_avg) < max_distance,
                        msg='classroom size exceeded expected bounds (may happen 1 out of 10,000 times)')

    def test_teacher_exists(self):
        n = 10
        classrooms = [
            graph_generation.new_classroom(
                avg_num_students=25,
                variation_coeff=0.1
            )
            for c in range(n)
            ]

        for c in classrooms:
            # Make sure there's at least one user with n-1 learners
            self.assertGreaterEqual(
                max(len(u.learner_set) for u in c),
                len(c) - 1,
                msg="no teacher found"
            )


if __name__ == '__main__':
    unittest.main()
