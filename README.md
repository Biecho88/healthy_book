<h1 align="center">Cook Book</h1>

[View the live project here.](#)

<h2 align="center"><img src="#" alt="Cook Book" border="0"></h2>

# Welcome to our Cookbook Website!

#### Discover the joy of cooking with our extensive collection of recipes. Whether you're a seasoned chef or just starting out in the kitchen, our website is your go-to destination for culinary inspiration. Are you ready to elevate your culinary skills and nourish your body with delicious, wholesome meals? Look no further! My cookbook is your ultimate guide to creating refreshing smoothies, vibrant salads, and satisfying sandwiches that will tantalize your taste buds and leave you feeling energized.

## Here's what you can expect from our cookbook website:

#### Vast Recipe Collection: Discover a plethora of recipes catering to your smoothie, salad, and sandwich cravings!

#### Search and Filter Functionality: Looking for a specific dish or ingredient? Use our intuitive search and filter options to quickly find what you're craving. You can search by meal name or specify ingrediend

#### Detailed Instructions: Each recipe comes with clear, step-by-step instructions to ensure your culinary creations turn out perfectly every time. We provide ingredient lists, cooking methods, and helpful tips to enhance your cooking experience.

#### Our website provides users with convenient functionality to add, edit, and delete recipes, ensuring a seamless cooking experience tailored to your preferences.

#### Mobile-Friendly Design: Access our website anytime, anywhere, from any device. Whether you're in the kitchen with your smartphone or planning meals on your tablet, our mobil-friendly design ensures a seamless browsing experience.

#### Start your culinary journey today and unleash your inner chef with our cookbook website!

## Happy Cooking!

# User experience (UX)

- ## *User stories*

- #### First time visitor

  1. As a first time visitor, I want to navigate the site effortlessly, enabling me to log in seamlessly and access the content I'm looking for with ease.
  2. As a first time visitor, I want to quickly find recipes that fit my dietary preferences, access clear and concise instructions.
  3. As a first time visitor, I want to explore a diverse range of recipes, discover new flavors, and gain inspiration for my culinary adventures in the kitchen.

- #### Returning visitor goals

  1. As a returning visitor, I want to explore new recipes added to the collection or to rediscover old favorites.
  2. As a returning visitor, I want to continue honing my cooking skills and knowledge.
  3. As a returning visitor, I want to add, edit or delete my recipes.

- #### Frequent User Goals

  1. As a frequent user, I want to check if the new features have been added.
  2. As a frequent user, I want to continuously explore new recipes across various cuisines, dietary preferences, and cooking styles.
  3. As a frequent user, I want to improve their cooking skills and techniques by experimenting with more advanced recipes, trying out different cooking methods, and mastering challenging culinary tasks.

- ## *Design*

- #### Color scheme

    Website features a striking color scheme designed to create a sleek and cohesive visual experience. The main page boasts a clean white background, evoking a sense of simplicity and clarity, with black text providing clear and legible content. Meanwhile, the header and footer sections command attention with their teal color, which adds a vibrant splash of energy to the overall design. Against these teal backgrounds, white text stands out prominently, ensuring that important navigation elements and essential information are easily accessible and visually engaging. This thoughtful combination of colors creates a modern and sophisticated ambiance, inviting users to explore our website with style and ease

- #### Typography
  
    Roboto font is the main font used throughout the whole website with sans-serif as the fallback font in case for any reason the font isn't being imported into the site correctly.

- #### Imagery

    Emojis have been used as decoration on the main webpage and as an image behind cards for the game.

## Languages used

- [HTML](https://en.wikipedia.org/wiki/HTML)
- [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

## Frameworks, Libraries & Programs used

1. [Git](https://git-scm.com/)
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
2. [GitHub:](https://github.com/)
    - GitHub is used to store the project code after being pushed from Git.
3. [Pixabay](https://pixabay.com/)
    - Pixabay Was used for images.
4. [Materialize 1.0.0](https://materializecss.com/)
    - Materialize is used to assist with the responsiveness and styling of the website.
5. [MongoDB](https://www.mongodb.com/)
    - Mongo is used to store the data andsearch through the recipes by text.
6. [Heroku](https://dashboard.heroku.com/)
    - Heroku is used for cloud-based hosting platform.

## My Testing

The W3C Markup Validator and W3C CSS Validator Services were used to validate every page of the project to ensure there were no syntax errors in the project.

- [Home page](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fhealthy-book-piotr-034b028d3ac7.herokuapp.com%2F)
- [Add Recipe page](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fhealthy-book-piotr-034b028d3ac7.herokuapp.com%2Fget_category)
- [Recipe page](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fhealthy-book-piotr-034b028d3ac7.herokuapp.com%2Fget_recipes)
    - This has few errors but unable to change due to extracting data from MongoDB
- [Login page](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fhealthy-book-piotr-034b028d3ac7.herokuapp.com%2Flog_in)
- [Register page](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fhealthy-book-piotr-034b028d3ac7.herokuapp.com%2Fregister)
- [CSS test results by text input](https://jigsaw.w3.org/css-validator/validator)
- [The text was chacked in the free grammar checker](https://www.grammarly.com/spell-checker)
- [The text for website and readme file was partly wrriten by ChatGPT 3.5](https://chat.openai.com/)
  
### Carried out manual testing as follows : 

#### Homepage
- Click on logo or Home and verify that home page appears.
- If visitor is not logged in “Log in” and "Register" should be displayed in the navigation and clicking this link will bring you to the relevant page.
- If visitor is logged in “Your Profile”, “Add recipe”, “Recipes”, “Log out” should be displayed in the navigation and clicking this link will bring you to the relevant page.
- Ensure slider displaying correct images.
- Confirmed that the header links, link to the correct pages
- Confirmed that the header links, link to the correct pages on smaller devices
- Confirmed that the social links in the footer open in a new browser window and go to the correct links

#### Register page
- Confirmed that the form work correctly, and user registration adds details to MongoDB database
- Confirmed that the register form selector work correctly


#### Log in  page
- Confirmed that the form work correctly, and user session is on
- Confirmed that the log in form selector work correctly

#### Add recipe page
- Confirmed that the form work correctly, and recipes are added
- Confirmed that the add recipe form selector work correctly

#### Edit recipe page
- Confirmed that the form work correctly, and recipes are eddited
- Confirmed that the edit form selector work correctly

#### Recipe page
- Confirmed that the website display recipes correctly from the database
- Confirmed that the "delete" button works correctly
    - user authorsation is missing as ones clicked recipe is deleted
- Confirmed that the "edit" button works correctly
- Confirmed that the user can only delete or edit recipes added by him/her
- Confirmed that the "search" button works correctly. Search is performed by text on "list of ingridiens" and "recipe name"

#### Footer
- Confirmed that the footer links, link to the correct pages

### Further testing

- The Website was tested on Google Chrome, Internet Explorer, Firefox and Safari browsers.
- The website was viewed on a variety of devices such as Desktop, Laptop, iPhone 14, iPhone 12 Pro Max & Samsung Galaxy S20
- A large amount of testing was done to ensure that the aplication has no bugs.
- Friends and family members were asked to review the site and documentation to point out any bugs and/or user experience issues.

### Screenshots from testing

#### Tested if the array with emojis works correctly

<h2 align="center"><img src="https://i.ibb.co/F6vcfpg/Emoji-Test.png" alt="Array list test" border="0"></h2>

#### Tested if console logs list of emoji correctly

<h2 align="center"><img src="https://i.ibb.co/p3bbzm1/Emoji-List-Test.png" alt="List of emoji test" border="0"></h2>

#### Manipulated DOM to build tiles test

<h2 align="center"><img src="https://i.ibb.co/1X60s0C/Build-Tile-Through-DOM.png" alt="Build tile through the DOM" border="0"></h2>

#### Data revealed test

<h2 align="center"><img src="https://i.ibb.co/pQmCt3z/Data-Revealed.png" alt="DataRevealed test" border="0"></h2>

#### Tested if paired tiles stay revealed

<h2 align="center"><img src="https://i.ibb.co/bBqMRW1/Paired-Tiles-Stay-Revealed.png" alt="Paired tiles stay revealed" border="0"></h2>

#### Massage at the end of the game

<h2 align="center"><img src="https://i.ibb.co/HTLSBhb/End-Of-Game.png" alt="End of game" border="0"></h2>

#### One of the friends tests shows emojis too big for the tile

<h2 align="center"><img src="https://i.ibb.co/wJsBVJ9/received-668982745078365.jpg" alt="Emojis to big for mobile phone screen" border="0"></h2>

#### The timer starts once START button is clicked

<h2 align="center"><img src="https://i.ibb.co/g4tGgPR/Timer-Check.png" alt="TimerCheck" border="0"></h2>

### Known Bugs

- None

## Deployment

### GitHub Pages

The project was deployed to GitHub Pages using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/Biecho88/memory-game)
2. At the top of the Repository (not the top of the page), locate the "Settings" Button on the menu.
3. Scroll down the Settings page until you locate the "GitHub Pages" Section.
4. Under "Source", click the dropdown called "None" and select "Master Branch".
5. The page will automatically refresh.
6. Scroll back down through the page to locate the now published site [link](https://biecho88.github.io/memory-game/) in the "GitHub Pages" section.

### Forking the GitHub Repository

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. At the top of the Repository (not the top of the page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
```

7. Press Enter. Your local clone will be created.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

Click [Here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) to retrieve pictures of some of the buttons and more detailed explanations of the above process.

## Credits

### Content

- All content was written by the developer.

### Acknowledgments

- My Mentor for helpful feedback.

- Tutor support at Code Institute for their support.

- Student support on Slack [Link](https://app.slack.com/client/T0L30B202/C058BTPP7A5)
