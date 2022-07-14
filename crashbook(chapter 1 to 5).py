#!/usr/bin/env python
# coding: utf-8

# # chapter 2
2-3. Personal Message: Store a person’s name in a variable, and print a message to that person. Your message should be simple, such as, “Hello Eric, 
would you like to learn some Python today?”
# In[1]:


a = "janshair"


# In[2]:


print("Hello " + a + " would you like to learn some Python today?")

. Name Cases: Store a person’s name in a variable, and then print that person’s name in lowercase, uppercase, and titlecase
# In[3]:


a= "janshair"


# In[4]:


print(a.lower())
print(a.upper())
print(a.title())

2-5. Famous Quote: Find a quote from a famous person you admire. Print the 
quote and the name of its author. Your output should look something like the 
following, including the quotation marks:
# In[5]:


print("Quaid-e-Azam Once said \"think a hundred times before you take a decesion but once the decesion you have taken stand by it as a once man\"  ")


# In[6]:


print("Albert Einstein once said, 'A person who never made a mistake never tried anything new'.")

6. Famous Quote 2: Repeat Exercise 2-5, but this time store the famous person’s name in a variable called famous_person. Then compose your message 
and store it in a new variable called message. Print your message.
# In[7]:


a = "Quadi-e-Azam Once said" 
print(f"{a}, \"think a hundred times before you take a decesion but once the decesion you have taken stand by it as a once man\"")

2-7. Stripping Names: Store a person’s name, and include some whitespace 
characters at the beginning and end of the name. Make sure you use each 
character combination, "\t" and "\n", at least once.
Print the name once, so the whitespace around the name is displayed.
Then print the name using each of the three stripping functions, lstrip(), 
rstrip(), and strip()
# In[8]:


name = "Janshair"
age = 23
interest = "AI& DS"
print(f"HEllo \t{a}")


# In[9]:


print(f".My name is {name}\n.My age is {age}\n.My favourite subject is {interest}")


# In[10]:


name = " Janshair"


# In[11]:


name.lstrip()


# In[12]:


name = "Janshair "


# In[13]:


name.rstrip()


# In[14]:


name = "  Janshair  "


# In[15]:


name.strip()


# In[16]:


age = 23


# In[17]:


print("Happy "+ str(age) +"rd birthday")


# In[18]:


3/2


# In[19]:


3.0/2


# In[20]:


import math


# In[21]:


math.ceil(1.5)


# In[22]:


math.floor(1.5)

2-8. Number Eight: Write addition, subtraction, multiplication, and division 
operations that each result in the number 8. Be sure to enclose your operations 
in print statements to see the results. You should create four lines that look 
like this:
# In[23]:


a = 8+4
b = 8-2
c = 8/2
d = 8*2


# In[24]:


print(f"Addition of 8+4  is: {a}")
print(f"Subtrarction of 8-2 is: {b}")
print(f"Division of 8/2 is: {c}")
print(f"Mutiplication of 8/4 is: {d}")

2-10. Adding Comments: Choose two of the programs you’ve written, and 
add at least one comment to each. If you don’t have anything specific to write 
because your programs are too simple at this point, just add your name and 
the current date at the top of each program file. Then write one sentence 
describing what the program does.
# In[25]:


#This program show the calendar of 2023
import calendar
year =2023
print(calendar.calendar(year))

2-11. Zen of Python: Enter import this into a Python terminal session and skim 
through the additional principles.
# In[26]:


import this


# # CHAPTER #3 LIST

# In[27]:


cities = ["Karachi","Queeta","lahore","Islamabad","Muree","Hyderabad"]


# In[28]:


cities


# In[29]:


cities[0],cities[1]


# In[30]:


cities[2].title()


# In[31]:


cities[1:4]


# In[32]:


print("I live in "+cities[0].upper())

3-1. Names: Store the names of a few of your friends in a list called names. Print 
each person’s name by accessing each element in the list, one at a time
# In[33]:


