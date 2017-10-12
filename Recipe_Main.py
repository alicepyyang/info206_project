from collections import OrderedDict
from itertools import takewhile, zip_longest
from os import listdir, remove
from os.path import join, isfile, splitext, basename
import webbrowser
import pickle
from collections import defaultdict


import readline

f = open("data_tags.pkl", 'rb')
data = pickle.load(f)

file = open("data_ing.pkl", 'rb')
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

        # return match indexed by state
        try: 
            return self.matches[state]
        except IndexError:
            return None

#-------------------------------------------------------------------------------

SUBDIR = 'recipes'

tags = {}
ingredients = []


completer = MyCompleter(ing_list)
readline.set_completer(completer.complete)
readline.parse_and_bind('tab: complete')
for kw in ing_list:
    readline.add_history(kw)

def main():
    global ingredients
    print('Welcome To portFOODlio: A Recipe Generator')
    ing = input("Enter the list of ingredients (comma seperated): ")
    ingredient = ing.split(',')
    ingredients.extend(ingredient)
    recipe_preference()
    #options = {'1': view_recipe,
     #          '2': download_recipe,
      #         '3': quit}
    #for key in sorted(options, key=int):
     #   print('{}) {}'.format(key, get_title(options[key].__name__)))
    #while True:
     #   choice = input('> ')
      #  if choice in options:
       #     options[choice]()
        #    break

#-------------------------------------------------------------------------------
def recipe_preference():
    print('\nUse the numbers to navigate the menu.')
    print('Please choose your recipe preference.')
    options = {'1': category,
               '2': world_cuisine,
               '3': no_preference,
               '4': quit}
    for key in sorted(options, key=int):
        print('{}) {}'.format(key, get_title(options[key].__name__)))
    while True:
        choice = input('> ')
        if choice in options:
            options[choice]()
            break

#-------------------------------------------------------------------------------
def world_cuisine():
    print('\nUse the numbers to navigate the menu.')
    print('Please choose a world cuisine for your recipe.')
    options = {'1': 'Asian',
               '2': 'Indian',
               '3': 'Italian',
               '4': 'Mexican',
               '5': 'South American',
               '6': 'African',
               '7': 'European',
               '8': 'Latin American',
               '9': 'Middle Eastern',
               '10': 'Austrian',
               '11': 'Bangladeshi',
               '12': 'Caribbean',
               '13': 'Dutch',
               '14': 'Eastern European',
               '15': 'French',
               '16': 'German',
               '17': 'Greek',
               '18': 'Indonesian',
               '19': 'Israeli',
               '20': 'Japanese',
               '21': 'Korean',
               '22': 'Lebanese',
               '23': 'Pakistani',
               '24': 'Scandinavian',
               '25': 'Spanish',
               '26': 'Thai',
               '27': 'Quit'}
    for key in sorted(options, key=int):
        print('{}) {}'.format(key, get_title(options[key])))
    while True:
        choice = input('> ')
        if choice in options and choice is not '27':
            tags['world_cuisine'] = options[choice]
            recipe_options()
            break
        else:
            quit()
#-------------------------------------------------------------------------------
def no_preference():
    tags['no_preference'] = 0
    print('\nno preference')
    recipe_options()
#-------------------------------------------------------------------------------
def category():
    print('\nUse the numbers to navigate the menu.')
    print('Please choose a category for your recipe.')
    options = {'1': 'Appetizers and Snacks',
               '2': 'Breakfast and Brunch',
               '3': 'Main Dish',
               '4': 'Desserts',
               '5': 'Drinks',
               '6': 'salad',
               '7': 'Fruits and Vegetables',
               '8': 'Side Dish',
               '9': 'Soups, Stews and Chili',
               '10': 'Quit'}
    for key in sorted(options, key=int):
        print('{}) {}'.format(key, get_title(options[key])))
    while True:
        choice = input('> ')
        if choice in options and choice is not '10':
            tags['category'] = options[choice]
            recipe_options()
            break
        else:
            quit()

def view_recipe():
    ing_count = defaultdict(int)
    for k,v in data.items():
        for ing in ingredients:
            if ing in ';'.join(v['ing']):
                ing_count[k] += 1
                if (('world_cuisine' in tags.keys() and \
                    tags['world_cuisine'] in ';'.join(v['tags'])) or ('category' in tags.keys() and tags['category'] in ';'.join(v['tags'])) or \
                    ('no_preference' in tags.keys())):
                    ing_count[k] += len(ingredients)
    ing_match = sorted(ing_count, key=lambda k: (ing_count[k]*1.0)/len(data[k]), reverse=True)
    for idx in range(0, len(ing_match), 5):
        for j in range(idx, idx + 5):
            print(j - idx + 1, ') Link: ' , ing_match[j])#, '\nMeta : ' , data[ing_match[j]])
        opt = int(input('Which recipe do you want or -1 for more recipes?'))
        if opt == -1:
            continue
        else:
            webbrowser.open(ing_match[(idx + opt - 1)])
            quit(); break

def recipe_options():
    print(tags)
    options = {'1': view_recipe,
               '2': download_recipe,
              '3': quit}
    for key in sorted(options, key=int):
        print('{}) {}'.format(key, get_title(options[key].__name__)))
    while True:
        choice = input('> ')
        if choice in options:
            options[choice]()
            break

def download_recipe():
    # raise NotImplementedError()
    print('Download Recipe')
    print('Use the numbers to navigate the menu.')
    options = {'1': from_youtube,
               '2': from_masterchef,
               '3': quit,}
    for key in sorted(options, key=int):
        print('{}) {}'.format(key, get_title(options[key].__name__)))
    while True:
        choice = input('> ')
        if choice in options:
            options[choice]()
            break

    # webbrowser.open('https://www.youtube.com/user/allrecipes')

def quit():
    # path = get_file('Type in the number of the recipe you '
    #                 'would like to delete and press enter.')
    # remove(path)
    print('quit')

def from_youtube():
    webbrowser.open('https://www.youtube.com/user/allrecipes')

def from_masterchef():
    webbrowser.open('https://tenplay.com.au/channel-ten/masterchef/recipes/all-recipes')

#-------------------------------------------------------------------------------

def get_file(prompt):
    # files = tuple(name for name in
    #               (join(SUBDIR, name) for name in listdir(SUBDIR))
    #               if isfile(name))
    # for index, path in enumerate(files, 1):
    #     print('{}) {}'.format(index, get_name(path)))
    # print('Type in the number of the recipe you '
    #       'would like to view and press enter.')
    # return files[int(input('> ')) - 1]
    print('get file')

def get_name(path):
    # return get_title(splitext(basename(path))[0])
    print('get name')

def get_title(name):
    return name.replace('_', ' ').title()


#-------------------------------------------------------------------------------

if __name__ == '__main__':
    main()
