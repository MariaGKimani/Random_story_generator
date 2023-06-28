# Importing random module
import random

# Storing random data into lists to create story.
when = ['A long time ago', 'Tomorrow', 'Before i was  born', 'In future', 'During Covid']
who = ['Snaida', 'Iron Man', 'Maria', 'Deo', 'Captain America']
went = ['Disney land', 'Club', 'API fest', 'Microsoft', 'Miami']
what = ['to see Disneys', 'to fight for justice', 'to dance', 'for an internship','to visit']

# Using string concatenition & randome.choice() to print a random element from all the lists 
print(random.choice(when) + ', ' + random.choice(who) + ' went to ' + random.choice(went) + ' ' + random.choice(what) + '.')