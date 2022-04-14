import json
import requests
## get new keyword ##
Key='eyJraWQiOiJyRzhja1lKNXFnS2FwNitpVG52UWpmM1pSK1lpRG9GOFY5c1pjR1B3MGUwPSIsImFsZyI6IlJTMjU2In0.eyJjdXN0b206b3JnYW5pemF0aW9uIjoiR2VvcmdlIG1hc29uIHVuaXZlcnNpdHkiLCJzdWIiOiJmYmVmYjI5Ni1mMmQzLTQwYmItYTdmMS0zN2Y3MDM3MzQ2ZDYiLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLnVzLWVhc3QtMS5hbWF6b25hd3MuY29tXC91cy1lYXN0LTFfRzVqWUlMRXFYIiwiY29nbml0bzp1c2VybmFtZSI6InB1bXBpbS50b25ndGFuZ0BnbWFpbC5jb20iLCJjdXN0b206am9iX3RpdGxlIjoiQWNhZGVtaWMiLCJnaXZlbl9uYW1lIjoiUGFrYXdhbiIsImF1ZCI6IjM4MGRpaXRtc2JhN2Q2MjIwaDhsc3ExYnFvIiwiZXZlbnRfaWQiOiJiOWUzMjhhZi1lNTEzLTQ1MWMtYTY2ZC1jNjQ2ZTBmYzNjN2EiLCJ0b2tlbl91c2UiOiJpZCIsImF1dGhfdGltZSI6MTYwNjQ5Mzc3MiwiZXhwIjoxNjA2NTAxMDM1LCJpYXQiOjE2MDY0OTc0MzUsImZhbWlseV9uYW1lIjoiVGhvbmd0YW5nIiwiZW1haWwiOiJwdW1waW0udG9uZ3RhbmdAZ21haWwuY29tIn0.ms0qKsvLLgB6nh_iWUi95Py9ub_PFr21q0aw7sdj9bXQB0FK_mBa-iuBDpWrqt-bkKXDL-RAnt5g_r-3Z444eF4vk8_VQtIFsP6Xzj9apfQlNv6BUrUsMu_aXK7jo0V1GqKK8xPhSee44UecXg3fA-nDA64qgKwg6srRhHL7FDyWzFgBsrrD3S37kYV5VoWOIocVnQDLlMaPXUJkT5_L_Rq3wI2bhI153X5fSegJxyZgdYJCM87ahxBST0ajh9BCHDehGSSiiE5uhUbbKwDehkBMWv4cfPl9i0mD1nMl8AV3TK27swpFczJ9VSgC62iGKtX1v7K5fORKelcY7z1WhA'

# 1. collect Economic indicator
query = "https://api.theexchange.fanniemae.com/v1/economic-forecasts/data/years/2020"
headers={'Authorization': Key}
result = requests.get(query,headers=headers)
result_dict = result.json()

with open('C:\Users\USER\Desktop\DEAN\AIT580\Project\Economic_indicator.json','w') as fout:
    json.dump(result_dict, fout,indent=2)
fout.close()
#
LineToSave = []
index = 0
for i in range(len(result_dict)):
    new_dict = result_dict[i]
    py_dict = new_dict['indicators']
    for each in py_dict['indicator']:
        Name = each['indicator-name']
        Date = each['effectiveDate']
        Value = each['points']
        for val in Value:
            index += 1
            quarter = val['quarter']
            value = val['value']
            forecast = val['forecast']
            # print (str(index)+' '+Name+' '+Date+' '+quarter)
            LineToSave.append(str(index)+','+Name+','+Date+','+quarter+','+str(value)+','+str(forecast))
# print (LineToSave)
with open('C:\Users\USER\Desktop\DEAN\AIT580\Project\Economic_indicator.csv','w') as fout:
    fout.write("index, Indicator name, Effective Date, Quarter, Value, Forecast\n")
    for line in LineToSave:
        fout.write(line+"\n")
fout.close()

