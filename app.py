from tkinter import *
import psutil
from tabulate import tabulate


class PcAddresses:
    def __init__(self,root):
        self.root=root
        self.root.title("Computer Addresses")
        self.root.geometry("700x300")
        self.root.iconbitmap("logo982.ico")
        self.root.resizable(0,0)



        def on_enter1(e):
            but_show['background']="black"
            but_show['foreground']="cyan"
  
        def on_leave1(e):
            but_show['background']="SystemButtonFace"
            but_show['foreground']="SystemButtonText"

        def on_enter2(e):
            but_clear['background']="black"
            but_clear['foreground']="cyan"
  
        def on_leave2(e):
            but_clear['background']="SystemButtonFace"
            but_clear['foreground']="SystemButtonText"

    
        def clear():
            text.delete("1.0","end")

        
        def show():
            details=psutil.net_if_addrs()
            interface=[]
            ip_address=[]
            netmask_ip=[]
            broadcast=[]
            for ins,ina in details.items():
                interface.append(ins)
                for address in ina:
                    if str(address.family)=="AddressFamily.AF_INET":
                        ip_address.append(address.address)
                        netmask_ip.append(address.netmask)
                        broadcast.append(address.broadcast)
            data={
                    "Interface":[*interface],
                    "IP-Address":[*ip_address],
                    "Netmask_ip":[*netmask_ip],
                    "Broadcast ip":[*netmask_ip]
                }
            with open("C:/TEMP/addresses.txt","w") as f:
                f.write(tabulate(data,headers="keys",tablefmt="github"+"\n\n"))
                f.close()

            with open("C:/TEMP/addresses.txt","r") as f:
                text.insert("end",f.read())
            
            







#====================frame======================================#
        mainframe=Frame(self.root,width=700,height=300,relief="ridge",bd=3)
        mainframe.place(x=0,y=0)

        firstframe=Frame(mainframe,width=694,height=70,relief="ridge",bd=3,bg="black")
        firstframe.place(x=0,y=0)

        secondframe=Frame(mainframe,width=694,height=225,relief="ridge",bd=3)
        secondframe.place(x=0,y=70)

#========================================================================#
        
        but_show=Button(firstframe,width=19,text="Show Addresses",font=('times new roman',12),cursor="hand2",command=show)
        but_show.place(x=100,y=17)
        but_show.bind("<Enter>",on_enter1)
        but_show.bind("<Leave>",on_leave1)

        but_clear=Button(firstframe,width=19,text="Clear",font=('times new roman',12),cursor="hand2",command=clear)
        but_clear.place(x=400,y=17)
        but_clear.bind("<Enter>",on_enter2)
        but_clear.bind("<Leave>",on_leave2)

#===========================================================================#

        scol=Scrollbar(secondframe,orient="vertical")
        scol.place(relx=1, rely=0, relheight=1, anchor='ne')
        
        text=Text(secondframe,height=11,width=83,font=('times new roman',12),yscrollcommand=scol.set,relief="sunken",bd=3,fg="black")      
        text.place(x=0,y=0)
        scol.config(command=text.yview)
        







if __name__ == "__main__":
    root=Tk()
    app=PcAddresses(root)
    root.mainloop()