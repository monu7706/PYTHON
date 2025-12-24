#  what is container data type ?
#  normal datatype me single value store karte hai lekin
#  container datatype me multiple value store kr sakte hai.
#  jaise 
#  a=10 ,b=4 normal variable 
# CONTAINER DATATYPE ARE
# 1) List []
# 2) tuple ()
# 3) set {}
# 4) dictionary {KEY:VALUE} multiple key aur values
# ho sakti hai

# list in python
# num=[1,2,3,4,5,6,7,8,9,10]
# print(num[1])   #INDEX KO DECLARE KARNE KE LIYE HM [] KA USE KARTE HAI & INDEX START WITH 0

# num.append(11)
# print(num)
# num.count(1)
# print (num.count(1))

#Tuple in python

# tuples IMMUTABLE HOTA HAI AUR list HOTA HAI MUTABLE
#IMMUTABLE MEANS CHANGE NAHI HO SAKTA MUTABLE MEANS CHANGE HO SAKTA HAI
#LIST ME CHANGABLE FEATURE HOTA HAI AUR TUPLE ME CHANGE NAHI HOTA 
#immutable menas change nahi ho sakta mutable means change ho sakta hai

# TUPLE
# num =(1, 5, 9)
# #     0  1  2              # forward NDEXING
# #    -3 -2  -1             # BACKWARD INDEXING IT WORK IN BOTH LIST AND TUPLES
# print(num)
# print(num[2])
# print(num[-2])

#sets in python 

# num={1,1,5,5,9}  #set remove duplicate value and print unique values
# print(num) 
# print(type(num))

# DICTIONARY IN PYTHON

# name={1:"adarsh",2:"dwivedi"}     # key always unique hota hai name or number kuch bhi ho sakta hai
# print(name)

# conditional statements in python

# age = int(input("enter age: "))
# if age >18:
#     print("you are eligible for vote")
# else:
#     print("you are not eligible for vote")    

# Advance if , Elif, else

# name = input("enter name: ")      # = assignment operator == comparison operator
# if name == "adarsh":
#     print("you are adarsh")
# elif name == "dwivedi":
#     print("you are dwivedi")
# else:
#     print("you are unknown")

    # Looping in python 

    # WHAT IS LOOP ?
    # 1) for loop 
    # 2) while loop
    # Koi bhi kaam hm repeatidtly karte hai to looping ka use karte hai

# i = 1
# while i <=10:
#     print("hello adarsh")
#     i = i+1

for i in range(1,11):
    print("hello adarsh") /ln
    print(i)

#list looping 
# num = [4,5,9,2,5,7]
# print(num[0])
# for i in num:
#      print(i)

# string  looping 

# name = "adarsh"
# print(name)
# for c in name:
#     print(c)
 

# function in python
# 2 types of functions
# 1) inbuilt function
# 2) user-defined function

#jab bhi def keyward likha hoga iska matlab hm log function creat kr rahe hai
# Syntax
# 1. def function name (parameter):
#        body
   
# FUNCTION WITH NO ARHUMENT 
# def add():              # FUNCTION DEFINITION
#     a=10
#     b=50
#     print(a+b)

# add()                 # FUNCTION CALL

# # FUNCTION WITH ARGUMENT

# def add(a,b):              # FUNCTION DEFINITION
#     print(a,"+",b,"=" , a+b)

# add(5,9)                 # FUNCTION CALL
# add(10,60)
# add(1,60)
# add(3,4)

# methods of lists means midification of list 
# 1 fruit.append("grapes") list ke end me ek element add karega
# 2. fruit.insert(2,"orange") index no batana padega voha pr add karega
# 3. fruit.pop(3) jis index ko likhenge usko delete karega list set
# 4. fruit.remove("banana") list me sabse pahle ane wala banana ko delete karega
# 5. fruits.clear() list ke saare elements ko delete kr deta hai
# 6. fruitis.extend("pear","banana") work like append but in this we can add multiple elements ek saath
# 7. fruits.index("kiwi") sabse pahle aane wale elements ki index batata hai output 3 aayega
# 8. fruits.count("banana") specified item list me kitni baar repeat ho raha hai uski count batata hai
# 9. numbers.sort() sort function is used to sort list in assending or descending order
# 10. fruits.sort(reverse=true) it will arrange fruits in descending order
# 11. fruit.reverse() reverse() function is used to reverse the order of the element in a list
# 12. fruits.copy , numbers.copy() create the shallow copy of the existing list


# methods in tuple 
#1. count() - marval_villians.count("loki") counts the no of times specified items repeated
#2. .index(max(marvel_power_level)) index() return the index no. of the first occurence of the element in tuple 
#3. len() finding the length of tuple
#4. max(),min() returning the largest or smallest elrment in the tuple
#5. sum() computing the sum of all element in the tuple
#6. sorted() sorting the element in the tuple 
#7. any(),all() checking whether any or all elements in a tuple meet the condition 

#tuples are immutable these functions cannot modify the original tuple


# sets
# 1. skills.add("python") add elements to a set  
# 2.skills.remove("data visulation") USED TO REMOVE specified element to a set
# 3.skills.discard("data visulation") used to remove specified element to a set
# 4.skills.pop() are used to remove and return an arbitrary element from the set since sets are unordered
#   element removed not necessarily first or last element removed
# 5. skills.clear() remove all the element from sets and return set().set
# 6. skills.copy() used to creat a shallow copy of set 
# 7.union() returns a new set containing all the unique elements from two or more sets
# 8. set1.intersection(set2) this function in python sets returns a new sets that contain only the common
#     elements that contain two or morew sets.
# 9. difference() returns a new set containing the element that are present in the first set but not
#   in the others set 


# dictionaries
# 1. tools.clear() used to remove all the items (key value pair) from dictionaries
# 2. copy() used to create shallow copy of dictionaries 
# 3. key() used to view the keys of the dictionary.
# 4. values() used to view the values of the dictionaries .
# 5. items() used to view object that contains key-value pair of the dictionaries it returns a list of
#    tuples where each tuple represent a key-value pair of the dictionaries. 
# 6. get() get a value of the specified key 
# 7. pop() used to remove the value of the specified keys.
# 8. popitem() it remove the last inserted key value pair from dictionaries
# 9. update() used to update the vlaue of the dictionary from the another dictionary 
#     if there is value present then update if not present then added as a new 
  
# continue in for loop
# numbers= [1,2,3,4,5,6,7,8,9,10]
# for number in numbers:
#     if number%2==0:              #if the number is even
#         continue                 #skip over rest of the loop 
#     print(number)                #otherwise, print the number


    #for item in sequecnce :
    #    if condition:
   #          break
         # rest of the code


# fruits =["apple", "banana", "cherry","orange","pear"]
# for fruit in fruits:
#     if fruit== "orange":       #if we find an orange 
#         break                  # stop the loop
#     print(fruit)


#use of pass keyword
#syntax:
# for item in sequence:
#     pass


# numbers=[1,2,3,4,5]
# for num in numbers:
#     if num %2==0:
#         pass
#     else:
#         print(num) 


