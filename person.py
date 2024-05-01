class Person:
    def __init__(self, name, age, gender, interests):
        self.name = name
        self.age = age
        self.gender = gender
        self.interests = interests

    def interests_(self):
        list_of_interests = []
        if self.interests == []:
            return "I have no interests."
        elif len(self.interests) == 1:
            interests = " ".join(self.interests)
            return f"My interest is {interests}."
        else:
            for i in range(len(self.interests) - 1):
                list_of_interests.append(self.interests[i])
            interests = ", ".join(list_of_interests)
            last_interest = self.interests[-1]
            return f"My interests are {interests} and {last_interest}."

    def hello(self):
        return f"Hello, my name is {self.name}, my gender is {self.gender} and I am {self.age} years old. {self.interests_()}"


if __name__ == "__main__":
    person = Person(
        "Ryan", 30, "male", ["being a hardarse", "agile", "SSD hard drives"]
    )
    greetings = person.hello()
    print(greetings)