## 2. collect Housing Indicator
# query = "https://api.theexchange.fanniemae.com/v1/housing-indicators/data/years/2020"
# headers={'Authorization': Key}
# result = requests.get(query,headers=headers)
# result_dict = result.json()
#
# with open('C:\Users\USER\Desktop\DEAN\AIT580\Project\Housing_indicator.json','w') as fout:
#     json.dump(result_dict, fout,indent=2)
# fout.close()
#
# LineToSave = []
# index = 0
# for i in range(len(result_dict)):
#     new_dict = result_dict[i]
#     py_dict = new_dict['indicators']
#     for each in py_dict['indicator']:
#         Name = each['indicator-name']
#         Date = each['effectiveDate']
#         Value = each['points']
#         for val in Value:
#             index += 1
#             quarter = val['quarter']
#             value = val['value']
#             forecast = val['forecast']
#             # print (str(index)+' '+Name+' '+Date+' '+quarter)
#             LineToSave.append(str(index)+','+Name+','+Date+','+quarter+','+str(value)+','+str(forecast))
# # print (LineToSave)
# with open('C:\Users\USER\Desktop\DEAN\AIT580\Project\Housing_indicator.csv','w') as fout:
#     fout.write("index, Indicator name, Effective Date, Quarter, Value, Forecast\n")
#     for line in LineToSave:
#         fout.write(line+"\n")
# fout.close()


## 3. collect HPSI age 18-34
# query = "https://api.theexchange.fanniemae.com/v1/nhs/hpsi/age-groups/1"
# headers={'Authorization': Key}
# result = requests.get(query,headers=headers)
# result_dict = result.json()
#
# with open('C:\Users\USER\Desktop\DEAN\AIT580\Project\HPSI_1.json','w') as fout:
#     json.dump(result_dict, fout,indent=2)
# fout.close()
#
# LineToSave = []
# for i, each in enumerate(result_dict):
#     Date = each['date']
#     Value = each['hpsiValue']
#     LineToSave.append(str(i)+','+'18-34 years old'+','+Date+','+str(Value))
# # print (LineToSave)
# with open('C:\Users\USER\Desktop\DEAN\AIT580\Project\HPSI_1.csv','w') as fout:
#     fout.write("index, Age group, Date, hpsiValue\n")
#     for line in LineToSave:
#         fout.write(line+"\n")
# fout.close()
# #
## 4. collect HPSI age 35-44
# query = "https://api.theexchange.fanniemae.com/v1/nhs/hpsi/age-groups/2"
# headers={'Authorization': Key}
# result = requests.get(query,headers=headers)
# result_dict = result.json()
#
# with open('C:\Users\USER\Desktop\DEAN\AIT580\Project\HPSI_2.json','w') as fout:
#     json.dump(result_dict, fout,indent=2)
# fout.close()
#
# LineToSave = []
# for i, each in enumerate(result_dict):
#     Date = each['date']
#     Value = each['hpsiValue']
#     LineToSave.append(str(i)+','+'35-44 years old'+','+Date+','+str(Value))
# # print (LineToSave)
# with open('C:\Users\USER\Desktop\DEAN\AIT580\Project\HPSI_2.csv','w') as fout:
#     fout.write("index, Age group, Date, hpsiValue\n")
#     for line in LineToSave:
#         fout.write(line+"\n")
# fout.close()


## 5. collect HPSI age 45-64
# query = "https://api.theexchange.fanniemae.com/v1/nhs/hpsi/age-groups/3"
# headers={'Authorization': Key}
# result = requests.get(query,headers=headers)
# result_dict = result.json()
#
# with open('C:\Users\USER\Desktop\DEAN\AIT580\Project\HPSI_3.json','w') as fout:
#     json.dump(result_dict, fout,indent=2)
# fout.close()
#
# LineToSave = []
# for i, each in enumerate(result_dict):
#     Date = each['date']
#     Value = each['hpsiValue']
#     LineToSave.append(str(i)+','+'45-64 years old'+','+Date+','+str(Value))
# # print (LineToSave)
# with open('C:\Users\USER\Desktop\DEAN\AIT580\Project\HPSI_3.csv','w') as fout:
#     fout.write("index, Age group, Date, hpsiValue\n")
#     for line in LineToSave:
#         fout.write(line+"\n")
# fout.close()

## 5. collect HPSI age 65+
# query = "https://api.theexchange.fanniemae.com/v1/nhs/hpsi/age-groups/4"
# headers={'Authorization': Key}
# result = requests.get(query,headers=headers)
# result_dict = result.json()
#
# with open('C:\Users\USER\Desktop\DEAN\AIT580\Project\HPSI_4.json','w') as fout:
#     json.dump(result_dict, fout,indent=2)
# fout.close()
#
# LineToSave = []
# for i, each in enumerate(result_dict):
#     Date = each['date']
#     Value = each['hpsiValue']
#     LineToSave.append(str(i)+','+'65+ years old'+','+Date+','+str(Value))
# # print (LineToSave)
# with open('C:\Users\USER\Desktop\DEAN\AIT580\Project\HPSI_4.csv','w') as fout:
#     fout.write("index, Age group, Date, hpsiValue\n")
#     for line in LineToSave:
#         fout.write(line+"\n")
# fout.close()



