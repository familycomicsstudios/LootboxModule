import random
class Lootbox():
    def __init__(self, rarity, loot, name="Normal"):
        self.rarity = rarity
        self.lootTable = loot
        self.name = name
    def __str__(self):
        return self.rarity+" "+self.name+" Lootbox"
    def open(self):
        lootList = []
        for thingy in self.lootTable:
            for i in range(0,self.lootTable[thingy]):
                lootList.append(thingy)
        random.shuffle(lootList)
        return lootList[0]
    def open_text(self):
        opened = self.open()
        print("You opened a "+self.__str__()+" and got "+opened+"!")
        return opened
    def lootList(self):
        lootList = []
        for thingy in self.lootTable:
            for i in range(0,self.lootTable[thingy]):
                lootList.append(thingy)
        return lootList

if __name__ == "__main__":
    # Run tests
    loot = Lootbox("Uncommon",{"10 Coins":5, "20 Coins":2})
    print(loot)
    print(loot.open_text())