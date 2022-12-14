import random
import math

class hero:
    def __init__(self, Hhealth, Hattack, Hluck, Hranged, Hdefence, Hmagic, Hname):
        self.health = Hhealth
        self.attack = Hattack
        self.luck = Hluck
        self.ranged = Hranged
        self.defence = Hdefence
        self.magic = Hmagic
        self.name = Hname

    def getHealth(self):
        return self.health
    def getAttack(self):
        return self.attack
    def getLuck(self):
        return self.luck
    def getRanged(self):
        return self.ranged
    def getDefence(self):
        return self.defence
    def getMagic(self):
        return self.magic
    def getName(self):
        return self.name

    def setHealth(self, newHealth):
        self.health = newHealth
    def setAttack(self, newAttack):
        self.attack = newAttack
    def setLuck(self, newLuck):
        self.luck = newLuck
    def setRanged(self, newRanged):
        self.ranged = newRanged
    def setDefence(self, newDefence):
        self.defence = newDefence
    def setMagic(self, newMagic):
        self.magic = newMagic
    def setName(self, newName):
        self.name = newName


class enemy:
    def __init__(self, Ehealth, Eattack, Especial, Echance, Ename):
        self.health = Ehealth
        self.attack = Eattack
        self.special = Especial
        self.chance = Echance
        self.name = Ename

    def getHealth(self):
        return self.health
    def getAttack(self):
        return self.attack
    def getSpecial (self):
        return self.special
    def getChance(self):
        return self.chance
    def getName(self):
        return self.name

    def setHealth(self, newHealth):
        self.health = newHealth
    def setAttack(self, newAttack):
        self.attack = newAttack
    def setSpecial(self, newSpecial):
        self.special = newSpecial
    def setChance(self, newChance):
        self.chance = newChance
    def setName(self, newName):
        self.name = newName



class boss (enemy):
    def __init__(self, Ehealth, Eattack, Especial, Echance, Ename, EsuperMove):
        super().__init__(Ehealth, Eattack, Especial, Echance, Ename)

        self.superMove = EsuperMove

    def getSuper(self):
        return self.superMove
    
    def setSuper(self, newSuperMove):
        self.superMove = newSuperMove

def enemyGen(levelBoss):
    temp = []
    file = open("adjective.txt","r")
    lines = file.readlines()
    adjective = lines[random.randint(0,len(lines)-1)][:-1]
    file.close
    file = open("animal.txt","r")
    lines = file.readlines()
    animal = lines[random.randint(0,len(lines)-1)][:-1]
    file.close

    if levelBoss == False:
        health = random.randint(50,100)
        attack = random.randint(10,15)
        special = random.randint(10,20)
        chance = random.randint(1,10)

        return enemy(health, attack, special, chance, adjective+" "+animal)

    else:
        health = random.randint(200,250)
        attack = random.randint(20,40)
        special = random.randint(50,60)
        chance = random.randint(1,8)
        superMove = random.randint(100,200)

        return boss(health, attack, special, chance, adjective+" "+animal, superMove)

def enemyAttack(hitChance, attackValue, name, defence):
    print(name, "is winding up for an attack...")
    hit = random.randint(0,10)
    if hitChance >= hit:
        print("it hits the hero!!!")
        loss = attackValue - defence
        print("You stagger losing...", loss, "health")
        return math.ceil(loss)
    else:
        print("The enemy misses!")
        return 0

def hitChance(luck):
    hit = random.randint(0,4)
    if luck < hit:
        print("MISS!")
        return False

    else:
        print("You hit the enemy!")
        return True

def isDead(health):
    if health < 1:
        return True
    else:
        return False

def loot(luck, genCharacter):
    lootChance = random.randint(0,4)
    if luck < lootChance:
        print("NO LOOT FOR YOU!")

    else:
        tableNum = random.randint(0,4)
        lootTableList = ["items","ranged","defence","magic","attack"]
        itemType = lootTableList[tableNum]
        file = open(itemType+".txt","r")
        lines = file.readlines()

        print("The enemy dropped a....")

        item = random.randint(0,len(lines)-1)

        itemLine = lines[item]
        splitItemLine = itemLine.split(",")

        name = splitItemLine[0]
        value = int(splitItemLine[1])

        print(name)

        if itemType == "attack":
            genCharacter.setAttack(genCharacter.getAttack()+value)
            print("Your new attack is...")
            print(genCharacter.getAttack())

        elif itemType == "ranged":
            genCharacter.setRanged(genCharacter.getRanged()+value)
            print("Your new Ranged Attack is...")
            print(genCharacter.getRanged())

        elif itemType == "defence":
            genCharacter.setDefence(genCharacter.getDefence()+value)
            print("Your new attack is...")
            print(genCharacter.getDefence())

        elif itemType == "magic":
            genCharacter.setMagic(genCharacter.getMagic()+value)
            print("Your new Magic attack is...")
            print(genCharacter.getMagic())

        else:
            
            if splitItemLine[2] == "luck":
                genCharacter.setLuck(genCharacter.getLuck()+value)
                print("Your new Luck  is...")
                print(genCharacter.getLuck())

            elif splitItemLine[2] == "health":
                genCharacter.setHealth(genCharacter.getLuck()+value)
                print("Your new Health  is...")
                print(genCharacter.getHealth())

                                     
def gameOver(enemyDead):
    if enemyDead == True:
        print("Time for another battle!!!")

    else:
        print("You are out health")
        print("Better luck next time!!")
        exit()

def battle(genEnemy, genCharacter):
    print("Whats that coming over the hill?????")
    print("Its a...", genEnemy.getName(), "Looking for a fight!")
    print("Check out its stats....")
    print(vars(genEnemy))

    battle = True

    while battle == True:
        
        print("1. Sword Attack\n2. Ranged Attack \n3. Magic Attack")
        choice = input()

        while choice != "1" and choice != "2" and choice != "3":
            print("OOPS....Only enter 1, 2 or 3...")
            print("1. Sword Attack\n2. Ranged Attack \n3. Magic Attack")
            choice = input()

        if choice == "1":
            damage = genCharacter.getAttack()

        elif choice == "2":
            damage = genCharacter.getRanged()

        else:
            damage = genCharacter.getMagic()

        print("You wind up for the attack!!!...")
        hit = hitChance(genCharacter.getLuck())

        if hit == True:
            genEnemy.setHealth(genEnemy.getHealth() - damage)
            print("You've hit the enemy!!!")
            print("The Enemies health is now....", genEnemy.getHealth())

        else:
            print("Your attack missed!")

        enemyDead = isDead(genEnemy.getHealth())

        if enemyDead == False:
            genCharacter.setHealth(genCharacter.getHealth() - enemyAttack(genEnemy.getChance(), genEnemy.getAttack(), genEnemy.getName(), genCharacter.getDefence()))
            
            characterDead = isDead(genCharacter.getHealth())

            if characterDead == True:
                battle = False
                return False

            else:
                print("Your characters remaining health is....", genCharacter.getHealth())

        else:
            battle = False
            print("You have defeated the enemy!")
            print("Did it drop any loot?.....")
            loot(genCharacter.getLuck(), genCharacter)

            return True



                
levelBoss = False
                                   
genCharacter = hero(100, 10, 11, 12, 1, 14, "LEE!")


print(vars(genCharacter))

whoDied = battle(enemyGen(levelBoss), genCharacter)
gameOver(whoDied)

whoDied = battle(enemyGen(levelBoss), genCharacter)
gameOver(whoDied)

whoDied = battle(enemyGen(levelBoss), genCharacter)
gameOver(whoDied)



print(vars(genCharacter))

    