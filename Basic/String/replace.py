
#  string.replace(old, new, count)

""" 
- The replace() method replaces all occurrences of a specified substring in a string and returns a new string without modifying the original string.

- old: The substring we want to replace.
- new: The new substring that we want to replace with old substring.
- count (optional): Specifies the maximum number of replacements to perform. If omitted, all occurrences are replaced.

- Returns a new string with the specified replacements made. The original string remains unchanged since strings in Python are immutable.

"""

s = "Hello World! Hello Pravin..."
x = s.replace("Hello","hi")
print(x)

# Only replace 1 world or str from original string...
y = s.replace("Hello", "hi" , 1)
print(y)

