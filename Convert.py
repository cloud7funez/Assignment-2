import cc_json_utils
import cc_dat_utils
import json

reader = open("leveldata.json", "r")
level_data = json.load(reader)
reader.close()
cc_json_utils.transform(level_data)

cc_dat1 = cc_dat_utils.make_cc_data_from_dat("ziqiaot.dat")
print(cc_dat1)