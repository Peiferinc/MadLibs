'''
Created on Apr 30, 2021

@author: Justin Peifer
'''
#the plan is to make multiple stories that are randomly chosen, but for right now it is just one.
print('Hello, and welcome to the greatest story simulator ever!')
adj1=input('Please enter an adjective.')
noun1=input('Now, enter a noun.')
verb1=input('Next, enter a verb (past tense).')
adverb1=input('How about an adverb?')
noun2=input('Another noun, please.')
print(f"{noun2.capitalize()} is a good one!")
noun3=input('One more noun.')
adj2=input(f'Another adjective please, {adj1} was so creative!')
print('Only four more left!')
verb2=input('Lets go with a present tense verb this time.')
adverb2=input('Now an adverb.')
verb3=input('Another past tense verb now.')
adj3=input('And finally, an adjective.')
print()
print('Perfect! Here is your story!')
print()
print(f'Today I went to the zoo.')
print(f'I saw a(n) {adj1} {noun1} jumping up and down in its tree.')
print(f' He {verb1} {adverb1} through the large tunnel that led to its {adj2} {noun2}.')
print(f'I got some peanuts and passed them through the cage to a gigantic gray {noun3} towering above my head)')
print('Feeding that animal made me hungry.')
print(f' I went to get a {adj2} scoop of ice cream. It filled my stomach.')
print(f'Afterwards I had to {verb2} {adverb2} to catch our bus.')
print(f'When I got home I {verb3} my mom for a {adj3} day at the zoo. ')
ans=input('I hope you liked it!')