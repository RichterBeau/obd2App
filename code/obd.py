import obd
import PIL
import threading
from guizero import App,Text,Box
from PIL import Image
obd.logger.setLevel(obd.logging.DEBUG)
ports =  obd.scan_serial()
print (ports)
connection = obd.OBD()

def getRPM():
    cmd = obd.commands.RPM
    response = connection.query(cmd)
    rpm0 = str(response.value)
    rpm = rpm0[0:5]
    rpmText.clear()
    rpmText.append(rpm)
    rpmText.after(1, getRPM)

def getSpd():
    cmd = obd.commands.SPEED
    response = connection.query(cmd)
    spd0 = str(response.value.to("mph"))
    spd = spd0[0:3]
    spdText.clear()
    spdText.append(spd)
    spdText.after(1, getSpd)

def getCool():
    cmd = obd.commands.COOLANT_TEMP
    response = connection.query(cmd)
    cool0 = str(response.value)
    cool = cool0 +" *C"
    coolText.clear()
    coolText.append(cool)
    coolext.after(1000, getCool)

def getCool():
    cmd = obd.commands.COOLANT_TEMP
    response = connection.query(cmd)
    cool0 = str(response.value)
    cool = cool0 +" *C"
    coolText.clear()
    coolText.append(cool)
    coolText.after(1000, getCool)

def getTime():
    cmd = obd.commands.RUN_TIME
    response = connection.query(cmd)
    time0 = str(response.value)
    time = time0 +" *Seconds"
    runText.clear()
    runText.append(time)
    runText.after(1000, getTime)
    

app = App(title="obd App", layout = "grid", width = 800)

rpmMeter = Text(app, text="    RPM  ", size=30, grid = [0,0])
rpmBox = Box(app, width = 400, height = 80,grid = [0,1])
rpmBox.set_border(4, "black")
rpmText = Text(rpmBox, text = "0", size = 30, align = "bottom")
rpmText.after(1, getRPM)

speedoMeter = Text(app, text="    Speed (mph)  ", size=30 ,grid = [1,0])
spdBox = Box(app, width = 400, height = 80, grid = [1,1])
spdBox.set_border(4, "black")
spdText = Text(spdBox, text = "0", size = 30, align = "bottom")
#spdText.after(1, getSpd)

coolMeter = Text(app, text="Coolant Temp  = ", size=25 ,grid = [0,3])
coolText = Text(app, text = "80 *C", size = 25, grid = [1,3])
#coolText.after(1000, getTime)

runTime = Text(app, text="Car Runtime  = ", size=25 ,grid = [0,4])
runText = Text(app, text = "0 Seconds", size = 25, grid = [1,4])
#runText.after(1000, getTime)

app.display()



