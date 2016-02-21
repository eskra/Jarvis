import json

def validate_user(user):
    f = open('user.txt', 'r+')

    users = f.read().split('\n')
    if user in users:
        return 'Hello ' + user
    else:
        f.write(user + '\n')

        #Check if user wants to set preferences
        preferences = True
        
        if preferences:
            preferences(user)
        
        return ('Nice to meet you ' + user)

    f.close()

def preferences(user, preference, setPreference):
    f = open(user + '.json', 'w+')

    my_dict = json.load(f)    
    mydict[preference] = setPreference
    json.dump(my_dict, f)
