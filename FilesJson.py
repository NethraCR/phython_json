# import json
# var = {
#       "Subjects": {
#                   "Maths":85,
#                   "English":90,
#                   "Science":78
#                    }
#       }
# with open("arraySample.json", "w") as p:
#  json.dump(var, p)

# import json
#
# # Opening JSON file
# f = open('data.json')
#
# # returns JSON object as a dictionary
# data = json.load(f)
#
# # # Iterating through the json
# # # list
# for i in data['student']:
#  print(i)
#
# # Closing file
# f.close()

import json

# Data to be written
dictionary ={
         "id": "05",
         "name": "Giri",
         "department": "Mech"
      }

with open("data.json", "a") as outfile:
   json.dump(dictionary, outfile)


