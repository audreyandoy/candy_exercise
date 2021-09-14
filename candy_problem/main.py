'''
DIRECTIONS
==========
1. Given the list `friend_favorites`, create 
a new data structure in the function `create_new_candy_data_structure` 
that describes the different kinds of candy paired with a list of friends that 
like that candy. 

friend_favorites = [
    ["Sally", [ "lollipop", "bubble gum", "laffy taffy"]],
    [ "Bob", ["milky way", "licorice", "lollipop"]],
	[ "Arlene", ["chocolate bar", "milky way", "laffy taffy"]],
	[ "Carlie", ["nerds", "sour patch kids", "laffy taffy"]]
]

2. In `get_friends_who_like_candy_type()`, return friends who like lollipops.

3. In, `create_candy_set()`, return a set of all the candies from
the data structure made in `create_new_candy_data_structure()`.

4. Write tests for all of the functions in this exercise.

'''

def create_new_candy_data_structure(data):
    candy_list = set()

    for friend in data:
        for candy in friend[1]:
            candy_list.add(candy)

    new_data = {}

    for candy in candy_list:
        new_data[candy] = []

    for friend in data:
        friend_name = friend[0] 
        candy_list = friend[1]
        for candy in candy_list:
            new_data[candy].append(friend_name)

    return new_data

def get_friends_who_like_specific_candy(data, candy_name):
    if candy_name is None or data is None:
        raise ValueError('Error: data or candy_name or not of the correct data type')

    return data[candy_name] 
    

def create_candy_set(data):
    return set(list(data.keys()))

