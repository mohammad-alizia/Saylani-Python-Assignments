user = {
    "first_name": "Amnah",
    "last_name": "Zia",
    "age": "22",
    "city": "Karachi"
}

for key, value in user.items():
    print(key + ":" + value)

user["qualification"] = "Intermediate"
user.update(qualification = "bachelors")
user.pop('qualification')