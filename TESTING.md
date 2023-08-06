# Testing

Return back to the [README.md](README.md) file.


### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.
I have ignored the warnings for trailing slashes.

| Page | W3C URL | Screenshot | Notes |
| --- | --- | --- | --- |
| Home |  ![screenshot](documentation/testing/validation/home-html.png) | pass |
| About | ![screenshot](documentation/testing/validation/about-html.png) | pass |
| Reviews | ![screenshot](documentation/testing/validation/reviews-html.png) | pass |
| Register |  ![screenshot](documentation/testing/validation/register-html.png) | pass |
| Login | ![screenshot](documentation/testing/validation/login-html.png) | pass |
| Add Review | ![screenshot](documentation/testing/validation/add-review-html.png) | pass |
| Manage Review |  ![screenshot](documentation/testing/validation/manage-reviews-html.png) | pass |
| Edit Review | ![screenshot](documentation/testing/validation/edit-review-html.png) |  The value of the for attribute of the label element must be the ID of a non-hidden form control. Duplicate ID star_rating as the star rating is iterated over and therefore shows an error |
| Profile | ![screenshot](documentation/testing/validation/profile-html.png) | Pass |


### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.


| File | Screenshot | Notes |
| --- | --- | --- |
| style.css | ![screenshot](documentation/testing/validation/css.png) | Pass: No Errors |


### JavaScript

