
# coding: utf-8

# In[ ]:


from collections import OrderedDict
from itertools import takewhile, zip_longest
from os import listdir, remove
from os.path import join, isfile, splitext, basename
import webbrowser
import pickle
from collections import defaultdict
import readline
import urllib.request
import urllib.parse
import re

#crawled data is stored in pickle files
f = open("../data/data_tags.pkl", 'rb')
data = pickle.load(f)

file = open("../data/data_ing.pkl", 'rb')
ing_list = pickle.load(file)
ing_list = [x.strip(' ') for x in ing_list]

class MyCompleter(object):  # Custom completer
    def __init__(self, options):
        self.options = sorted(options)

    def complete(self, text, state):
        if state == 0:  # on first trigger, build possible matches
            if text:  # cache matches (entries that start with entered text)
                self.matches = [s for s in self.options 
                   if text in s]
            else:  # no text entered, all matches possible
                self.matches = self.options[:]

        try: 
            return self.matches[state]
        except IndexError:
            return None

#-------------------------------------------------------------------------------

SUBDIR = 'recipes'

tags = {}
ingredients = []
preference_selection = ['allrecipes.com']
video_selection = ''

completer = MyCompleter(ing_list)
readline.set_completer(completer.complete)
readline.parse_and_bind('tab: complete')
for kw in ing_list:
    readline.add_history(kw)

#main function where user is prompted to input the list of ingredients that will be stored in a list
def main():
    """Main function to promp user to input the list of ingredients."""
    global ingredients
    from IPython.display import Image, display
    display(Image('../GUI/img.jpg'))
    print('Welcome To portFOODlio!\nYour own personalized recipe portfolio!')
    print('\nAre you hungry but have no clue as to what to cook?\nNo worries! \nJust provide us with the list of ingredients you would like to incorporate in a dish and we will do the rest for you!')
    ing = input("\nEnter the list of ingredients (comma seperated): ")
    ingredient = ing.split(',')
    ingredients.extend(ingredient)
    recipe_preference()

#-------------------------------------------------------------------------------
#function where user is prompted to select the recipe preference
def recipe_preference():
    """Function where user is prompted to select the recipe preference."""
    print('\nUse the numbers to navigate the menu.')
    print('Please choose your recipe preference.')
    options = {'1': category,
               '2': world_cuisine,
               '3': no_preference,
               '4': quit}
    for key in sorted(options, key=int):
        print('{} - {}'.format(key, get_title(options[key].__name__)))
    while True:
        choice = input('> ')
        if choice in options:
            options[choice]()
            break
        else:
          print("Invalid selection. Please enter another number: ")
#-------------------------------------------------------------------------------
#function that is executed when the user selects 'category' for recipe preference
def category():
    """Function where user is prompted to select a specific category."""
    global video_selection
    print('\nUse the numbers to navigate the menu.')
    print('Please choose a category for your recipe.')
    options = {'1': 'Appetizers and Snacks',
               '2': 'Breakfast and Brunch',
               '3': 'Main Dish',
               '4': 'Desserts',
               '5': 'Drinks',
               '6': 'Salad',
               '7': 'Fruits and Vegetables',
               '8': 'Side Dish',
               '9': 'Soups, Stews and Chili',
               '10': 'Go Back to Preference Selection',
               '11': 'Quit'}
    
    #Appetizer
    from IPython.display import Image, display
    display(Image('https://www.pamperedchef.com/iceberg/com/recipe/89659-lg.jpg'))
    #Breakfast
    from IPython.display import Image, display
    display(Image('https://s-media-cache-ak0.pinimg.com/736x/e7/d2/f7/e7d2f75dacd45fe3b5370a5ac5b20dfa--breakfast-pancakes-breakfast-club.jpg'))
    #MainDish
    from IPython.display import Image, display
    display(Image('https://i.pinimg.com/736x/69/e5/51/69e5514e0dee00e0a023cd5189ca8432--clam-ideas-singapore-food.jpg'))
    #Desserts
    from IPython.display import Image, display
    display(Image('https://s-media-cache-ak0.pinimg.com/originals/5a/2d/aa/5a2daa4956b4526dd9ad18c8a240dab7.jpg'))

    
    for key in sorted(options, key=int):
        print('{} - {}'.format(key, get_title(options[key])))
    while True:
        choice = input('> ')
        if choice == '10':
          recipe_preference()
        elif choice == '11':
          quit()
        else:
          tags['category'] = options[choice]
          preference_selection.append(options.get(choice))
          video_selection = ' '.join(ingredients + preference_selection)
          recipe_options_category()
          break

