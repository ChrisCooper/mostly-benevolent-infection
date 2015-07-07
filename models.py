import fun

class User:
    """
    A basic user with site version, email, and coaching relationships.

    Relationships are stored as sets.
    """
    def __init__(self):
        self.email = fun.cool_email()

        # Site version is a simple integer
        self.site_version = 1

        # The users that coach this user
        self.coach_set = set()

        # The users that are coached by this user
        self.learner_set = set()

    def add_coach(self, coach):
        """The coach argument becomes a coach of this user, and the coach's learner set is updated"""
        self.coach_set.add(coach)
        coach.learner_set.add(self)