names = ['Ali','Fahad','Saad','Hassan','Salah']


# In[34]:


print(names)

# 3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just 
printing each person’s name, print a message to them. The text of each message should be the same, but each message should be personalized with the 
person’s name.
# In[35]:


print("My friend name is ",names[0])
print("My friend name is ",names[1])
print("My friend name is ",names[2])
print("My friend name is ",names[3])
print("My friend name is ",names[4])

3-3. Your Own List: Think of your favorite mode of transportation, such as a 
motorcycle or a car, and make a list that stores several examples. Use your list 
to print a series of statements about these items, such as “I would like to own a 
Honda motorcycle.”
# In[36]:


cars = ['BMW','Ferrari','Civic','Lamborgini','Royce Royal']


# In[37]:


print("I would like to own " +cars[1]+ " car.")


# In[38]:


cars[0]="Tesla"


# In[39]:


cars


# In[40]:


cars.append("Ford")


# In[41]:


cars


# In[42]:


cars


# In[ ]:





# In[43]:


cars.insert(2,'Porsche')


# In[44]:


cars


# In[45]:


cars.insert(2,"Porshe")


# In[46]:


del cars[2]


# In[47]:


cars.append('Civic')


# In[48]:


cars

-4. Guest List: If you could invite anyone, living or deceased, to dinner, who 
would you invite? Make a list that includes at least three people you’d like to 
invite to dinner. Then use your list to print a message to each person, inviting 
them to dinner.
# In[49]:


dinner_list = ['Ali','Shan','Babar','Zuhair']


# In[50]:


print(dinner_list)


# In[51]:


for i in dinner_list:
    print("You are invite in dinner Mr.",i)

3-5. Changing Guest List: You just heard that one of your guests can’t make the 
dinner, so you need to send out a new set of invitations. You’ll have to think of 
someone else to invite.
# In[52]:


dinner_list.remove('Zuhair')


# In[53]:


dinner_list


# In[54]:


dinner_list.append('Saad')


# In[55]:


for i in dinner_list:
    print("You are invite in dinner Mr.",i)

3-6. More Guests: You just found a bigger dinner table, so now more space is 
available. Think of three more guests to invite to dinner.
# In[56]:


dinner_list

3-7. Shrinking Guest List: You just found out that your new dinner table won’t 
arrive in time for the dinner, and you have space for only two guests.
# In[57]:


dinner_list


# In[58]:


cars


# In[59]:


cars.sort(reverse=True)


# In[60]:


cars


# In[61]:


#For temporarily sorted
print(sorted(cars))


# In[62]:


cars.reverse()


# In[63]:


print(type(cars))


# In[64]:


print(len(cars))

3-8. Seeing the World: Think of at least five places in the world you’d like to 
visit.
•	 Store the locations in a list. Make sure the list is not in alphabetical order.
•	 Print your list in its original order. Don’t worry about printing the list neatly, 
just print it as a raw Python list.
•	 Use sorted() to print your list in alphabetical order without modifying the 
actual list.
•	 Show that your list is still in its original order by printing it.
•	 Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.
•	 Show that your list is still in its original order by printing it again.
•	 Use reverse() to change the order of your list. Print the list to show that its 
order has changed.
•	 Use reverse() to change the order of your list again. Print the list to show 
it’s back to its original order.
•	 Use sort() to change your list so it’s stored in alphabetical order. Print the 
list to show that its order has been changed.
•	 Use sort() to change your list so it’s stored in reverse alphabetical order.
Print the list to show that its order has changed.
# In[65]:


areas = ['Saudia Arab','Dubai','Malta','Japan','Phalestine']
print(areas)


# In[66]:


print(sorted(areas))


# In[67]:


print(areas)


# In[68]:


areas.reverse()


# In[69]:


areas


# In[70]:


areas.sort(reverse=True)


# In[71]:


areas


# In[72]:


areas.sort()


# In[73]:


