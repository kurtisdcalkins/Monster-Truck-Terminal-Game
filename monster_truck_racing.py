# Import the Random library for use in the game
import random

class Truck:
    #Creates a truck class
    def __init__(self, name, power, handling, health = 1.00):
        self.name = name
        self.power = power
        self.handling = handling
        self.health = health
        self.is_broken = False

    def __repr__(self):
        return "{name}: \n       Power rating: {power} out of 10\n       Handling rating: {handling} out of 10".format(name = self.name, power = self.power, handling = self.handling)

    def damaged(self, amount):
        # Truck's health decreases when damaged. The amount is how much risk the driver takes.
        if amount > 0:
            self.health -= float(amount * random.random() / 10)
            if self.health <= 0:
              self.health = float(0)
              self.is_broken = True

    def fix(self):
        # Fixing a truck will change its is-broken status to False
        self.is_broken = False
        # The fix can only increase the health of the truck by 2 points
        if self.health == 0:
            self.health = float(.2)
        print("You fixed {name} and can now race again!".format(name = self.name))

    def rep(self):
        # Repairs a truck to give it more health
        # If the truck is broken, then fix it
        if self.health == 0:
            self.fix()
        # Adds health to the truck, but can never get to max health from a repair
        self.health += float((1-self.health)*.6)


class Driver:
    #Creates a driver class
    def __init__(self, name, truck, skill = 3, lost = False, num_repairs = 1, risk = -1):
        self.name = name
        self.truck = truck
        self.skill = skill
        self.lost = lost
        self.num_repairs = num_repairs
        self.risk = risk

    def __repr__(self):
        return "{name} is racing in {truck}! {name} starts out with a skill level of {skill} out of 10 and can gain skill points the more races they compete in. \nYou can only make one repair during the racing competition, so use it strategically.".format(name = self.name, skill = self.skill, truck = self.truck.name)
    
    def driver_lost(self):
        driver.lost = True

    def gain_skill(self):
        # For every race a driver wins, they gain some skill points
        self.skill += 1

    def repair_truck(self):
        # You can choose to repair your truck
        if self.truck.is_broken == False and self.num_repairs == 0:
            print('\nYou\'ve used up all of your repairs. You must continue racing with the truck as-is.')
        if self.truck.is_broken and self.num_repairs > 0:
            print('You\'re truck is broken. You must repair the truck to continue racing.')
            input('Press "Enter" to repair the truck')
            self.truck.fix()
            self.num_repairs -= 1
            print("You made some repairs on {truck} and it now has {health:.0%} health.".format(truck = self.truck.name, health = self.truck.health))
        else:
            if driver.truck.health < 1 and self.num_repairs > 0:
                make_repair = input("Do you want to make a repair before the next race ('Y' or 'N')? You do not have to right now. ")
                if make_repair.capitalize() == 'Y': 
                    self.truck.rep()
                    self.num_repairs -= 1
                    print("You made some repairs on {truck} and it now has {health:.0%} health.".format(truck = self.truck.name, health = self.truck.health))
        


# Create a racing bracket as a dictionary
def bracket_setup(num_races, race_round):
    input('Welcome to '+race_round+'! Press "Enter" to view the racing match-ups.\n')
    count = 0
    while count < (num_races): # To create the match-ups
        key = random.choice(entrants) # randomly selects one competitor and assigns it to a key
        entrants.remove(key) # removes that competitor from the list for the next random selections
        value = random.choice(entrants)
        entrants.remove(value)
        round[key] = value # Adds the two racing competitors to a dictionary as a key, value pair
        count += 1
    # Showing the racing bracket with just the truck names
    for key, value in round.items():
        if key != driver and value != driver:
            print(key.truck.name + ' vs ' + value.truck.name)
            # Assign a random risk level to each of the drivers
            key.risk = random.randint(1, 9)
            value.risk = random.randint(1, 9)
        if key == driver:
            opponent_name = value.name
            opponent_truck = value.truck.name
            print('->' + key.truck.name + '(You) vs ' + value.truck.name + '<-')
        if value == driver:
            print('->' + key.truck.name + ' vs ' + value.truck.name + '(You)<-')
            opponent_name = key.name
            opponent_truck = key.truck.name
    # Determines if the player can still race and, if so, shows their opponent and asks for the risk level
    if (driver in round.keys()) or (driver in round.values()):   # Finds the driver if it is a key and returns the opponent which is the associated value
        print(f"\nYou will be racing against {opponent_name} in {opponent_truck}.")
        # Ask the driver how much to risk damage (over-ride the value randomly chosen in 'race_setup')
        driver.risk = int(input("\nYou can push your truck really hard to win the race. However, the more you push its limits, the more likely you are to damage the truck during the race. How much risk are you willing to take on a scale of 0-10, 10 being the most risky? "))
        while driver.risk not in range(0, 11):
            driver.risk = int(input("\nThat is not a valid risk value. Please choose a risk value between 0 and 10. "))
        print(f'You have chosen a risk level of: {driver.risk}')   
    else:
        print('\nYou\'re out of the competition. See who wins below!')
    
