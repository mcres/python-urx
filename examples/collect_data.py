#!/usr/bin/python3

import urx
import logging
import time

if __name__ == "__main__":

    logging.basicConfig(level=logging.DEBUG)
    robot = urx.Robot("192.168.1.50", use_rt=False)
    logging.info("Robot object is available as robot")
    logging.info("Checking out if robot recieves orders...")
    robot.set_digital_out(7, True)
    fieldnames = {"JointData":["T_motor3", "T_micro1"], "RobotModeData":["isProgramPaused"],
        "ForceModeData":["x","y"]}
    filepath="data"
    robot.set_data_saved(rate=1,fieldnames=fieldnames,file_path=filepath)

    # select data to be saved
    #r.set_data_saved(True,1,fieldnames,'/home/marti/Desktop/UR_1.csv')
    time.sleep(10)
