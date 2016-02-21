import json
import os.path

def validate_user(user):
    f = open('user.txt','w+')

    users = f.read().split('\n')
    if user in users:
        return ("Hello"+user,user)
    else:

        f.write(user+'\n')
        f.close()


        path = 'C:/Users/Ajwad/PycharmProjects/untitled/' # change to final path later

        newuserfile=os.path.join(path,user+".json")
        f=open(newuserfile,"w+")
        jsoncontent= dict()
        jsoncontent['user']=user
        jsoncontent['music']=None
        jsoncontent['travel']=None
        jsoncontent['diet']= None
        json.dump(jsoncontent,f)

        return('Nice to meet you'+user,user)

#validate_user('ajwad')