# The Neighbourhood
## Contributors
If you have any queries or suggestions, feel free to connect with me over email. moseskinyua12@gmail.com

## Author
Mugo Moses

## Description
The Neighbourhood is a web app that allows users to sign in, set user profile, find different businesses around the hood, find contact information for authorities and health facilities.The app alos allows user to create post that are visible to everyone in the hood and also one can view details of a single hood.


## Screenshots
<img src="" alt="">
<img src="" alt="">

## Setup and Installation
### Requirements
1. Clone the repository by running

        https://github.com/Moses-254-Mugo/The_Hood
    Navigate to the project

        cd The_Hood
 2. Create a virtual enviroment

         pip install virtualenv 

    To activate the created virtual environment, run

        source virtual/bin/activate
3. Create database
    You will need to create a new postgress database by typing the following command to access postgress

        $ psql

    Then run below query to create a new database named 

        # create databases dbHood;
5. Create Database migrations
    make migrations on postgres using django

        python3.8 manage.py makemigrations The_Hood
    then run the below command.

        python3.8 manage.py migrate

6. Run the app
    To run the application on your development machine,

        pythong3.8 manage.py runserver
### Running Tests
To run tests;

        python3.8 manage.py test


## Technologies Used
* Python3.8
* Django
* HTML
* Bootstrap
* CSS

## User Stories
1. Sign in with the application to start using.
2. Set up a profile about me and a general location and my neighborhood name.
3. Find a list of different businesses in my neighborhood.
4. Find Contact Information for the health department and Police authorities near my neighborhood.
5. Create Posts that will be visible to everyone in my neighborhood.
6. Change My neighborhood when I decide to move out.
7. Only view details of a single neighborhood.

## Support and contact details
If you have any questions, want to contribute to the code? Please email at
moseskinyua12@gmail.com

## License
The project is under[MIT License](LICENSE).