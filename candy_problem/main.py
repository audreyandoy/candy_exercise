'''
DIRECTIONS
==========

1. In `get_friends_most_favored_candy()`, return a dictionary of candy names and the
amount of times each candy appears in the `friend_favorites` list.

friend_favorites = [
    ["Sally", ["lollipop", "bubble gum", "laffy taffy" ]],
    ["Bob", ["milky way", "licorice", "lollipop" ]],
    ["Arlene", ["chocolate bar", "milky way", "laffy taffy" ]],
    ["Carlie", ["nerds", "sour patch kids", "laffy taffy" ]]
]

2. Given the list `friend_favorites`, create 
a new data structure in the function `create_new_candy_data_structure` 
that describes the different kinds of candy paired with a list of friends that 
like that candy. 

friend_favorites = [
    ["Sally", ["lollipop", "bubble gum", "laffy taffy" ]],
    ["Bob", ["milky way", "licorice", "lollipop" ]],
    ["Arlene", ["chocolate bar", "milky way", "laffy taffy" ]],
    ["Carlie", ["nerds", "sour patch kids", "laffy taffy" ]]
]

3. In `get_friends_who_like_specified_candy()`, return 
a tuple of friends who like the candy specified in the candy_name parameter.

4. In `create_candy_set()`, return a set of all the candies from
the data structure made in `create_new_candy_data_structure()`.

5. Starting with nominal cases, write tests for each of the functions below then 
write tests to handle edge cases.
'''

#1
def get_friends_most_favored_candy(favorites):
    candy_dict = {}
    
    for friend in favorites:
        for candy in friend[1]:
            if candy not in candy_dict:
                candy_dict[candy] = 1
            elif candy in candy_dict:
                candy_dict[candy] += 1

    return candy_dict

#2
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

#3
def get_friends_who_like_specific_candy(data, candy_name):
    if candy_name is None or data is None:
        raise ValueError('Error: data or candy_name or not of the correct data type')

    return data[candy_name] 
    
#4
def create_candy_set(data):
    candy_dict = create_new_candy_data_structure(data)
    return set(candy_dict)

