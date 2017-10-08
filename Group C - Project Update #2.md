**Masterchef - A recipe recommendation engine**

**Design Document**

Amy Huang | Alice Yang | Rajasi Desai | Tanya Piplani

**Problem Statement** 

To recommend a list of possible recipes based on the ingredients provided by the user. The user also has the option of selecting type of cuisine, and category.

**Use Cases **

The program is intended for everyone who has ingredients available and wants to incorporate them in a dish. The user will input the main ingredients they would like to use and the program will suggest to the user a list of recipes. The user will also input type of cuisine and category of the meal they wish to cook. The recipes will be sorted in the order of the number of ingredients matching the input provided by the user.

**Assumptions and Constraints **

We expect the user to enter a list of primary ingredients essential to cook a dish. The code will search for the all the list of ingredients in the dataset and return the best match. The code can handle lower and upper case in the ingredients entered by the user and those present in the dataset. We are assuming the user will not make any spelling errors and enter the ingredients in singular form(e.g. berry).To improve the robustness of the code, we intend to handle these challenges in future iterations.

Constraints: After the list of ingredients, the user can also choose from a set of categories provided. The constraint is that the user needs to choose only from the categories provided on screen and does not have an option to input any other category.

Since we are incorporating web scraping and SQLite with Python, our major concern is integrating the three systems to run smoothly. Due to time constraints and an amateur knowledge of all three systems involved, this is a challenging process.

**Architecture **

The recipe generator model consists of the following components-

1. Python web crawler: 

