PATH = "./data_file.txt"

txt = " bla bla "
# Strip remove spaces in the way
x = txt.strip()

# Read lines take each of the lines in a file and save it as a list of strings
with open(PATH) as name_file:
    names = name_file.readlines()

# Replace changes a text for another
for name in names:
    name.replace("new_text", name)
