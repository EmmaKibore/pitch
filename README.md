# Pitch
A web application that allows users to post pitches, comment and even vote on other pitches.

By Emma Kibore

## Description
This is a web application that allows various users to submit a short pitch. Users can also be able to view other pitches from different categories (Pick-up Lines, Interview Pitches, Product Pitches, Promotion Pitches), comment and vote. For a user to do any of that, they need to have registered.

## Prerequisites
* Python3.6

## Setup/Installation Requirements
* internet access
* $ git clone https://github.com/kepha-okari/one-minute-pitch.git
* $ cd one-minute-pitch
* $ python3.6 -m venv virtual (install virtual environment)
* $ source virtual/bin/activate
* $ python3.6 -m pip install -r requirements.txt (install all dependencies)
* Inside the manage.py module change the config_name parameter from 'production' to 'developement' ie app = create_app('production') should be app = create_app('developement')
* $./start.sh
