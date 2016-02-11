import cc_data
import cc_json_data
import cc_dat_utils
import sys
import json

def transform(json_file):
    cc_dat = cc_data.CCDataFile()
    for each_level in json_file:
        ccl = cc_data.CCLevel()
        ccl.level_number = each_level["level_number"]
        ccl.time = each_level["time"]
        ccl.num_chips = each_level["num_chips"]
        ccl.upper_layer = each_level["upper_layer"]
        ccl.lower_layer = each_level["lower_layer"]
        optional_layer = each_level["optional_layer"]

        ccmt = cc_data.CCMapTitleField()
        ccmt.title = handling_optional(3, optional_layer)
        cc_dat.levels.append(ccmt)

        if handling_optional(4, optional_layer) != []:
            cctc = cc_data.CCTrapControlsField()
            cctc.brown_button_trap = handling_optional(4, optional_layer)
            cc_dat.levels.append(cctc)

        if handling_optional(5, optional_layer) != []:
            cccm = cc_data.CCCloningMachineControl()
            cccm.red_button = handling_optional(5, optional_layer)
            cc_dat.levels.append(cccm)

        ccep = cc_data.CCEncodedPasswordField()
        ccep.password = handling_optional(6, optional_layer)
        cc_dat.levels.append(ccep)

        if handling_optional(7, optional_layer) != []:
            ccmh = cc_data.CCMapHintField()
            ccmh.hint = handling_optional(7, optional_layer)
            cc_dat.levels.append(ccmh)

        if handling_optional(10, optional_layer) != []:
            ccmm = cc_data.CCMonsterMovementField()
            ccmm.monster = handling_optional(10, optional_layer)
            cc_dat.levels.append(ccmm)

    output_file = cc_dat_util.write_cc_data_to_dat(cc_dat, "ziqiaot_CC.dat")
    return output_file

def handling_optional(type, optionalField):
    for option in optionalField:
        if option["type"] == type:
            if option["type"] == 3:
                return option["title"]
            elif option["type"] == 4:
                return option["trap_control_list"]
            elif option["type"] == 5:
                return option["cloning_machine_list"]
            elif option["type"] == 6:
                return option["password"]
            elif option["type"] == 7:
                return option["hint"]
            elif option["type"] == 10:
                return option["monster_trail"]