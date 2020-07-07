import os


def modify_file_version1(old_file_path, new_file_path, old_str1, new_str1, old_str20, new_str20, old_str30, new_str30):
    with open(old_file_path, "r") as f1, open(new_file_path, "w") as f2:
        for line in f1:
            if old_str1 in line:
                line = line.replace(old_str1, new_str1)
            if old_str20 in line:
                line = line.replace(old_str20, new_str20)
            if old_str30 in line:
                line = line.replace(old_str30, new_str30)
            f2.write(line)
    print("generate new file {} success".format(new_file_path))


def modify_file_version2(old_file_path, new_file_path, old_str1, new_str1, old_str2, new_str2):
    with open(old_file_path, "r") as f1, open(new_file_path, "w") as f2:
        for line in f1:
            if old_str1 in line:
                line = line.replace(old_str1, new_str1)
            if old_str2 in line:
                line = line.replace(old_str2, new_str2)
            # if old_str20 in line:
            #     line = line.replace(old_str20, new_str20)
            # if old_str30 in line:
            #     line = line.replace(old_str30, new_str30)
            f2.write(line)
    print("generate new file {} success".format(new_file_path))


def modify_file_version3(old_file_path, new_file_path, old_str1, new_str1, old_str2, new_str2, old_str3, new_str3):
    with open(old_file_path, "r") as f1, open(new_file_path, "w") as f2:
        for line in f1:
            if old_str1 in line:
                line = line.replace(old_str1, new_str1)
            if old_str2 in line:
                print(old_str2, new_str2)
                line = line.replace(old_str2, new_str2)
            if old_str3 in line:
                line = line.replace(old_str3, new_str3)
            # if old_str20 in line:
            #     line = line.replace(old_str20, new_str20)
            # if old_str30 in line:
            #     line = line.replace(old_str30, new_str30)
            f2.write(line)
    print("generate new file {} success".format(new_file_path))


def modify_file_version4(old_file_path, new_file_path, old_str1, new_str1, old_str2, new_str2, old_str3, new_str3,
                         old_str4, new_str4, old_str20, new_str20, old_str30, new_str30):
    with open(old_file_path, "r") as f1, open(new_file_path, "w") as f2:
        for line in f1:
            if old_str1 in line:
                line = line.replace(old_str1, new_str1)
            if old_str2 in line:
                print(old_str2, new_str2)
                line = line.replace(old_str2, new_str2)
            if old_str3 in line:
                line = line.replace(old_str3, new_str3)
            if old_str4 in line:
                line = line.replace(old_str4, new_str4)
            if old_str20 in line:
                line = line.replace(old_str20, new_str20)
            if old_str30 in line:
                line = line.replace(old_str30, new_str30)
            f2.write(line)
    print("generate new file {} success".format(new_file_path))


def modify_file_version7(old_file_path, new_file_path, old_str1, new_str1, old_str3, new_str3,
                         old_str4, new_str4, old_str20, new_str20, old_str30, new_str30, old_str40, new_str40,
                         old_str60, new_str60):
    with open(old_file_path, "r") as f1, open(new_file_path, "w") as f2:
        for line in f1:
            if old_str1 in line:
                line = line.replace(old_str1, new_str1)
            if old_str3 in line:
                line = line.replace(old_str3, new_str3)
            if old_str4 in line:
                line = line.replace(old_str4, new_str4)
            if old_str20 in line:
                line = line.replace(old_str20, new_str20)
            if old_str30 in line:
                line = line.replace(old_str30, new_str30)
            if old_str40 in line:
                line = line.replace(old_str40, new_str40)
            if old_str60 in line:
                line = line.replace(old_str60, new_str60)
            f2.write(line)
    print("generate new file {} success".format(new_file_path))


def modify_file_version9(old_file_path, new_file_path, old_str1, new_str1, old_str2, new_str2, old_str3, new_str3,
                         old_str4, new_str4, old_str20, new_str20, old_str30, new_str30, old_str40, new_str40,
                         old_str50, new_str50, old_str60, new_str60):
    with open(old_file_path, "r") as f1, open(new_file_path, "w") as f2:
        for line in f1:
            if old_str1 in line:
                line = line.replace(old_str1, new_str1)
            if old_str2 in line:
                print(old_str2, new_str2)
                line = line.replace(old_str2, new_str2)
            if old_str3 in line:
                line = line.replace(old_str3, new_str3)
            if old_str4 in line:
                line = line.replace(old_str4, new_str4)
            if old_str20 in line:
                line = line.replace(old_str20, new_str20)
            if old_str30 in line:
                line = line.replace(old_str30, new_str30)
            if old_str40 in line:
                line = line.replace(old_str40, new_str40)
            if old_str50 in line:
                line = line.replace(old_str50, new_str50)
            if old_str60 in line:
                line = line.replace(old_str60, new_str60)
            f2.write(line)
    print("generate new file {} success".format(new_file_path))


