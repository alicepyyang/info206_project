# portFOODlio - Your Recipe Portfolio

Created By: Amy Huang, Alice Yang, Rajasi Desai, Tanya Piplani

## What is portFOODlio?
Have you ever encountered the scenario where you open your fridge looking for something to eat, but only see some leftover ingredients that you don't know how to incorporate together in a dish? This is where portFOODlio will come in handy! portFOODlio is an interactive program that allows the user to input any number of ingredients and it will suggest recipes based on the the ingredients inputted and recipe preference selected by the user. The user will have the option to either view the recipe on a webpage or watch a YouTube video of a recipe. This program will help the user relieve some stress from having to sift through multiple recipes to find a recipe to use and, thus, preventing ingredients from being wasted. 

## How to run portFOODlio?
**Option 1:** Navigate to your computer's terminal(command line) and run the 'Recipe_Main.py' file

**Option2:** Navigate to Jupyter Notebook and run the 'Recipe_Main.py' file

## Program Architecture
**1. Python Web Crawler**

**Beautiful Soup** is a python library for pulling data out of HTML and XML files. BeautifulSoup is used in portFOODlio to extract over 30k+ recipes and ingredients data from allrecipes.com webpage. The crawler parses the html of the webpage passing through various hierarchical levels of URLs until a recipe is found. The data from the python crawler is stored in the form of a dictionary consisting of the recipe URL (which contains the name of the dish), the list of ingredients with their required quantities, and the recipe itself. The data from the dictionary is stored into a pickle file that is read by the main program engine. The **Pickle Module** implements a fundamental, but powerful algorithm for serializing and de-serializing a Python object structure. 

**2. Main Program Engine**
The main program engine consists of a series of functions that are called and executed based on the user's selections. The program starts with a main() function where the user is prompted to input the ingredients they would like to see a recipe for. The ingredients are stored in a list for later usage.

The user is then prompted to select a recipe preference. The user has the option to select either category, world cuisine, no preference, or quit the program.

If the user selects category, then they will be prompted to select a more specific category of recipe. For example, Breakfast and Brunch, Main Dish, or Desserts. 

If the user selects world cuisine, then they will be prompted to select a more specific type of world cuisine. For example, Chinese, Indian, Korean, or Italian.

Once the specific preference has been selected, the program will enter the function that prompts the user what way they would like to view the data. They can either choose to view a list of recipes or to view a video on YouTube. Again, the user has the ability to quit the program anytime or navigate to a previous page to make a new selection.

If the user selects to view recipes, then there will be a list of five recipes displayed on the page. The user has the option to keep displaying more recipes until they find the one they would like to view. Once they select a recipe, a webpage will open up and redirect them to the specific recipe webpage on allrecipes.com. 

If the user selects to view a YouTube video, then a webpage will open up and redirect them to a recipe on YouTube.

The user also has the ability to navigate back and forth between selection criterias to make changes before finalizing a recipe to view. The user also has the option to quit the program anytime. 



## Instructions to run the code
We have provided a *__init_.ipynb* jupyter notebook file in the src directory. Just launch that on a browser and execute the first cell.