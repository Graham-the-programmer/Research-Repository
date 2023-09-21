import random


class Fighter:
    def __init__(self, name, nop = 2, hp = 10):
        self.name = name
        self.weapons = []
        self.nop = nop
        self.hp = hp
        self.dead = False
        

    def attack(self, other_fighter):
       dice = random.randint(1, 6)
       other_fighter.hp =  other_fighter.hp - dice
       print("{name} rolls dice and attacks {other_fighter} for {dice} points, {other_fighter} has {other_fighter_hp} hp".format(name = self.name, other_fighter = other_fighter.name, dice = dice, other_fighter_hp = other_fighter.hp))
       return dice, other_fighter.hp
    

    
    def use_potion(self):
        dice = random.randint(1, 6)
        if self.nop <= 0:
            print("{name} has no more potions, {name} hp is still {hp}".format(name = self.name, hp = self.hp))
        else:
            self.hp += dice
            if self.hp >= 10:
                self.hp = 10
            self.nop -= 1
            print("{name} used a potion for {dice} hp, {name} now has {hp} hp and {nop} potions remaining".format(name = self.name, dice = dice, hp = self.hp, nop = self.nop))

    def grab_weapon(self):
        print("--{name} pulls a weapon from the chest--".format(name = self.name))
        wep = random.choice(weapon_list)
        self.weapons.append(wep)
        print("{wep_type}: Damage: {damage} Durability: {durability}".format(wep_type = wep.type, damage = wep.damage, durability = wep.durability))
        
        if wep.durability == 0:
            self.weapons.remove(wep)
            print("{wep_type} was broken lol".format(wep_type = wep.type))

    
    
    def use_weapon(self, other_fighter):
        if self.weapons == []:
            print("You have no weapon")
        else:
             for weapon in (self.weapons):
                 print(self.weapons.index(weapon) + 1,':::',  weapon)          
                 wepchoice = input("Which weapon will you use:")
             if wepchoice == "1":
                wepchoice = self.weapons[0]
                print("You chose", wepchoice.type)                        #fix numberchoosing wep system
                damage = wepchoice.damage +  random.randint(1, 6)
                other_fighter.hp = other_fighter.hp - damage
                wepchoice.durability -= 1
                print("You attack {other} with {wep} doing {damage} damage, {other} now has {otherhp}hp and your {wep} has {dur} durability.".format(other = other_fighter.name, otherhp = other_fighter.hp, wep = wepchoice.type, damage = damage, dur = wepchoice.durability))
                if wepchoice.durability == 0:
                    self.weapons.remove(wepchoice)
                    print("Your {wep} broke".format(wep = wepchoice.type))
             else: 
                wepchoice == "2"
                wepchoice = self.weapons[1]
                print("You chose", wepchoice.type)
                damage = wepchoice.damage +  random.randint(1, 6)
                other_fighter.hp = other_fighter.hp - damage
                wepchoice.durability -= 1
                print("You attack {other} with {wep} doing {damage} damage, {other} now has {otherhp}hp and your {wep} has {dur} durability.".format(other = other_fighter.name, otherhp = other_fighter.hp, wep = wepchoice.type, damage = damage, dur = wepchoice.durability))
                if wepchoice.durability == 0:
                    self.weapons.remove(wepchoice)
                    print("Your {wep} broke".format(wep = wepchoice.type))
               
               
               
               
def death_check(self, other_fighter):     
    if self.hp <= 0:
        self.dead = True
        print("You've been killed, GAME OVER")
    elif other_fighter.hp <= 0:
        other_fighter.dead = True
        print("You killed {other}, YOU WIN!!!!".format(other = other_fighter.name))               
            

            
            
            
           
   





class Weapon:
    def __init__(self, type, damage, durability):
        self.type = type
        self.damage = damage
        self.durability = durability

    def __repr__(self):
       return("{type}: Damage: {damage} Durability: {durability}".format(type = self.type, damage = self.damage, durability = self.durability)) 
        

        

def end_of_turn():
    if f1.dead or f2.dead == True:
        print("GAME OVER")
    else:
        print("you're turn ended")
        input("press enter to continue...")
        if f2.hp <= 5 and f2.nop >= 1:
            f2.use_potion()
        else:
            f2.attack(f1)
        input("press enter to continue...")
        print("It's your turn")















a = Weapon("Sword", 5, random.randint(0, 4) )
b = Weapon("Axe", 4, random.randint(0, 4)) 
c = Weapon("Wooden plank", 1, random.randint(0, 4)) 

weapon_list = [a, b, c]




print("Welcome to simple fight v1!!")
fighter_name = input("Please choose a name for your fighter: ")

f1 = Fighter(fighter_name)
f2 = Fighter("Graham")



def player_turn():
    if f1.dead or f2.dead == True:                                    #fix this itertaing though the turns once dead and weapon selection
        print("GAME OVER")
    else:
        choice1 = input("""What do you want to do? 
                        A:  Attack
                        B:  Use potion
                        C:  Grab weapon
                        D:  Use weapon
                            :  """)
        while choice1 != 'A' and choice1 != 'B' and choice1 != "C" and choice1 != "D":
            choice1 = input("Please select A, B, C or D ")
        if choice1 == "A":
            f1.attack(f2)
        elif choice1 == "B":
            f1.use_potion()
        elif choice1 == "C":
            f1.grab_weapon()
        elif choice1 == "D":
            f1.use_weapon(f2)
            if f1.weapons == []:
                choice1 = input("Please select A, B, or C: ")
                if choice1 == "A":
                    f1.attack(f2)
                elif choice1 == "B":
                    f1.use_potion()
                elif choice1 == "C":
                    f1.grab_weapon()
           
player_turn()
death_check(f1, f2)
end_of_turn()
death_check(f1, f2)
player_turn()
death_check(f1, f2)
end_of_turn()
death_check(f1, f2)
player_turn()
death_check(f1, f2)
end_of_turn()
death_check(f1, f2)
player_turn()
death_check(f1, f2)
end_of_turn()           
player_turn()
death_check(f1, f2)
end_of_turn()
death_check(f1, f2)
player_turn()
death_check(f1, f2)
end_of_turn()
death_check(f1, f2)
player_turn()
death_check(f1, f2)
end_of_turn()
death_check(f1, f2)
player_turn()
death_check(f1, f2)
end_of_turn()               









# Add either turn class or function, have enemy ai make choice fix this

#use dictionary for 3rd class list
