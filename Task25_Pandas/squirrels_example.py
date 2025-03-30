import pandas

data = pandas.read_csv("central_park_squirrel.csv")

colors_dict = {
    "color": [],
    "counter": []
}

# Print how many squirrels are grey
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])

# Check how many are from each color
for color in data.PrimaryFurColor:
    found_color = False
    for saved_color in colors_dict["color"]:
        if saved_color == color:
            colors_dict["counter"] += 1
            found_color = True
    if not found_color:
        colors_dict["color"].append(color)
        colors_dict["counter"].append(1)

df = pandas.DataFrame(colors_dict)
df.to_csv("Squirrel_count.csv")