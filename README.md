# SEGA MASTER SYSTEM GAME REVIEW APP

This is my first backend project. I decieded to make an app that allows the user to make a review of their Sega Master System Console Games and allows them to see the reviews made by others. Once logged in the user can create, read, edit or delete their personal reviews.
The Theme was chosen as the sega master system was the 2nd console I owned and I thought it would be fun to develop an app that would allow me to store data about what I thought of the games that I had played and share them with others. Its intended target is for anyone that would like to make a review about the Sega games they have played and would be useful to user as they can give a rating and a review for personal use or to share.

![screenshot](documentation/images/responsive.png)

## UX

### Colour Scheme

- `#000000` used for primary text.

I used [coolors.co](https://coolors.co/000000-dd0707-ffffff-3b82f6) to generate my colour palette. I decieded on the black and white colours as they matched the colour of the console.

![screenshot](documentation/images/pallete.png)

I used different coloured buttons on different coloured backgrounds for good contrast using a colours from the palette.

![screenshot](documentation/images/red-button.png)

![screenshot](documentation/images/red-black-button.png)

![screenshot](documentation/images/blue-button.png)


### Typography

- [Special Elite](https://fonts.google.com/specimen/Special+Elite) was used for the body text

- [Bungee Inline](https://fonts.google.com/specimen/Bungee) was used for all other secondary text.

- [Font Awesome](https://fontawesome.com) icons were used throughout the site, such as the icons on the username and password fields.

- [Tailwind Elements](https://tailwind-elements.com/docs/standard/navigation/footer/) svg footer icons were provided with a footer template and then styles applied to match the theme of my app from the 'Buttons dark theme'.


## User Stories

### New Site Users

- As a new site user, I would like to be able to register for an account with a username and password.
- As a new site user, I would like to be able to log in with my username and password, so that I can access my account.
- As a new site user, I would like to be able to log out of my account.
- As a new site user, I would like to be able to see my profile page, so that I can quickly see the reviews I have made.
- As a new site user, I would like to be able to make a review/s of master system games.
- As a new site user, I would like to be able to see my game review/s, so that I can edit them.
- As a new site user, I would like to be able to see my game reviews/s, so that I can delete them.
- As a new site user, I would like to be able to change my author name, so that it appears on all of my reviews.
- As a new site user, I would like to be able to see other users reviews on the site.

### Returning Site Users

- As a returning site user, I would like to be able to login back to my account.
- As a returning site user, I would like to be able to see the reviews that I made the last time a was on the site.

### Site Admin

Please see future improvements section.

## Wireframes

To follow best practice, wireframes were developed for mobile, tablet, and desktop sizes.
I've used [Figma](https://figma.com) to design my site wireframes.

<details><summary>Homepage</summary>
<img src="documentation/wireframes/mobile/mb-homepage.png">
<img src="documentation/wireframes/tablet/tab-homepage.png">
<img src="documentation/wireframes/desktop/desk-homepage.png">
</details>

<details><summary>About</summary>
<img src="documentation/wireframes/mobile/mb-about.png">
<img src="documentation/wireframes/tablet/tab-about.png">
<img src="documentation/wireframes/desktop/desk-about.png">
</details>

<details><summary>Reviews</summary>
<img src="documentation/wireframes/mobile/mb-reviews.png">
<img src="documentation/wireframes/tablet/tab-reviews.png">
<img src="documentation/wireframes/desktop/desk-reviews.png">
</details>

<details><summary>Register</summary>
<img src="documentation/wireframes/mobile/mb-register.png">
<img src="documentation/wireframes/tablet/tab-register.png">
<img src="documentation/wireframes/desktop/desk-register.png">
</details>

<details><summary>Login</summary>
<img src="documentation/wireframes/mobile/mb-login.png">
<img src="documentation/wireframes/tablet/tab-login.png">
<img src="documentation/wireframes/desktop/desk-login.png">
</details>

<details><summary>Profile</summary>
<img src="documentation/wireframes/mobile/mb-profile.png">
<img src="documentation/wireframes/tablet/tab-profile.png">
<img src="documentation/wireframes/desktop/desk-profile.png">
</details>

<details><summary>Add Review</summary>
<img src="documentation/wireframes/mobile/mb-add-review.png">
<img src="documentation/wireframes/tablet/tab-add-review.png">
<img src="documentation/wireframes/desktop/desk-add-review.png">
</details>

<details><summary>Manage Review</summary>
<img src="documentation/wireframes/mobile/mb-manage.png">
<img src="documentation/wireframes/tablet/tab-manage.png">
<img src="documentation/wireframes/desktop/desk-manage.png">
</details>

<details><summary>Edit Review</summary>
<img src="documentation/wireframes/mobile/mb-edit.png">
<img src="documentation/wireframes/tablet/tab-edit.png">
<img src="documentation/wireframes/desktop/desk-edit.png">
</details>


## Features


### Existing Features

- **Register As New User**

    - A new user can register on the site for an account with a username and password. The username must include 1 uppercase letter, 1 number, no whitespaces and be 8-16 characters long. The password must include 1 uppercase letter, 1 lowercase letter, 1 number, 1 special character, no whitespaces and be 8-16 characters long. The password is hashed using werkzeug for security.

![screenshot](documentation/screenshots/register.png)

- **Login**

    - A returning user can log back in using their username and password. 

![screenshot](documentation/screenshots/register.png)

- **Add Review**

    - The user can fill out the form and add a review. They can choose a game and a game genre from a dropdown and search for each in the search field.

![screenshot](documentation/screenshots/add-review.png)
![screenshot](documentation/screenshots/game-name.png)
![screenshot](documentation/screenshots/game-genre.png)

- **Edit Review**

    - Details about this particular feature, including the value to the site, and benefit for the user. Be as detailed as possible!

![screenshot](documentation/screenshots/edit-button.png)

- **Delete Review**

    - The user can delete a review by clicking or pressing the delete button. This will remove it from the app and wont be shown anymore on the reviews page and the database.

![screenshot](documentation/screenshots/delete-button.png)

- **Number Of Reviews Listed and Game Names**

    - When the user adds reviews on the profile page the number of reviews and the game names appear for the games reviews they have added.

![screenshot](documentation/screenshots/games-added.png)

- **Star Rating**

    - The site allows the user to add a star rating from 1-10 to their review by clicking a radio button.

![screenshot](documentation/screenshots/star-rating.png)

- **Change Review Author To Be Displayed On All Users Reviews**

    - On the profile page the user can change their author name which will update on all of their reviews. this will not appear if they have not added any reviews.

![screenshot](documentation/screenshots/change-author.png)

- **Display an image and a button to add a review if no reviews have been made**

    - If no reviews have been made an image, text and a button linking to the add review page is visible to the user.

![screenshot](documentation/screenshots/no-reviews.png)

- **Pull data from reviews and show in forms when editing**

    - When a user wants to edit a review the app pulls the review data into the new form so that they can edit it. Currently this feature does not pull accross star rating and game genre.

![screenshot](documentation/screenshots/edit-form.png)

- **Any user can read reviews that users have made**

    - Reviews.html is where all current reviews in the database are rendered for anyone to read.

![screenshot](documentation/screenshots/review-page.png)


### Future Features

- Sudo User
    - To have the ability as a sudo user to create, edit or delete a review on the frontend app by logging in with sudo login and password
- To Add Images
    - To allow the user to add images to the reviews, or scrape images from a source like Wikipedia so that when a game name is selected the appropriate game image is displayed in the review. Or a combination of both.
- To Stop Users From Submitting A Blank Game Name Or Game Genre
    - To add a warning or not allow the form to be submitted if these are not selected
- To Import The Json Data To My MongoDB Database
	- This would futureproof any changes and keep alll data in the backend
- To Give Each Data Set Its Own ID and Catagory Table
	- This would allow me to make future updates once to data sets and not have to change data for each individual users review to make site wide changes. This would mean that the the app is more scalable and manageable.
- To store the star rating so that when a form/review is edited the user doesnt have to give it a star rating again
- To store the game genre so that when a form/review is edited the user doesnt have to select a genre again.
- To have a publish/unpublish button on the edit reviw page so that the user can deciede if they want their review to be published live.

## Tools & Technologies Used

- [HTML](https://en.wikipedia.org/wiki/HTML) used for the main site content.
- [CSS](https://en.wikipedia.org/wiki/CSS) used for the main site design and layout.
- [JavaScript](https://www.javascript.com) used for user interaction on the site.
- [Python](https://www.python.org) used as the back-end programming language.
- [Git](https://git-scm.com) used for version control. (`git add`, `git commit`, `git push`)
- [GitHub](https://github.com) used for secure online code storage.
- [GitHub Pages](https://pages.github.com) used for hosting the deployed front-end site.
- [Gitpod](https://gitpod.io) used as a cloud-based IDE for development.
- [Flask](https://flask.palletsprojects.com) used as the Python framework for the site.
- [MongoDB](https://www.mongodb.com) used as the non-relational database management with Flask.
- [Heroku](https://www.heroku.com) used for hosting the deployed back-end site.
- [Tailwind](https://www.tailwindcss.com) used as a css framework to build the frontend.
- [Tailwind Elements](https://www.tailwind-elements.com) Open source UI kit.



## Database Design

![screenshot](documentation/database/mongodb.png)


## Testing

For all testing, please refer to the [TESTING.md](TESTING.md) file.

## Deployment

The live deployed application can be found deployed on [Heroku](https://game-review-milestone-3.herokuapp.com).

### Heroku Deployment

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

- Select **New** in the top-right corner of your Heroku Dashboard, and select **Create new app** from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), and finally, select **Create App**.
- From the new app **Settings**, click **Reveal Config Vars**, and set your environment variables.

| Key | Value |
| --- | --- |
| `SECRET_KEY` | user's own value |


Heroku needs two additional files in order to deploy properly.
- requirements.txt
- Procfile

You can install this project's **requirements** (where applicable) using:
- `pip3 install -r requirements.txt`

If you have your own packages that have been installed, then the requirements file needs updated using:
- `pip3 freeze --local > requirements.txt`

The **Procfile** can be created with the following command:
- `echo web: gunicorn app_name.wsgi > Procfile`
- *replace **app_name** with the name of your primary Django app name; the folder where settings.py is located*

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

Either:
- Select **Automatic Deployment** from the Heroku app.

Or:
- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a app_name` (replace *app_name* with your app name)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type:
	- `git push heroku main`

The project should now be connected and deployed to Heroku!

### Local Deployment

This project can be cloned or forked in order to make a local copy on your own system.

For either method, you will need to install any applicable packages found within the *requirements.txt* file.
- `pip3 install -r requirements.txt`.

You will need to create a new file called `env.py` at the root-level,
and include the same environment variables listed above from the Heroku deployment steps.

Sample `env.py` file:

```python
import os

os.environ.setdefault("DATABASE_URL", "user's own value")
os.environ.setdefault("SECRET_KEY", "user's own value")
os.environ.setdefault("DEBUG", "True")
```

Once the project is cloned or forked, in order to run it locally, you'll need to follow these steps:
- Start the Django app: `python3 manage.py runserver`
- Stop the app once it's loaded: `CTRL+C` or `⌘+C` (Mac)
- Make any necessary migrations: `python3 manage.py makemigrations`
- Migrate the data to the database: `python3 manage.py migrate`
- Create a superuser: `python3 manage.py createsuperuser`
- Load fixtures (if applicable): `python3 manage.py loaddata file-name.json` (repeat for each file)
- Everything should be ready now, so run the Django app again: `python3 manage.py runserver`

If you'd like to backup your database models, use the following command for each model you'd like to create a fixture for:
- `python3 manage.py dumpdata your-model > your-model.json`
- *repeat this action for each model you wish to backup*

#### Cloning

You can clone the repository by following these steps:

1. Go to the [GitHub repository](https://github.com/MJstephenson/game-reviews) 
2. Locate the Code button above the list of files and click it 
3. Select if you prefer to clone using HTTPS, SSH, or GitHub CLI and click the copy button to copy the URL to your clipboard
4. Open Git Bash or Terminal
5. Change the current working directory to the one where you want the cloned directory
6. In your IDE Terminal, type the following command to clone my repository:
	- `git clone https://github.com/MJstephenson/game-reviews.git`
7. Press Enter to create your local clone.

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/MJstephenson/game-reviews)

Please note that in order to directly open the project in Gitpod, you need to have the browser extension installed.
A tutorial on how to do that can be found [here](https://www.gitpod.io/docs/configure/user-settings/browser-extension).

#### Forking

By forking the GitHub Repository, we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository.
You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/MJstephenson/game-reviews)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!

### Local VS Deployment

There are no differences between the local site and the live deployment site on Heroku.


## Credits

### Content

| Source | Location | Notes |
| --- | --- | --- |
| [Tailwind elements](https://tailwind-elements.com/docs/standard/navigation/navbar/) | navbar | responsive navbar |
| [Tailwind Elements](https://tailwind-elements.com/docs/standard/forms/inputs/#floating) | forms | helper inputs with labels |
| [Tailwind Elements](https://tailwind-elements.com/docs/standard/navigation/footer/) | footer | footer site wide |
| [Geeksforgeeks](https://www.geeksforgeeks.org/read-json-file-using-python/) | import json file  | for forms |
| [TTL255](https://ttl255.com/jinja2-tutorial-part-2-loops-and-conditionals/#:~:text=For%20loops%20start%20with%20%7B%25,we%20go%20over%20the%20elements.) | jinga inline for loops  | for applying styles inline |
| [Elbriga14](https://github.com/Elbriga14/EveryVideoGameEver/blob/main/GamesDB/MasterSystemGames.json) | json file | master system games data |
| [W3 Schools](https://www.w3schools.com/python/default.asp) | python resources | for python syntax and methods |
| [Scaler Topics](https://www.scaler.com/topics/convert-string-to-int-python/) | intergers | convert string to interger |
| [Real Python](https://realpython.com/primer-on-jinja-templating/) | Jinga Loops | for explaining jinga loops and else if statements |
| [Codemy](https://www.youtube.com/watch?v=8ebIEefhBpM) | Werkzeug hash | for explaining wekzeug password hash |
| [Eyehunts](https://tutorial.eyehunts.com/js/javascript-confirm-delete-before-delete-code/) | alert popup | to confirm delete |


### Media

| Source | Location | Type | Notes |
| --- | --- | --- | --- |
| [Wikimedia commons](https://commons.wikimedia.org/wiki/File:Sega-Master-System-Controllers.jpg) | about page | image | background image |
| [Pxfuel](https://www.pxfuel.com/en/desktop-wallpaper-julyh) | landing page | image | background image |
| [Fav Png](https://favpng.com/png_view/sonic-the-hedgehog-photos-sonic-the-hedgehog-3-sonic-sega-all-stars-racing-sonic-the-hedgehog-2-knuckles-the-echidna-png/jVXX1q86) | Log in, profile pages | image | background images|
| [Fav Png](https://favpng.com/png_view/sonic-the-hedgehog-2-sonic-generations-doctor-eggman-xbox-360-png/gdLEsjn5) | register page | image | background image |
| [Retro Video Gaming](https://retro-video-gaming.com/2012/07/15/captain-silver-for-sega-master-system/) | about page | image | games image |
| [Retro Otaku](https://www.retro-otaku.com/2009/09/gaming-sessions-24-january-2009/) | No Reviews | image | background image for no reviews |

### Acknowledgements

- I would like to thank my partner Lucy, for believing in me, and allowing me to make this transition into software development.

