#simulate coinflip
import random
outcomes={'heads':0,'tails':0}
sides=list(outcomes.keys())
for i in range(10000):
    outcomes[random.choice(sides)]+=1
print("COIN FLIP SIMULATOR")
print("Heads:",outcomes['heads'])
print("Tails:",outcomes['tails'])
    
