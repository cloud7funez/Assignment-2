import cc_json_utils
import json

reader = open("leveldata.json", "r")
level_data = json.load(reader)
reader.close()
to_dat = cc_json_utils.transform(level_data)

print(to_dat)