areas


# 3-9. Dinner Guests: Working with one of the programs from Exercises 3-4 
# through 3-7 (page 46), use len() to print a message indicating the number 
# of people you are inviting to dinner.

# In[74]:


dinner_list


# In[75]:


print(len(dinner_list))

3-11. Intentional Error: If you haven’t received an index error in one of your 
programs yet, try to make one happen. Change an index in one of your programs to produce an index error. Make sure you correct the error before closing the program
# In[76]:


list1 = ['a','b','c','d']


# In[77]:


#list1[4]
list1 = [3]


# # CHAPTER 4 Working with Lists

# In[78]:


numbers = [1,2,3,4,5,6,7]
for number in numbers:
    print(number)


# In[79]:


for i in range(10):
    print(i,end = " ")


# In[80]:


names = ['Ali','Asad','Ammar','Amir','Anus']


# In[81]:


for name in names:
    print(name.upper()+ ", Welcome to the python society")
    print("I can't wait to show you new program, " + name.title() + ".\n")
    
print("Thank you Janshair!!")    

4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store these 
pizza names in a list, and then use a for loop to print the name of each pizza.

# In[82]:


pizzas = ['Fajita','Afghani','BBQ chiken','Margherita']


# In[83]:


for pizza in pizzas:
    print(pizza)

•	 Modify your for loop to print a sentence using the name of the pizza 
instead of printing just the name of the pizza. For each pizza you should 
have one line of output containing a simple statement like I like pepperoni 
pizza.
# In[84]:


for pizza in pizzas:
    print('I like ',pizza)

	 Add a line at the end of your program, outside the for loop, that states 
how much you like pizza. The output should consist of three or more lines 
about the kinds of pizza you like and then an additional sentence, such as 
I really love pizza!
# In[85]:


for pizza in pizzas:
    print('I like ',pizza)
    
print("\nAnd I love All kind of Pizza")

. Animals: Think of at least three different animals that have a common characteristic. Store the names of these animals in a list, and then use a for loop to 
print out the name of each animal.
# In[86]:


animals = ['Tiger','Lion','Leopard']
for animal in animals:
    print(animal,'is a carnivores animal.')

Modify your program to print a statement about each animal, such as 
A dog would make a great pet.
# In[87]:


for animal i  animals:
    print(animal)


# In[88]:


for i in range(1,6):
    print(i)


# In[89]:


number = set(range(1,5))


# In[90]:


print(number)


# In[91]:


numbers = list(range(1,7))
print(numbers)


# In[92]:



num = tuple(range(1,7))
print(num)


# In[93]:


even = []
odd =[]
for i in range(1,10):
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
    


# In[94]:


print(even)
print(odd)


# Simple Statistics with a List of Numbers

# In[95]:


a = [1,2,3,55,77,99,77,22,66,77,99,2,100,44,22]


# In[96]:


a


# In[97]:


b = set(a)


# In[98]:


b


# In[99]:


max(b)


# In[100]:


min(b)


# In[101]:


#LIST COMPREHESSION


# In[102]:


a = [1,2,3,4,5,6,7,8]
for x in  a:
    print(x**2)


# In[103]:


for x in range(1,6):
    print(x**2)


# In[104]:


square = [value**2 for value in range(1,10)]
print(square)


# In[105]:


a = [1,33,44,55,3,6,7]


# In[106]:


a.sort()


# In[107]:


squares = [value**2 for value in range(1,7)]
print(squares)


# 4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20, 
# inclusive.

# In[108]:


for x in range(1,21):
    print(x)

4-4. One Million: Make a list of the numbers from one to one million, and then 
use a for loop to print the numbers. (If the output is taking too long, stop it by 
pressing ctrl-C or by closing the output window.)
# In[109]:


number = [1,10,100,1000,10000,100000,1000000]
for x in number:
    print(x)


# CREATE TABLE OF EVERY NUMBER

# In[110]:


