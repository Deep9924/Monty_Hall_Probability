import random

# variables
n = 10000000
choice_changed = 0
choice_unchanged = 0

for _ in range(n):
    # randomizing each time to get better result
    door_list = [1,2,3]
    user_choice = random.randint(1,3)
    prize_door = random.randint(1,3)

    # removing user's choice as there will be two door left in the list
    door_list.remove(user_choice)

    # if user did not picked the prize door then remove it so host will not pick the prize door
    # if user picked the prize door then keep the list as we there will be two door for host to pick from
    if (user_choice != prize_door):
        door_list.remove(prize_door)

    # host is revealing another door
    host = random.choice(door_list)
    # After revealing remove the door from list as we will not use this
    door_list.remove(host)

    # if user keep their choice and is also the prize door 
    # then add 1 for keeping their choice and winning
    if (user_choice == prize_door):
        choice_unchanged += 1
    # if user keep their choice and is not the prize door
    # then add 1 for not changing their choice
    else:
        choice_changed += 1

# Calculate the result
total1 = (choice_changed / n) * 100
total2 = (choice_unchanged / n) * 100

# Print the result
print("If choice is changed the probability is: {}\n".format(total1))
print("If choice is unchanged the probability is: {}\n".format(total2))
