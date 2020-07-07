#!/usr/bin/env bash
python generate_file_upgrade.py
python generate_file_make_upgradefile.py
chmod -R 777 ./*
./make_upgradefile-999-999.sh
./make_upgradefile-999-1000.sh
./make_upgradefile-999-1001.sh
./make_upgradefile-1000-999.sh
./make_upgradefile-1000-1000.sh
./make_upgradefile-1000-1001.sh
./make_upgradefile-1001-999.sh
./make_upgradefile-1001-1000.sh
./make_upgradefile-1001-1001.sh
./make_upgradefile-20000-20000.sh
./make_upgradefile-30000-30000.sh
./make_upgradefile-65535-65535.sh
./make_upgradefile-ddb-crc.sh
./make_upgradefile-dii-crc.sh
./make_upgradefile-downloadpid-1030-tableid-1.sh
./make_upgradefile-dsi-crc.sh
./make_upgradefile-incorrect-hardver.sh
./make_upgradefile-incorrect-machinedes.sh
./make_upgradefile-incorrect-manufacturedes.sh
./make_upgradefile-incorrect-oui.sh
./make_downloadheader-crc.sh

