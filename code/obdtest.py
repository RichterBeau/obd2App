import obd
import smtplib
from guizero import App,Text,Box

obd.logger.setLevel(obd.logging.DEBUG)
ports =  obd.scan_serial()
print (ports)
connection = obd.OBD()

#chk=0
eFROM = "richterbeaua@gmail.com"
eTO = "6316455069@vtext.com"
Subject = "Speeding Alert"
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)


def speedAlert(): #currently not working, issue with defining chkbit
    if chk == 0:
        text = "Someone is going ph in your car!"
        eMessage = 'Subject: {}\n\n{}'.format(Subject, text)
        server.login("richterbeaua@gmail.com", "tyecavldtgopuspz")
        server.sendmail(eFROM, eTO, eMessage)
        chk = 1
        


def update():
    cmd1 = obd.commands.SPEED  
    cmd2 = obd.commands.RPM
    cmd3 = obd.commands.COOLANT_TEMP
    cmd4 = obd.commands.RUN_TIME
    response1 = connection.query(cmd1)
    response2 = connection.query(cmd2)
    response3 = connection.query(cmd3)
    response4 = connection.query(cmd4)
    rpm0 = str(response2.value)             #RPM
    rpm = rpm0[0:5]
    rpmText.clear()
    rpmText.append(rpm)
    spd0 = str(response1.value.to("mph"))   #SPEED
    #spdCompare = spd0[3]
    #if spdCompare == ".": #if the 4th character of the string is . the speed is 3 digits
          #speedAlert()
    spd = spd0[0:3]
    spdText.clear()
    spdText.append(spd)
    cool0 = str(response3.value)            #COOLANT TEMP
    cool = cool0 
    coolText.clear()
    coolText.append(cool)
    time0 = str(response4.value)            # RUN TIME
    time = time0 
    runText.clear()
    runText.append(time)
    spdText.after(1, update)


app = App(title="obd App", layout = "grid", width = 800)

rpmMeter = Text(app, text="    RPM  ", size=30, grid = [0,0])
rpmBox = Box(app, width = 400, height = 80,grid = [0,1])
rpmBox.set_border(4, "black")
rpmText = Text(rpmBox, text = "0", size = 30, align = "bottom")


speedoMeter = Text(app, text="    Speed (mph)  ", size=30 ,grid = [1,0])
spdBox = Box(app, width = 400, height = 80, grid = [1,1])
spdBox.set_border(4, "black")
spdText = Text(spdBox, text = "0", size = 30, align = "bottom")


coolMeter = Text(app, text="Coolant Temp  = ", size=25 ,grid = [0,3])
coolText = Text(app, text = "80 *C", size = 25, grid = [1,3])


runTime = Text(app, text="Car Runtime  = ", size=25 ,grid = [0,4])
runText = Text(app, text = "0 Seconds", size = 25, grid = [1,4])
runText.after(1, update)

app.display()