I have used the recommended [JShint Validator](https://jshint.com) to validate all of my JS files.

| File | Screenshot | Notes |
| --- | --- | --- |
| script.js | ![screenshot](documentation/testing/validation/jshint.png) | One unused variable from external file |


### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

![screenshot](documentation/testing/validation/python.png)


## Browser Compatibility

I have tested my deployed project on multiple browsers to check for compatibility issues. As a developer I am using Linux Ubuntu so I am not able to test Microsoft Edge or Safari browsers on my machine.

| Browser | Screenshot | Notes |
| --- | --- | --- |
| Chrome | ![screenshot](documentation/testing/screenshots/browser-compatability/chrome-test.png) | Works as expected |
| Firefox | ![screenshot](documentation/testing/screenshots/browser-compatability/firefox-test.png) | Works as expected |
| Brave | ![screenshot](documentation/testing/screenshots/browser-compatability/brave-test.png) | Works as expected |
| Opera | ![screenshot](documentation/testing/screenshots/browser-compatability/opera-test.png) | Works as expected |


## Responsiveness

I have tested my deployed project on multiple devices to check for responsiveness issues. I have tested all pages and they work as expected. Below are screenshots of the homepage on various devices.

| Device | Screenshot | Notes |
| --- | --- | --- |
| Mobile (DevTools) | ![screenshot](documentation/testing/screenshots/responsiveness/mobile-test.png) | Works as expected |
| Tablet (DevTools) | ![screenshot](documentation/testing/screenshots/responsiveness/tablet-test.png) | Works as expected |
| Desktop | ![screenshot](documentation/testing/screenshots/responsiveness/desktop-test-test.png) | Works as expected |
| XL Monitor | ![screenshot](documentation/testing/screenshots/responsiveness/xlmonitor-test.png) | Works as expected |
| Doogee N40 Pro | ![screenshot](documentation/testing/screenshots/responsiveness/n40-pro.png) | Navbar becomes gray |
| iPhone X | ![screenshot](documentation/testing/screenshots/responsiveness/iphone-x.png) | Navbar becomes gray |


## Lighthouse Audit

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues. I would have tested the herouku live app but I ran into this error so I tested on my local app.

![screenshot](documentation/testing/screenshots/lighthouse/lighthouse-error.png)

| Page | Size | Screenshot | Notes |
| --- | --- | --- | --- |
| Home | Mobile | ![screenshot](documentation/testing/screenshots/lighthouse/home-mobile.png) | warning on explicit image sizes |
| Home | Desktop | ![screenshot](documentation/testing/screenshots/lighthouse/home-desktop.png) | minor warnings |
| About | Mobile | ![screenshot](documentation/testing/screenshots/lighthouse/about-mobile.png) | warning on explicit image sizes |
| About | Desktop | ![screenshot](documentation/testing/screenshots/lighthouse/about-desktop.png) | minor warnings |
| Reviews | Mobile | ![screenshot](documentation/testing/screenshots/lighthouse/reviews-mobile.png) | tailwind css |
| Reviews | Desktop | ![screenshot](documentation/testing/screenshots/lighthouse/reviews-desktop.png) | minor warnings |
| Register | Mobile | ![screenshot](documentation/testing/screenshots/lighthouse/register-mobile.png) | warning on explicit image sizes |
| Register | Desktop | ![screenshot](documentation/testing/screenshots/lighthouse/register-desktop.png) | minor warnings |
| Log in | Mobile | ![screenshot](documentation/testing/screenshots/lighthouse/login-mobile.png) | reduce unused javascript |
| Log in | Desktop | ![screenshot](documentation/testing/screenshots/lighthouse/login-desktop.png) | minor warnings |
| Profile | Mobile | ![screenshot](documentation/testing/screenshots/lighthouse/profile-mobile.png) | reduce unused javascript |
| Profile | Desktop | ![screenshot](documentation/testing/screenshots/lighthouse/profile-desktop.png) | minor warnings |
| Manage reviews | Mobile | ![screenshot](documentation/testing/screenshots/lighthouse/manage-reviews-mobile.png) | reduce unused javascript |
| Manage reviews | Desktop | ![screenshot](documentation/testing/screenshots/lighthouse/manage-reviews-desktop.png) | minor warnings |
| Add Review | Mobile | ![screenshot](documentation/testing/screenshots/lighthouse/add-review-mobile.png) | aria id's button contrast, unused javascript |
| Add Review | Desktop | ![screenshot](documentation/testing/screenshots/lighthouse/add-review-desktop.png) | minor warnings, aria id's button contrast |
| Edit review | Mobile | ![screenshot](documentation/testing/screenshots/lighthouse/edit-review-mobile.png) | warning on explicit image sizes layput shift and aria labels |
| Edit review | Desktop | ![screenshot](documentation/testing/screenshots/lighthouse/edit-review-desktop.png) | warning on explicit image sizes layput shift and aria labels |


## Defensive Programming

⚠️⚠️⚠️⚠️⚠️ START OF NOTES (to be deleted) ⚠️⚠️⚠️⚠️⚠️

Defensive programming (defensive design) is extremely important!

When building projects that accept user inputs or forms, you should always test the level of security for each.
Examples of this could include (not limited to):

Forms:
- Users cannot submit an empty form

PP3 (Python-only):
- Users must enter a valid letter/word/string when prompted
- Users must choose from a specific list only

Flask:
- Users cannot brute-force a URL to navigate to a restricted page
- Users cannot perform CRUD functionality while logged-out
- User-A should not be able to manipulate data belonging to User-B, or vice versa
- Non-Authenticated users should not be able to access pages that require authentication


You'll want to test all functionality on your application, whether it's a standard form,
or uses CRUD functionality for data manipulation on a database.
Make sure to include the `required` attribute on any form-fields that should be mandatory.
Try to access various pages on your site as different user types (User-A, User-B, guest user, admin, superuser).

You should include any manual tests performed, and the expected results/outcome.

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

Defensive programming was manually tested with the below user acceptance testing:

| Page | User Action | Expected Result | Pass/Fail | Comments |
| --- | --- | --- | --- | --- |
| Home Page | | | | |
| | Click on Logo | Redirection to Home page | Pass | |
| | Click on Home link in navbar | Redirection to Home page | Pass | |
| Gallery Page | | | | |
| | Click on Gallery link in navbar | Redirection to Gallery page | Pass | |
| | Load gallery images | All images load as expected | Pass | |
| Contact Page | | | | |
| | Click on Contact link in navbar | Redirection to Contact page | Pass | |
| | Enter first/last name | Field will accept freeform text | Pass | |
| | Enter valid email address | Field will only accept email address format | Pass | |
| | Enter message in textarea | Field will accept freeform text | Pass | |
| | Click the Submit button | Redirects user to form-dump | Pass | User must click 'Back' button to return |
| Sign Up | | | | |
| | Click on Sign Up button | Redirection to Sign Up page | Pass | |
| | Enter valid email address | Field will only accept email address format | Pass | |
| | Enter valid password (twice) | Field will only accept password format | Pass | |
| | Click on Sign Up button | Asks user to confirm email page | Pass | Email sent to user |
| | Confirm email | Redirects user to blank Sign In page | Pass | |
| Log In | | | | |
| | Click on the Login link | Redirection to Login page | Pass | |
| | Enter valid email address | Field will only accept email address format | Pass | |
| | Enter valid password | Field will only accept password format | Pass | |
| | Click Login button | Redirects user to home page | Pass | |
| Log Out | | | | |
| | Click Logout button | Redirects user to logout page | Pass | Confirms logout first |
| | Click Confirm Logout button | Redirects user to home page | Pass | |
| Profile | | | | |
| | Click on Profile button | User will be redirected to the Profile page | Pass | |
| | Click on the Edit button | User will be redirected to the edit profile page | Pass | |
| | Click on the My Orders link | User will be redirected to the My Orders page | Pass | |
| | Brute forcing the URL to get to another user's profile | User should be given an error | Pass | Redirects user back to own profile |

⚠️⚠️⚠️⚠️⚠️ START OF NOTES (to be deleted) ⚠️⚠️⚠️⚠️⚠️

Repeat for all other tests, as applicable to your own site.
The aforementioned tests are just an example of a few different project scenarios.

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

## User Story Testing

| User Story | Screenshot |
| --- | --- |
| As a new site user, I would like to ____________, so that I can ____________. | ![screenshot](documentation/feature01.png) |
| As a new site user, I would like to ____________, so that I can ____________. | ![screenshot](documentation/feature02.png) |
| As a new site user, I would like to ____________, so that I can ____________. | ![screenshot](documentation/feature03.png) |
| As a returning site user, I would like to ____________, so that I can ____________. | ![screenshot](documentation/feature04.png) |
| As a returning site user, I would like to ____________, so that I can ____________. | ![screenshot](documentation/feature05.png) |
| As a returning site user, I would like to ____________, so that I can ____________. | ![screenshot](documentation/feature06.png) |
| As a site administrator, I should be able to ____________, so that I can ____________. | ![screenshot](documentation/feature07.png) |
| As a site administrator, I should be able to ____________, so that I can ____________. | ![screenshot](documentation/feature08.png) |
| As a site administrator, I should be able to ____________, so that I can ____________. | ![screenshot](documentation/feature09.png) |
| repeat for all remaining user stories | x |

## Bugs

⚠️⚠️⚠️⚠️⚠️ START OF NOTES (to be deleted) ⚠️⚠️⚠️⚠️⚠️

It's very important to document any bugs you've discovered while developing the project.
Make sure to include any necessary steps you've implemented to fix the bug(s) as well.

For JavaScript and Python applications, it's best to screenshot the errors to include them as well.

**PRO TIP**: screenshots of bugs are extremely helpful, and go a long way!

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

- JS Uncaught ReferenceError: `foobar` is undefined/not defined

    ![screenshot](documentation/bug01.png)

    - To fix this, I _____________________.

- JS `'let'` or `'const'` or `'template literal syntax'` or `'arrow function syntax (=>)'` is available in ES6 (use `'esversion: 11'`) or Mozilla JS extensions (use moz).

    ![screenshot](documentation/bug02.png)

    - To fix this, I _____________________.

- Python `'ModuleNotFoundError'` when trying to import module from imported package

    ![screenshot](documentation/bug03.png)

    - To fix this, I _____________________.

- Django `TemplateDoesNotExist` at /appname/path appname/template_name.html

    ![screenshot](documentation/bug04.png)

    - To fix this, I _____________________.

- Python `E501 line too long` (93 > 79 characters)

    ![screenshot](documentation/bug04.png)

    - To fix this, I _____________________.


**Fixed Bugs**


| Bug | Status |
| --- | --- |
| [JS Uncaught ReferenceError: `foobar` is undefined/not defined](https://github.com/MJstephenson/game-reviews/issues/1) | Closed |
| [Python `'ModuleNotFoundError'` when trying to import module from imported package](https://github.com/MJstephenson/game-reviews/issues/2) | Closed |
| [Django `TemplateDoesNotExist` at /appname/path appname/template_name.html](https://github.com/MJstephenson/game-reviews/issues/3) | Closed |


## Unfixed Bugs

⚠️⚠️⚠️⚠️⚠️ START OF NOTES (to be deleted) ⚠️⚠️⚠️⚠️⚠️

You will need to mention unfixed bugs and why they were not fixed.
This section should include shortcomings of the frameworks or technologies used.
Although time can be a big variable to consider, paucity of time and difficulty understanding
implementation is not a valid reason to leave bugs unfixed.

If you've identified any unfixed bugs, no matter how small, be sure to list them here.
It's better to be honest and list them, because if it's not documented and an assessor finds the issue,
they need to know whether or not you're aware of them as well, and why you've not corrected/fixed them.

Some examples:

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

- On devices smaller than 375px, the page starts to have `overflow-x` scrolling.

    ![screenshot](documentation/unfixed-bug01.png)

    - When applying required to the code for the forms in game name and game genre, the required text box did not appear and the user could still submit the form.

- For PP3, when using a helper `clear()` function, any text above the height of the terminal does not clear, and remains when you scroll up.

    ![screenshot](documentation/unfixed-bug02.png)

    - Attempted fix: I tried to adjust the terminal size, but it only resizes the actual terminal, not the allowable area for text.

- When validating HTML with a semantic `section` element, the validator warns about lacking a header `h2-h6`. This is acceptable.

    ![screenshot](documentation/unfixed-bug03.png)

    - Attempted fix: this is a known warning and acceptable, and my section doesn't require a header since it's dynamically added via JS.

⚠️⚠️⚠️⚠️⚠️ START OF NOTES (to be deleted) ⚠️⚠️⚠️⚠️⚠️

If you legitimately cannot find any unfixed bugs or warnings, then use the following sentence:

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

There are no remaining bugs that I am aware of.
