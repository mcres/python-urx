#!/usr/bin/python3

import urx
import logging
import time

if __name__ == "__main__":

    logging.basicConfig(level=logging.DEBUG)
    robot = urx.Robot("192.168.1.100", use_rt=False)
    logging.info("Robot object is available as robot")

    fieldnames = {"JointData":["T_motor3", "T_micro1"], "RobotModeData":["isProgramPaused"],
        "ForceModeData":["x","y"]}
    filepath="robot_data.csv"
    robot.set_data_saved(rate=1,fieldnames=fieldnames,file_path=filepath)

    time.sleep(10)
