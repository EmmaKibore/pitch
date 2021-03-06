# Pitch
A web application that allows users to post pitches, comment and even vote on other pitches.

By Emma Kibore

## Description
This is a web application that allows various users to submit a short pitch. Users can also be able to view other pitches from different categories (Pick-up Lines, Interview Pitches, Product Pitches, Promotion Pitches), comment and vote. For a user to do any of that, they need to have registered.

## BDD
| Behaviour             |      Input       |                Output                               |
| :-------------        | :--------------- | :---------------------------------------------------|
| Display Various Pitch |      N/A         |Various pitches grouped by categories are displayed  |
| Categories            |                  |                                                     |
| :-------------------- | :--------------- | :---------------------------------------------------|
| Display pitches       | Click on a       | A page with a list of pitches from the selected     |
|                       | Category         |   category                                          |
| :-------------------- | :--------------- | :---------------------------------------------------|
| Add new pitch         | Click new pitch  |  User should sign in to add new pitch               |
| :-------------------- | :--------------- | :---------------------------------------------------|
| View Pitches          | Click on a pitch | View a pitch and comment                            |
| :-------------------- | :--------------- | :-------------------------------------------------- |
| Comment on a pitch    | Click Comment    | registered User displays a form where a user can    |
|                       |                  |     comment on a particular pitch                   |

## Prerequisites
* Python3.6

## Setup/Installation Requirements
* internet access
* $ git clone https://github.com/EmmaKibore/Pitch.git
* $ cd one-minute-pitch
* $ python3.6 -m venv virtual (install virtual environment)
* $ source virtual/bin/activate
* $ python3.6 -m pip install -r requirements.txt (install all dependencies)
* Inside the manage.py module change the config_name parameter from 'production' to 'developement' ie app = create_app('production') should be app = create_app('developement')
* $./start.sh

## Support and Contacts
In case of any issues or inquiries ,you can reach me through:
* Telephone: + (254) 702499205
* email: emmaKibore@gmail.com

## Known Bugs
No known Bugs

## Tecnologies Used
* Python3.6
* Flask framework
* Bootstrap
* PostgresSQL

## License
* MIT License

Copyright Emma Kibore
