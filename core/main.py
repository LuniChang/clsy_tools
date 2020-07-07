import win32api
import win32gui
import win32con
import time
import tkinter as tk



from control.reply_everyday import ReplyEveryDay



import common.screen as screen




# 从顶层窗口向下搜索主窗口，无法搜索子窗口
# FindWindow(lpClassName=None, lpWindowName=None)  窗口类名 窗口标题名


handle = screen.getWinHandle()
main = tk.Tk()

replyEveryday = ReplyEveryDay(handle, 5)


def resetHandle():
    handle = screen.getWinHandle()
    replyEveryday.handle = handle
 

main.title("碧蓝航线工具")
main.geometry("480x780")

fm1 = tk.Frame(main)
fm1.pack()


tk.Label(fm1, text="模拟器分辨率1024*576").grid(row=0, column=2, columnspan=3)


tk.Button(fm1, text="重设窗口句柄", width=10, height=1,
          command=resetHandle).grid(row=1, column=1)

missionType=tk.IntVar()
missionType.set(0)

missionlevel=tk.StringVar()
missionlevel.set("4,4,2,3")

teamNum=tk.StringVar()
teamNum.set("1,2,3,4")

def startEveryday():
    replyEveryday.missionType=missionType.get()
    replyEveryday.missionlevel=missionlevel.get().split(",")
    replyEveryday.teamNum=teamNum.get().split(",")
    replyEveryday.start()

tk.Label(fm1,text="0自动左到右1234按顺序").grid(row=3,column=0)

tk.Entry(fm1,textvariable=missionType,width=10).grid(row=3,column=1)
tk.Label(fm1,text=missionlevel).grid(row=3,column=0)

tk.Label(fm1,text="难度").grid(row=4,column=0)
tk.Entry(fm1,textvariable=missionlevel,width=10).grid(row=4,column=1)

tk.Label(fm1,text="队伍").grid(row=5,column=0)
tk.Entry(fm1,textvariable=teamNum,width=10).grid(row=5,column=1)
tk.Button(fm1, text="开始每日", width=20, height=1,
          command=startEveryday).grid(row=6, column=0)
tk.Button(fm1, text="结束每日", width=20, height=1,
          command=replyEveryday.stop).grid(row=6, column=1)





tk.Label(main, text="工具操作").pack()

# fmTools=tk.Frame(main).pack()
tk.Button(main, text="窗口截图",
          width=10, height=1,
          command=lambda: screen.grabCaptureDef(hwnd=handle, needShow=True)).pack()


tk.Label(main, text="左X百分比").pack()
xLeft = tk.Entry(main, textvariable=float)
xLeft.pack()

tk.Label(main, text="左Y百分比").pack()
yLeft = tk.Entry(main)
yLeft.pack()

tk.Label(main, text="右X百分比").pack()
xRight = tk.Entry(main)
xRight.pack()

tk.Label(main, text="右Y百分比").pack()
yRight = tk.Entry(main)
yRight.pack()
btnPerCap = tk.Button(main, text="百分比截图",
                      width=10, height=1,
                      command=lambda: screen.grabCaptureRectPerHash(
                          hwnd=handle, tLeft=xLeft.get(), tTop=yLeft.get(), tRight=xRight.get(), tBottom=yRight.get(), needShow=True))
btnPerCap.pack()

tk.Label(main, text="取图片哈希路径").pack()
textPath = tk.Entry(main)
textPath.pack()
texthash = tk.Entry(main)
texthash.pack()
hashBtn = tk.Button(main, text="取图片哈希", width=10, height=1, command=lambda: texthash.insert(
    index=0, string=screen.getImgHashByPath(path=textPath.get())))
hashBtn.pack()


# 进入消息循环
main.mainloop()


exit()