def modify_file_version8(old_file_path, new_file_path, old_str1, new_str1, old_str3, new_str3,
                         old_str4, new_str4, old_str20, new_str20, old_str30, new_str30, old_str40, new_str40,
                         old_str60, new_str60, old_str70, new_str70):
    with open(old_file_path, "r") as f1, open(new_file_path, "w") as f2:
        for line in f1:
            if old_str1 in line:
                line = line.replace(old_str1, new_str1)
            # if old_str2 in line:
            #     print(old_str2, new_str2)
            #     line = line.replace(old_str2, new_str2)
            if old_str3 in line:
                line = line.replace(old_str3, new_str3)
            if old_str4 in line:
                line = line.replace(old_str4, new_str4)
            if old_str20 in line:
                line = line.replace(old_str20, new_str20)
            if old_str30 in line:
                line = line.replace(old_str30, new_str30)
            if old_str40 in line:
                line = line.replace(old_str40, new_str40)
            # if old_str50 in line:
            #     line = line.replace(old_str50, new_str50)
            if old_str60 in line:
                line = line.replace(old_str60, new_str60)
            if old_str70 in line:
                line = line.replace(old_str70, new_str70)
            f2.write(line)
    print("generate new file {} success".format(new_file_path))


def modify_file_version10(old_file_path, new_file_path, old_str1, new_str1, old_str2, new_str2, old_str3, new_str3,
                          old_str4, new_str4, old_str20, new_str20, old_str30, new_str30, old_str40, new_str40,
                          old_str50, new_str50, old_str60, new_str60, old_str70, new_str70):
    with open(old_file_path, "r") as f1, open(new_file_path, "w") as f2:
        for line in f1:
            if old_str1 in line:
                line = line.replace(old_str1, new_str1)
            if old_str2 in line:
                print(old_str2, new_str2)
                line = line.replace(old_str2, new_str2)
            if old_str3 in line:
                line = line.replace(old_str3, new_str3)
            if old_str4 in line:
                line = line.replace(old_str4, new_str4)
            if old_str20 in line:
                line = line.replace(old_str20, new_str20)
            if old_str30 in line:
                line = line.replace(old_str30, new_str30)
            if old_str40 in line:
                line = line.replace(old_str40, new_str40)
            if old_str50 in line:
                line = line.replace(old_str50, new_str50)
            if old_str60 in line:
                line = line.replace(old_str60, new_str60)
            if old_str70 in line:
                line = line.replace(old_str70, new_str70)
            f2.write(line)
    print("generate new file {} success".format(new_file_path))


def modify_file_version11(old_file_path, new_file_path, old_str1, new_str1, old_str2, new_str2, old_str3, new_str3,
                          old_str4, new_str4, old_str20, new_str20, old_str30, new_str30, old_str40, new_str40,
                          old_str50, new_str50, old_str60, new_str60, old_str70, new_str70, old_str80, new_str80):
    with open(old_file_path, "r") as f1, open(new_file_path, "w") as f2:
        for line in f1:
            if old_str1 in line:
                line = line.replace(old_str1, new_str1)
            if old_str2 in line:
                print(old_str2, new_str2)
                line = line.replace(old_str2, new_str2)
            if old_str3 in line:
                line = line.replace(old_str3, new_str3)
            if old_str4 in line:
                line = line.replace(old_str4, new_str4)
            if old_str20 in line:
                line = line.replace(old_str20, new_str20)
            if old_str30 in line:
                line = line.replace(old_str30, new_str30)
            if old_str40 in line:
                line = line.replace(old_str40, new_str40)
            if old_str50 in line:
                line = line.replace(old_str50, new_str50)
            if old_str60 in line:
                line = line.replace(old_str60, new_str60)
            if old_str70 in line:
                line = line.replace(old_str70, new_str70)
            if old_str80 in line:
                line = line.replace(old_str80, new_str80)
            f2.write(line)
    print("generate new file {} success".format(new_file_path))


