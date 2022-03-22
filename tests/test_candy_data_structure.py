import pytest
from candy_problem.main import * 


def test_create_candy_data_structure_type():
    # Arrange
    friend_favorites = [
        ["Sally", [ "lollipop”, “bubble gum", "laffy taffy"]],
        ["Bob", ["milky way", "licorice", "lollipop"]],
        ["Arlene", ["chocolate bar", "milky way", "laffy taffy"]],
        ["Carlie", ["nerds", "sour patch kids", "laffy taffy"]]
    ]

    # Act
    new_candy_data = create_new_candy_data_structure(friend_favorites)
    
    # Assert
    assert type(new_candy_data) == dict
    

def test_create_candy_data_structure_values():

    # Arrange
    friend_favorites = [
        ["Sally", [ "lollipop”, “bubble gum", "laffy taffy"]],
        ["Bob", ["milky way", "licorice", "lollipop"]],
        ["Arlene", ["chocolate bar", "milky way", "laffy taffy"]],
        ["Carlie", ["nerds", "sour patch kids", "laffy taffy"]]
    ]

    # Act
    new_candy_data = create_new_candy_data_structure(friend_favorites)
    
    # Assert
    assert type(new_candy_data) == dict

def test_create_candy_data_structure_values():

    # Arrange
    friend_favorites = [
        ["Sally", [ "lollipop”, “bubble gum", "laffy taffy"]],
        ["Bob", ["milky way", "licorice", "lollipop"]],
        ["Arlene", ["chocolate bar", "milky way", "laffy taffy"]],
        ["Carlie", ["nerds", "sour patch kids", "laffy taffy"]]
    ]

    # Act
    new_candy_data = create_new_candy_data_structure(friend_favorites)
    
    # Assert
    assert len(new_candy_data) == 8
    assert new_candy_data["lollipop"] == ["Sally", "Bob"]


def test_get_friends_who_like_specific_candy():
    # Arrange
    friend_favorites = [
        ["Sally", [ "lollipop”, “bubble gum", "laffy taffy"]],
        ["Bob", ["milky way", "licorice", "lollipop"]],
        ["Arlene", ["chocolate bar", "milky way", "laffy taffy"]],
        ["Carlie", ["nerds", "sour patch kids", "laffy taffy"]]
    ]
    
    data = create_new_candy_data_structure(friend_favorites)
    candy_type = "lollipop"

    # Act
    result = get_friends_who_like_specific_candy(data, candy_type)

    # Assert
    assert result == ["Sally", "Bob"]
    assert len(result) == 2
    assert type(result) == list 


def test_create_candy_set():

    # Arrange
    friend_favorites = [
        ["Sally", [ "lollipop”, “bubble gum", "laffy taffy"]],
        ["Bob", ["milky way", "licorice", "lollipop"]],
        ["Arlene", ["chocolate bar", "milky way", "laffy taffy"]],
        ["Carlie", ["nerds", "sour patch kids", "laffy taffy"]]
    ]
    
    data = create_new_candy_data_structure(friend_favorites)

    # Act
    result = create_candy_set(data)
    
    # Assert
    assert type(result) == set
    assert len(result) == 8