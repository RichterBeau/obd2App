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
    

app = App(title="obd App", layout = "grid", width = 700)

rpmMeter = Text(app, text="    RPM  ", size=30, grid = [30,30])
rpmBox = Box(app, width = 300, height = 80,grid = [30,60])
rpmBox.set_border(4, "black")
rpmText = Text(rpmBox, text = "0", size = 30, align = "bottom")
#rpmText.after(1, getRPM)



speedoMeter = Text(app, text="    Speed (mph)  ", size=30 ,grid = [100,30])
spdBox = Box(app, width = 300, height = 80, grid = [100,60])
spdBox.set_border(4, "black")
spdText = Text(spdBox, text = "0", size = 10, align = "bottom")
spdText.after(1, getSpd)


app.display()



