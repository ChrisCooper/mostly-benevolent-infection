"""
The proper infection algorithms are implemented here.

This file is the best tested and the most robust.
"""

import models

def infect(user, new_site_version):

    if user is None:
        raise ValueError('User to infect cannot be None')

    if not isinstance(user, models.User):
        raise TypeError('User to infect must be a models.User instance')

    user.site_version = new_site_version