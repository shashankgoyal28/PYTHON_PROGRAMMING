# strings are immutable data type
a = "?? ??har ry ????"
print(len(a))
print(a.upper())
print(a.lower())
print(a.rstrip("?"))
print(a.replace("harry", "john"))
print(a.split(" "))
blogheading = "introduction to js"
print(blogheading.capitalize())
str1 = "Welcome to the console"
print(str1.center(50))
print(a.count("harry"))
str1 = "Welcome to the console!!!!"
print(str1.endswith("!!!!"))

str1 = "Welcome to the console!!!!"
print(str1.endswith("to", 4, 10))

str1 = "he's name is danny.he is an honest mans"
print(str1.find("ishh"))
print(str1.index("ishh"))

str1 = "welcomeToTheconsole"
print(str1.isalnum())

str1 = "welcomeToTheconsole"
print(str1.swapcase())
