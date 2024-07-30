'''
Explaining OOP concept in a easy way.
Points to remember:
_name(single underscore) represents Protected class
__name(double underscore) represents Private class
We will see when and how to use these.

Consider a storyline set in a universe where humans have developed
a serum that grants superpowers to individuals with specific DNA
disorders. One day, these superheroes decide to establish a headquarters
where they can monitor all crimes and stop them effectively.

So here, let us consider a hierarchy Humans > Supes > Headquaters i.e, Humans
being at top of the hierarchy
'''
import json

'''
Variables which are used repeatedly across the program
Best practice to do while using variables
'''
classHeroes = "Heroes"
classHumans = "Humans"
classNormalHumans = "NormalHumans"


class Humans:
    '''
    Since Humans are at top level who createdf the serum. They are
    the masters making this class as Base or Master class


    Below are the Class attributes with _ before the variable
    '''

    _humans = "NormalHumans"
    _members = "Members"

    def __init__(self) -> None:
        '''
        Init function always executes whenever you create an instance of a class.
        Here whenever you create an instance of class Humans, __init__executes.
        So all the dependencies of a class can be written here. For ex: configurations,
        loading of files, database connections etc.,
        '''
        self.location = "humans.json"
        self.file = open(self.location)
        self.load = json.load(self.file)

    def readFile(self):
        return self.load


class Heroes(Humans):
    '''
    Class - Which has properties and methods
    In our case SuperHeroes have general properties like universe, name and super power
    and methods vary from each super heroes since each of them have different powers.
    Eg. Ironman and Captain america are humans and they have their names(properties). 
    However, their names are different and also their superpower(methods). In general it is a function
    which takes args and qwargs to perform action based on their properties.

    inheritance - this class Heroes inherit from master class Humans
                        or
    Heroes class is derived from Humans class.
                        or
    Heroes is subclass of Humans

    '''
    _members = "Members"  # class attribute
    _universe1 = "Universe1"
    _universe2 = "Universe2"

    @staticmethod
    def intro():
        '''
        A static method, does nothing. Used to structure a class
        You can put things that are static.
        '''
        text = ''' ____                        _                              
/ ___| _   _ _ __   ___ _ __| |__   ___ _ __ ___   ___  ___ 
\___ \| | | | '_ \ / _ \ '__| '_ \ / _ \ '__/ _ \ / _ \/ __|
 ___) | |_| | |_) |  __/ |  | | | |  __/ | | (_) |  __/\__ |
|____/ \__,_| .__/ \___|_|  |_| |_|\___|_|  \___/ \___||___/
            |_|                                             
            '''
        print(text)

    def __init__(self) -> None:
        self.location = "supes.json"
        self.file = open(self.location)
        self.load = json.load(self.file)
        Heroes.intro()

    def readFile(self):
        return self.load

    def __addHeros(self, data):
        with open(self.location, 'w') as file:
            json.dump(data, file, indent=4)

    def validateMember(self, new_member, universe):
        data = self.readFile()
        vanguard = data[universe][Heroes._members]
        for name in vanguard:
            if name.get("Name") == new_member.get("Name"):
                return f"{new_member['Name']} already exists"
        vanguard.append(new_member)
        self.__addHeros(data)
        return f"New member {new_member['Name']} added to The Vanguard."


class Supes(Heroes):
    '''
    inheritance - this class Supes inherit from class Heroes
                        or
    Supes class is derived from Heroes class.
                        or
    Supes is subclass of Heroes
    '''

    def __init__(self) -> None:
        super().__init__()
        self.humans = NormalHumans()

    def whois(self):
        print("we are Supes")

    def __theVanguard(self):
        print(self.__class__.__name__)
        return Heroes.readFile(self).get(self._universe1)

    def _membersOfTheVanguard(self):
        return Supes.__theVanguard(self).get(self._members)

    def __theElementals(self):
        return Heroes.readFile(self).get(self._universe2)

    def _membersOfTheElementals(self):
        if self.__class__.__name__ == classNormalHumans:
            print(
                f"Hello {self.__class__.__name__}, you dont get to see who we are and good luck troubleshooting this error👇")
            return None
        return Supes.__theElementals(self).get(self._members)

    def getHumans(self):
        return self.humans.theEverydayHeroes().get(self.humans._humans).get(self._members)


class NormalHumans(Humans):
    def whois(self):
        print("we are Humans")

    def theEverydayHeroes(self):
        return Humans.readFile(self)

    def getSupes(self):
        return Supes._membersOfTheElementals(self)


def introduce(who):
    return who.whois()


class HeadQuaters(Supes, NormalHumans):
    '''
    Headquarters is a place where everything is monitored.
    It can access both Supes and Humans.
    Therefore, it inherits from more than one class.
    Specifically, Headquarters inherits from both Supes and NormalHumans,
    which is an example of multiple inheritance.'''

    @staticmethod
    def intro():
        print("Accessing data from headquaters...")

    def __init__(self) -> None:
        super().__init__()
        self.humans = NormalHumans()
        HeadQuaters.intro()

    def imHead(self):
        print("Hello from Head quaters")

    def universe(self):
        for universe in self.readFile():
            print(
                f"Universe name {universe}. Team name {self.readFile().get(universe).get('TeamName')}")
        for uni in self.humans.theEverydayHeroes():
            print(
                f"Universe name {uni}. Team name {self.humans.theEverydayHeroes().get(uni).get('TeamName')}")

    def getMembers(self, universe):
        if universe == self.humans._humans:
            for members in self.humans.theEverydayHeroes().get(
                    universe).get('Members'):
                print(f'Name: {members.get("Name")}')
                print(f'Superpower: {members.get("Superpower")}')
                print(f'Role: {members.get("Role")}')
        else:
            for members in self.readFile().get(universe).get("Members"):
                print(f'Name: {members.get("Name")}')
                print(f'Superpower: {members.get("Superpower")}')
                print(f'Role: {members.get("Role")}')


read = Supes()
introduce(read)
read = NormalHumans()
introduce(read)
tv = read.theEverydayHeroes()
read = HeadQuaters()
tv = read.imHead()
print(tv)
heroes = Heroes()
print(heroes.intro())
new_member = {
    "Name": "NeuroNet",
    "Superpower": "Technopathy > can control and communicate with electronic devices, hack systems, and manipulate digital information.",
    "Role": "Tech Specialist, Intelligence Operative",
    "Background": "A former cyber security expert who gained the ability to interface with technology directly after an experimental brain-computer interface went wrong."
}

add = heroes.validateMember(new_member, "Universe1")
print(add)
print(heroes.universe())
uni = heroes.getMembers("NormalHumans")
hum = heroes.getSupes()
