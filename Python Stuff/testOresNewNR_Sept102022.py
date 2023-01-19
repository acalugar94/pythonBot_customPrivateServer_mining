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

# force use of ImageNotFoundException
# pyautogui.useImageNotFoundException()

class doAll:
    start_time = time.time()
    tracker = 0

    def afterLoginCenterAndZoom(self):
        doSomething = 0

    def openNRclientAndNavigate(self):
        doSomething = 1
        x1, y1 = pyautogui.locateCenterOnScreen("findWindowsSearchBar.png")
        print('x1: ' + str(x1) +', y1: ' + str(y1))
        pyautogui.moveTo(x1, y1, duration=0.5)
        pyautogui.click()
        sleep(1)

        pyautogui.write('Near', interval=0.1)
        pyautogui.press('enter')
        sleep(15)


    def doLoginAndCheck(self):
        #x3, y3 = pyautogui.locateCenterOnScreen("isLoggedOut_imageToVerify.png")

        print("Start of doLoginAndCheck: ")

        dealt_successfully = False
        while not dealt_successfully:
            print("In first check: ")
            x2, y2 = pyautogui.locateCenterOnScreen('isLoggedOut_imageToVerify.png')
            print('x2: ' + str(x2) +', y2: ' + str(y2))
            pyautogui.moveTo(x2, y2, duration=2)
            print("Found image, moving and clicking on 'Existing User' button: ")
            pyautogui.click()
            sleep(1)

            # if username is saved, defaults to password.  if username not saved, defaults to username.  so, we can do below steps to bypass
            #pyautogui.press('enter')
            #sleep(2)
            #pyautogui.press('backspace', presses=12)
            #pyautogui.write('Bizz Woke', interval=0.15)
            #pyautogui.press('tab')
            print("Entering password: ")
            pyautogui.write('TestPassword1337!', interval=0.15)
            print("Clicking enter: ")
            pyautogui.press('enter')
            print("Sleeping 8 seconds: ")
            sleep(8)

            try:
                x3, y3 = pyautogui.locateCenterOnScreen("isLoggedOut_imageToVerify.png")
                print('x3: ' + str(x3) +', y3: ' + str(y3))
                print("NOT LOGGED IN:  Leaving dealt_successfully as False. ")
                # dealt_successfully = True
            except:
                print("LOGGED IN:  Setting dealt_successfully as True. ")
                dealt_successfully = True

        self.clickCompassAndAlign()


    def clickCompassAndAlign(self):
        startTime = time.time()
        x5, y5 = pyautogui.locateCenterOnScreen("compass.png")
        pyautogui.moveTo(x5, y5, duration=0.5)
        pyautogui.click()
        sleep(1)
        pyautogui.keyDown('up')
        sleep(1.5)
        pyautogui.keyUp('up')

        # pyautogui.press('up', presses=10)

    def checkIfInvetoryFull(self):
        inventory_full = False
        while not inventory_full:
            try:
                x4, y4 = pyautogui.locateCenterOnScreen('checkIfLastInventorySlotIsEmpty.png')
                print('x4: ' + str(x4) +', y4: ' + str(y4))
                # call method that does mining/woodcutting/etc
            except:
                print("INVENTORY FULL!  Calling banking method...")
                inventory_full = True

    def checkIfInvetoryFullBoolean(self):
        is28thSlotOccupied = pyautogui.locateOnScreen('checkLastInvSlot1.png')
        print("Checking if inventory full...")

        if str(is28thSlotOccupied) == "None":
            # x20, y21 = pyautogui.locateCenterOnScreen('checkIfLastInventorySlotIsEmpty.png')
            # pyautogui.moveTo(x20, y21) #, pyautogui.easeInOutQuad
            # pyautogui.click()
            print("Inventory full!  Returning true...")
            return True
        else:
            print("Inventory NOT full!  Returning false...")
            return False

    def bankMagicLogsOnFullInventory(self):
        x6, y6 = pyautogui.locateCenterOnScreen('findMagicLogsBank.png')
        pyautogui.moveTo(x6 + 5, y6 + 5, duration=0.25)
        pyautogui.click()
        sleep(3)

    def locateUpdatedOreClusterMinimap_updated1(self):
        print('1) Looking for first ore cluster on minimap...')
        isFirstOreClusterFound = pyautogui.locateOnScreen('firstOreTopofCluster_updated1.png')

        if not str(isFirstOreClusterFound) == "None":
            x8, y8 = pyautogui.locateCenterOnScreen('firstOreTopofCluster_updated1.png') # , confidence=0.9
            # pyautogui.moveTo(x8 + (random.randrange(1, 7)), y8 + (random.randrange(1, 7)), pyautogui.easeInOutQuad)

            xa8 = x8 + random.randint(1,3)
            ya8 = y8 + random.randint(22,27)
            pyautogui.moveTo(xa8, ya8) #, pyautogui.easeInOutQuad
            pyautogui.click()
            print('Found 1st steps.  Moving... (RANDOMLY!)')
            # firstStepsDone = True
            sleep(3)
        else:
            print('NOT Found 1st steps!  Retrying through recursion...')
            sleep(3)
            self.locateUpdatedOreClusterMinimap_updated1()

    def locateUpdatedOreClusterMinimap_updated2(self):
        print('2) Looking for second ore cluster on minimap...')
        isSecondOreClusterFound = pyautogui.locateOnScreen('firstOreCluster_updated2.png') # , confidence=0.9

        if not str(isSecondOreClusterFound) == "None":
            x9, y9 = pyautogui.locateCenterOnScreen('firstOreCluster_updated2.png')
            # pyautogui.moveTo(x9 + (random.randrange(1, 7)), y9 + (random.randrange(1, 7)), pyautogui.easeInOutQuad)

            xa9 = x9 + random.randint(1,3)
            ya9 = y9 + random.randint(2,5)
            pyautogui.moveTo(xa9, ya9) #, pyautogui.easeInOutQuad
            pyautogui.click()
            print('Found 2nd steps.  Moving (RANDOMLY)...')
            # firstStepsDone = True
            sleep(3)
        else:
            print('NOT Found 2nd steps!  Retrying through recursion...')
            sleep(3)
            self.locateUpdatedOreClusterMinimap_updated2()

    def locateUpdatedOreClusterMinimap_updated3(self):
        print('3) Looking for third ore cluster on minimap...')
        isThirdOreClusterFound = pyautogui.locateOnScreen('thirdOreTopOfCluster1.png')

        if not str(isThirdOreClusterFound) == "None":
            x10, y10 = pyautogui.locateCenterOnScreen('thirdOreTopOfCluster1.png')
            # xa10 = x10 + random.randint(1,9)
            # ya10 = y10 + random.randint(4, 19)
            ya10 = y10 + 25
            # pyautogui.moveTo(x10 + (random.randrange(1, 7)), y10 + (random.randrange(1, 7)), pyautogui.easeInOutQuad)
            pyautogui.moveTo(x10, ya10) #, pyautogui.easeInOutQuad
            pyautogui.click()
            print('Found 3rd steps.  Moving...')
            # firstStepsDone = True
            sleep(6)
        else:
            print('NOT Found 3rd steps!  Retrying FIRSTLY with other option (edge case scenario)...')
            sleep(2)

            isThirdOreClusterBackupFound = pyautogui.locateOnScreen('thirdOreTopOfCluster2.png')
            if not str(isThirdOreClusterBackupFound) == "None":
                x11, y11 = pyautogui.locateCenterOnScreen('thirdOreTopOfCluster2.png')
                # xa11 = x11 + random.randint(38,48)
                # ya11 = y11 + random.randint(85, 114)
                ya11 = y11 + 15
                pyautogui.moveTo(x11, ya11) #, pyautogui.easeInOutQuad
                pyautogui.click()
                print('Found 3rd steps.  Moving (VERY RANDOMLY)...')
            else:
                print("3) NOT FOUND EITHER!  Exiting...")

            # self.locateUpdatedOreClusterMinimap_updated3()

    def locateUpdatedOreClusterMinimap_updated4(self):
        print('4) Looking for fourth ore cluster on minimap...')
        isLastOreClusterFound = pyautogui.locateOnScreen('thirdOreTopOfCluster3.png')

        if not str(isLastOreClusterFound) == "None":
            x12, y12 = pyautogui.locateCenterOnScreen('thirdOreTopOfCluster3.png')
            # xa12 = x12 + random.randint(8,14)
            # ya12 = y12 + random.randint(2, 10)
            xa12 = x12 + 5
            ya12 = y12 + 20

            # pyautogui.moveTo(x10 + (random.randrange(1, 7)), y10 + (random.randrange(1, 7)), pyautogui.easeInOutQuad)
            pyautogui.moveTo(xa12, ya12) #, pyautogui.easeInOutQuad
            pyautogui.click()
            print('Found 4th and last steps.  Moving (SLIGHTLY RANDOMLY)...')
            # firstStepsDone = True
            sleep(6)
        else:
            print('NOT Found 4th and last steps!  Retrying through backup option...')
            sleep(3)

            isLastOreClusterBackupFound = pyautogui.locateOnScreen('topRightCornerNearRuniteOre1.png')
            if not str(isLastOreClusterBackupFound) == "None":
                x13, y13 = pyautogui.locateCenterOnScreen('topRightCornerNearRuniteOre1.png')
                #xa13 = x13 + random.randint(20,28)
                #ya13 = y13 + random.randint(3, 11)

                pyautogui.moveTo(x13, y13) #, pyautogui.easeInOutQuad
                pyautogui.click()
                print('Found 4th and last steps (BACKUP!).  Moving (SLIGHTLY RANDOMLY)...')
                # firstStepsDone = True
                sleep(6)
            else:
                print("4) NOT FOUND EITHER!  Exiting...")
            # self.locateUpdatedOreClusterMinimap_updated4()
            # self.locateUpdatedOreClusterMinimap_updated4()

    def standInFrontOfBank_runiteOre(self):
        print('*BANKING* -> Going to stand in front of deposit/bank chest from runite ore...')
        isBankSignFound = pyautogui.locateOnScreen('bankSign1.png')

        if not str(isBankSignFound) == "None":
            x14, y14 = pyautogui.locateCenterOnScreen('bankSign1.png')
            # xa12 = x12 + random.randint(8,14)
            # ya12 = y12 + random.randint(2, 10)
            xa14 = x14
            ya14 = y14

            # pyautogui.moveTo(x10 + (random.randrange(1, 7)), y10 + (random.randrange(1, 7)), pyautogui.easeInOutQuad)
            pyautogui.moveTo(xa14, ya14) #, pyautogui.easeInOutQuad
            pyautogui.click()
            print('Found 4th and last steps.  Moving (SLIGHTLY RANDOMLY)...')
            # firstStepsDone = True
            sleep(6)
        else:
            print('NOT Found 4th and last steps!  Retrying through recursion...')
            sleep(3)
            self.standInFrontOfBank_runiteOre()


    def walkToRuniteOreFromBank(self):

        firstStepsDone = False
        secondStepsDone = False
        thirdStepsDone = False
        fourthAndLastStepsDone = False

        while not firstStepsDone:
            try:
                self.locateUpdatedOreClusterMinimap_updated1()
                firstStepsDone = True
                sleep(1)
            except:
                print('NOT FOUND 1st steps (walking from bank to runite ore)!  Retrying...')
                sleep(3)
                print('Calling self.locateUpdatedOreClusterMinimap_updated1() again...')
                self.locateUpdatedOreClusterMinimap_updated1()

        while not secondStepsDone:
            try:
                self.locateUpdatedOreClusterMinimap_updated2()
                secondStepsDone = True
                sleep(1)
            except:
                print('NOT FOUND 2nd steps (walking from bank to runite ore)!  Retrying...')
                sleep(3)
                print('Calling self.locateUpdatedOreClusterMinimap_updated2() again...')
                self.locateUpdatedOreClusterMinimap_updated2()

        while not thirdStepsDone:
            try:
                self.locateUpdatedOreClusterMinimap_updated3()
                thirdStepsDone = True
                sleep(1)
            except:
                print('NOT FOUND 3rd steps (walking from bank to runite ore)!  Retrying...')
                sleep(3)
                print('Calling self.locateUpdatedOreClusterMinimap_updated3() again...')
                self.locateUpdatedOreClusterMinimap_updated3()

        while not fourthAndLastStepsDone:
            try:
                self.locateUpdatedOreClusterMinimap_updated4()
                fourthAndLastStepsDone = True
                sleep(1)
            except:
                print('NOT FOUND 4th and last steps!  Retrying...')
                sleep(3)
                print('Calling self.locateUpdatedOreClusterMinimap_updated4() again...')
                self.locateUpdatedOreClusterMinimap_updated4()

        # we should NOW be within actual ore colour on screen -> do actual mining of ore now

    def walkToBankFromRuniteOre(self):

        firstStepsDone2 = False
        secondStepsDone2 = False
        thirdStepsDone2 = False
        fourthAndLastStepsDone2 = False
        inFrontOfBankStep = False

        while not firstStepsDone2:
            try:
                self.locateUpdatedOreClusterMinimap_updated4()
                firstStepsDone2 = True
                sleep(1)
            except:
                print('NOT FOUND 1st steps (walking from runite ore to bank)!  Retrying... ')
                sleep(3)
                print('Calling self.locateUpdatedOreClusterMinimap_updated4() again...')
                self.locateUpdatedOreClusterMinimap_updated4()

        while not secondStepsDone2:
            try:
                self.locateUpdatedOreClusterMinimap_updated3()
                secondStepsDone2 = True
                sleep(1)
            except:
                print('NOT FOUND 2nd steps (walking from runite ore to bank)!  Retrying...')
                sleep(3)
                print('Calling self.locateUpdatedOreClusterMinimap_updated3() again...')
                self.locateUpdatedOreClusterMinimap_updated3()

        while not thirdStepsDone2:
            try:
                self.locateUpdatedOreClusterMinimap_updated2()
                thirdStepsDone2 = True
                sleep(1)
            except:
                print('NOT FOUND 3rd steps (walking from runite ore to bank)!  Retrying...')
                sleep(3)
                print('Calling self.locateUpdatedOreClusterMinimap_updated2() again...')
                self.locateUpdatedOreClusterMinimap_updated2()

        while not fourthAndLastStepsDone2:
            try:
                self.locateUpdatedOreClusterMinimap_updated1()
                fourthAndLastStepsDone2 = True
                sleep(1)
            except:
                print('NOT FOUND 4th and last steps (walking from runite ore to bank)!  Retrying...')
                sleep(3)
                print('Calling self.locateUpdatedOreClusterMinimap_updated1() again...')
                self.locateUpdatedOreClusterMinimap_updated1()

        while not inFrontOfBankStep:
            try:
                self.standInFrontOfBank_runiteOre()
                inFrontOfBankStep = True
                sleep(1)
            except:
                print('NOT ABLE TO STAND IN FRONT OF BANK (walking from runite ore to bank)!  Retrying...')
                sleep(3)
                print('Calling self.standInFrontOfBank_runiteOre() again...')
                self.standInFrontOfBank_runiteOre()
        # we should NOW be within actual ore colour on screen -> do actual mining of ore now

    def openBank(self):
        print('*BANKING* -> Clicking the bank deposit box to quick-deposit...')
        isBankDepositImageFound = pyautogui.locateOnScreen('bankSign1.png', confidence = 0.9)

        if not str(isBankDepositImageFound) == "None":
            x17, y17 = pyautogui.locateCenterOnScreen('bankSign1.png', confidence = 0.9)
            # xa12 = x12 + random.randint(8,14)
            # ya12 = y12 + random.randint(2, 10)
            xa17 = x17 + 7
            ya17 = y17 - 5 

            # pyautogui.moveTo(x10 + (random.randrange(1, 7)), y10 + (random.randrange(1, 7)), pyautogui.easeInOutQuad)
            pyautogui.moveTo(xa17, ya17) #, pyautogui.easeInOutQuad
            pyautogui.click()
            print('Moving directly below deposit box through minimap bank icon...')
            # firstStepsDone = True
            sleep(5)

            # we are now ALWAYS directly below deposit box - we can do proper deposit now from the assocaited image
            isBankDepositTopFound = pyautogui.locateOnScreen('directlyToRightOfDepositBox_top1.png', confidence = 0.9)
            if not str(isBankDepositTopFound) == "None":
                x18, y18 = pyautogui.locateCenterOnScreen('directlyToRightOfDepositBox_top1.png', confidence = 0.9)
                # xa12 = x12 + random.randint(8,14)
                # ya12 = y12 + random.randint(2, 10)
                xa18 = x18
                ya18 = y18

                # pyautogui.moveTo(x10 + (random.randrange(1, 7)), y10 + (random.randrange(1, 7)), pyautogui.easeInOutQuad)
                pyautogui.moveTo(xa18, ya18) #, pyautogui.easeInOutQuad
                pyautogui.click()
                print('Found deposit box and clicked...')
                # firstStepsDone = True
                sleep(3)
            else:
                print('NOT Found bank deposit box!  Retrying through recursion...')
                sleep(3)
                self.openBank()


        else:
            print('NOT moved to directly below deposit box!  Retrying through recursion...')
            sleep(3)
            self.openBank()

    def doDepositAfterOpeningBank(self):
        print('*BANKING* -> After clicking deposit box, click deposit all items for quick banking...')
        isBankDepositImageFound = pyautogui.locateOnScreen('depositAll_withinBank1.png')

        if not str(isBankDepositImageFound) == "None":
            x17, y17 = pyautogui.locateCenterOnScreen('depositAll_withinBank1.png')
            # xa12 = x12 + random.randint(8,14)
            # ya12 = y12 + random.randint(2, 10)
            # x17 = x14
            # y17 = y14

            # pyautogui.moveTo(x10 + (random.randrange(1, 7)), y10 + (random.randrange(1, 7)), pyautogui.easeInOutQuad)
            pyautogui.moveTo(x17, y17) #, pyautogui.easeInOutQuad
            pyautogui.click()
            print('Found deposit all items button and clicked.')
            # firstStepsDone = True
            sleep(2)
        else:
            print('NOT Found deposit all items button!  Retrying through recursion...')
            sleep(3)
            self.doDepositAfterOpeningBank()

    def keepGoingRightAfterBanking(self):
        print('*SIMPLIFIED* -> Keep clicking right after banking!')
        isClientScreenImageFound = pyautogui.locateOnScreen('clientScreen_goRightToRuniteOre1.png')

        if not str(isClientScreenImageFound) == "None":
            x17, y17 = pyautogui.locateCenterOnScreen('clientScreen_goRightToRuniteOre1.png')
            # xa12 = x12 + random.randint(8,14)
            # ya12 = y12 + random.randint(2, 10)
            xa17 = x17 - 38
            ya17 = y17 + 15

            # pyautogui.moveTo(x10 + (random.randrange(1, 7)), y10 + (random.randrange(1, 7)), pyautogui.easeInOutQuad)
            pyautogui.moveTo(xa17, ya17) #, pyautogui.easeInOutQuad
            pyautogui.click()
            print('IN SIMPLIFIED MOVE TO ORE METHOD:  Clicking minimap to the right...')
            # firstStepsDone = True
            sleep(2)
            pyautogui.click()
            print('IN SIMPLIFIED MOVE TO ORE METHOD:  Clicking minimap to the right...')
            sleep(2)
            pyautogui.click()
            print('IN SIMPLIFIED MOVE TO ORE METHOD:  Clicking minimap to the right...')
            sleep(2)
            pyautogui.click()
            print('IN SIMPLIFIED MOVE TO ORE METHOD:  Clicking minimap to the right...')
            sleep(2)
            pyautogui.click()
            print('IN SIMPLIFIED MOVE TO ORE METHOD:  Clicking minimap to the right...')
            sleep(2)
            
        else:
            print('?????')
            sleep(3)
            self.keepGoingRightAfterBanking()

    def keepGoingLeftWhenInvFull(self):
        print('*SIMPLIFIED* -> Keep clicking left when inventory full!')
        isClientScreenImage2Found = pyautogui.locateOnScreen('prayerSymbol1.png')

        if not str(isClientScreenImage2Found) == "None":
            x17, y17 = pyautogui.locateCenterOnScreen('prayerSymbol1.png')
            # xa12 = x12 + random.randint(8,14)
            # ya12 = y12 + random.randint(2, 10)
            xa17 = x17 +25
            ya17 = y17

            # pyautogui.moveTo(x10 + (random.randrange(1, 7)), y10 + (random.randrange(1, 7)), pyautogui.easeInOutQuad)
            pyautogui.moveTo(xa17, ya17) #, pyautogui.easeInOutQuad
            pyautogui.click()
            print('IN SIMPLIFIED MOVE TO ORE METHOD:  Clicking minimap to the left...')
            # firstStepsDone = True
            sleep(2)
            pyautogui.click()
            print('IN SIMPLIFIED MOVE TO ORE METHOD:  Clicking minimap to the left...')
            sleep(2)
            pyautogui.click()
            print('IN SIMPLIFIED MOVE TO ORE METHOD:  Clicking minimap to the left...')
            sleep(2)
            pyautogui.click()
            print('IN SIMPLIFIED MOVE TO ORE METHOD:  Clicking minimap to the left...')
            sleep(2)
            # pyautogui.click()
            # print('IN SIMPLIFIED MOVE TO ORE METHOD:  Clicking minimap to the left...')
            # sleep(2)
        else:
            print('?????')
            sleep(3)
            self.keepGoingLeftWhenInvFull()

                
        
    def afterGoingRightFindClickRuneOre(self):
        thisRuneOreColor = 9012322
        color_runiteOre = (98, 132, 137)
        print("Looking for runite ore...")

        s = pyautogui.screenshot()
        for x in range(s.width):
            for y in range(s.height):
                xy = (x,y)
                if s.getpixel((x, y)) == color_runiteOre:
                    pyautogui.moveTo(x + 10, y, float(decimal.Decimal(random.randrange(3397, 3565)) / 10000),
                                     pyautogui.easeInOutQuad)
                    sleep(0.5)
                    pyautogui.click(x + 10, y)  # do something here
                    print("Found runite ore!  Clicking and sleeping 10 seconds...")
                    sleep(10)
                    return


    def walkToBankFromCurrentOre(self):
        doSomething = 2

    def doQuickBankingDeposit(self):
        doSomething = 3

    

    def defineAllBankImages(self):
        find_bank_box2 = pyautogui.locateOnScreen("data/bank_box_tiny5.png", confidence=0.9)
        find_bank_box5 = pyautogui.locateOnScreen("data/bank_box_tiny2.png", confidence=0.9)
        find_bank_box3 = pyautogui.locateOnScreen("data/bank_box_tiny_new1.png", confidence=0.9)
        find_bank_box4 = pyautogui.locateOnScreen("data/bank_box_tiny_right1.png", confidence=0.9)
        find_bank_box7 = pyautogui.locateOnScreen("data/bank_box_tiny_new3.png", confidence=0.9)
        find_bank_box8 = pyautogui.locateOnScreen("data/bank_box_tiny_new4.png", confidence=0.9)

    def getAdamantiteOreColorPoints(self):
        thisAdamantOreColor = 5662806

