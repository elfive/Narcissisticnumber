import time
import threading
import datetime

print("开始于:%s" %datetime.datetime.now().strftime("%Y/%d/%m %H:%M:%S"))
start=time.time()

ThreadsCount = int(input("同时运行的进程数，必须大于1："))
#线程数
EndNum = int(input("终止范围，必须大于100："))
#计算范围，默认100开始，终止数可以任意修改，大于100即可


threads = []
PartStart = []
PartEnd = []
Result = []

def CheckNum(Number):
    tmp=str(Number)
    len_num=len(tmp)
    sum_num = 0
    for i in range(len_num):
        sum_num=sum_num+(int(tmp[i])**len_num)
    if sum_num==int(Number):
        return True
        #print(Number,"是水仙花数")
    else:
        return False
        #print(Number,"不是水仙花数")

def ThreadCheck(Start,End):
    for j in range(int(Start),int(End)):
        if CheckNum(j):
            #print(j,"是水仙花数")
            Result.append(str(j)+"是水仙花数")

d=int(((EndNum-99)/ThreadsCount)+0.5)
for i in range(0,ThreadsCount):
    PartStart.append(100+i*d)
    PartEnd.append(PartStart[i]+d-1)
PartEnd[ThreadsCount-1]=EndNum
#print(";".join(str(item) for item in PartStart))
#print(";".join(str(item) for item in PartEnd))

#创建线程
for i in range(0,ThreadsCount):
    #print("启动第",i,"个线程")
    t = threading.Thread(target=ThreadCheck,args=(PartStart[i],PartEnd[i],))
    threads.append(t)

if __name__ == '__main__':

    #启动线程
    for i in range(0,ThreadsCount):
        threads[i].start() 
    for i in range(0,ThreadsCount):
        threads[i].join()

    #主线程
    Result.sort(key=lambda t:t[0])
    print("\n".join(Result))
    end = time.time()
    input("结束于:%s" %datetime.datetime.now().strftime("%Y/%d/%m %H:%M:%S")+"\n"+"本次耗时："+str(end-start))
