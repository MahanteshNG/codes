def check(ls):
    if ls[0]==4 or 5 or 6 or 3:
        if ls[0]==3:
            if ls[1]==7:
                return 1
            return 1
        return 1
    else:
        return 0



ls=list(input())
ll=len(ls)
lpp=[]
lqq=[]
sum1=0
sum2=0
print("length",ll)
if 13<=ll:
    if ll<=16:
        q=check(ls)
        if q==1:
            lp=ls[-2::-2]
            for i in range(0,(len(lp))):
                lpp.append(int(lp[i]))
            print("second digit",lpp)
            for j in range((len(lpp))):
                lpp[j]=lpp[j]*2
                if (lpp[j]//10)>=1:
                    lpp[j]=(lpp[j]//10)+(lpp[j]%10)
                sum1+=lpp[j]
            print("step1",lpp)
            print("step2",sum1)



            lq = ls[-1::-2]
            for d in range(0,len(lq)):
                lqq.append(int(lq[d]))
            print(lqq)
            for k in range(0,len(lqq)):
                sum2+=lqq[k]
            print("step 3",sum2)
            print(sum1+sum2)
            f=(sum1+sum2)%10
            print("step 4",f)
            if f==0:
                print("valid")
            else:
                print("invalid44")
        else:
            print("invalid33")
    else:
        print("invalid22")
else:
    print("invalid11")
#379354508162306






