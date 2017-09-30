from collections import OrderedDict
from itertools import takewhile, zip_longest
from os import listdir, remove
from os.path import join, isfile, splitext, basename
import webbrowser

#-------------------------------------------------------------------------------

SUBDIR = 'recipes'

def main():
    print('Welcome to Recipe Generator')
    ingredient1 = input('Enter your first ingredient: ')
    ingredient2 = input('Enter your second ingredient: ')
    ingredient3 = input('Enter your third ingredient: ')
    recipe_type()
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


#-------------------------------------------------------------------------------
def vegetarian_recipe():
    print('\nVegetarian Recipe Generator')
    recipe_preference()
#-------------------------------------------------------------------------------


def nonvegetarian_recipe():
    print('\nNon-Vegetarian Recipe Generator')
    recipe_preference()

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
    options = {'1': asian,
               '2': indian,
               '3': italian,
               '4': mexican,
               '5': southern,
               '6': quit}
    for key in sorted(options, key=int):
        print('{}) {}'.format(key, get_title(options[key].__name__)))
    while True:
        choice = input('> ')
        if choice in options:
            options[choice]()
            break
#-------------------------------------------------------------------------------
def no_preference():
    print('\nno preference')
    recipe_options()
#-------------------------------------------------------------------------------
def category():
    print('\nUse the numbers to navigate the menu.')
    print('Please choose a category for your recipe.')
    options = {'1': appetizer,
               '2': breakfast,
               '3': dinner,
               '4': dessert,
               '5': quit}
    for key in sorted(options, key=int):
        print('{}) {}'.format(key, get_title(options[key].__name__)))
    while True:
        choice = input('> ')
        if choice in options:
            options[choice]()
            break
#-------------------------------------------------------------------------------

def appetizer():
    print('\nHere is your appetizer recipe. Enjoy!')
    recipe_options()
#-------------------------------------------------------------------------------

def breakfast():
    print('\nHere is your breakfast recipe. Enjoy!')
    recipe_options()
#-------------------------------------------------------------------------------

def dinner():
    print('\nHere is your dinner recipe. Enjoy!')
    recipe_options()
#-------------------------------------------------------------------------------

def dessert():
    print('\nHere is your dessert recipe. Enjoy!')
    recipe_options()
#-------------------------------------------------------------------------------
def asian():
    print('\nHere is your asian recipe. Enjoy!')
    recipe_options()
#-------------------------------------------------------------------------------
def indian():
    print('\nHere is your indian recipe. Enjoy!')
    recipe_options()
#-------------------------------------------------------------------------------
def italian():
    print('\nHere is your italian recipe. Enjoy!')
    recipe_options()
#-------------------------------------------------------------------------------
def mexican():
    print('\nHere is your mexican recipe. Enjoy!')
    recipe_options()
#-------------------------------------------------------------------------------
def southern():
    print('\nHere is your southern recipe. Enjoy!')
    recipe_options()
#-------------------------------------------------------------------------------
def view_recipe():
    # path = get_file('Type in the number of the recipe you '
    #                 'would like to view and press enter.')
    # print('Reciple for', get_name(path))
    # with open(path) as file:
    #     lines = filter(None, map(str.strip, file))
    #     for step in enumerate(takewhile('heading1'.__ne__, lines), 1):
    #         print('{}. {}'.format(*step))
    #     columns = OrderedDict((name.strip(), [])
    #                           for name in next(lines).split(','))
    #     max_split = len(columns) - 1
    #     for info in takewhile('heading2'.__ne__, lines):
    #         fields = tuple(map(str.strip, info.split(',', max_split)))
    #         for key, value in zip_longest(columns, fields, fillvalue=''):
    #             columns[key].append(value)
    # ingredients = columns['ingredients']
    # weights = columns['weight']
    # measurements = columns['measurement']
    # assert len(ingredients) == len(weights) == len(measurements)
    # print('Ingredients')
    # for specification in zip(ingredients, weights, measurements):
    #     print(*specification)
    print('view recipe')

def recipe_options():
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