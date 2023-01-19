import time
import random
import decimal
import cv2
import numpy as np

from time import sleep
from random import randint
from threading import Timer
import json
import os
import pyautogui
from pynput import mouse
from pynput.mouse import Button, Controller
#from src.doRelogAntiban import DoRelogAntiban


class ManageInventory:
    start_time = time.time()
    tracker = 0

    def defineAllBankImages(self):
        find_bank_box2 = pyautogui.locateOnScreen("data/bank_box_tiny5.png", confidence=0.9)
        find_bank_box5 = pyautogui.locateOnScreen("data/bank_box_tiny2.png", confidence=0.9)
        find_bank_box3 = pyautogui.locateOnScreen("data/bank_box_tiny_new1.png", confidence=0.9)
        find_bank_box4 = pyautogui.locateOnScreen("data/bank_box_tiny_right1.png", confidence=0.9)
        find_bank_box7 = pyautogui.locateOnScreen("data/bank_box_tiny_new3.png", confidence=0.9)
        find_bank_box8 = pyautogui.locateOnScreen("data/bank_box_tiny_new4.png", confidence=0.9)

    def checkForRandoms(self):
        # 1) take screenshot of text region
        # 2) replace all non-blue (rgb value: 0, 0, 132) pixels with any arbitrary colour (i.e white)
        # 3) have loop/if statement that checks whether 'Perficientes' or whatever username text is there
        # 4) if true, we know there is a random event
        #
        # 5) TO DO!  Figure out method to click the random event that popped up

        # gets screenshot of area
        print("Taking screenshot of text area. ")
        s3 = pyautogui.screenshot("storeTextScreenshot.png", region=(8, 376, 488, 124))
        smaller_img = cv2.imread("storeTextScreenshot.png")
        larger_img = cv2.imread("data/random_event_text1.png")
        print("Changing all non-blue (132) text to white: ")
        smaller_img[smaller_img != 132] = 0
        print("Saving image to data/getScreenText.png: ")
        cv2.imwrite('parseTextScreenText.png', smaller_img)
        print("Image saved")

        # above will SUCCESSFULLY parse ALL text in chat box - change all
        # non-blue (aka random event colour messages or yells)

        # NOW: use Template Matching to search for a smaller image within a larger image ->
        # a static image of what we need to find (SMALL)
        # inside our newly taken and parsed chat box in only blue and black (LARGE)
        methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
                   'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

        do_templating = cv2.matchTemplate(larger_img, smaller_img, eval(methods[0]))
        # print("do_templating: " + str(do_templating))
        # print("do_templating size: " + str(do_templating.size))
        # print("do_templating type: " + str(do_templating.type))
        print("do_templating non zeros: " + str(np.count_nonzero(do_templating)))

        # this will check if the NumPy array is empty or not (aka full of ALL zeros)
        # if it is, then we know, we did not find a corresponding image
        # while doing template matching.
        # THUS: if the count = 0, skip, else, we need to deal with random event

        if np.count_nonzero(do_templating) == 0:
            print("Empty matrix! ")
            # return True
        else:
            print("Found image!  DO ANTIBAN METHOD!")
            self.dealWithRandoms()

    def findRandomTalkToText(self):
        # TOODO:
        return True

    def dealWithRandoms(self):
        color_sandwhich_lady_side_left = (141, 87, 78)
        color_sandwhich_lady_facing_down = (173, 108, 97)
        color_sandwhich_lady_side_right = (200, 112, 108)

        # 1) Since position of character is relative (screen will always center), have arbitrary wait and then
        # 2) Move cursor to either right, left, top, or bottom of character
        # 3) For each of these options, if the cursor will pop up a display on top-left corner, click
        # 4) This will make event go away
        # 5) After click, can have arbitrary wait + if check to see if the option is there or gone,
        # and repeat if not gone
        # 6) CAVEAT: Need to create a Runescape text parser that can read the message -> similar approach to chat box
        # parser made above!

        # left, right, bottom, up
        # Pressed at(238, 208)
        # Pressed at(280, 208)
        # Pressed at(264, 225)
        # Pressed at(264, 186)
        dealt_successfully = False
        while not dealt_successfully:
            # move mouse to LEFT of character
            pyautogui.moveTo(238, 200, float(decimal.Decimal(random.randrange(3397, 3565)) / 10000),
                             pyautogui.easeInOutQuad)
            pyautogui.click(button="right")
            sleep(1)

            # **** +20 to X moves the cursor to the RIGHT ****
            # **** -20 to X moves curson to the LEFT ****
            # **** +20 to Y moves the cursor DOWN  ****
            # **** -20 to Y moves the cursor UP  ****

            print("1) Finding talk-to text (LEFT): ")
            find_talk_text1 = pyautogui.locateOnScreen("talkToTextManual1.png", confidence=0.9)

            if not str(find_talk_text1) == "None":
                talk_text_point = pyautogui.center(find_talk_text1)
                pyautogui.moveTo(talk_text_point.x, talk_text_point.y,
                                 float(decimal.Decimal(random.randrange(3397, 3565)) / 10000), pyautogui.easeInOutQuad)
                sleep(1)
                pyautogui.click()
                dealt_successfully = True
                return True
                # sleep(randint(1, 2))
            else:
                pyautogui.moveTo(218, 173, float(decimal.Decimal(random.randrange(3397, 3565)) / 10000))
                # pyautogui.moveTo(talk_text_point.x + 15, talk_text_point.y + 15, float(decimal.Decimal(random.randrange(3397, 3565)) / 10000), pyautogui.easeInOutQuad)

            '''
            print("1) Taking screenshot of top-left text for LEFT of character mouse move-to: ")
            left_screenshot = pyautogui.screenshot("storeLeftMouseScreenshot.png", region=(5, 34, 51, 17))
            smaller_img = cv2.imread("storeLeftMouseScreenshot.png")
            larger_img = cv2.imread("data/antiBan_talkToTextBlacked1.png")
            print("Changing all non-white (229) text to black (0): ")
            smaller_img[smaller_img != 229] = 0
            print("Saving image to data/getScreenText.png: ")
            cv2.imwrite('parseLeftMouseScreenshot.png', smaller_img)
            print("Image saved")

            methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
                       'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

            do_templating_LEFT = cv2.matchTemplate(larger_img, smaller_img, eval(methods[0]))
            if np.count_nonzero(do_templating_LEFT) == 0:
                print("Empty matrix! ")
                # return True
            else:
                print("Found image!  Do a simple click (TRUE for LEFT of character!)")
                print("Count 1 (LEFT): " + str(np.count_nonzero(do_templating_LEFT)))
                sleep(2)
                pyautogui.click()
                dealt_successfully = True
            sleep(1)
            '''

            # move mouse to RIGHT of character
            pyautogui.moveTo(280, 200, float(decimal.Decimal(random.randrange(3397, 3565)) / 10000),
                             pyautogui.easeInOutQuad)
            pyautogui.click(button="right")
            sleep(1)

            print("2) Finding talk-to text (RIGHT): ")
            find_talk_text2 = pyautogui.locateOnScreen("talkToTextManual1.png", confidence=0.9)

            if not str(find_talk_text2) == "None":
                talk_text_point2 = pyautogui.center(find_talk_text2)
                pyautogui.moveTo(talk_text_point2.x, talk_text_point2.y,
                                 float(decimal.Decimal(random.randrange(3397, 3565)) / 10000), pyautogui.easeInOutQuad)
                sleep(1)
                pyautogui.click()
                dealt_successfully = True
                return True
                # sleep(randint(1, 2))
            else:
                pyautogui.moveTo(321, 171, float(decimal.Decimal(random.randrange(3397, 3565)) / 10000))
                # pyautogui.moveTo(talk_text_point2.x + 15, talk_text_point.y + 15, float(decimal.Decimal(random.randrange(3397, 3565)) / 10000), pyautogui.easeInOutQuad)

            '''
            print("2) Taking screenshot of top-left text for RIGHT of character mouse move-to: ")
            left_screenshot = pyautogui.screenshot("storeRightMouseScreenshot.png", region=(5, 34, 51, 17))
            smaller_img2 = cv2.imread("storeRightMouseScreenshot.png")
            # larger_img = cv2.imread("data/antiBan_talkToTextBlacked1.png")
            print("Changing all non-white (229) text to black (0): ")
            smaller_img2[smaller_img2 != 229] = 0
            print("Saving image to data/getScreenText.png: ")
            cv2.imwrite('parseRightMouseScreenshot.png', smaller_img2)
            print("Image saved")

            methods2 = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
                       'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

            do_templating_RIGHT = cv2.matchTemplate(larger_img, smaller_img2, eval(methods2[0]))
            if np.count_nonzero(do_templating_RIGHT) == 0:
                print("Empty matrix! ")
                # return True
            else:
                print("Found image!  Do a simple click (TRUE for RIGHT of character!)")
                print("Count 2 (RIGHT): " + str(np.count_nonzero(do_templating_RIGHT)))
                sleep(2)
                pyautogui.click()
                dealt_successfully = True
            sleep(1)
            '''

            # move mouse BELOW character
            pyautogui.moveTo(264, 220, float(decimal.Decimal(random.randrange(3397, 3565)) / 10000),
                             pyautogui.easeInOutQuad)
            pyautogui.click(button="right")
            sleep(1)

            print("3) Finding talk-to text (BELOW): ")
            find_talk_text3 = pyautogui.locateOnScreen("talkToTextManual1.png", confidence=0.9)

            if not str(find_talk_text3) == "None":
                talk_text_point3 = pyautogui.center(find_talk_text3)
                pyautogui.moveTo(talk_text_point3.x, talk_text_point3.y,
                                 float(decimal.Decimal(random.randrange(3397, 3565)) / 10000), pyautogui.easeInOutQuad)
                sleep(1)
                pyautogui.click()
                dealt_successfully = True
                return True
                # sleep(randint(1, 2))
            else:
                pyautogui.moveTo(233, 196, float(decimal.Decimal(random.randrange(3397, 3565)) / 10000))
                # pyautogui.moveTo(talk_text_point3.x + 15, talk_text_point3.y + 15, float(decimal.Decimal(random.randrange(3397, 3565)) / 10000), pyautogui.easeInOutQuad)

            '''
            print("3) Taking screenshot of top-left text for BELOW character mouse move-to: ")
            below_screenshot = pyautogui.screenshot("storeBelowMouseScreenshot.png", region=(5, 34, 51, 17))
            smaller_img3 = cv2.imread("storeBelowMouseScreenshot.png")
            # larger_img = cv2.imread("data/antiBan_talkToTextBlacked1.png")
            print("Changing all non-white (229) text to black (0): ")
            smaller_img3[smaller_img3 != 229] = 0
            print("Saving image to data/getScreenText.png: ")
            cv2.imwrite('parseBelowMouseScreenshot.png', smaller_img3)
            print("Image saved")

            methods2 = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
                        'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

            do_templating_BELOW = cv2.matchTemplate(larger_img, smaller_img3, eval(methods2[0]))
            if np.count_nonzero(do_templating_BELOW) == 0:
                print("Empty matrix! ")
                # return True
            else:
                print("Found image!  Do a simple click (TRUE for BELOW character!)")
                print("Count 3 (BELOW): " + str(np.count_nonzero(do_templating_BELOW)))
                sleep(2)
                pyautogui.click()
                dealt_successfully = True
            sleep(1)
            '''

            # move mouse ABOVE character
            pyautogui.moveTo(264, 180, float(decimal.Decimal(random.randrange(3397, 3565)) / 10000),
                             pyautogui.easeInOutQuad)
            pyautogui.click(button="right")
            sleep(1)

            print("4) Finding talk-to text (ABOVE): ")
            find_talk_text4 = pyautogui.locateOnScreen("talkToTextManual1.png", confidence=0.9)

            if not str(find_talk_text4) == "None":
                talk_text_point4 = pyautogui.center(find_talk_text4)
                pyautogui.moveTo(talk_text_point4.x, talk_text_point4.y,
                                 float(decimal.Decimal(random.randrange(3397, 3565)) / 10000), pyautogui.easeInOutQuad)
                sleep(1)
                pyautogui.click()
                dealt_successfully = True
                # sleep(randint(1, 2))
                return True
            else:
                pyautogui.moveTo(221, 150, float(decimal.Decimal(random.randrange(3397, 3565)) / 10000))
                # pyautogui.moveTo(talk_text_point4.x + 15, talk_text_point4.y + 15, float(decimal.Decimal(random.randrange(3397, 3565)) / 10000), pyautogui.easeInOutQuad)

            '''
            print("4) Taking screenshot of top-left text for ABOVE character mouse move-to: ")
            below_screenshot = pyautogui.screenshot("storeAboveMouseScreenshot.png", region=(5, 34, 51, 17))
            smaller_img4 = cv2.imread("storeAboveMouseScreenshot.png")
            # larger_img = cv2.imread("data/antiBan_talkToTextBlacked1.png")
            print("Changing all non-white (229) text to black (0): ")
            smaller_img4[smaller_img4 != 229] = 0
            print("Saving image to data/getScreenText.png: ")
            cv2.imwrite('parseBelowMouseScreenshot.png', smaller_img4)
            print("Image saved")

            methods2 = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
                        'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

            do_templating_ABOVE = cv2.matchTemplate(larger_img, smaller_img4, eval(methods2[0]))
            if np.count_nonzero(do_templating_ABOVE) == 0:
                print("Empty matrix! ")
                # return True
            else:
                print("Found image!  Do a simple click (TRUE for ABOVE character!)")
                print("Count 4 (ABOVE): " + str(np.count_nonzero(do_templating_ABOVE)))
                sleep(2)
                pyautogui.click()
                dealt_successfully = True
            sleep(1)
            '''
            print("MANUALLY ENDING LOOP (will cause check to fire off again!)")
            dealt_successfully = True
            return True
            # print("Out of loop, then dealth with randoms successfully! Continuing...")
            # sleep(2)

            # is_in_bank = pyautogui.screenshot(region=(2, 32, 513, 335))
            # sleep(1)
            is_bank_opened2 = pyautogui.locateOnScreen("data/deposit_all_icon1.png", confidence=0.9)

            if not str(is_bank_opened2) == "None":
                print("Found deposit items image.  Close bank! ")
                pyautogui.moveTo(488, 52, float(decimal.Decimal(random.randrange(3397, 3565)) / 10000),
                                 pyautogui.easeInOutQuad)
                sleep(1)
                pyautogui.click()

            dealt_successfully = True

    def doBankDeposit(self):
        is_bank_opened2 = pyautogui.locateOnScreen("data/deposit_all_icon1.png", confidence=0.9)
        print("Found deposit items image.  Deposit and close. ")
        bank_opened_center2 = pyautogui.center(is_bank_opened2)
        pyautogui.moveTo(bank_opened_center2.x, bank_opened_center2.y,
                         float(decimal.Decimal(random.randrange(3397, 3565)) / 10000), pyautogui.easeInOutQuad)
        pyautogui.click()

        pyautogui.moveTo(488, 52, float(decimal.Decimal(random.randrange(3397, 3565)) / 10000),
                         pyautogui.easeInOutQuad)
        sleep(1)
        pyautogui.click()
        print("Closing and done banking. ")

    def findGoldOreColour(self):

        # put gold ore colour here
        color = (166, 141, 36)
        color2 = (149, 127, 32)
        color3 = (163, 138, 35)
        color4 = (164, 139, 35)
        color5 = (155, 131, 33)
        color6 = (166, 141, 36)
        color_range = (range(149, 166), range(127, 141), range(30, 37))
        color7 = (163, 139, 35)
        color8 = (166, 142, 36)

        self.checkForRandoms()

        print("Looking for gold ore colour: ")
        s = pyautogui.screenshot(region=(0, 0, 763, 530))
        for x in range(s.width):
            for y in range(s.height):
                xy = (x, y)
                # if s.getpixel((x, y)) == (color or color2 or color3 or color4 or color5 or color6 or color7 or color8):
                if s.getpixel(xy)[0] in range(149, 168) and s.getpixel(xy)[1] \
                        in range(127, 142) and s.getpixel(xy)[2] in range(30, 38):
                    print("Found.  Clicking gold ore colour: ")
                    pyautogui.moveTo(x, y, float(decimal.Decimal(random.randrange(3397, 3565)) / 10000),
                                     pyautogui.easeInOutQuad)
                    pyautogui.click(x, y)  # do something here
                    sleep(4)
                    return True

        print("Didn't find. ")

    def doSimpleMoveToGoldOre(self):
        done_simple_moving = False
        while not done_simple_moving:
            found_ore = False
            inv_full = False

            # ENDLESS LOOP HERE
            while not found_ore or not inv_full:

                self.findGoldOreColour()
                if self.is_inv_full():
                    # do bank
                    print("In do banking method! Doing simple banking: ")
                    self.doBanking()
                    # sleep(randint(15, 30))
            sleep(randint(1, 2))
            done_simple_moving = True

    def doSimpleBanking(self):
        done_simple_banking2 = False
        while not done_simple_banking2:
            print("Doing simple banking: ")
            find_bank_box_simple = pyautogui.locateOnScreen("data/small_minimap_peice3.png", confidence=0.9)
            bank_box_point = pyautogui.center(find_bank_box_simple)
            pyautogui.moveTo(bank_box_point.x - 380, bank_box_point.y + 50, 0.2)
            pyautogui.click()
            sleep(randint(1, 2))
            done_simple_banking2 = True

    # build out logic to do bankign once inventory is full
    def doBanking(self):
        done_banking = False
        closed_banking = False

        # self.checkForRandoms()

        # print("Attempting to find bank box: ")
        # find_bank_box2 = pyautogui.locateOnScreen("data/bank_box_tiny5.png", confidence=0.9)
        # find_bank_box5 = pyautogui.locateOnScreen("data/bank_box_tiny2.png", confidence=0.9)
        # find_bank_box3 = pyautogui.locateOnScreen("data/bank_box_tiny_new1.png", confidence=0.9)
        # find_bank_box4 = pyautogui.locateOnScreen("data/bank_box_tiny_right1.png", confidence=0.9)
        # find_bank_box6 = pyautogui.locateOnScreen("data/bank_box_tiny_new2.png", confidence=0.9)
        # find_bank_box7 = pyautogui.locateOnScreen("data/bank_box_tiny_new3.png", confidence=0.9)
        # find_bank_box8 = pyautogui.locateOnScreen("data/bank_box_tiny_new4.png", confidence=0.9)

        while not done_banking:
            print("Attempting to locate bank image: ")

            # this is for the single box above the bank
            find_new_bank_aboveBank = pyautogui.locateOnScreen("data/bank_1above.png", confidence=0.9)

            # for all 4 possible directions of 1st ore
            find_new_bank_above1st = pyautogui.locateOnScreen("data/bank_above1stOre.png", confidence=0.9)
            find_new_bank_left1st = pyautogui.locateOnScreen("data/bank_left1stOre.png", confidence=0.9)
            find_new_bank_right1st = pyautogui.locateOnScreen("data/bank_right1stOre.png", confidence=0.9)
            find_new_bank_middle1stAnd2nd = pyautogui.locateOnScreen("data/bank_middle1stAnd2ndOre.png", confidence=0.9)

            # for all 3 other possible directions of 2nd ore (upper is covered)
            find_new_bank_left2nd = pyautogui.locateOnScreen("data/bank_left2ndOre.png", confidence=0.9)
            find_new_bank_right2nd = pyautogui.locateOnScreen("data/bank_right2ndOre.png", confidence=0.9)
            find_new_bank_bottom2nd = pyautogui.locateOnScreen("data/bank_bottom2ndOre.png", confidence=0.9)

            # for only possible direction of 3rd ore
            find_new_bank_only3rd = pyautogui.locateOnScreen("data/bank_3rdOreOnlyOne.png", confidence=0.9)

            # for only possible direction of 4th one
            find_new_bank_only4th = pyautogui.locateOnScreen("data/bank_4thOreOnlyOne.png", confidence=0.9)

            # for only possible direction of 5th one
            find_new_bank_only5th = pyautogui.locateOnScreen("data/bank_5thOreOnlyOne.png", confidence=0.9)

            # for only possible direction of 6th one
            find_new_bank_only6th = pyautogui.locateOnScreen("data/bank_6thOreOnlyOne.png", confidence=0.9)

            # for only possible direction of 6th one
            find_new_bank_only7th = pyautogui.locateOnScreen("data/bank_7thOreOnlyOne.png", confidence=0.9)

            # find_bank_box2 = pyautogui.locateOnScreen("data/bank_box_tiny5.png", confidence=0.9)
            # find_bank_box5 = pyautogui.locateOnScreen("data/bank_box_tiny2.png", confidence=0.9)
            # find_bank_box3 = pyautogui.locateOnScreen("data/bank_box_tiny_new1.png", confidence=0.9)
            # find_bank_box4 = pyautogui.locateOnScreen("data/bank_box_tiny_right1.png", confidence=0.9)
            # find_bank_box6 = pyautogui.locateOnScreen("data/bank_box_tiny_new2.png", confidence=0.9)
            # find_bank_box7 = pyautogui.locateOnScreen("data/bank_box_tiny_new3.png", confidence=0.9)
            # find_bank_box8 = pyautogui.locateOnScreen("data/bank_box_tiny_new4.png", confidence=0.9)
            # find_bank_box9 = pyautogui.locateOnScreen("data/bank_box_tiny_new5.png", confidence=0.9)
            # print("Not done banking: trying to bank. ")

            if not str(find_new_bank_middle1stAnd2nd) == "None":
                bank_box_point_middle1st2nd = pyautogui.center(find_new_bank_middle1stAnd2nd)
                pyautogui.moveTo(bank_box_point_middle1st2nd.x, bank_box_point_middle1st2nd.y,
                                 float(decimal.Decimal(random.randrange(3397, 3565)) / 10000), pyautogui.easeInOutQuad)
                print("Found 1 (middle of 1st and 2nd ores). Banking. ")
                pyautogui.click()
                sleep(4)

                is_bank_opened = pyautogui.locateOnScreen("data/deposit_all_icon1.png", confidence=0.9)
                if not str(is_bank_opened) == "None":
                    print("Inside bank.  Bank opened successfully. ")
                    done_banking = True
                else:
                    print("Not inside bank for some reason.  Check for randoms, then click again!")
                    sleep(2)
                    self.checkForRandoms()
                    '''
                    pyautogui.moveTo(bank_box_point_middle1st2nd.x, bank_box_point_middle1st2nd.y,
                                     float(decimal.Decimal(random.randrange(3397, 3565)) / 10000),
                                     pyautogui.easeInOutQuad)
                    pyautogui.click()
                    print("Clicked again.  Should be inside bank now!")
                    sleep(2)
                    done_banking = True
                    '''

            elif not str(find_new_bank_right2nd) == "None":
                bank_box_right2nd = pyautogui.center(find_new_bank_right2nd)
                pyautogui.moveTo(bank_box_right2nd.x, bank_box_right2nd.y,
                                 float(decimal.Decimal(random.randrange(3397, 3565)) / 10000), pyautogui.easeInOutQuad)
                print("Found 2 (right of 2nd ore). Banking. ")
                pyautogui.click()
                sleep(4)

                is_bank_opened = pyautogui.locateOnScreen("data/deposit_all_icon1.png", confidence=0.9)
                if not str(is_bank_opened) == "None":
                    print("Inside bank.  Bank opened successfully. ")
                    done_banking = True
                else:
                    print("Not inside bank for some reason.  Check for randoms, then click again!")
                    sleep(2)
                    self.checkForRandoms()
                    '''
                    pyautogui.moveTo(bank_box_right2nd.x, bank_box_right2nd.y,
                                     float(decimal.Decimal(random.randrange(3397, 3565)) / 10000),
                                     pyautogui.easeInOutQuad)
                    pyautogui.click()
                    print("Clicked again.  Should be inside bank now!")
                    sleep(2)
                    done_banking = True
                    '''

            elif not str(find_new_bank_right1st) == "None":
                bank_box_point_right1st = pyautogui.center(find_new_bank_right1st)
                pyautogui.moveTo(bank_box_point_right1st.x, bank_box_point_right1st.y,
                                 float(decimal.Decimal(random.randrange(3397, 3565)) / 10000), pyautogui.easeInOutQuad)
                print("Found 3 (right of 1st ore). Banking. ")
                pyautogui.click()
                sleep(4)

                is_bank_opened = pyautogui.locateOnScreen("data/deposit_all_icon1.png", confidence=0.9)
                if not str(is_bank_opened) == "None":
                    print("Inside bank.  Bank opened successfully. ")
                    done_banking = True
                else:
                    print("Not inside bank for some reason.  Check for randoms, then click again!")
                    sleep(2)
                    self.checkForRandoms()
                    '''
                    pyautogui.moveTo(bank_box_point_right1st.x, bank_box_point_right1st.y,
                                     float(decimal.Decimal(random.randrange(3397, 3565)) / 10000),
                                     pyautogui.easeInOutQuad)
                    pyautogui.click()
                    print("Clicked again.  Should be inside bank now!")
                    sleep(2)
                    done_banking = True
                    '''

            elif not str(find_new_bank_bottom2nd) == "None":
                bank_box_point_bottom2nd = pyautogui.center(find_new_bank_bottom2nd)
                pyautogui.moveTo(bank_box_point_bottom2nd.x, bank_box_point_bottom2nd.y,
                                 float(decimal.Decimal(random.randrange(3397, 3565)) / 10000), pyautogui.easeInOutQuad)
                print("Found 4 (bottom of 2nd ore). Banking. ")
                pyautogui.click()
                sleep(4)

                is_bank_opened = pyautogui.locateOnScreen("data/deposit_all_icon1.png", confidence=0.9)
                if not str(is_bank_opened) == "None":
                    print("Inside bank.  Bank opened successfully. ")
                    done_banking = True
                else:
                    print("Not inside bank for some reason.  Check for randoms, then click again!")
                    sleep(2)
                    self.checkForRandoms()
                    '''
                    pyautogui.moveTo(bank_box_point_bottom2nd.x, bank_box_point_bottom2nd.y,
                                     float(decimal.Decimal(random.randrange(3397, 3565)) / 10000),
                                     pyautogui.easeInOutQuad)
                    pyautogui.click()
                    print("Clicked again.  Should be inside bank now!")
                    sleep(2)
                    done_banking = True
                    '''

            elif not str(find_new_bank_only3rd) == "None":
                bank_box_point_only3rd = pyautogui.center(find_new_bank_only3rd)
                pyautogui.moveTo(bank_box_point_only3rd.x, bank_box_point_only3rd.y,
                                 float(decimal.Decimal(random.randrange(3397, 3565)) / 10000), pyautogui.easeInOutQuad)
                print("Found 7 (only 3rd ore). Banking. ")
                pyautogui.click()
                sleep(4)

                is_bank_opened = pyautogui.locateOnScreen("data/deposit_all_icon1.png", confidence=0.9)
                if not str(is_bank_opened) == "None":
                    print("Inside bank.  Bank opened successfully. ")
                    done_banking = True
                else:
                    print("Not inside bank for some reason.  Check for randoms, then click again!")
                    sleep(2)
                    self.checkForRandoms()
                    '''
                    pyautogui.moveTo(bank_box_point_only3rd.x, bank_box_point_only3rd.y,
                                     float(decimal.Decimal(random.randrange(3397, 3565)) / 10000),
                                     pyautogui.easeInOutQuad)
                    pyautogui.click()
                    print("Clicked again.  Should be inside bank now!")
                    sleep(2)
                    done_banking = True
                    '''

            elif not str(find_new_bank_only4th) == "None":
                bank_box_point_only4th = pyautogui.center(find_new_bank_only4th)
                pyautogui.moveTo(bank_box_point_only4th.x, bank_box_point_only4th.y,
                                 float(decimal.Decimal(random.randrange(3397, 3565)) / 10000), pyautogui.easeInOutQuad)
                print("Found 8 (only 4th ore). Banking. ")
                pyautogui.click()
                sleep(4)

                is_bank_opened = pyautogui.locateOnScreen("data/deposit_all_icon1.png", confidence=0.9)
                if not str(is_bank_opened) == "None":
                    print("Inside bank.  Bank opened successfully. ")
                    done_banking = True
                else:
                    print("Not inside bank for some reason.  Check for randoms, then click again!")
                    sleep(2)
                    self.checkForRandoms()
                    '''
                    pyautogui.moveTo(bank_box_point_only4th.x, bank_box_point_only4th.y,
                                     float(decimal.Decimal(random.randrange(3397, 3565)) / 10000),
                                     pyautogui.easeInOutQuad)
                    pyautogui.click()
                    print("Clicked again.  Should be inside bank now!")
                    sleep(2)
                    done_banking = True
                    '''

            elif not str(find_new_bank_left1st) == "None":
                bank_box_point_left1st = pyautogui.center(find_new_bank_left1st)
                pyautogui.moveTo(bank_box_point_left1st.x, bank_box_point_left1st.y,
                                 float(decimal.Decimal(random.randrange(3397, 3565)) / 10000), pyautogui.easeInOutQuad)
                print("Found 9 (left of 1st ore). Banking. ")
                pyautogui.click()
                sleep(4)

                is_bank_opened = pyautogui.locateOnScreen("data/deposit_all_icon1.png", confidence=0.9)
                if not str(is_bank_opened) == "None":
                    print("Inside bank.  Bank opened successfully. ")
                    done_banking = True
                else:
                    print("Not inside bank for some reason.  Check for randoms, then click again!")
                    sleep(2)
                    self.checkForRandoms()
                    '''
                    pyautogui.moveTo(bank_box_point_left1st.x, bank_box_point_left1st.y,
                                     float(decimal.Decimal(random.randrange(3397, 3565)) / 10000),
                                     pyautogui.easeInOutQuad)
                    pyautogui.click()
                    print("Clicked again.  Should be inside bank now!")
                    sleep(2)
                    done_banking = True
                    '''

            elif not str(find_new_bank_left2nd) == "None":
                bank_box_point_left2nd = pyautogui.center(find_new_bank_left2nd)
                pyautogui.moveTo(bank_box_point_left2nd.x, bank_box_point_left2nd.y,
                                 float(decimal.Decimal(random.randrange(3397, 3565)) / 10000), pyautogui.easeInOutQuad)
                print("Found 10 (left of 2nd ore). Banking. ")
                pyautogui.click()
                sleep(4)

                is_bank_opened = pyautogui.locateOnScreen("data/deposit_all_icon1.png", confidence=0.9)
                if not str(is_bank_opened) == "None":
                    print("Inside bank.  Bank opened successfully. ")
                    done_banking = True
                else:
                    print("Not inside bank for some reason.  Check for randoms, then click again!")
                    sleep(2)
                    self.checkForRandoms()
                    '''
                    pyautogui.moveTo(bank_box_point_left2nd.x, bank_box_point_left2nd.y,
                                     float(decimal.Decimal(random.randrange(3397, 3565)) / 10000),
                                     pyautogui.easeInOutQuad)
                    pyautogui.click()
                    print("Clicked again.  Should be inside bank now!")
                    sleep(2)
                    done_banking = True
                    '''

            elif not str(find_new_bank_only6th) == "None":
                bank_box_point_only6th = pyautogui.center(find_new_bank_only6th)
                pyautogui.moveTo(bank_box_point_only6th.x, bank_box_point_only6th.y,
                                 float(decimal.Decimal(random.randrange(3397, 3565)) / 10000), pyautogui.easeInOutQuad)
                print("Found 11 (only 6th ore). Banking. ")
                pyautogui.click()
                sleep(4)

                is_bank_opened = pyautogui.locateOnScreen("data/deposit_all_icon1.png", confidence=0.9)
                if not str(is_bank_opened) == "None":
                    print("Inside bank.  Bank opened successfully. ")
                    done_banking = True
                else:
                    print("Not inside bank for some reason.  Check for randoms, then click again!")
                    sleep(2)
                    self.checkForRandoms()
                    '''
                    pyautogui.moveTo(bank_box_point_only6th.x, bank_box_point_only6th.y,
                                     float(decimal.Decimal(random.randrange(3397, 3565)) / 10000),
                                     pyautogui.easeInOutQuad)
                    pyautogui.click()
                    print("Clicked again.  Should be inside bank now!")
                    sleep(2)
                    done_banking = True
                    '''

            elif not str(find_new_bank_only7th) == "None":
                bank_box_point_only7th = pyautogui.center(find_new_bank_only7th)
                pyautogui.moveTo(bank_box_point_only7th.x, bank_box_point_only7th.y,
                                 float(decimal.Decimal(random.randrange(3397, 3565)) / 10000), pyautogui.easeInOutQuad)
                print("Found 12 (only 7th ore). Banking. ")
                pyautogui.click()
                sleep(4)

                is_bank_opened = pyautogui.locateOnScreen("data/deposit_all_icon1.png", confidence=0.9)
                if not str(is_bank_opened) == "None":
                    print("Inside bank.  Bank opened successfully. ")
                    done_banking = True
                else:
                    print("Not inside bank for some reason.  Check for randoms, then click again!")
                    sleep(2)
                    self.checkForRandoms()
                    '''
                    pyautogui.moveTo(bank_box_point_only7th.x, bank_box_point_only7th.y,
                                     float(decimal.Decimal(random.randrange(3397, 3565)) / 10000),
                                     pyautogui.easeInOutQuad)
                    pyautogui.click()
                    print("Clicked again.  Should be inside bank now!")
                    sleep(2)
                    done_banking = True
                    '''

            elif not str(find_new_bank_only5th) == "None":
                bank_box_point_only5th = pyautogui.center(find_new_bank_only5th)
                pyautogui.moveTo(bank_box_point_only5th.x, bank_box_point_only5th.y,
                                 float(decimal.Decimal(random.randrange(3397, 3565)) / 10000), pyautogui.easeInOutQuad)
                print("Found 13 (only 5th ore). Banking. ")
                pyautogui.click()
                sleep(4)

                is_bank_opened = pyautogui.locateOnScreen("data/deposit_all_icon1.png", confidence=0.9)
                if not str(is_bank_opened) == "None":
                    print("Inside bank.  Bank opened successfully. ")
                    done_banking = True
                else:
                    print("Not inside bank for some reason.  Check for randoms, then click again!")
                    sleep(2)
                    self.checkForRandoms()
                    '''
                    pyautogui.moveTo(bank_box_point_only5th.x, bank_box_point_only5th.y,
                                     float(decimal.Decimal(random.randrange(3397, 3565)) / 10000),
                                     pyautogui.easeInOutQuad)
                    pyautogui.click()
                    print("Clicked again.  Should be inside bank now!")
                    sleep(2)
                    done_banking = True
                    '''

            elif not str(find_new_bank_above1st) == "None":
                bank_box_point_above1st = pyautogui.center(find_new_bank_above1st)
                pyautogui.moveTo(bank_box_point_above1st.x, bank_box_point_above1st.y,
                                 float(decimal.Decimal(random.randrange(3397, 3565)) / 10000), pyautogui.easeInOutQuad)
                print("Found 14 (above 1st ore). Banking. ")
                pyautogui.click()
                sleep(4)

                is_bank_opened = pyautogui.locateOnScreen("data/deposit_all_icon1.png", confidence=0.9)
                if not str(is_bank_opened) == "None":
                    print("Inside bank.  Bank opened successfully. ")
                    done_banking = True
                else:
                    print("Not inside bank for some reason.  Check for randoms, then click again!")
                    sleep(2)
                    self.checkForRandoms()
                    '''
                    pyautogui.moveTo(bank_box_point_above1st.x, bank_box_point_above1st.y,
                                     float(decimal.Decimal(random.randrange(3397, 3565)) / 10000),
                                     pyautogui.easeInOutQuad)
                    pyautogui.click()
                    print("Clicked again.  Should be inside bank now!")
                    sleep(2)
                    done_banking = True
                    '''

            elif not str(find_new_bank_aboveBank) == "None":
                bank_box_point_aboveBank = pyautogui.center(find_new_bank_aboveBank)
                pyautogui.moveTo(bank_box_point_aboveBank.x, bank_box_point_aboveBank.y,
                                 float(decimal.Decimal(random.randrange(3397, 3565)) / 10000), pyautogui.easeInOutQuad)
                print("Found 15 (above bank). Banking. ")
                pyautogui.click()
                sleep(4)

                is_bank_opened = pyautogui.locateOnScreen("data/deposit_all_icon1.png", confidence=0.9)
                if not str(is_bank_opened) == "None":
                    print("Inside bank.  Bank opened successfully. ")
                    done_banking = True
                else:
                    print("Not inside bank for some reason.  Check for randoms, then click again!")
                    sleep(2)
                    self.checkForRandoms()
                    '''
                    pyautogui.moveTo(bank_box_point_aboveBank.x, bank_box_point_aboveBank.y,
                                     float(decimal.Decimal(random.randrange(3397, 3565)) / 10000),
                                     pyautogui.easeInOutQuad)
                    pyautogui.click()
                    print("Clicked again.  Should be inside bank now!")
                    sleep(2)
                    done_banking = True
                    '''

            else:
                print("Retrying... ")
                sleep(1)

        sleep(1)
        # print("Inside bank.  Doing deposit all for ALL methods: ")

        while not closed_banking:
            print("Bank not closed.  Doing first initial try to deposit.")
            is_bank_opened = pyautogui.locateOnScreen("data/deposit_all_icon1.png", confidence=0.9)

            # if is NOT none, means that we DID find image.  means bank is NOT closed yet
            if not str(is_bank_opened) == "None":
                self.doBankDeposit()
            else:
                print("Didn't find! Retrying once more.  ")
                print("--------------------------------------------")
                # sleep(4)
                if not str(is_bank_opened) == "None":
                    self.doBankDeposit()
                closed_banking = True
        self.tracker += 1
        elapsed_time = time.time() - self.start_time

        print("Done banking! Banked a total of: " + str(self.tracker) + " times, over the duration of: " +
              str(elapsed_time) + "seconds. ")

        print("Repeating findGoldOreColour(): ")
        self.findGoldOreColour()

    def track_inventory(self):
        inv_tracker = 0

    def is_inv_empty(self):
        check_last_inv = pyautogui.locateOnScreen("data/fully_empty_inventory.png")
        print("Checking if inv fully empty: " + str(check_last_inv))

        if not str(check_last_inv) == "None":
            print("Found.  Inventory is empty. ")
            return True
        else:
            print("Not found.  Inventory is NOT empty. ")
            return False

    def is_inv_full(self):
        # in the small area defined (for 28th inv item in backpack, based on 1 client being sized at top left)
        check_last_inv = pyautogui.locateOnScreen("data/last_inv_space_IS_EMPTY.png")
        # currently looks at whole screen -> CAN BE OPTIMIZED BY SETTING PROPER REGION PARAMETERS!
        # region=(693, 722, 30, 30), confidence=0.5

        print("Checking inv (if 'None' then inventory FULL!) : " + str(check_last_inv))
        time.sleep(randint(1, 2))
        # if unable to find this image, that means inventory is FULL.  so, return true.
        if str(check_last_inv) == "None":
            print("Inventory full.  Returning true: ")
            return True
        else:
            print("Inventory NOT full.  Returning false: ")
            return False