number = int(input('Enter the number'))
print("Multiplicaton table of",number)
for count in range(int(input("Enter the range"))):
    print(number,'x',(count),'=',number*count)

4-5. Summing a Million: Make a list of the numbers from one to one million, 
and then use min() and max() to make sure your list actually starts at one and 
ends at one million. Also, use the sum() function to see how quickly Python can 
add a million numbers.
# In[111]:


lis1 = [1,10,100,1000,10000,100000,1000000]
#for max
print('Maximum value in list is ',max(list1))
#for min
print('Minimum value in list is ',min(list1))
#sum of list
print("Sum of all value in list is ",sum(list1))


# 4-6. Odd Numbers: Use the third argument of the range() function to make a list 
# of the odd numbers from 1 to 20. Use a for loop to print each number

# In[ ]:


odd = []
even= []
for x in range (int(input('Enter the number'))):
    if x%2!=0:
        odd.append(x)
    else:
        even.append
        


# In[ ]:


print('Is odd number list',odd)

4-7. Threes: Make a list of the multiples of 3 from 3 to 30. Use a for loop to 
print the numbers in your list.
# In[ ]:


number = 3
print("List of the multiples of 3",number)
for count in range(1,11):
    print(count*number,end = ' ')

4-8. Cubes: A number raised to the third power is called a cube. For example, 
the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that 
is, the cube of each integer from 1 through 10), and use a for loop to print out 
the value of each cube.
# In[ ]:


list1 =[]
for x in range(1,11):
    list1.append(x**3)
print(list1)

4-9. Cube Comprehension: Use a list comprehension to generate a list of the 
first 10 cubes.
# In[ ]:


cubes = [val**3 for val in range(1,11)]
print(cubes)


# In[ ]:


players = ['babar','shaheen','fakhar','rizwan','hassan','shadab']
for player in players[0:3]:
    print(player.title())


# In[ ]:


my_foods = ['cake','chocolate','biryani','noddles','egg']
my_freinds_food = my_foods[:]


# In[ ]:


my_foods.append('Ice-cream')
print(my_foods)


# In[ ]:


my_freinds_food.append('pepsi')
print(my_freinds_food)

4-10. Slices: Using one of the programs you wrote in this chapter, add several 
lines to the end of the program that do the following:
•	 Print the message, The first three items in the list are:. Then use a slice to 
print the first three items from that program’s list.
•	 Print the message, Three items from the middle of the list are:. Use a slice 
to print three items from the middle of the list.
•	 Print the message, The last three items in the list are:. Use a slice to print 
the last three items in the list.
# In[ ]:


fruits = ['Apple','Banana','Cherry','Mango','Gauva','Pineapple','Strawberry','Graphes','Orange']
#first three items
print("First three fruits",fruits[0:3])

#middle three items
print("First three fruits",fruits[-6:-3])

#last three items
print("last three fruits",fruits[-3:])

4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1 
(page 60). Make a copy of the list of pizzas, and call it friend_pizzas.
Then, do the following:
•	 Add a new pizza to the original list.
•	 Add a different pizza to the list friend_pizzas.
•	 Prove that you have two separate lists. Print the message, My favorite 
pizzas are:, and then use a for loop to print the first list. Print the message, 
My friend’s favorite pizzas are:, and then use a for loop to print the second list. Make sure each new pizza is stored in the appropriate list
# In[ ]:


pizzas = ['Fajjita','BBq','Afghani','Italian']
freinds_pizzas = pizzas[:]

for pizza in pizzas:
    if freinds_pizzas == pizzas:
        pizzas.append('Meat pizza')
        print('My pizzas    ',pizzas)

pizzas = ['Fajjita','BBq','Afghani','Italian']
freinds_pizzas = pizzas[:]
for piza in freinds_pizzas:
    if freinds_pizzas == pizzas:
        freinds_pizzas.append('Veggei pizza')
        print("My freind's pizzas",freinds_pizzas)

        


