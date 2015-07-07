import fun

class User(object):
    """
    A basic user with site version, email, and coaching relationships.

    Relationships are stored as sets.
    """
    def __init__(self):
        self.email = fun.cool_email()

        # Site version is a simple integer
        self._site_version = 1

        # The users that coach this user
        self.coach_set = set()

        # The users that are coached by this user
        self.learner_set = set()

    def add_coach(self, coach):
        """The coach argument becomes a coach of this user, and the coach's learner set is updated"""
        self.coach_set.add(coach)
        coach.learner_set.add(self)

    def __repr__(self):
        return '<User "{email}" c{num_coaches} l{num_learners}>'.format(
            email=self.email,
            num_coaches=len(self.coach_set),
            num_learners=len(self.learner_set),
        )

    @property
    def site_version(self):
        """The version of the site that the user sees"""
        return self._site_version

    @site_version.setter
    def site_version(self, value):
        if not isinstance(value, int):
            raise TypeError('Site version must be an int')
        self._site_version = value
