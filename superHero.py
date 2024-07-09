import json


class Heroes:
    def __init__(self) -> None:
        self.location = "supes.json"
        self.file = open(self.location)
        self.load = json.load(self.file)

    def readFile(self):
        return self.load


class Humans:
    def __init__(self) -> None:
        self.location = "humans.json"
        self.file = open(self.location)
        self.load = json.load(self.file)

    def readFile(self):
        return self.load


class Supes(Heroes):
    def __init__(self) -> None:
        # super().__init__()
        self.humans = NormalHumans()

    def __theVanguard(self):
        print(self.__class__.__name__)
        return Heroes.readFile(self).get('Universe1')

    def _membersOfTheVanguard(self):
        return Supes.__theVanguard(self).get('Members')

    def __theElementals(self):
        return Heroes.readFile(self).get('Universe2')

    def _membersOfTheElementals(self):
        return Supes.__theElementals(self).get('Members')

    def getHumans(self):
        return self.humans.theEverydayHeroes()


class NormalHumans(Humans):
    def theEverydayHeroes(self):
        return Humans.readFile(self)


read = Supes()
tv = read.getHumans()
# read = NormalHumans()
# tv = read.theEverydayHeroes()
print(tv)
