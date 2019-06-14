%matplotlib inline
import pandas as pd
//NMH FILES
filepath = r"C:\Users\T02574\Documents\nhm.csv"

df1 = pd.read_csv(filepath) 

tt="project"
for i in range(1,df1["project_id"].max()+1):
    df2=df1[df1.project_id==i]
    import matplotlib.pyplot  as plt
    tt=tt+str(i) 
    %matplotlib inline

    plt.plot(df2.SNo,df2.MeanNMHDays,'-ok',color='g',label="mean days")
    plt.plot(df2.SNo,df2.AverageDays,color='orange',label="average")
    plt.title(tt)
    plt.ylabel("NMH DAYS")
    tt=tt+".png"
    plt.legend()
    for x,y in zip(df2.SNo,df2.MeanNMHDays):
               label="{:.2f}".format(y)
               plt.annotate(label,(x,y),ha="right")
               if(df2["SNo"].count()>12):
                   plt.savefig('D://Pics//'+tt,dpi=(600))
               else :
                   plt.savefig('D://Pics//'+tt)
    tt="project"        
//EHS FILES
filepath = r"C:\Users\T02574\Documents\ehs.csv"

df1 = pd.read_csv(filepath) 

tt="project"
for i in range(1,df1["project_id"].max()+1):
    df2=df1[df1.project_id==i]
    import matplotlib.pyplot  as plt
    tt=tt+str(i) 
    %matplotlib inline

    plt.plot(df2.SNo,df2.MeanEHSDays,'-ok',color='g',label="mean days")
    plt.plot(df2.SNo,df2.AverageDays,color='orange',label="average")
    plt.title(tt)
    plt.ylabel("EHS DAYS")
    tt=tt+".png"
    plt.legend()
    for x,y in zip(df2.SNo,df2.MeanEHSDays):
               label="{:.2f}".format(y)
               plt.annotate(label,(x,y),ha="right")
               if(df2["SNo"].count()>12):
                   plt.savefig('D://Pics//'+tt,dpi=(600))
               else :
                   plt.savefig('D://Pics//'+tt)
    tt="project"        
