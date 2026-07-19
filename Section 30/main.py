# FileNotFound
try:
    file = open("a_file.txt")
    a_dict = {"key": "val"}
    print(a_dict["abcd"])
# It is better to specify the error we are handling
except FileNotFoundError:
    open("a_file.txt", "w")
# We can have multiple except statements, we can also get hold of the error message
except KeyError as err:
    print(f"the key {err} doesn't exist")
# This executes when no except clause executes
else:
    print(file.read())
# Finally isn't really used that much
finally:
    file.close()
    print("File closed")