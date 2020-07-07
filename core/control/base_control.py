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

    


    def clickOnGetItems(self):
        win32gui.SetForegroundWindow(self.handle)
        self.leftClick(self.getPosX(50), self.getPosY(65))

    def battleContinue(self):
        win32gui.SetForegroundWindow(self.handle)
        self.leftClick(self.getPosX(99), self.getPosY(99))
        self.resetCusor()


  

    def resetCusor(self):
        time.sleep(0.5)
        win32api.SetCursorPos((0, 0))



        


   

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
        self.leftClickPer(10,20+teamNo*10)

      


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