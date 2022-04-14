import json
import requests

Key='eyJraWQiOiJyRzhja1lKNXFnS2FwNitpVG52UWpmM1pSK1lpRG9GOFY5c1pjR1B3MGUwPSIsImFsZyI6IlJTMjU2In0.eyJjdXN0b206b3JnYW5pemF0aW9uIjoiR2VvcmdlIG1hc29uIHVuaXZlcnNpdHkiLCJzdWIiOiJmYmVmYjI5Ni1mMmQzLTQwYmItYTdmMS0zN2Y3MDM3MzQ2ZDYiLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLnVzLWVhc3QtMS5hbWF6b25hd3MuY29tXC91cy1lYXN0LTFfRzVqWUlMRXFYIiwiY29nbml0bzp1c2VybmFtZSI6InB1bXBpbS50b25ndGFuZ0BnbWFpbC5jb20iLCJjdXN0b206am9iX3RpdGxlIjoiQWNhZGVtaWMiLCJnaXZlbl9uYW1lIjoiUGFrYXdhbiIsImF1ZCI6IjM4MGRpaXRtc2JhN2Q2MjIwaDhsc3ExYnFvIiwiZXZlbnRfaWQiOiJmYzdiNTk2NS0wNzg4LTQ4NjEtYjRjZC02ZWVmOTExOThlMjQiLCJ0b2tlbl91c2UiOiJpZCIsImF1dGhfdGltZSI6MTYwNjcyNDUwNCwiZXhwIjoxNjA2NzI4NDA2LCJpYXQiOjE2MDY3MjQ4MDYsImZhbWlseV9uYW1lIjoiVGhvbmd0YW5nIiwiZW1haWwiOiJwdW1waW0udG9uZ3RhbmdAZ21haWwuY29tIn0.C3QvLIgKNo13U3DjHw0fl8KbxzZhm_IgeEs17-sIeWUIDDzGakxD4ELF8eQJfxMdHtuV2dfOAmekNzCsmKyOO1ZG9FkEgyfX4mvZR-p0F1n5oPkxm4YZv6ihA9Lo3jURw_mmDad41Ulo3Clx6TxalOEdxsit_Jgghzwdyc1rCR_wnqsDiBwjAVFt76RC6Sffctvu7JbNPHtEfxvxlX6rh8U1WnOd1DugK9wxV7o6pOGSKs5TRUPbKIaEU_yzhlloUkngWMAhMw_-wMTJjq_wEDgpKHwMYVQVIwwXFNvfPtwlXAqL3r3CnMpKj1luQJ58vQQEJBnSHQoz4U_HY5TXgA'
States=['AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH',
        'NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','UT','VT','VA','WA','WV','WI','WY']
# 'TX'
for state in States:
    query = "https://api.theexchange.fanniemae.com/v1/covid/state-name?state="+state
    headers={'Authorization': Key}
    result = requests.get(query,headers=headers)
    result_dict = result.json()
# print (result_dict)
    folder = 'C:\Users\USER\Desktop\Data Ana Master\AIT580\Project\Covid_'+state+'.json'
    with open(folder,'w') as fout:
        json.dump(result_dict, fout,indent=2)
    fout.close()
    # print (state+' '+'save json')
    LineToSave = []
    index = 0
    for each in result_dict['data-points']:
        County = each['county']
        State = each['state']
        Fipscode = each['fips-code']
        Daily = each['daily-stats']
        for case in Daily:
            Deaths = case['deaths']
            Confirm = case['confirmed-cases']
            if Confirm != 0 or Deaths != 0:
                index += 1
                Update = case['last-updated']
                LineToSave.append(str(index)+','+County+','+State+','+Fipscode+','+Update+','+str(Confirm)+','+str(Deaths))
        # print (LineToSave)
    folderCSV = 'C:\Users\USER\Desktop\Data Ana Master\AIT580\Project\Covid_'+state+'.csv'
    with open(folderCSV,'w') as fout:
        fout.write("index, County, State, Fips Code, Last updated, Confirm Case, Deaths\n")
        for line in LineToSave:
            fout.write(line+"\n")
    fout.close()
    # print (state+' '+'save csv')

## Can't reguest TX ##