def racing(race_round):
    print('\n\nThe racing round results are shown here:')
    for key, value in round.items():
        race(key, value)
    round_results()
    if race_round != 'the Finals':
        racer_updates()
        if driver.lost == True:
            pass
        else:
            driver.repair_truck()
    else:
        for key, value in results.items():
            if key == driver:
                print(f"\nYou beat {value.name} in {value.truck.name} in the Finals! \nYou have won the racing championship!!!!")
            if value == driver:
                print(f"\nYou lost to {key.name} in {key.truck.name} in the Finals! Better luck next time.")
            if key != driver and value != driver:
                print(f"\n{key.name} in {key.truck.name} beat {value.name} in {value.truck.name} in the Finals!\n{key.name} in {key.truck.name} is the racing champion!!!!!")



# Racing compares the values for the driver and truck and determines a winner
def race(racer1, racer2):
    # Calculate the racing rating value for each racer
    # 'racer.truck.health' scales the truck's power and handling
    # 'racer.risk' essentially increases the driver skill
    racer1_rating = (racer1.truck.health)*(racer1.truck.power + racer1.truck.handling) * (racer1.skill * (1+racer1.risk/10))
    racer2_rating = (racer2.truck.health)*(racer2.truck.power + racer2.truck.handling) * (racer2.skill * (1+racer1.risk/10))
    # Every race, the trucks can gain damage based on how much risk the driver takes
    racer1.truck.damaged(racer1.risk)
    racer2.truck.damaged(racer2.risk)
    # Compares the racer ratings for the race and prints the round results
    if racer1_rating >= racer2_rating:
        results[racer1] = racer2
    if racer1_rating < racer2_rating:
        results[racer2] = racer1

#Displays the racing round results and adds skill to the winning driver
def round_results():
    for key, value in results.items():
        key.gain_skill()
        if key == driver:
            print(f'->You defeated {value.truck.name}!<-')
        if value == driver:
            print(f'->{key.truck.name} defeated you<-')
        if key != driver and value != driver:
            print(f'{key.truck.name} defeated {value.truck.name}')

# Adds the winners to the entrants list unless their truck is broken and cannot be repaired in which case the loser of that race will replace them
def racer_updates():
    summary = ''
    for key, value in results.items():
        if key.truck.is_broken == True and key.num_repairs == 0:
            entrants.append(value)
            print(f'{key.truck.name} is broken and cannot be repaired for the next race. {value.truck.name} will advance in place of {key.truck.name}')
            if key == driver:
                summary = 'Although, you won the race, you are out of the competition. You will have to watch the rest of the races as a spectator.'
            if value == driver:
                summary = f'Although you lost the race, {key.truck.name} is now broken and out of the competition. You take its place in the next round of racing.' + '\nAfter the race your truck has {health:.0%} health.'.format(health = driver.truck.health)
        else:
            entrants.append(key)
            if key == driver:
                summary = f'You beat {value.truck.name} and are moving on to the next round!'+"\nYou now have a skill rating of {skill}!".format(skill = driver.skill) + '\nAfter the race your truck has {health:.0%} health.'.format(health = driver.truck.health)
            if value == driver:
                driver.driver_lost()
                summary = 'You have lost the race and are now out of the competition. You will have to watch the rest of the races as a spectator.'
    print("\n" + summary + "\n")

        
# Initializing the Truck class with all of the choices of trucks
a = Truck("Bigfoot", 8, 9)
b = Truck("Grave Digger", 8, 10)
c = Truck("Toxic", 7, 7)
d = Truck("Overkill Evolution", 8, 9)
e = Truck("Avenger", 8, 7)
f = Truck("Black Pearl", 8, 9)
g = Truck("Son-uva Digger", 9, 10)
h = Truck("Max-D", 9, 8)
i = Truck("Blue Thunder", 8, 9)
j = Truck("Bounty Hunter", 9, 9)
k = Truck("Iron Outlaw", 8, 8)
l = Truck("Over Bored", 9, 9)
m = Truck("El Toro Loco", 8, 7)
n = Truck("Stone Crusher", 8, 7)
o = Truck("Raminator", 7, 9)
p = Truck("Rage", 7, 7)

# Creating variables
other_trucks = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p] # Full list of trucks
truck_choices = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p'] # A list of choices for user input selection
chosen_truck = '' #Creating an empty variable. This will be assigned by the input choice from the player
#summary = ''

