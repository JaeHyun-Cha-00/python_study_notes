# Ask user for their name
name = input("What's your name? ")

# Remove whitespace from str
name = name.strip()

# Capitlize user's name
name = name.capitalize()

# Capitlize in title base
name = name.title()

# We can chain!
name = name.strip().title()

# Split user's name into first name and last name
first, last = name.split(" ")

#auto-generate space for you
print("Hello,", name)

print("Hello, " + name)

# print(*objects, sep='', end='\n', file=sys.stdout, flush=False)

# \n erased
print("hello, ", end="")
print(name)

# what does sep do?
print("hello,", name, sep="???")

# Want to use quotation
print('hello, "friend"')
print("hello, \"friend\"")

# Used the most
print(f"hello, {name}")
