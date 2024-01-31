class Person():
    def __init__(self, name, bank_account = 25, happiness = 8, hygiene = 8):
        self.name = name
        self.bank_account = bank_account
        self.happiness = happiness
        self.hygiene = hygiene

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if type(value) == str and len(value) > 0:
            self._name = value
        else:
            raise ValueError("invalid name")
        
    def is_clean(self):
        if self.hygiene > 7:
            return True and "I am clean"
        else:
            return False and "I am not clean"

    def is_happy(self):
        if self.happiness > 7:
            return True and "I am happy"
        else:
            return False and "I am not happy"

    def get_paid(self, amount):
        if type(amount) == (int or float) and amount > 0:
            self.bank_account += amount
            return "all about the benjamins"
        else:
            return "invalid amount"

    def take_bath(self):
        self.hygiene += 4
        return "♪ Rub-a-dub just relaxing in the tub ♫"

    def work_out(self):
        self.happiness += 2
        self.hygiene -= 3
        return "♪ another one bites the dust ♫"
    
    def call_friend(self, friend):
        if isinstance(friend, Person):
            friend.happiness += 3
            self.happiness += 3
            return f"Hi {friend.name}! It's {self.name}. How are you?"
        else:
            return "invalid friend"
    
    def start_conversation(self, friend, topic):
        if isinstance(friend, Person):
            if topic == "politics":
                self.happiness -= 2
                friend.happiness -= 2
                return "blah blah partisan blah lobbyist"
            elif topic == "weather":
                self.happiness += 1
                friend.happiness += 1
                return "blah blah sun blah rain"
            else:
                return "blah blah blah blah blah"
        else:
            return "invalid friend"
        

tim = Person("Tim", 30, 8, 8)
hussein = Person("Hussein", 60, 9, 10)

print(tim.call_friend(hussein))
print(tim.start_conversation(hussein, "sports"))
print(hussein.get_paid(1000))
print(hussein.is_happy())
print(hussein.is_clean())