# In[ ]:




4-12. More Loops: All versions of foods.py in this section have avoided using 
for loops when printing to save space. Choose a version of foods.py, and 
write two for loops to print each list of foods.
# In[ ]:


fruits=[[1,2,3,4,5],["Apple","Banana","Avocado","Oranges","Mango"]]


for i in range(len(fruits)):
    for j in range(len(fruits[i])):
        print(fruits[i][j], end='\t')
    print()


# # TUPLE
Lists work well for storing sets of items that can change throughout the 
life of a program. The ability to modify lists is particularly important when 
you’re working with a list of users on a website or a list of characters in a 
game. However, sometimes you’ll want to create a list of items that cannot 
change. Tuples allow you to do just that. Python refers to values that cannot 
change as immutable, and an immutable list is called a tuple.
# In[ ]:


dimenssions = (200,50)
print(dimenssions[0])
print(dimenssions[1])


# In[ ]:


dimenssion[0]=250


# In[ ]:


for dimenssion in dimenssions:
    print(dimenssion)

4-13. Buffet: A buffet-style restaurant offers only five basic foods. Think of five 
simple foods, and store them in a tuple.
• Use a for loop to print each food the restaurant offers.
• Try to modify one of the items, and make sure that Python rejects the change.
•	 The restaurant changes its menu, replacing two of the items with different 
foods. Add a block of code that rewrites the tuple, and then use a for
loop to print each of the items on the revised menu.
# In[ ]:


menus = ('Biryani','Nehari','Noodles','Pizza','Burger')
#• Use a for loop to print each food the restaurant offers.
for menu in menus:
    print('\nThe Resturant is offering',menu)
    


# In[ ]:


#• Try to modify one of the items, and make sure that Python rejects the change.
menus[1] = 'Pilaou'


# In[ ]:


#The restaurant changes its menu, replacing two of the items with different 
#foods. Add a block of code that rewrites the tuple, and then use a for
#loop to print each of the items on the revised menu.

#1st way to update menu
new_menu = ('Pizza','Pilaou','Nehari','Tikka','Burger')
for menu in new_menu:
    print('New menu is:',menu)



# In[ ]:


#2nd way to update menu

new_menu2 = ('Pizza','Pilaou','Nehari','Tikka','Burger')
x = list(new_menu2)
x[1] = 'Lassania'
for menu in x:
    print('Update menu is',menu)


# # CHAPTER #5 if Statements
# 

# In[ ]:


cars = ['audi','bmw','lamborgini','city','corola']
for car in cars:
    if car =='bmw':
        print(car.upper())
    else:
        print(car.title())


# In[ ]:


car = 'bmw'
car =='bmw'


# In[ ]:


car = 'Audi'
car.lower()=='audi'
car


# In[ ]:


cars = ['audi','bmw','toyota']
for car in cars:
    if 'bmw' in car:
        print(car.upper())
    else:
        print(car.lower())


# In[ ]:


age_0 = 22
age_1 = 18
age_0>=21 and age_1>=21


# In[ ]:


fruits = ['apple','mango','cherry','banana']
'mango' not in fruits


# In[ ]:


banned_users = ['akram','daniyal','shahid']
user = 'Aiza'
if user not in banned_users:
    print(user.title(), 'You can enter')
else:
    pribnt("you can't enter")


# In[ ]:


banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")

5-1. Conditional Tests: Write a series of conditional tests. Print a statement 
describing each test and your prediction for the results of each test. Your code 
should look something like this:
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
•	 Look closely at your results, and make sure you understand why each line 
evaluates to True or False.
•	 Create at least 10 tests. Have at least 5 tests evaluate to True and another 
5 tests evaluate to False.
# In[ ]:





# In[ ]:


#Create at least 10 tests. Have at least 5 tests evaluate to True and another 
#5 tests evaluate to False.
vegetable = ['potatto','tomato','onion','ginger'] 
#1
'ginger' in vegetable 


