Mostly-Benevolent Infection
===========================

Mostly-Benevolent Infection illustrates how one might spread new features to users of Khan Academy.

The main principle is to avoid giving different versions to users in the same classroom or with coaching relationships.

In this guide, all commands are assumed to be executed in the project root directory. 

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


Reflections
-------------

Things that could use tweaking:

- Only one session at a time is supported (multiple tabs... not today!) via an ugly global variable
- The client-side JSX transformer is being used, and there's no compressing of JavaScript
- Tests don't extend to web app section

Extra Notes
-------------

Thanks to:

- [MomsWhoThink.com](http://www.momswhothink.com/) for the adjectives and adverbs lists
- [The United States Social Security Administration](http://www.ssa.gov) for the names list

The name generator gave these gems within the first 15 or 20 outputs. I am pleased:

- Malky.the.properly.scientific
- Janice.the.politely.aloof
- Adriel.the.unnecessarily.excited
- Myleigh.the.questioningly.demonic
- Christina.the.seldom.interesting