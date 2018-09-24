menu = []
menu.append(["egg", "spam", "meat"])
menu.append(["egg", "sosig :)", "meat"])
menu.append(["egg", "spam"])
menu.append(["egg", "meat", "spam"])
menu.append(["egg", "meat", "sosig :)", "spam"])
menu.append(["spam", "meat", "sosig :)", "spam"])
menu.append(["spam", "egg", "sosig :)", "spam"])

for meal in menu:
    if not "spam" in meal:
        print(meal)
        for ingredient in meal:
            print(ingredient)