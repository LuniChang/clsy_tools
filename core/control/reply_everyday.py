import win32api
import win32gui
import win32con
import time

from control.base_control import BaseControl

import common.screen as screen


class ReplyEveryDay(BaseControl):

    missionType = 0
    missionlevel = ["4","4","2","3"]
    teamNum = ["1","2","3","4"]
    def __init__(self, handle, interval):
        self.handle = handle
        self.interval = interval

    def onSelectTeam(self):
        print("onSelectTeam")
        return screen.autoCompareResImgHash(self.handle, "everyday\\select_team_82_86_100_100.png")
    def onBattleEnd(self):
        print("onBattleEnd")
        return screen.autoCompareResImgHash(self.handle, "everyday\\win_35_15_65_30.png") \
            or screen.autoCompareResImgHash(self.handle, "everyday\\get_item_35_15_65_30.png")\
            or screen.autoCompareResImgHash(self.handle, "everyday\\end_82_86_100_100.png")\
            or screen.autoCompareResImgHash(self.handle, "everyday\\end_0_0_30_10.png")



   
    def clickBattle(self):
        self.leftClickPer(85, 90)

    def isAtHome(self):
        print("isAtHome")
        return screen.autoCompareResImgHash(self.handle, "everyday\\home_0_0_40_30.png")
    def inLevel(self):
        print("inLevel")
        return screen.autoCompareResImgHash(self.handle, "everyday\\inlevel_0_0_40_70.png")


    def run(self):
        battleCount = 0
        toBattleType = 0
        while self._isRun:
            win32gui.SetForegroundWindow(self.handle)

            # 底部菜单hash
            self.resetCusor()

            if self.isAtHome():
  
                if self.missionType == 0:

            
                    self.leftClickPer(20*(toBattleType+1),50)

                  
                   
                    if battleCount >= 8:
                        break
                    #     battleCount = 0
                    # pass
                else :
                    toBattleType=self.missionType-1
                    self.leftClickPer(20*(toBattleType+1),50)
            

                time.sleep(2)

            if self.inLevel():
                print("battleCount",battleCount)
                if self.missionType == 0:
                    curToBattleType=toBattleType
           
                    toBattleType = int(battleCount/2)
                    # if battleCount==2:
                    #    toBattleType = 1
                    # if battleCount==4:
                    #    toBattleType = 2
                    # if battleCount==6:
                    #    toBattleType = 3
                    if toBattleType>curToBattleType :
                        self.leftClickPer(2,2)#返回每日界面
                        time.sleep(1)
                        continue
                
                level=int(self.missionlevel[toBattleType])   
        
                self.leftClickPer(35,10+level*16)
                time.sleep(1)

            if self.onSelectTeam():
                teamCode=int(self.teamNum[toBattleType])
 
                self.toSelectTeam(teamCode)
                self.clickBattle()
                battleCount = battleCount+1

     
            if self.onBattleEnd():
                self.battleContinue()
                time.sleep(2)


            

            time.sleep(self.interval)
            # screen.grabCaptureDir(self.handle,"reply_battle")