A python based web crawler is implemented to extract the dataset consisting of recipes and ingredients from [www.allrecipes.com](http://www.allrecipes.com) . The crawler parses the html of the webpage passing through various hierarchical levels of urls until a recipe is found. As there are many levels to the website corresponding to the categories, nested functions have been implemented for the same-

* explore_main_link(link) - this function extracts the list of urls from the main page http://allrecipes.com/recipes/

* explore_level_1(link) - this function is called by the export_main_link function. It is provided will all the urls present in the html of the main page. It further drills down to the ‘hub-daughters__container’ class of ‘div’ tag in the html of the links provided.

* explore_level_2(link) - this function is called by the explore_level_1 function. It parses all the urls of the ‘grid slider desktop-view’ class in the ‘div’ tag and passes them to the next function.

* explore_level_3(link) - this function parses the ‘grid salvattore-grid grid-fixed’ class of the ‘section’ tag and passes the links to the next function.

* Explore_level_4(link) - this is the last function being called for parsing. It is used to extract the ingredients and recipe directions present on the html page from the ‘recipe-ingred_txt added’ and ‘recipe-directions__list--item’ classes respectively.

Code snippet for one of the functions in the crawler file-

def explore_level_3(link):

	html = request(link)

	soup = BeautifulSoup(html, "lxml")

	link_list = []

	for u in soup.findAll('section',{'class' : 'grid salvattore-grid grid-fixed'}):

		for v in u.findAll('a', href=True):

			link_list.append("http://allrecipes.com/" + v['href'])

	link_list = list(set(link_list))

	for i in link_list:

		try:

			explore_level_4(i)

		except Exception as e:

			print(e)

			print(i)

			time.sleep(20);

These functions are called in a loop which traverses till the end of every category combination until the list of recipes is found. 

The data from the python crawler is in the form of a dictionary consisting of the recipe url (which contains the name of the dish), the list of ingredients with their required quantities and the recipe. The dictionary is of the form-

Data = {"recipe-url" : {“ingredients”:[ing0, ing1 ...] , “recipe”:[step0, step1 ...] }

This data from the dictionary is dumped to a pickle file.

 

 2. SQLite:

** **Interaction of scraped data with the recommendation engine - We intend to interface the scraped data with python in one of the two ways:

1. Scraped Data in the form of a pickle file can be directly read in the main code. On primary analysis, this process might require more computation.

2. Scraped Data can be stored in a SQLite database and then passed to the main program through the database. This can be more efficient way of storing and fetching data.

3. Main program engine:

 The main python code consists of a sequence of functions. The use will be shown various options on the program interface. In order to navigate through the different options, they will enter the option number. This will prompt the program to execute the designated function. 

* def main(): This function allows the user to input three ingredients that are stored in three variables (ingredient 1, ingredient 2, ingredient 3)

* def recipe_type (): The user will have the option to choose between vegetarian and non-vegetarian recipes

* def recipe_preference(): The user can choose with category, world cuisine, or no preference

* def category(): The user can choose a category of recipe from appetizer, breakfast, dinner, and dessert

* def world_cuisine(): The user can choose a world cuisine from Asian, Indian, Italian Mexican, and Southern

* def recipe_options(): After the use chooses a specific recipe type, they can choose to either view the recipe or download the recipe. 

* def view_recipe(): In this function, the ingredients that were initially specified in the main() function will be queried against the database to locate the most optimal recipe. Then the recipe will be displayed on the program interface. 

* def download_recipe(): If the user chooses to download the recipe, they will be redirected to an external webpage that contains a video version of the recipe that can be downloaded. This will be possible through the import of the web browser library. 

Code snippet of recipe_type function from the main module-

def recipe_type():

    print('\nUse the numbers to navigate the menu.')

    print('Please choose the type of recipe?')

    options = {'1': vegetarian_recipe,

               '2': nonvegetarian_recipe,

               '3': quit}

    for key in sorted(options, key=int):

        print('{}) {}'.format(key, get_title(options[key].__name__)))

    while True:

        choice = input('> ')

        if choice in options:

            options[choice]()

            break

**Implementation Plan** 

We are using the following components in our project:

1. Web scraping using BeautifulSoup, urllib2, pickle

**Beautiful Soup** is a Python library for pulling data out of HTML and XML files. It works with your favorite parser to provide idiomatic ways of navigating, searching, and modifying the parse tree. It commonly saves programmers hours or days of work.

The **[pickl**e](https://docs.python.org/2/library/pickle.html#module-pickle) module implements a fundamental, but powerful algorithm for serializing and de-serializing a Python object structure. 

b. SQLite3 Database is being used to store and retrieve data.

**SQLite3** is a very easy to use database engine. It is self-contained, serverless, zero-configuration and transactional. The Python Standard Library includes a module called "sqlite3" intended for working with this database.

SQLite connection with Python-

import sqlite3

conn = sqlite3.connect('R_Gen.db')

c = conn.cursor()

c.execute("SELECT * FROM Ingredients WHERE Ingredient_ID=2")

print(c.fetchone())

conn.commit()

conn.close()

c. Module imports like defaultdict, Ordereddict etc, functions, for loops 

			

<table>
  <tr>
    <td>Team Member</td>
    <td>Feature</td>
    <td>Anticipated Date</td>
  </tr>
  <tr>
    <td>Amy Huang</td>
    <td>Design and code the flow and architecture of the main python program</td>
    <td>
October 15</td>
  </tr>
  <tr>
    <td>Alice Yang</td>
    <td>Design and code the flow and architecture of the main python program</td>
    <td>
October 15</td>
  </tr>
  <tr>
    <td>Rajasi Desai</td>
    <td>Integration of SQLite with Python,
 Interfacing scraped data with SQLite</td>
    <td>October 6
October 15</td>
  </tr>
  <tr>
    <td>Tanya Piplani</td>
    <td>Web scraping
Interfacing scraped data with SQLite
Search capability by taking user input and returning recommendations</td>
    <td>October 1
October 10
October 15</td>
  </tr>
</table>


**Test plan**  

We will demonstrate the working of the program by using practical examples. Practical examples will help strengthen the trust in the accuracy of the program.One of the most important ways in which we will be convinced by the working of the program, is by observing whether the recipes generated belong to the category and menu type selected by the user. For example, selecting eggs, as ingredient with category as Breakfast should yield results like scrambled eggs, omelette, sunny side up, etc and not results like Egg Curry(since this is more of a Dinner recipe).

Test cases-

* We will enter names of ingredients and input categories, and observe whether the recipes displayed are in descending order (i.e. recipe with the most ingredients matching will be displayed first).

* We will enter the ingredient names in upper and lower case to demonstrate the case insensitive nature of the program. Entering lowercase and/or uppercase ingredients will not throw an error, and the list of recipes displayed will in no way be affected by the case of the input.

* If spell check code is incorporated in the first iteration, we will showcase how entering an ingredient with an erroneous spelling displays the same set of recipes as when the same ingredients are entered with the correct spelling.

