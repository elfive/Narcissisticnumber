from timeit import timeit
import datetime
import time
import multiprocessing
from operator import itemgetter, attrgetter

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
def ProcessCheck(Start,End,ResQueue):
    ChildResult=[]
    for j in range(int(Start),int(End)+1):
        if CheckNum(j):
            #print(j,"是水仙花数")
            ResQueue.put(j)

if __name__ == '__main__':

    ProcessCount = int(input("同时运行的进程数，必须大于1："))
    #进程数 
    EndNum = int(input("终止范围，必须大于100："))
    #计算范围，默认100开始，终止数可以任意修改，大于100即可
    PartStart = [100]*ProcessCount          #每个process计算的起点
    PartEnd = [EndNum]*ProcessCount         #每个process计算的终点
    FinalResult = []                        #所有结果存储在Result数组中

    TotalCount = EndNum-99
    d=int((2*TotalCount/(ProcessCount**2+ProcessCount))+0.5)
    #PartStart.append(100)
    for i in range(1,ProcessCount):
        PartStart[i] = EndNum-int(0.5*d*(ProcessCount-i)*(ProcessCount-i+1))+1
        PartEnd[i-1] = PartStart[i]-1
    
    start=time.time()
    print("开始于:%s" %datetime.datetime.now().strftime("%Y/%d/%m %H:%M:%S"))
    Result=multiprocessing.Queue()           #创建一个进程间通讯的队列
    threads=[]
    
    for i in range(ProcessCount):
        p=multiprocessing.Process(target=ProcessCheck, args=(PartStart[i],PartEnd[i],Result,))
        threads.append(p)
    for i in range(ProcessCount):
        threads[i].start()
    for i in range(ProcessCount):
        threads[i].join()
    
    for i in range(Result.qsize()):
        FinalResult.append(int(Result.get()))
    FinalResult.sort()
    for i in  range(len(FinalResult)):
        print(str(FinalResult[i])+"是水仙花数")
    end = time.time()
    input("结束于:%s" %datetime.datetime.now().strftime("%Y/%d/%m %H:%M:%S")+"\n"+"本次耗时："+str(end-start))
   
