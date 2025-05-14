def greet():
    print("Hello, World!")
    print("This is a test function.")
    print("It will be used to test the day8 module.")



def name(user):
    print(f"hell {user}")

name('siam')

def life_in_weeks(year_passed):
    weeks_per_year = 52
    total_weeks  = 90 * weeks_per_year
    
    weeks_left = total_weeks - (year_passed * weeks_per_year)
    print(f'You have lived for {year_passed * weeks_per_year} weeks.')
    print(f'You have {total_weeks} weeks in total.')
    print(f'You have {weeks_left} weeks left.')
    print(f'You have {weeks_left // 52} years left.')


# life_in_weeks(25)

def calculate_love_score(name1, name2):
    # Combine and normalize the names
    combined_names = (name1 + name2).replace(" ", "").lower()

    # Count letters in "TRUE"
    true_count = sum(combined_names.count(letter) for letter in "true")

    # Count letters in "LOVE"
    love_count = sum(combined_names.count(letter) for letter in "love")

    # Combine into two-digit score
    love_score = int(f"{true_count}{love_count}")

    # Print result in required format
    print(f"Love Score = {love_score}")

calculate_love_score("sam", "Nadia")