#-------------------------------------------------------------------------------
#function that is executed when the user selects 'world cuisine' for recipe preference
def world_cuisine():
    """Function where user is prompted to select a specific world cuisine."""
    global video_selection
    #Chinese
    from IPython.display import Image, display
    display(Image('https://cdn.vox-cdn.com/thumbor/cVvqLXAShOCcxKwydCYb5bzghBg=/42x0:956x686/920x690/filters:focal(42x0:956x686):format(webp)/cdn.vox-cdn.com/uploads/chorus_image/image/52453689/shutterstock_446808100.0.0.jpeg'))
    #French
    from IPython.display import Image, display
    display(Image('http://img1.10bestmedia.com/Images/Photos/315339/p-image--34-_54_990x660.jpg'))
    #Indian
    from IPython.display import Image, display
    display(Image('https://img.buzzfeed.com/buzzfeed-static/static/2017-01/11/12/campaign_images/buzzfeed-prod-fastlane-03/16-mouthwatering-ways-to-make-great-indian-food-a-2-21890-1484156176-0_dblbig.jpg'))
    #Italian
    from IPython.display import Image, display
    display(Image('http://luvo.tetherinc.netdna-cdn.com/wp-content/uploads/2015/09/Six-Tips-Healthy-Italian-Food-Luvo-Mast.jpg'))
    #Mexican
    from IPython.display import Image, display
    display(Image('https://img.grouponcdn.com/deal/iJVvZzL5wXt2WdwKgQhLgN/186347703-3642x2185/v1/c700x420.jpg'))
    print('\nUse the numbers to navigate the menu.')
    print('Please choose a world cuisine for your recipe.')
    options = {'1': 'Chinese',
               '2': 'French',
               '3': 'German',
               '4': 'Greek',
               '5': 'Indian',
               '6': 'Japanese',
               '7': 'Korean',
               '8': 'Lebanese',
               '9': 'Pakistani',
               '10': 'Spanish',
               '11': 'Thai',
               '12': 'Italian',
               '13': 'Mexican',
               '14': 'Latin American',
               '15': 'Middle Eastern',
               '16': 'Go Back to Preference Selection',
               '17': 'Quit'}
  
    for key in sorted(options, key=int):
        print('{} - {}'.format(key, get_title(options[key])))
    while True:
        choice = input('> ')
        if choice == '16':
          recipe_preference()
        elif choice == '17':
          quit()
        elif choice in options:
            tags['world_cuisine'] = options[choice]
            preference_selection.append(options.get(choice))
            video_selection = ' '.join(ingredients + preference_selection)
            recipe_options_world()
            break
        else:
          print("Invalid selection. Please enter another number: ")
#-------------------------------------------------------------------------------
#function that is executed when the user selects 'no preference' for recipe preference
def no_preference():
    """Function executed if user selects no preference for recipe type."""
    tags['no_preference'] = 0
    recipe_options_category()

#-------------------------------------------------------------------------------
#function is executed to prompt user to either view or download recipe if chosen from category. 
def recipe_options_category():
    """Function executed to prompt user to select how to view recipe if category is selected."""
    print(tags)
    print('\nUse the numbers to navigate the menu.')
    options = {'1': view_recipes,
               '2': view_youtube_recipe,
               '3': go_back_to_category_selection,
              '4': quit}
    for key in sorted(options, key=int):
        print('{} - {}'.format(key, get_title(options[key].__name__)))
    while True:
        choice = input('> ')
        if choice in options:
          options[choice]()
          break
        else:
          print("Invalid selection. Please enter another number: ")
#-------------------------------------------------------------------------------
#function is executed to prompt user to either view or download recipe if chosen from world cuisine. 
def recipe_options_world():
    """Function executed to prompt user to select how to view recipe if world cuisine is selected."""
    print(tags)
    print('\nUse the numbers to navigate the menu.')
    options = {'1': view_recipes,
               '2': view_youtube_recipe,
               '3': go_back_to_world_cuisine_selection,
              '4': quit}
    for key in sorted(options, key=int):
        print('{} - {}'.format(key, get_title(options[key].__name__)))
    while True:
        choice = input('> ')
        if choice in options:
          options[choice]()
          break
        else:
          print("Invalid selection. Please enter another number: ")

#-------------------------------------------------------------------------------
#function to navigate back to category options
def go_back_to_category_selection():
    """Function executed if user wants to navigate back to category selection page."""
    category()
#-------------------------------------------------------------------------------
#function to navigate back to world cuisine options
def go_back_to_world_cuisine_selection():
    """Function executed if user wants to navigate back to world cuisine selection page."""
    world_cuisine()
#-------------------------------------------------------------------------------
#function that is executed when the user selects 'view recipe'. web browser opens to the recipe of choice.
def view_recipes():
    """Function executed if user wants to view recipe."""
    ing_count = defaultdict(int)
    for k,v in data.items():
        for ing in ingredients:
            if ing in ';'.join(v['ing']):
                ing_count[k] += 1
                if (('world_cuisine' in tags.keys() and                     tags['world_cuisine'] in ';'.join(v['tags'])) or ('category' in tags.keys() and tags['category'] in ';'.join(v['tags'])) or                     ('no_preference' in tags.keys())):
                    ing_count[k] += len(ingredients)
    ing_match = sorted(ing_count, key=lambda k: (ing_count[k]*1.0)/len(data[k]), reverse=True)
    for idx in range(0, len(ing_match), 5):
        for j in range(idx, idx + 5):
            print(j - idx + 1,'- Link:' , ing_match[j])
        opt = int(input('\nEnter the number for the recipe you would like to view or -1 for more recipes?'))
        if opt == -1:
            continue
        else:
            webbrowser.open(ing_match[(idx + opt - 1)])
            quit(); break

def quit():
    exit()
#-------------------------------------------------------------------------------
#function executed when user wants to view YouTube recipe
def view_youtube_recipe():
    """Function executed if user wants to view YouTube recipe."""
    query_string = urllib.parse.urlencode({"search_query" : video_selection})
    html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
    webbrowser.open("http://www.youtube.com/watch?v=" + search_results[0])
#-------------------------------------------------------------------------------

def get_file(prompt):
    print('get file')

def get_name(path):
    # return get_title(splitext(basename(path))[0])
    print('get name')

def get_title(name):
    return name.replace('_', ' ').title()

#-------------------------------------------------------------------------------

if __name__ == '__main__':
    main()