def make_special_bootlogo_file():
    new_str_dict = {1200: 1200, 1201: 1201, 1202: 1202, 1203: 1203, 1204: 1204, 1205: 1205, 1100: 1100, 1101: 1101, 1102: 1102,
                    1103: 1103, 1104: 1104}
    old_file_path = "./make_upgradefile.sh"
    new_file_path = "./upgrade-specil-{}.cfg"
    old_str1 = "DSN 1000"
    old_str2 = 'InputFileNumber 5'

    old_str3 = 'InputFile1 "4 vmlinux.bin 1 1000"'
    old_str4 = 'InputFile2 "5 fsi.bin 1 1000"'
    old_str20 = 'InputFile3 "6 bootlogo.bin 1 1000"'
    old_str30 = 'InputFile4 "8 see.ubo 1 1000"'
    old_str40 = 'InputFile5 "10 EKT_CFG_DATA.squashfs 1 1000"'

    old_str50 = 'USBOutputFile "UpgradeFile.bin"'
    old_str60 = 'OTAUpgOutputFile "UpgradeFile.ts"'

    for dsn_ver, bootlogo_ver in new_str_dict.items():
        # for new_str1 in new_str_list:
        if dsn_ver == 1200:
            new_file_path = new_file_path.format(dsn_ver)
            new_str_1 = "DSN {}".format(dsn_ver)
            new_str2 = 'InputFileNumber 1'

            new_str3 = 'InputFile1 "6 bootlogo_white.bin 1 {}"'.format(bootlogo_ver)
            new_str4 = ''
            new_str20 = ''
            new_str30 = ''
            new_str40 = ''

            new_str50 = 'USBOutputFile "./DSN5414a_100/bootlogo_white//UpgradeFile.bin"'
            new_str60 = 'OTAUpgOutputFile "./DSN5414a_100/bootlogo_white//UpgradeFile.ts"'

            modify_file_version9(old_file_path, new_file_path, old_str1, str(new_str_1), old_str2, new_str2, old_str3,
                                 new_str3, old_str4, new_str4, old_str20, new_str20, old_str30, new_str30, old_str40,
                                 new_str40, old_str50, new_str50, old_str60, new_str60)
            new_file_path = "./upgrade-specil-{}.cfg"

        elif dsn_ver == 1201:
            new_file_path = new_file_path.format(dsn_ver)
            new_str_1 = "DSN {}".format(dsn_ver)
            new_str2 = 'InputFileNumber 1'

            new_str3 = 'InputFile1 "6 bootlogo_black_no_progress.bin 1 {}"'.format(bootlogo_ver)
            new_str4 = ''
            new_str20 = ''
            new_str30 = ''
            new_str40 = ''

            new_str50 = 'USBOutputFile "./DSN5414a_100/bootlogo_black_no_progress/UpgradeFile.bin"'
            new_str60 = 'OTAUpgOutputFile "./DSN5414a_100/bootlogo_black_no_progress/UpgradeFile.ts"'

            modify_file_version9(old_file_path, new_file_path, old_str1, str(new_str_1), old_str2, new_str2, old_str3,
                                 new_str3, old_str4, new_str4, old_str20, new_str20, old_str30, new_str30, old_str40,
                                 new_str40, old_str50, new_str50, old_str60, new_str60)
            new_file_path = "./upgrade-specil-{}.cfg"

        elif dsn_ver == 1202:
            new_file_path = new_file_path.format(dsn_ver)
            new_str_1 = "DSN {}".format(dsn_ver)
            new_str2 = 'InputFileNumber 1'

            new_str3 = 'InputFile1 "7 loader_resource_white.bin 1 {}"'.format(bootlogo_ver)
            new_str4 = ''
            new_str20 = ''
            new_str30 = ''
            new_str40 = ''

            new_str50 = 'USBOutputFile "./DSN5414a_100/loader_resource_white//UpgradeFile.bin"'
            new_str60 = 'OTAUpgOutputFile "./DSN5414a_100/loader_resource_white//UpgradeFile.ts"'

            modify_file_version9(old_file_path, new_file_path, old_str1, str(new_str_1), old_str2, new_str2, old_str3,
                                 new_str3, old_str4, new_str4, old_str20, new_str20, old_str30, new_str30, old_str40,
                                 new_str40, old_str50, new_str50, old_str60, new_str60)
            new_file_path = "./upgrade-specil-{}.cfg"

        elif dsn_ver == 1203:
            new_file_path = new_file_path.format(dsn_ver)
            new_str_1 = "DSN {}".format(dsn_ver)
            new_str2 = 'InputFileNumber 1'

            new_str3 = 'InputFile1 "7 loader_resource_black.bin 1 {}"'.format(bootlogo_ver)
            new_str4 = ''
            new_str20 = ''
            new_str30 = ''
            new_str40 = ''

            new_str50 = 'USBOutputFile "./DSN5414a_100/loader_resource_black//UpgradeFile.bin"'
            new_str60 = 'OTAUpgOutputFile "./DSN5414a_100/loader_resource_black//UpgradeFile.ts"'

            modify_file_version9(old_file_path, new_file_path, old_str1, str(new_str_1), old_str2, new_str2, old_str3,
                                 new_str3, old_str4, new_str4, old_str20, new_str20, old_str30, new_str30, old_str40,
                                 new_str40, old_str50, new_str50, old_str60, new_str60)
            new_file_path = "./upgrade-specil-{}.cfg"

        elif dsn_ver == 1204:
            new_file_path = new_file_path.format(dsn_ver)
            new_str_1 = "DSN {}".format(dsn_ver)
            new_str2 = 'InputFileNumber 1'

            new_str3 = 'InputFile1 "6 boot_err_code.bin 1 {}"'.format(bootlogo_ver)
            new_str4 = ''
            new_str20 = ''
            new_str30 = ''
            new_str40 = ''

            new_str50 = 'USBOutputFile "./DSN5414a_100/boot_err_code/UpgradeFile.bin"'
            new_str60 = 'OTAUpgOutputFile "./DSN5414a_100/boot_err_code/UpgradeFile.ts"'

            modify_file_version9(old_file_path, new_file_path, old_str1, str(new_str_1), old_str2, new_str2, old_str3,
                                 new_str3, old_str4, new_str4, old_str20, new_str20, old_str30, new_str30, old_str40,
                                 new_str40, old_str50, new_str50, old_str60, new_str60)
            new_file_path = "./upgrade-specil-{}.cfg"

        elif dsn_ver == 1205:
            new_file_path = new_file_path.format(dsn_ver)
            new_str_1 = "DSN {}".format(dsn_ver)
            new_str2 = 'InputFileNumber 1'

            new_str3 = 'InputFile1 "7 loader_err_code.bin 1 {}"'.format(bootlogo_ver)
            new_str4 = ''
            new_str20 = ''
            new_str30 = ''
            new_str40 = ''

            new_str50 = 'USBOutputFile "./DSN5414a_100/loader_err_code/UpgradeFile.bin"'
            new_str60 = 'OTAUpgOutputFile "./DSN5414a_100/loader_err_code/UpgradeFile.ts"'

            modify_file_version9(old_file_path, new_file_path, old_str1, str(new_str_1), old_str2, new_str2, old_str3,
                                 new_str3, old_str4, new_str4, old_str20, new_str20, old_str30, new_str30, old_str40,
                                 new_str40, old_str50, new_str50, old_str60, new_str60)
            new_file_path = "./upgrade-specil-{}.cfg"

        elif dsn_ver == 1100:
            new_file_path = new_file_path.format(dsn_ver)
            new_str_1 = "DSN {}".format(dsn_ver)
            new_str2 = 'InputFileNumber 1'

            new_str3 = 'InputFile1 "4 vmlinux.bin 1 {}"'.format(bootlogo_ver)
            new_str4 = ''
            new_str20 = ''
            new_str30 = ''
            new_str40 = ''

            new_str50 = 'USBOutputFile "./DSN5414a_100/portion/{}/UpgradeFile.bin"'.format(dsn_ver)
            new_str60 = 'OTAUpgOutputFile "./DSN5414a_100/portion/{}/UpgradeFile.ts"'.format(dsn_ver)

            modify_file_version9(old_file_path, new_file_path, old_str1, str(new_str_1), old_str2, new_str2, old_str3,
                                 new_str3, old_str4, new_str4, old_str20, new_str20, old_str30, new_str30, old_str40,
                                 new_str40, old_str50, new_str50, old_str60, new_str60)
            new_file_path = "./upgrade-specil-{}.cfg"

        elif dsn_ver == 1101:
            new_file_path = new_file_path.format(dsn_ver)
            new_str_1 = "DSN {}".format(dsn_ver)
            new_str2 = 'InputFileNumber 1'

            new_str3 = 'InputFile1 "5 fsi.bin 1 {}"'.format(bootlogo_ver)
            new_str4 = ''
            new_str20 = ''
            new_str30 = ''
            new_str40 = ''

            new_str50 = 'USBOutputFile "./DSN5414a_100/portion/{}/UpgradeFile.bin"'.format(dsn_ver)
            new_str60 = 'OTAUpgOutputFile "./DSN5414a_100/portion/{}/UpgradeFile.ts"'.format(dsn_ver)

            modify_file_version9(old_file_path, new_file_path, old_str1, str(new_str_1), old_str2, new_str2, old_str3,
                                 new_str3, old_str4, new_str4, old_str20, new_str20, old_str30, new_str30, old_str40,
                                 new_str40, old_str50, new_str50, old_str60, new_str60)
            new_file_path = "./upgrade-specil-{}.cfg"

        elif dsn_ver == 1102:
            new_file_path = new_file_path.format(dsn_ver)
            new_str_1 = "DSN {}".format(dsn_ver)
            new_str2 = 'InputFileNumber 1'

            new_str3 = 'InputFile1 "6 bootlogo.bin 1 {}"'.format(bootlogo_ver)
            new_str4 = ''
            new_str20 = ''
            new_str30 = ''
            new_str40 = ''

            new_str50 = 'USBOutputFile "./DSN5414a_100/portion/{}/UpgradeFile.bin"'.format(dsn_ver)
            new_str60 = 'OTAUpgOutputFile "./DSN5414a_100/portion/{}/UpgradeFile.ts"'.format(dsn_ver)

            modify_file_version9(old_file_path, new_file_path, old_str1, str(new_str_1), old_str2, new_str2, old_str3,
                                 new_str3, old_str4, new_str4, old_str20, new_str20, old_str30, new_str30, old_str40,
                                 new_str40, old_str50, new_str50, old_str60, new_str60)
            new_file_path = "./upgrade-specil-{}.cfg"

        elif dsn_ver == 1103:
            new_file_path = new_file_path.format(dsn_ver)
            new_str_1 = "DSN {}".format(dsn_ver)
            new_str2 = 'InputFileNumber 1'

            new_str3 = 'InputFile1 "8 see.ubo 1 {}"'.format(bootlogo_ver)
            new_str4 = ''
            new_str20 = ''
            new_str30 = ''
            new_str40 = ''

            new_str50 = 'USBOutputFile "./DSN5414a_100/portion/{}/UpgradeFile.bin"'.format(dsn_ver)
            new_str60 = 'OTAUpgOutputFile "./DSN5414a_100/portion/{}/UpgradeFile.ts"'.format(dsn_ver)

            modify_file_version9(old_file_path, new_file_path, old_str1, str(new_str_1), old_str2, new_str2, old_str3,
                                 new_str3, old_str4, new_str4, old_str20, new_str20, old_str30, new_str30, old_str40,
                                 new_str40, old_str50, new_str50, old_str60, new_str60)
            new_file_path = "./upgrade-specil-{}.cfg"

        elif dsn_ver == 1104:
            new_file_path = new_file_path.format(dsn_ver)
            new_str_1 = "DSN {}".format(dsn_ver)
            new_str2 = 'InputFileNumber 1'

            new_str3 = 'InputFile1 "10 EKT_CFG_DATA.squashfs 1 {}"'.format(bootlogo_ver)
            new_str4 = ''
            new_str20 = ''
            new_str30 = ''
            new_str40 = ''

            new_str50 = 'USBOutputFile "./DSN5414a_100/portion/{}/UpgradeFile.bin"'.format(dsn_ver)
            new_str60 = 'OTAUpgOutputFile "./DSN5414a_100/portion/{}/UpgradeFile.ts"'.format(dsn_ver)

            modify_file_version9(old_file_path, new_file_path, old_str1, str(new_str_1), old_str2, new_str2, old_str3,
                                 new_str3, old_str4, new_str4, old_str20, new_str20, old_str30, new_str30, old_str40,
                                 new_str40, old_str50, new_str50, old_str60, new_str60)
            new_file_path = "./upgrade-specil-{}.cfg"

    print("streantool file Generate complete")


