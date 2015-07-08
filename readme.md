Mostly-Benevolent Infection
===========================

Mostly-Benevolent Infection illustrates how one might spread new features to users of Khan Academy.

The main principle is to avoid giving different versions to users in the same classroom or with coaching relationships.
Infection is illustrated through a simple web interface displaying the graph of users. 
This is not really a robust or friendly application, but rather a simple visualization!

The project could also have been implemented more easily completely in JavaScript, but I decided to put the
infection logic in the server. Deciding when updates go out is best left to the people running the site.

Of course, real life would also be using Google Datastore, instead of in-memory processing!

Setting up
----------

In this guide, all commands are to be executed in the project root directory. 

This app has been tested with Python 2.7.6 on Ubuntu 14.04 and Python 2.7.5 on OS X 10.9.5.

    # Create a virtual-env for the app. Optional but recommended
    virtualenv env; source env/bin/activate
    
    # Install required packages
    pip install -r requirements.txt

If either of these commands fail because they're not installed, here are guides for
[pip](https://pip.pypa.io/en/latest/installing.html) and
[virtualenv](https://virtualenv.pypa.io/en/latest/installation.html)

Running tests
-------------

    nosetests


Running the app
-------------

    python main.py

The app should now be running at [http://127.0.0.1:5000/](http://127.0.0.1:5000/)


Limited infection
---------------

There are many approaches, but I took the greedy one, starting from a given user. The algorithm aims to minimize
outgoing edges from the infected partition by expanding to nodes of low partition-leaving degree and high
partition-internal degree first.


Reflections
-------------

Fun things to add with more time:

- user email shown on mouseover
- Some CSS for the page in general
 
Things that could use tweaking:

- Only one session at a time is supported (multiple tabs... not today!) via an ugly global variable
- The client-side JSX transformer is being used, and there's no compressing of JavaScript
- Tests don't extend to the web app section, or to limited_infect
- Limits on school and class sizes are not enforced
- I'm not familiar enough with how React re-renders to be braver in combining it withthe d3 postions. They're pretty
separate right now, but it's not that way
- Infection status is tested based on 1ness or 2ness or the site_version. Too much hard-coding
- The logic of the react interface state is a bit convoluted and could use some more design work
- The entire list of infected nodes is transmitted on each infection. Should probably just be a diff!

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