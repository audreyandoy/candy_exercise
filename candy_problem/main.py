'''
DIRECTIONS
==========
1. Given the list `friend_favorites`, create 
a new data structure in the function `create_new_candy_data_structure` 
that describes the different types of candy paired with a list of friends that 
like that candy. 

2. In `get_favorite_candy_by_name()`, return the candies
that Arlene likes.

3. In, `create_candy_set()`, return a set of all the candies from
the data structure made in `create_new_candy_data_structure()`.

4. Write tests for all of the functions in this exercise.

'''

friend_favorites = [
    ["Sally", [ "lollipop", "bubble gum", "laffy taffy"]],
    [ "Bob", ["milky way", "licorice", "lollipop"]],
	[ "Arlene", ["chocolate bar", "milky way", "laffy taffy"]],
	[ "Carlie", ["nerds", "sour patch kids", "laffy taffy"]]
]


def create_new_candy_data_structure(data):
    candy_list = []
    for friend in friend_favorites:
        for candy in friend[1]:
             candy_list.append(candy)

    unique_candy_list = list(set(candy_list))

    new_data = {}

    for candy in candy_list:
        new_data[candy] = []

    print(new_data)
    
    

create_new_candy_data_structure(friend_favorites)



def get_favorite_candy_by_name(data, name):
    pass 
    

def create_candy_set(data):
    pass 
