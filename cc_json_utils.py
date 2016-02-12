import cc_data
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

        title = handling_optional(3, optional_layer)
        ccmt = cc_data.CCMapTitleField(title)
        ccl.optional_fields.append(ccmt)

        if handling_optional(4, optional_layer) != None:
            brown_button_trap = handling_optional(4, optional_layer)
            butt_trap_list = []
            l = len(brown_button_trap)
            i = 0
            while (i < l):
                buttCoor = brown_button_trap[i]
                trapCoor = brown_button_trap[i+1]
                butt_trap_list.append(cc_data.CCTrapControl
                                      (buttCoor[0],buttCoor[1],trapCoor[0],trapCoor[1]))
                i = i + 2

            cctc = cc_data.CCTrapControlsField(butt_trap_list)
            ccl.optional_fields.append(cctc)


        if handling_optional(5, optional_layer) != None:
            red_button = handling_optional(5, optional_layer)
            red_button_cloning_list = []
            for each_set in red_button:
                buttCoor = each_set[0]
                cloningCoor = each_set[1]
                red_button_cloning_list.append(cc_data.CCCloningMachineControl
                                (buttCoor[0],buttCoor[1],cloningCoor[0],cloningCoor[1]))

            cccm = cc_data.CCCloningMachineControl(red_button_cloning_list)
            ccl.optional_fields.append(cccm)

        password = handling_optional(6, optional_layer)
        ccep = cc_data.CCEncodedPasswordField(password)
        ccl.optional_fields.append(ccep)

        if handling_optional(7, optional_layer) != None:
            hint = handling_optional(7, optional_layer)
            ccmh = cc_data.CCMapHintField(hint)
            ccl.optional_fields.append(ccmh)

        if handling_optional(10, optional_layer) != None:
            monsters = handling_optional(10, optional_layer)
            monster_list = []
            for each_monster in monsters:
                mx = each_monster[0]
                my = each_monster[1]
                monCoor = cc_data.CCCoordinate(mx, my)
                monster_list.append(monCoor)
            ccmm = cc_data.CCMonsterMovementField(monster_list)
            ccl.optional_fields.append(ccmm)

        cc_dat.levels.append(ccl)

    cc_dat_utils.write_cc_data_to_dat(cc_dat, "ziqiaot.dat")

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