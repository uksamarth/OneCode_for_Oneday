my_string = "Hello World"
print(my_string)
# here you can use any quatation marks to define a string.
# for example:
string1 = "Hey there! It's me Samarth."
string2 = 'He said, "I am Samarth."'
print(string1)
print(string2)
# according the usage we have to use the quatation marks.
string3 = """ This is a multiple line string.
        You can use this to write a paragraph."""
print(string3)

name = "Samarth"
greeting = "Good Morning\n" + name
print(greeting)

age = 20
age_str = str(age)
print("My age is " + age_str)

# concept of string formatting
print(f"Hello {name}! My age is {age}.")

#final greeting
name = "samarth"
final_greet = "Good Morning, {}"
sam_greet = final_greet.format(name)
print(sam_greet)