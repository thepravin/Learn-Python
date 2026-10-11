
s = "ABCDE$%"
print('s.isalpha', s.isalpha())
print('s.isdigit', s.isdigit())
print('s.islower', s.islower())
print('s.isupper', s.isupper())
print('len',len(s))


print('s.lower', s.lower())
print('s.upper', s.upper())


a = "          pravin            "
print(a.lstrip())
print(a.rstrip())

print("")
print("")
print("")
print("")

b = "i am a coder."
print(b.endswith("er.")) #returns true or false
print(b.capitalize()) #capitalizes 1st char
print(b.replace("am","ma"))
print(b)
print(b.find("am")) # return 1st index of 1st occurrence
print(b.find('a'))
print(b.count("a"))