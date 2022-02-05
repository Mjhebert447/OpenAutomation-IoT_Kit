#!/usr/bin/python3


import RPi.GPIO as GPIO
import mariadb
import time
import asyncio

global strt_time
global glb_power_st
glb_power_st = False
strt_time = 0
pwr_prnt = 0


async def init():
    global strt_time
    global glb_power_st
    global pwr_prnt
    # Placeholder value until this can be replaced by a database argument
    flag = True
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11, GPIO.OUT, initial=GPIO.LOW)
    
    if flag is True:
        glb_power_st = True

        if pwr_prnt == 0:
            print('powering on')
            GPIO.output(11, True)
            pwr_prnt += 1
    if strt_time == 0:
        strt_time = time.time()
        print('Starting Cycle time: ', strt_time)
        # False Refers to the initial assignment
        return False
    else:
        await asyncio.sleep(10)
        # True refers to the strt_time variable being assigned
        return True


# this function checks the database for new entries and if so returns a value

async def chkdb():
    print('chkdb placeholder')
    try:
        conn1 = mariadb.connect(
            user='controlapp',
            password="demopass123",
            host="172.0.0.1",
            port=3306,
            database="test"
        )
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        raise RuntimeError

    # await asyncio.sleep(10)
    print("scheduled task chkdb")


# this function calculates the current time vs the start time that is taken as part of
# the initialization process. it then returns a value when the time difference is large enough
# that value is used in the main function to dictate that the program needs to end and clean up
async def chktime():
    tmptime = strt_time
    # await asyncio.sleep(10)
    curr_time = time.time()
    print(strt_time, ": strt time")
    print(curr_time, ": curr time")
    timediff = ((curr_time - tmptime) / 60)
    print(' the time is ', curr_time, " ", timediff, ' minutes have gone past')
    if timediff > 12:
        print(timediff, " minutes tracked")
        return True


async def main():
    print('Starting Application')
    global glb_power_st
    # loop = asyncio.set_event_loop()
    runcount = 0
    while True:
        try:
            runcount += 1
            init_state = await init()
            print(init_state)
            # if init_state is False:
            # await asyncio.sleep(5)
            # print(initst)
            # print(strt_time)

            if glb_power_st is True:
                GPIO.output(11, True)
                print
            chktime_state = await chktime()
            if chktime_state is True:
                GPIO.output(11, False)
                glb_power_st = False
                print(glb_power_st)
                print("powering off")
                # code to print to database
                print('writing to DB')
                # code to confirm entries are accurate
                print('data wrote successfully')
                print('runcount: ', runcount)
                break

        except RuntimeError as e:
            print(f"something has failed: {e}")


# loop.run_until_complete(main())
asyncio.run(main())