# In[ ]:


#2
'carrot' not in vegetable


# In[ ]:


#3
print(len(vegetable) == 4)


# In[ ]:


#4
print(type(vegetable) ==list)


# In[ ]:


#5
print(len(vegetable)!=5)


# In[ ]:


#1
'ginger' not in vegetable 


# In[ ]:


#2
'carrot'  in vegetable


# In[ ]:


#3
print(len(vegetable) != 4)


# In[ ]:


#4
print(type(vegetable) !=list)


# In[ ]:


#5
print(len(vegetable)==5)


# In[ ]:


vegetables = ['potatto','tomato','onion','ginger'] 
for vegetable in vegetables:
    if 'tomato' in vegetable:
        vegetables.append('carrot')
    print(vegetable)
    

5-2. More Conditional Tests: You don’t have to limit the number of tests you 
create to 10. If you want to try more comparisons, write more tests and add 
them to conditional_tests.py. Have at least one True and one False result for 
each of the following:
# In[ ]:


# Tests for equality and inequality with strings

car = 'Audi'
car =='audi'


# In[ ]:


#Tests using the lower() function
name = 'Janshair'
name.lower() =='janshair'


# In[ ]:


name


# In[ ]:


# Numerical tests involving equality and inequality, greater than and 
#less than, greater than or equal to, and less than or equal to

age_1 =22
age_2=26

age_1==age_2




# In[ ]:


age_2!=age_1


# In[ ]:


age_1>age_2


# In[ ]:


age_1<age_2


# In[ ]:


#Tests using the and keyword and the or keyword
(age_1>10) and (age_2>20)


# In[ ]:


(age_1>10) or (age_2>20)


# In[ ]:


# Test whether an item is in a list
game = ['hockey','cricket','football','tennis','badminton']
'hockey' in game


# In[ ]:


# Test whether an item is not in a list
'football' not in game

5-3. Alien Colors #1: Imagine an alien was just shot down in a game. Create a 
variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.


# In[ ]:


# Write an if statement to test whether the alien’s color is green. If it is, print 
#a message that the player just earned 5 points.

alien_color = input("Enter the alien's color:")
if alien_color == 'green':
    print('You earned 5 points')


# In[ ]:


#Write one version of this program that passes the if test and another that 
#fails. (The version that fails will have no output.)

alien_color = input("Enter the alien's color:")
if alien_color == 'green':
    print('You earned 5 points')

5-4. Alien Colors #2: Choose a color for an alien as you did in Exercise 5-3, and 
write an if-else chain.
# In[ ]:


#	 If the alien’s color is green, print a statement that the player just earned 
#points for shooting the alien.
#If the alien’s color isn’t green, print a statement that the player just earned 
#10 points.
#Write one version of this program that runs the if block and another that 
#runs the else block

alien_color = input("Enter the alien's color:")
if alien_color == 'green':
    print('You earned 5 points')
    
else:
    print('You earned 10 points')

5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elifelse chain
# In[ ]:


#If the alien is green, print a message that the player earned 5 points.
#If the alien is yellow, print a message that the player earned 10 points.
#If the alien is red, print a message that the player earned 15 points.
#Write three versions of this program, making sure each message is printed 
#for the appropriate color alien.


alien_color = input("Enter the alien's color:")
if alien_color == 'green':
    print('You earned 5 points')


elif alien_color == 'yellow':
    print('You earned 10 points')
    

if alien_color == 'red':
    print('You earned 10 points')

else:
    print('You earned no points')

5-6. Stages of Life: Write an if-elif-else chain that determines a person’s 
stage of life. Set a value for the variable age, and then:
# In[ ]:


#If the person is less than 2 years old, print a message that the person is 
#a baby.

#If the person is at least 2 years old but less than 4, print a message that 
#the person is a toddler.

#If the person is at least 4 years old but less than 13, print a message that 
#the person is a kid.