# --------Start of the Game play---------
# Asks for the driver's name using input
driver_name = input("Welcome to the the monster truck race! Please enter your name: ")

# Choose difficulty rating
difficulty = int(input("Hi " + driver_name + "! What difficulty rating would you like? Type the number corresponding to the difficulty rating: \n1) Easy \n2) Medium \n3) Difficult\n"))

# Uses input to allow the player to choose their truck (they must choose a letter)
choice = input(f"What truck would you like to drive? Type the letter of the truck you choose: \na) {a} \nb) {b} \nc) {c} \nd) {d} \ne) {e} \nf) {f} \ng) {g} \nh) {h} \ni) {i} \nj) {j} \nk) {k} \nl) {l} \nm) {m} \nn) {n} \no) {o} \np) {p} \n")

# If a choice does not match the pre-defined list of truck_choices, it will prompt for a choice again
while choice not in truck_choices:
    # Uses input to allow the player to choose their truck (they must choose a letter)
    choice = input(f"That is not a valid choice! Which truck would you like to drive? Type the letter of the truck you choose: \na) {a.name} \nb) {b.name} \nc) {c.name} \nd) {d.name} \ne) {e.name} \nf) {f.name} \ng) {g.name} \nh) {h.name} \ni) {i.name} \nj) {j.name} \nk) {k.name} \nl) {l.name} \nm) {m.name} \nn) {n.name} \no) {o.name} \np) {p.name} \n")


# Matches the string choice in the truck_choices list to the other_trucks (since the indices are the same) and assigns the Truck to chosen_truck variable
chosen_truck = other_trucks[truck_choices.index(choice)]
# Removes the chosen truck from the list of other_trucks.
other_trucks.remove(chosen_truck)

# Displays the truck chosen and then waits for input to continue
input("You have chosen to drive " + str(chosen_truck.name) +"!" + "\nPress 'Enter' to continue.\n")

# Assigns the Driver class with the driver's names and their trucks
driver = Driver(driver_name, chosen_truck)
opponent1 = Driver('John', other_trucks[0], random.randint(1, difficulty))
opponent2 = Driver('Jeff', other_trucks[1], random.randint(1, difficulty))
opponent3 = Driver('Jane', other_trucks[2], random.randint(1, difficulty))
opponent4 = Driver('Julia', other_trucks[3], random.randint(1, difficulty))
opponent5 = Driver('Julio', other_trucks[4], random.randint(1, difficulty))
opponent6 = Driver('Jaime', other_trucks[5], random.randint(1, difficulty))
opponent7 = Driver('James', other_trucks[6], random.randint(1, difficulty))
opponent8 = Driver('Jurickson', other_trucks[7], random.randint(1, difficulty))
opponent9 = Driver('Javier', other_trucks[8], random.randint(1, difficulty))
opponent10 = Driver('Jesse', other_trucks[9], random.randint(1, difficulty))
opponent11 = Driver('Jeremy', other_trucks[10], random.randint(1, difficulty))
opponent12 = Driver('Josh', other_trucks[11], random.randint(1, difficulty))
opponent13 = Driver('Jake', other_trucks[12], random.randint(1, difficulty))
opponent14 = Driver('Jen', other_trucks[13], random.randint(1, difficulty))
opponent15 = Driver('Jessica', other_trucks[14], random.randint(1, difficulty))

# Creates an entrants list for use in the function 'bracket_setup' to create the racing match-ups
entrants = [driver, opponent1, opponent2, opponent3, opponent4, opponent5, opponent6, opponent7, opponent8, opponent9, opponent10, opponent11, opponent12, opponent13, opponent14, opponent15]

# Tell the player about their driver
print(driver)

# Round 1
print("\n"+"="*10 + "Round 1" + "="*10)
round = {}
results = {}
bracket_setup(8, 'Round 1')

input("\nPress 'Enter' to start the racing!")
#Race
racing('Round 1')
#print(summary)


# Round 2
print("\n"+"="*10 + "Round 2" + "="*10)
round = {}
results = {}
bracket_setup(4, 'Round 2')

input("\nPress 'Enter' to start the racing!")
#Race
racing('Round 2')


# Semi-Final Round
print("\n"+"="*10 + "Semi-Final Round" + "="*10)
round = {}
results = {}
bracket_setup(2, 'the Semi-finals')

input("\nPress 'Enter' to start the racing!")
#Race
racing('the Semi-finals')



# Final Round
print("\n"+"="*10 + "Final Round" + "="*10)
round = {}
results = {}
bracket_setup(1, 'the Finals')

input("\nPress 'Enter' to start the racing!")
#Race
racing('the Finals')