def make_app_bootlogo_file():
    list_version = [[999, 999, 999, 999, 999, 999], [999, 1000, 1000, 1000, 1000, 1000],
                    [999, 1001, 1001, 1001, 1001, 1001], [1000, 999, 999, 999, 999, 999],
                    [1000, 1000, 1000, 1000, 1000, 1000], [1000, 1001, 1001, 1001, 1001, 1001],
                    [1001, 999, 999, 999, 999, 999], [1001, 1000, 1000, 1000, 1000, 1000],
                    [1001, 1001, 1001, 1001, 1001, 1001], [20000, 20000, 20000, 20000, 20000, 20000],
                    [30000, 30000, 30000, 30000, 30000, 30000], [65535, 65535, 65535, 65535, 65535, 65535]]

    old_file_path = "./make_upgradefile.sh"
    new_file_path = "./make_upgradefile-{}-{}.sh"
    old_str1 = "upgrade.cfg"
    old_str3 = 'Upgradefile.bin'


    for [dsn_ver, app_ver, bootlogo_ver, loaderresource_ver, cfg_ver, av_ver] in list_version:
        new_file_path = new_file_path.format(dsn_ver, app_ver)
        new_str_1 = "upgrade-{}-{}.cfg".format(dsn_ver, app_ver)
        new_str3 = './DSN5414a_100/{}/{}/Upgradefile.bin'.format(dsn_ver, app_ver)


        modify_file_version2(old_file_path, new_file_path, old_str1, str(new_str_1), old_str3,new_str3)
        new_file_path = "./make_upgradefile-{}-{}.sh"