if __name__ == '__main__':
    # doAll().openBank()
    # doAll().openNRclientAndNavigate()
    # doAll().bankMagicLogsOnFullInventory()
    # doAll().doLoginAndCheck()
    #
    # doAll().walkToRuniteOreFromBank()
    # sleep(2)
    # print('*************** FINISHED WALKING TO RUNITE ORE SUCCESSFULLY *******')
    # sleep(2)
    # doAll().walkToBankFromRuniteOre()
    # sleep(1)
    # print('*************** FINISHED WALKING TO BANK SUCCESSFULLY *******')
    # doAll().openBank()
    # doAll().doDepositAfterOpeningBank()
    # print('*************** FINISHED DEPOSITING ALL ITEMS AND CLOSING BANK SUCCESSFULLY *******')

    infiniteLoop = False
    while not infiniteLoop:
        isInventoryFull = False
        doAll().keepGoingRightAfterBanking()
        while not isInventoryFull:
            doAll().afterGoingRightFindClickRuneOre()
            isInvFullLocal = doAll().checkIfInvetoryFullBoolean()
            if isInvFullLocal == True:
                isInventoryFull = True
        doAll().keepGoingLeftWhenInvFull()
        sleep(3)
        print('*************** FINISHED WALKING TO BANK SUCCESSFULLY *******')
        doAll().openBank()
        doAll().doDepositAfterOpeningBank()
        print('*************** FINISHED 1 SUCCESSFULL RUN - RERUNNING... *******')