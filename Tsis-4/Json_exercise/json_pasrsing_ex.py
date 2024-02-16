# json_pasrsing_ex
import json #omporting library
#open and read sample-data.json file as f
with open('sample-data.json' , 'r') as f:
    data = json.load(f) #loading file
print("Interface Status")
print("="*80)
# DN                                                 Description           Speed    MTU
print("DN" , " "*49 , "Description" ," "*11 ,"Speed" ," "*4 , "MTU")  
# -------------------------------------------------- --------------------  ------  ------
print("-"*50 , "-"*25 , "-"*6 , "-"*9)
for a in data["imdata"]: #entering to imdata
    for b in a["l1PhysIf"]: #entering subdict l1PhysIf
        for c in a["l1PhysIf"]["attributes"]: #in attributes printing these data
            print(a["l1PhysIf"]["attributes"]["dn"], "\t" ,"\t" , "\t", "\t"," "*1,a["l1PhysIf"]["attributes"]["speed"], "\t",a["l1PhysIf"]["attributes"]["mtu"])