def make_incorrect_hardversion():
    old_file_path = "./make_upgradefile.sh"
    new_file_path = "./make_upgradefile-incorrect-hardver.sh"
    old_str1 = "upgrade.cfg"
    old_str3 = 'Upgradefile.bin'

    new_str_1 = "upgrade-incorrect-hardver.cfg"
    new_str3 = './DSN5414a_100/incorrect_hardware/Upgradefile.bin'

    modify_file_version2(old_file_path, new_file_path, old_str1, str(new_str_1), old_str3, new_str3)

    print("streantool file Generate complete")


def make_incorrect_oui():
    old_file_path = "./make_upgradefile.sh"
    new_file_path = "./make_upgradefile-incorrect-oui.sh"
    old_str1 = "upgrade.cfg"
    old_str3 = 'Upgradefile.bin'

    new_str_1 = "upgrade-incorrect-oui.cfg"
    new_str3 = './DSN5414a_100/incorrect_oui/Upgradefile.bin'

    modify_file_version2(old_file_path, new_file_path, old_str1, str(new_str_1), old_str3, new_str3)

    print("streantool file Generate complete")



def make_unsigend_app():
    old_file_path = "./streamtool.cfg"
    new_file_path = "./streamtool-unsigned-app.cfg"

    old_str1 = "SoftWareNo 1016"
    old_str20 = 'USBOutputFile "UpgradeFile.bin"'
    old_str30 = 'OTAUpgOutputFile "UpgradeFile.ts"'

    new_str_1 = "SoftWareNo 15000"
    new_str20 = 'USBOutputFile "./7414-v2/unsigned_application/UpgradeFile.bin"'
    new_str30 = 'OTAUpgOutputFile "./7414-v2/unsigned_application/UpgradeFile.ts"'

    modify_file_version1(old_file_path, new_file_path, old_str1, str(new_str_1), old_str20, new_str20, old_str30,
                         new_str30)


