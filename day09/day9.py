person ={"name":"siam","age":22,122:"hell"}

print(person["name"])
print(person["age"])
print(person[122])

person["name"] = "sami"
person[133] = "hello"

print(person)

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

for student in student_scores:
    print(student_scores[student])


    
def converts():
    grades ={}
    for key in student_scores:
        if student_scores[key] >= 90:
            grades[key] = "A"
        elif student_scores[key]  >= 80:
            grades[key] = "B"
        elif student_scores[key]  >= 70:
            grades[key] = "C"
        elif student_scores[key]  >= 60:
            grades[key] = "D"
        else:
            grades[key] = "F"

    return grades
    
    
student_grades = converts()
print(student_grades)



travel_log ={
    "france":['paris', 'lille', 'lyon'],
    "food":{
        "breakfast": "egg",
        "lunch": "rice",
        "dinner": "fish"
    },
    "spain": "madrid"
}

print(travel_log["france"][0])
print(travel_log["food"]["breakfast"])

for key in travel_log:
    print(key)
    for city in travel_log[key]:
        print(city)