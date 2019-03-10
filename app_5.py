from app_3 import User
import json

user = User("Jose")
user.add_movie("The Matrix","Sci-Fi")
user.add_movie("The Interview","Comedy")

with open('my_file.txt','r') as f:
    json_data = json.load(f)    
    user = User.from_json(json_data)
    print(user.json())