# def make_wrong_sigend():
#     list_version = [15000, 15000, 15000, 15000, 15000, 15000]
#     old_file_path = "./make_upgradefile.sh"
#     new_file_path = "./upgrade-wrong-signed.cfg"
#     old_str1 = "DSN 1000"
#     old_str2 = 'InputFileNumber 5'
#
#     old_str3 = 'InputFile1 "4 vmlinux.bin 1 1000"'
#     old_str4 = 'InputFile2 "5 fsi.bin 1 1000"'
#     old_str20 = 'InputFile3 "6 bootlogo.bin 1 1000"'
#     old_str30 = 'InputFile4 "8 see.ubo 1 1000"'
#     old_str40 = 'InputFile5 "10 EKT_CFG_DATA.squashfs 1 1000"'
#
#     old_str50 = 'USBOutputFile "UpgradeFile.bin"'
#     old_str60 = 'OTAUpgOutputFile "UpgradeFile.ts"'
#     old_str70 = 'AppRSAPrivateKey "app_privatekey.bin"'
#
#     [dsn_ver, app_ver, bootlogo_ver, loaderresource_ver, cfg_ver, av_ver] = list_version
#
#     new_str_1 = "DSN {}".format(dsn_ver)
#     new_str2 = 'InputFileNumber 5'
#
#     new_str3 = 'InputFile1 "4 vmlinux.bin 1 {}"'.format(vmlinux_ver)
#     new_str4 = 'InputFile2 "5 fsi.bin 1 {}"'.format(fsi_ver)
#     new_str20 = 'InputFile3 "6 bootlogo.bin 1 {}"'.format(bootlogo_ver)
#     new_str30 = 'InputFile4 "8 see.ubo 1 {}"'.format(see_ver)
#     new_str40 = 'InputFile5 "10 EKT_CFG_DATA.squashfs 1 {}"'.format(cfg_ver)
#
#     new_str50 = 'USBOutputFile "./DSN5414a_100/wrong_signed/UpgradeFile.bin"'
#     new_str60 = 'OTAUpgOutputFile "./DSN5414a_100/wrong_signed/UpgradeFile.ts"'
#     new_str70 = 'AppRSAPrivateKey "privatekey.bin"'
#
#     modify_file_version10(old_file_path, new_file_path, old_str1, str(new_str_1), old_str2, new_str2, old_str3,
#                           new_str3, old_str4, new_str4, old_str20, new_str20, old_str30, new_str30, old_str40,
#                           new_str40, old_str50, new_str50, old_str60, new_str60, old_str70, new_str70)
#
#     print("streantool file Generate complete")


