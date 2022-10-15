from guizero import App, Combo, Text, CheckBox, PushButton, info, Box, Picture

#def do_configure(channel):
def do_configure(args):
    print (args)
    # print ("configure", channel)
    # if channel <= 7:
       # info("configure", channel)



app = App(title="TH7 Thermocouple Pi-HAT", width=600, height=600)

title_box = Box(app, width="fill", align="top", border=True, height=100)
title = Text(title_box, text="TH7 Vcc=5.11 Vref=4.096 status=OK ", align="bottom")

th7_box = Box(app, width="fill", layout="grid", align="top", border=True)
bot_box = Box(app, width="fill", layout="auto", align="bottom", border=True, height=100)


ydown = 0
titleth7 = Text(th7_box, text=" ", grid=[0,ydown], align="left")
ydown += 1
blank_line = Text(th7_box, text=" ", grid=[0,ydown], align="left")
ydown += 1
blank_line = Text(th7_box, text=" ", grid=[0,ydown], align="left")
ydown += 1

#title BAR over th readings and control
channel_no = Text(th7_box, text=" channel ", grid=[0,ydown], align="left")
thermocouple_type = Text(th7_box, text=" Type ", grid=[1,ydown], align="left")
conf1_title = Text(th7_box, text="configure ", grid=[2,ydown], align="left")
temperature_title = Text(th7_box, text="  Temperature ", grid=[3,ydown], align="left")
status_title = Text(th7_box, text="  status ", grid=[4,ydown], align="left")
ydown += 1

channel = [1,2,3,4,5,6,7,8]
conf = [1,2,3,4,5,6,7,8]
temp = [1,2,3,4,5,6,7,8]
status = [1,2,3,4,5,6,7,8]
th_choice = ["K","K","K","K","K","K","K","R"]



conf[1] = PushButton(th7_box, command=lambda : do_configure(1) , text="config"+str(1), grid=[2,ydown+0], align="left")
conf[2] = PushButton(th7_box, command=lambda : do_configure(2) , text="config"+str(2), grid=[2,ydown+1], align="left")
conf[3] = PushButton(th7_box, command=lambda : do_configure(3) , text="config"+str(3), grid=[2,ydown+2], align="left")
conf[4] = PushButton(th7_box, command=lambda : do_configure(4) , text="config"+str(4), grid=[2,ydown+3], align="left")
conf[5] = PushButton(th7_box, command=lambda : do_configure(5) , text="config"+str(5), grid=[2,ydown+4], align="left")
conf[6] = PushButton(th7_box, command=lambda : do_configure(6) , text="config"+str(6), grid=[2,ydown+5], align="left")
conf[7] = PushButton(th7_box, command=lambda : do_configure(7) , text="config"+str(7), grid=[2,ydown+6], align="left")

for i in range (1,8):
  channel[i] = Text(th7_box, text=str(i), grid=[0,ydown], align="left")
  th_choice[i] = Combo(th7_box, options=["K", "J", "R", "T"], grid=[1,ydown], align="left")
  temp[i] = Text(th7_box, text="137.4", grid=[3,ydown], align="left")
  status[i] = Text(th7_box, text="OK", grid=[4,ydown], align="left")
  ydown += 1



app.display()


