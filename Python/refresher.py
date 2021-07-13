def who_do_you_know():
    people = input("Enter the names of people you know :\n ")
   
  
  
    people_without_spaces =[person.strip() for person in people.split(",")]
    
    #for person in people_list:
     # people_without_spaces.append(person.strip())
    return people_without_spaces

def ask_user():
    person = input("Enetr a name of someone you know :\n")
    if person in who_do_you_know():
        print(f"You know {person}")


ask_user()