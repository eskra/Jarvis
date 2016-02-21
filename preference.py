import json

def AddMusicPreference(user,variable,preference):

 userfile=user+".json"

 jsonfile= open(userfile,'r')
 data=json.load(jsonfile)

 data[variable]=preference
 jsonfile= open(userfile,"w+")
 jsonfile.write(json.dumps(data))
 jsonfile.close()
     #data[variable]=preference
     #json.dump(data,f)
     #print(f)
     #f.close()



AddMusicPreference("ajwad","music","articonkey")
