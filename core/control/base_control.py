import win32api
import win32gui
import win32con
import common.screen as screen
import threading
import time
class BaseControl:
    
    handle=0
    interval=5

    _isRun = False

    def __init__(self):
        pass

    def stop(self):
        self._isRun=False
      
    def start(self):
        if self._isRun:
            return
        self._isRun=True
        t=threading.Thread(target=self.run)
        t.start()

    def getPosX(self,srcPer):
        srcPer=srcPer*0.01
        wLeft, wTop, wRight, wBottom = screen.appGetWindowRect(self.handle)
        width = wRight-wLeft
        return int(wLeft+(width*srcPer))

    def getPosY(self,srcPer):
        srcPer=srcPer*0.01
        wLeft, wTop, wRight, wBottom = screen.appGetWindowRect(self.handle)
        height = wBottom-wTop
        return int(wTop+(height*(srcPer)))

    def onGetItems(self):
        print("onGetItems")
        return self.matchResImgInWindow("on_get_item_40_20_60_40.png")


    def dragPer(self,x,y,toX,toY):
        win32api.SetCursorPos((self.getPosX(x), self.getPosY(y)))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN , 0, 0, 0, 0)
        time.sleep(0.2)  
        moveToX=self.getPosX(toX)
        moveToY=self.getPosY(toY)
        win32api.mouse_event(win32con.MOUSEEVENTF_ABSOLUTE + win32con.MOUSEEVENTF_MOVE, moveToX*47, moveToY*85, 0, 0)  
        time.sleep(0.2)
        win32api.SetCursorPos((moveToX, moveToY))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)  
        self.resetCusor()

    def leftClick(self,x,y):
        win32api.SetCursorPos((x, y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN |
        win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)  
        self.resetCusor()

    def leftClickPer(self,x,y):
        win32api.SetCursorPos((self.getPosX(x), self.getPosY(y)))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN , 0, 0, 0, 0)  
        time.sleep(0.2)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP , 0, 0, 0, 0)  
         
        self.resetCusor() 

    

    def clickNeedLeaderCat(self):
        win32gui.SetForegroundWindow(self.handle)
        win32api.SetCursorPos((self.getPosX(95), self.getPosY(35)))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN |
        win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0) 
        self.resetCusor()

    def clickOnGetItems(self):
        win32gui.SetForegroundWindow(self.handle)
        self.leftClick(self.getPosX(50), self.getPosY(65))

    def battleContinue(self):
        win32gui.SetForegroundWindow(self.handle)
        self.leftClick(self.getPosX(85), self.getPosY(90))
        self.resetCusor()

    def closeNewMission(self):
        win32gui.SetForegroundWindow(self.handle)
        self.leftClick(self.getPosX(50), self.getPosY(72))
        self.resetCusor()

    def switchTeam(self):
        print("onSelectTeam")
        win32gui.SetForegroundWindow(self.handle)
        self.leftClickPer(82,96)
        time.sleep(1)
        self.resetCusor()
        
    def resetTeamLocation(self):
        print("resetTeamLocation")
        win32gui.SetForegroundWindow(self.handle)
        self.leftClickPer(82,96)
        time.sleep(3)
        self.leftClickPer(82,96)
        time.sleep(3)
        self.resetCusor()

    def moveLeft(self,num=1):
        print("moveLeft")
        win32gui.SetForegroundWindow(self.handle)
        self.leftClickPer(50-num*10,50)
        time.sleep(num)
        self.resetCusor()

    def moveRight(self,num=1):
        print("moveRight")
        win32gui.SetForegroundWindow(self.handle)
       
        self.leftClickPer(50+num*10,50)
        time.sleep(num)
        self.resetCusor()

    def moveUp(self,num=1):
        print("moveUp")
        win32gui.SetForegroundWindow(self.handle)
        self.leftClickPer(50,50-num*13)
        time.sleep(num)
        self.resetCusor()

    def moveDown(self,num=1):
        print("moveDown")
        win32gui.SetForegroundWindow(self.handle)
   
        self.leftClickPer(50,50+num*15)
        time.sleep(num)
        self.resetCusor()

    def resetCusor(self):
        time.sleep(0.5)
        win32api.SetCursorPos((0, 0))

    def onBattleEnd(self):
        return screen.autoCompareResImgHash(self.handle,"on_battle_end_10_10_90_30.png") \
            or screen.autoCompareResImgHash(self.handle,"battle_end1_30_80_50_95.png") 



    def onBattleEndCount(self):
        return self.matchResImgInWindow("battle_end_68_86_92_96.png")\
            # or screen.autoCompareResImgHash(self.handle,"battle_end2_68_86_92_96.png")


    def isInMap(self):
        return screen.autoCompareResImgHash(self.handle,"in_map_65_90_100_100.png")

    def onGetSR(self):
        print("onGetSR") 
        return screen.autoCompareResImgHashValue(self.handle,"on_get_sr_70_20_95_60.png")>0.2

    def onGetSSR(self):
        print("onGetSSR") 
        return screen.autoCompareResImgHashValue(self.handle,"on_get_ssr_70_10_90_50.png")>0.2

    def clickOnGetSR(self):
        self.leftClickPer(98,98)
        
    def isNewMission(self):#TODO 待优化
        print("isNewMission")
        return screen.autoCompareResImgHashValue(self.handle,"new_mission_28_26_70_76.png") \
            or self.matchResImgInWindow(self.handle,"newtask_28_26_70_30.png") \
            or self.matchResImgInWindow("newtask_30_68_66_76.png") 

    def onSelectTeam(self):
        print("onSelectTeam")
        return screen.autoCompareResImgHash(self.handle,"on_select_team_78_80_92_88.png")
    def onSelectTeamByMatch(self):#这种方式在地图会有问题
        print("onSelectTeamByMatch")
        return self.matchResImgInWindow("on_select_team_78_80_92_88.png")  
    def intoMap(self):
        win32gui.SetForegroundWindow(self.handle)
        self.leftClick(self.getPosX(80), self.getPosY(85))   

    def atTeamIntoMap(self):
        win32gui.SetForegroundWindow(self.handle)
        win32api.SetCursorPos((self.getPosX(80), self.getPosY(85)))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN |
        win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)      
        self.resetCusor()      

    #阵容小于3或者大于6不能用
    def toSelectTeam(self,teamNo):
        win32gui.SetForegroundWindow(self.handle)
        if teamNo==1 :
           win32api.SetCursorPos((self.getPosX(30), self.getPosY(50)))#点击1队
        elif teamNo==2:
           win32api.SetCursorPos((self.getPosX(55), self.getPosY(50)))#点击2队
        elif teamNo==3:    
           win32api.SetCursorPos((self.getPosX(80), self.getPosY(50)))#点击3队
        elif teamNo==4:    
           win32api.SetCursorPos((self.getPosX(30), self.getPosY(55)))#点击4队
        elif teamNo==5:    
           win32api.SetCursorPos((self.getPosX(55), self.getPosY(55)))#点击5队
        elif teamNo==6:    
           win32api.SetCursorPos((self.getPosX(80), self.getPosY(55)))#点击6队
        else :
            pass

        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN |
        win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)    


    def matchResImgInWindow(self,imgName,threshold=0.8):
        xylist=screen.matchResImgInWindow(self.handle,imgName,threshold)
        if len(xylist) >0:
            return True
        else:
            return False

    
    def isHpEmpty(self):
        return screen.autoCompareResImgHash(self.handle,"hp_empty_10_40_90_62.png")

    def run(self):
        pass

 

pass