def make_incorrect_manufacturedes():
    old_file_path = "./make_upgradefile.sh"
    new_file_path = "./make_upgradefile-incorrect-manufacturedes.sh"
    old_str1 = "upgrade.cfg"
    old_str3 = 'Upgradefile.bin'

    new_str_1 = "upgrade-incorrect-manufacturedes.cfg"
    new_str3 = './DSN5414a_100/incorrect_manuf/Upgradefile.bin'

    modify_file_version2(old_file_path, new_file_path, old_str1, str(new_str_1), old_str3, new_str3)

    print("streantool file Generate complete")


def make_incorrect_machinedes():
    old_file_path = "./make_upgradefile.sh"
    new_file_path = "./make_upgradefile-incorrect-machinedes.sh"
    old_str1 = "upgrade.cfg"
    old_str3 = 'Upgradefile.bin'

    new_str_1 = "upgrade-incorrect-machinedes.cfg"
    new_str3 = './DSN5414a_100/incorrect_machinedes/Upgradefile.bin'

    modify_file_version2(old_file_path, new_file_path, old_str1, str(new_str_1), old_str3, new_str3)

    print("streantool file Generate complete")


def make_downloadpid_1030_tableid_1():
    old_file_path = "./make_upgradefile.sh"
    new_file_path = "./make_upgradefile-downloadpid-1030-tableid-1.sh"
    old_str1 = "upgrade.cfg"
    old_str3 = 'Upgradefile.bin'

    new_str_1 = "upgrade-downloadpid-1030-tableid-1.cfg"
    new_str3 = './DSN5414a_100/downloadpid_1030_tableid_1/Upgradefile.bin'

    modify_file_version2(old_file_path, new_file_path, old_str1, str(new_str_1), old_str3, new_str3)

    print("streantool file Generate complete")


def make_dsi_crc():
    old_file_path = "./make_upgradefile.sh"
    new_file_path = "./make_upgradefile-dsi-crc.sh"
    old_str1 = "upgrade.cfg"
    old_str3 = 'Upgradefile.bin'

    new_str_1 = "upgrade-dsi-crc.cfg"
    new_str3 = './DSN5414a_100/dsi_crc/Upgradefile.bin'

    modify_file_version2(old_file_path, new_file_path, old_str1, str(new_str_1), old_str3, new_str3)

    print("streantool file Generate complete")


def make_dii_crc():
    old_file_path = "./make_upgradefile.sh"
    new_file_path = "./make_upgradefile-dii-crc.sh"
    old_str1 = "upgrade.cfg"
    old_str3 = 'Upgradefile.bin'

    new_str_1 = "upgrade-dii-crc.cfg"
    new_str3 = './DSN5414a_100/dii_crc/Upgradefile.bin'

    modify_file_version2(old_file_path, new_file_path, old_str1, str(new_str_1), old_str3, new_str3)

    print("streantool file Generate complete")


def make_ddb_crc():
    old_file_path = "./make_upgradefile.sh"
    new_file_path = "./make_upgradefile-ddb-crc.sh"
    old_str1 = "upgrade.cfg"
    old_str3 = 'Upgradefile.bin'

    new_str_1 = "upgrade-ddb-crc.cfg"
    new_str3 = './DSN5414a_100/ddb_crc/Upgradefile.bin'

    modify_file_version2(old_file_path, new_file_path, old_str1, str(new_str_1), old_str3, new_str3)

    print("streantool file Generate complete")


def make_downloadheader_crc():
    old_file_path = "./make_upgradefile.sh"
    new_file_path = "./make_downloadheader-crc.sh"
    old_str1 = "upgrade.cfg"
    old_str3 = 'Upgradefile.bin'

    new_str_1 = "upgrade-downloadheader-crc.cfg"
    new_str3 = './DSN5414a_100/downloadheader_crc/Upgradefile.bin'

    modify_file_version2(old_file_path, new_file_path, old_str1, str(new_str_1), old_str3, new_str3)

    print("streantool file Generate complete")


