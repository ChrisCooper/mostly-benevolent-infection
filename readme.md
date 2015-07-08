Mostly-Benevolent Infection
===========================

Mostly-Benevolent Infection illustrates how one might spread new features to users of Khan Academy.

The main principle is to avoid giving different versions to users in the same classroom or with coaching relationships.

In this guide, all commands are assumed to be executed in the project root directory

Setting up
----------

This app has been tested with Python 2.7.6.

    # Create a virtual-env for the app. Optional but recommended
    virtualenv env; source env/bin/activate
    
    # Install required packages
    pip install -r requirements.txt


Running tests
-------------

    nosetests


Running the app
-------------

    python main.py

The app should now be running at [http://127.0.0.1:5000/](http://127.0.0.1:5000/)