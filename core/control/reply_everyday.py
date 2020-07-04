import win32api
import win32gui
import win32con
import time

from control.base_control import BaseControl

import common.screen as screen


class ReplyEveryDay(BaseControl):

    missionType = 0
    missionlevel = ["10","10","10","10"]
    teamNum = ["10","10","10","10"]
    def __init__(self, handle, interval):
        self.handle = handle
        self.interval = interval

    def onSelectTeam(self):
        print("onSelectTeam")
        return screen.autoCompareResImgHash(self.handle, "everyday//on_select_team_78_82_90_88.png")

    def onReady(self):
        return screen.autoCompareResImgHash(self.handle, "everyday//ready_80_84_96_94.png")

    def clickBattle(self):
        self.leftClickPer(85, 90)

    def isAtHome(self):
        print("isAtHome")
        return screen.autoCompareResImgHash(self.handle, "everyday//home_0_0_40_30.png")
    def inLevel(self):
        print("inLevel")
        return screen.autoCompareResImgHash(self.handle, "everyday//inlevel_0_0_40_70.png")

    def clickEx(self):
        self.leftClickPer(90, 20)

    def clickHard(self):
        self.leftClickPer(90, 45)

    def clickNormal(self):
        self.leftClickPer(90, 55)

    def clickEasy(self):
        self.leftClickPer(90, 70)
    def onBattleEndCount(self):
        return self.matchResImgInWindow("battle_end_68_86_92_96.png")\
            or screen.autoCompareResImgHash(self.handle,"battle_end2_68_86_92_96.png")


    def run(self):
        battleCount = 0
        toBattleLevel = 0
        while self._isRun:
            win32gui.SetForegroundWindow(self.handle)

            # 底部菜单hash
            self.resetCusor()

            if self.isAtHome():
  
                if self.missionType == 0:
                    if toBattleLevel == 1:
                        self.clickEx()
                    if toBattleLevel == 2:
                        self.clickHard()
                    if toBattleLevel == 3:
                        self.clickNormal()
                    if toBattleLevel == 4:
                        self.clickEasy()
                    battleCount = battleCount+1
                    toBattleLevel = int(battleCount/2)+2

                    if battleCount > 8:
                        battleCount = 0
                    pass

                if self.missionType == 1:
                    self.clickEx()

                if self.missionType == 2:
                    self.clickHard()

                if self.missionType == 3:
                    self.clickNormal()

                if self.missionType == 4:
                    self.clickEasy()

                time.sleep(2)

            if self.onSelectTeam():
                self.clickNeedLeaderCat()
                time.sleep(2)
                self.intoMap()
                time.sleep(2)

            if self.onReady():
                self.clickBattle()

            if self.onBattleEnd():
                self.battleContinue()
                time.sleep(2)

            if self.onGetItems():
                self.battleContinue()
                time.sleep(2)
            if self.onBattleEndCount():

                self.battleContinue()
                time.sleep(3)

            time.sleep(self.interval)
            # screen.grabCaptureDir(self.handle,"reply_battle")