def make_big_file():
    list_version = [10000, 10000, 10000, 10000, 10000, 10000]
    old_file_path = "./make_upgradefile.sh"
    new_file_path = "./upgrade-big.cfg"
    old_str1 = "DSN 1000"
    # old_str2 = 'InputFileNumber 5'

    old_str3 = 'InputFile1 "4 1000 enc_fakesigned_app.bin"'
    old_str4 = 'InputFile2 "6 1000 enc_fakesigned_bootlogo.bin"'
    old_str20 = 'InputFile3 "7 1000 enc_fakesigned_loaderresource.bin""'
    old_str30 = 'InputFile4 "10 1000 enc_fakesigned_CFG.bin"'
    old_str40 = 'InputFile5 "14 1000 enc_fakesigned_av_cpu_256m.bin"'

    # old_str50 = 'USBOutputFile "UpgradeFile.bin"'
    old_str60 = 'OTAUpgOutputFile "UpgradeFile.ts"'

    [dsn_ver, app_ver, bootlogo_ver, loaderresource_ver, cfg_ver, av_ver] = list_version
    new_str_1 = "DSN {}".format(dsn_ver)
    # new_str2 = 'InputFileNumber 4'

    new_str3 = 'InputFile1 "4 {} big_enc_fakesigned_app.bin"'.format(app_ver)
    new_str4 = 'InputFile2 "6 {} big_enc_fakesigned_bootlogo.bin"'.format(bootlogo_ver)
    new_str20 = 'InputFile3 "7 {} big_enc_fakesigned_loaderresource.bin"'.format(loaderresource_ver)
    new_str30 = 'InputFile4 "10 {} big_enc_fakesigned_CFG.bin"'.format(cfg_ver)
    new_str40 = 'InputFile5 "14 {} big_enc_fakesigned_av_cpu_256m.bin"'.format(av_ver)

    # new_str50 = 'USBOutputFile "./DSN5414a_100/big_size/UpgradeFile.bin"'
    new_str60 = 'OTAUpgOutputFile "./DSN5414a_100/big_size/UpgradeFile.ts"'

    modify_file_version7(old_file_path, new_file_path, old_str1, str(new_str_1), old_str3,
                         new_str3, old_str4, new_str4, old_str20, new_str20, old_str30, new_str30, old_str40,
                         new_str40, old_str60, new_str60)
    print("streantool file Generate complete")


def make_excessive_big_file():
    list_version = [10003, 10003, 10003, 10003, 10003, 10003]
    old_file_path = "./make_upgradefile.sh"
    new_file_path = "./upgrade-excessive-big.cfg"
    old_str1 = "DSN 1000"
    # old_str2 = 'InputFileNumber 5'

    old_str3 = 'InputFile1 "4 1000 enc_fakesigned_app.bin"'
    old_str4 = 'InputFile2 "6 1000 enc_fakesigned_bootlogo.bin"'
    old_str20 = 'InputFile3 "7 1000 enc_fakesigned_loaderresource.bin""'
    old_str30 = 'InputFile4 "10 1000 enc_fakesigned_CFG.bin"'
    old_str40 = 'InputFile5 "14 1000 enc_fakesigned_av_cpu_256m.bin"'

    # old_str50 = 'USBOutputFile "UpgradeFile.bin"'
    old_str60 = 'OTAUpgOutputFile "UpgradeFile.ts"'

    [dsn_ver, app_ver, bootlogo_ver, loaderresource_ver, cfg_ver, av_ver] = list_version

    new_str_1 = "DSN {}".format(dsn_ver)
    # new_str2 = 'InputFileNumber 4'

    new_str3 = 'InputFile1 "4 {} excessive_big_enc_fakesigned_app.bin"'.format(app_ver)
    new_str4 = 'InputFile2 "6 {} excessive_big_enc_fakesigned_bootlogo.bin"'.format(bootlogo_ver)
    new_str20 = 'InputFile3 "7 {} excessive_big_enc_fakesigned_loaderresource.bin"'.format(loaderresource_ver)
    new_str30 = 'InputFile4 "10 {} excessive_big_enc_fakesigned_CFG.bin"'.format(cfg_ver)
    new_str40 = 'InputFile5 "14 {} excessive_big_enc_fakesigned_av_cpu_256m.bin"'.format(av_ver)

    # new_str50 = 'USBOutputFile "./DSN5414a_100/excessive_big_size/UpgradeFile.bin"'
    new_str60 = 'OTAUpgOutputFile "./DSN5414a_100/excessive_big_size/UpgradeFile.ts"'

    modify_file_version7(old_file_path, new_file_path, old_str1, str(new_str_1), old_str3,
                         new_str3, old_str4, new_str4, old_str20, new_str20, old_str30, new_str30, old_str40,
                         new_str40, old_str60, new_str60)
    print("streantool file Generate complete")


def create_folder(folder_name):
    """
    base current floder, creat folder
    :param folder_name: folder name (str)
    :return: None
    """
    curPath = os.getcwd()
    tempPath = folder_name
    targetPath = curPath + os.path.sep + tempPath
    if not os.path.exists(targetPath):
        os.makedirs(targetPath)
    else:
        print("file already exists!")


if __name__ == '__main__':
    make_app_bootlogo_file()

    make_incorrect_hardversion()
    make_incorrect_oui()
    # make_wrong_sigend()
    make_incorrect_manufacturedes()
    make_incorrect_machinedes()
    make_downloadpid_1030_tableid_1()
    make_dsi_crc()
    make_dii_crc()
    make_ddb_crc()
    make_downloadheader_crc()
    # make_big_file()
    # make_excessive_big_file()
    # make_special_bootlogo_file()
