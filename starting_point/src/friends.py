
# task 1
def get_name(person):
    return person["name"]

# task 2
def get_favourite_tv_show(person):
    return person["favourites"]["tv_show"]

# task 3

def likes_to_eat(person, snack):
    for value in person["favourites"]["snacks"]:
        if value == snack:
            return True
    return False

# task 4 

def add_friend(person, new_friend):
    person["friends"].append(new_friend)

# task 5

def remove_friend(person, unfriend):
    person["friends"].remove(unfriend)

# task 6

def total_money(people):
    total = 0
    for person in people:
        total += person["monies"]
    return total