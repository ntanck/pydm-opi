#!/usr/bin/env python3
import argparse
import os

from siriushlacon.utils.launch import LogLevel, launch_pydm
from siriushlacon.vbc.consts import MAIN_WINDOW_PY as VBC_MAIN_WINDOW_PY

os.environ["PYDM_DEFAULT_PROTOCOL"] = "ca://"
os.environ["EPICS_CA_AUTO_ADDR_LIST"] = "YES"

BBB_IOC_ADDR = [
    "10.128.40.1:5064",
    "10.128.40.1:5068",
    "10.128.40.2:5064",
    "10.128.40.2:5068",
    "10.128.40.3:5064",
    "10.128.40.3:5068",
    "10.128.40.4:5064",
    "10.128.40.4:5068",
    "10.128.40.5:5064",
    "10.128.40.5:5068",
    "10.128.40.6:5064",
    "10.128.40.6:5068",
    "10.128.40.7:5064",
    "10.128.40.7:5068",
    "10.128.40.8:5064",
    "10.128.40.8:5068",
    "10.128.40.9:5064",
    "10.128.40.9:5068",
    "10.128.40.10:5064",
    "10.128.40.10:5068",
]
if "EPICS_CA_ADDR_LIST" not in os.environ:
    os.environ["EPICS_CA_ADDR_LIST"] = " ".join(BBB_IOC_ADDR)
else:
    os.environ["EPICS_CA_ADDR_LIST"] = (
        " ".join(BBB_IOC_ADDR) + os.environ["EPICS_CA_ADDR_LIST"]
    )

if __name__ == "__main__":
    parser = argparse.ArgumentParser("VAC Pumps Controller")
    args = parser.parse_args()
    launch_pydm(
        displayfile=VBC_MAIN_WINDOW_PY, hide_nav_bar=True, log_level=LogLevel.INFO
    )