#If the person is at least 13 years old but less than 20, print a message that 
#the person is a teenager.

#If the person is at least 20 years old but less than 65, print a message that 
#the person is an adult.

#If the person is age 65 or older, print a message that the person is an 
#elder.

age = int(input('Enter your age'))
if age<2:
    print('person is a baby')
elif age == 2 or age<4:
    print('person is a toddler')

elif age ==4 or age<13:
    print('person is a kid')

elif age ==13 or age<20:
    print('person is a teenager')

elif age ==20 or age<65:
    print('person is a adult')

elif age ==65 or age>65:
    print('person is a older')

5-7. Favorite Fruit: Make a list of your favorite fruits, and then write a series of 
independent if statements that check for certain fruits in your list
# In[ ]:


#Make a list of your three favorite fruits and call it favorite_fruits.
#Write five if statements. Each should check whether a certain kind of fruit 
#is in your list. If the fruit is in your list, the if block should print a statement, 
#such as You really like bananas!

favorite_fruits = ['apple','banana','mango']
if 'banana' in favorite_fruits:
    print('I really like banana')


# In[ ]:


requested_toppings = ['mushroom','green peppers', 'extra chesse']
for requested_topping in requested_toppings:
    print('Adding ' + requested_topping + '.')
print("\nFinished making your pizza!")


# In[ ]:


requested_toppings = ['mushroom','green peppers', 'extra chesse']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print('Sorry right now we are out of gree peppers')
    else:
        print('Adding ' + requested_topping + '.')
print("\nFinished making your pizza!")


# In[ ]:


requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print('Adding ' + requested_topping + '.')
    print('\nFininsehd making your pizza')
else:
    print('Are you sure you want simple pizza')


# In[ ]:


available_toppings = ['mushrooms','olive','green peppers','pepperoni','pineapple','extra chesse']
requested_toppings = ['mushrooms','french fries' ,'extra chesse']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print('Adding ' + requested_topping + '.')
    else:
        print("Sorry we don't have " + requested_topping + ".")
print('\nFininsehd making your pizza')
        

5-8. Hello Admin: Make a list of five or more usernames, including the name 
'admin'. Imagine you are writing code that will print a greeting to each user 
after they log in to a website. Loop through the list, and print a greeting to 
each user

•	 If the username is 'admin', print a special greeting, such as Hello admin, 
would you like to see a status report?
•	 Otherwise, print a generic greeting, such as Hello Eric, thank you for logging in again.
# In[ ]:


user_names = ['Ali','Kamran','Dua','Shan','Fahad']
for user_name in user_names:
    if user_name =='Dua':
        print('Hello! ' + user_name + " would you like to see a status report?")
    else:
        print('Hello ' + user_name + ' thank you for login again')

5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is 
not empty.

•	 If the list is empty, print the message We need to find some users!
•	 Remove all of the usernames from your list, and make sure the correct 
message is printed.
# In[ ]:



user_names= []
if user_names:
    for user_name in user_names:
        print('Hello ' + user_name +  " thank you for login again")
else:
    print('We need to find some users!')
        

5-10. Checking Usernames: Do the following to create a program that simulates 
how websites ensure that everyone has a unique username.
•	 Make a list of five or more usernames called current_users.
•	 Make another list of five usernames called new_users. Make sure one or 
two of the new usernames are also in the current_users list.
•	 Loop through the new_users list to see if each new username has already 
been used. If it has, print a message that the person will need to enter a 
new username. If a username has not been used, print a message saying 
that the username is available.
•	 Make sure your comparison is case insensitive. If 'John' has been used, 
'JOHN' should not be accepted.

# In[ ]:


user_names = []:
for a in range(5):
    user_name = input('Enter the guest name')
    if (user_name == 'Asad') or (user_name in user_names) or (len(user_name)==0):
        continue
    else:
        user_names.append(user_name)
print(user_names)
    


# In[ ]:





# In[ ]:




