# Exercies #Day #9

#AGENDA: Dictionaries

programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", 
                          "Function": "A piece of code that you can easily call over and over again."}

# Retrieving items from dictionary
print(programming_dictionary['Bug'])

# Adding new items to Dictionary
programming_dictionary["loop"] = "The action od doing something over and over again"
print(programming_dictionary)

# create an empty distionary
empty_dictionary = {}

# Wipe an existing dictionary
programming_dictionary = {}

# edit an item in a dictionary
programming_dictionary['bugs'] = "A moth in your computer"

# Loop through a dictionary
for thing in programming_dictionary:
    print(thing)

print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")

# Write a program that converts their scores to grades. By the end of your program, you should have a new dictionary called student_grades that should contain student names for keys and their grades for values. The final version of the student_grades dictionary will be checked.

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}


#TODO-2: Write your code below to add the grades to student_grades.👇
for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80: 
        student_grades[student] = "Exceeds Expectations"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"
        


print(student_grades)

print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")

# My OWN Exercise 

basketball_player_scores = {
  "Jordan": 62,
  "Kyrie": 39,
  "Curry": 49, 
  "Kevin": 29,
  "Durant": 52,
}

basketball_player_ranking = {}

for player in basketball_player_scores:
    score = basketball_player_scores[player]

    if score > 60:
        basketball_player_ranking[player] = "All of Fame"
    elif score > 50:
        basketball_player_ranking[player] = "Final MVP"
    elif score > 40:
        basketball_player_ranking[player] = "Conference MVP"
    elif score > 30:
        basketball_player_ranking[player] = "Season MVP"
    else:
        basketball_player_ranking[player] = "Above Average Player"


print(basketball_player_ranking)

print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")

# Nesting

capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nesting a list in a dictionary

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}
# Nesting Dictioanry in a Dictionary

travel_log_2 = {
    "France": {"cities_visited":["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visited":["Berlin", "Hamburg", "Stuttgart"], "total_visits": 7},
}

# Nesting a Dictionary in a list

travel_log_2 = [
    {
    "country": "France",
    "cities_visited":["Paris", "Lille", "Dijon"], 
    "total_visits": 12
    },
    {
        "country": "Germany",
        "cities_visited":["Berlin", "Hamburg", "Stuttgart"], 
        "total_visits": 7
    },
]

# Write a function that will work with the following line of code on line 21 to add the entry for Russia to the travel_log.

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

def add_new_country(country_visited, time_visited, cities_visited):
    new_country = {}
    new_country["country"] = country_visited
    new_country["visits"] = time_visited
    new_country["cities"] = cities_visited
    travel_log.append(new_country)

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)

print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")


from art import logo
print(logo)

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  # bidding_record = {"Angela": 123, "James": 321}
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid: 
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
  name = input("What is your name?: ")
  price = int(input("What is your bid?: $"))
  bids[name] = price
  should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
  if should_continue == "no":
    bidding_finished = True
    find_highest_bidder(bids)
  
