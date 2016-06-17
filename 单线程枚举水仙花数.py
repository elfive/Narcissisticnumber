
import time
import datetime

def CheckNum(Number):
    tmp=str(Number)
    len_num=len(tmp)
    sum_num = 0
    for i in range(len_num):
        sum_num=sum_num+(int(tmp[i])**len_num)
    if sum_num==int(Number):
        return True
        #print(x,"是水仙花数")
    else:
        return False
        #print(x,"不是水仙花数")


print("                  指令代码，auto代表自动检测100-999，数字代表单个检测\n"
      "                         auto后面加数字则表示运行到指定处截止")
command=input("请输入指令代码：")
print("开始于:%s" %datetime.datetime.now().strftime("%Y/%d/%m %H:%M:%S"))
#command="auto9999999"
start=time.time()
if str(command[0:4])=="auto":
    StrLen=len(command)
    if StrLen>=7:
        tmp=command[4:]
        if tmp.isdigit():
            EndNum=int(tmp)
        else:
            print("请输入一个正确的数值！")
            quit()
    elif StrLen>4:
        tmp=command[4:]
        if tmp.isdigit():
            print("数字值必须大于100！")
        else:
            print("请输入一个正确的数值！")
        quit()
    else:
        EndNum=999
    for i in range(100,EndNum,1):
        if CheckNum(i):
            print(i,"是水仙花数")
else:
    if not command.isdigit():
        print("请输入一个正确的数值！")
        quit()
    elif int(Command)<100:
        print("数字值必须大于100！")
        quit()
    else:
        if CheckNum(int(command)):
            print(command,"是水仙花数")
        else:
            print(command,"不是水仙花数")
end = time.time()
input("结束于:%s" %datetime.datetime.now().strftime("%Y/%d/%m %H:%M:%S")+"\n"+"本次耗时："+str(end-start))


