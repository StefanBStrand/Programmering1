colors = {"red": "#FF0000",
          "blue": "#0000FF",
          "green": "#008000"}

colors["green"] = "#008001"  # Changing the value for green.
print(colors)
colors["grey"] = "#808080"  # adding a new entry ( if the
print(colors)
del colors["blue"]
print(colors)


