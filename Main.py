'''
Created on Apr 30, 2021

@author: Justin Peifer
'''
#the plan is to make multiple stories that are randomly chosen, but for right now it is just one.
import random

print(f'Hello, and welcome to the greatest story simulator ever!')
print("Today's story is...")
#story=2
#use this to force it to do a specific story
story=random.randint(1,2)
if story==1:
    print('A Trip to the Zoo.')
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
elif story==2:
    print('Spooky Stuff')
    adj1=input('Please enter an adjective.')
    noun1=input('Now, enter a plural noun.')
    noun2=input('That was such a good one, can you give me another plural noun?')
    silly1=input('Next, enter a silly word.')
    liquid1=input('How about a type of liquid?')
    adj2=input('Another adjective please.')
    noun3=input('Give me another noun.')
    print("We're halfway there!")
    verb1=input('How about a verb this time?')
    verb2=input('Now lets go with two verbs that end in "ing"')
    verb3=input()
    noun4=input('Two more plural nouns.')
    noun5=input()
    noun6=input('And now a singular noun.')
    number=input('And finally, a number.')
    #this time using\n to place new lines instead of repeating print() like in story #1
    print(f"Great! Here's your story! \n American children are fascinated by {adj1} stuff - like stories that scare the {noun1} off them or make their {noun2} stand on end. \n Scientists say this is because being frightened causes the {silly1} gland to function and puts the {liquid1} into their blood. \n And everyone knows that makes kids feel {adj2}. \n When they are scared by a movie or a/an {noun3}, boys laugh and holler and {verb1}. \n But girls cover their eyes with their {noun4} and keep screaming and {verb2}.\n Most kids get over this by the time they are {number} years old. \n Then they like movies and {verb3}, or cops shooting {noun5} or if they are girls, they like movies about a boy meeting a/an {noun6} and falling in love. \n Of course, that can be scary too!")
    end=input('Hope you enjoyed it!')
else:
    print("sorry, you don't get a story")
    end=input()