'''
Developed by Ellen Red

'''

import network
from microdot_asyncio import Microdot, Response, send_file
from microdot_asyncio_websocket import with_websocket
from microdot_utemplate import render_template
import ujson
import motor
import imu
import kalman_pid


ssid = "" 
password = ""
ap = network.WLAN(network.AP_IF)
ap.config(essid=ssid, password=password)
ap.active(True)

while ap.active == False:
    pass

print('Connection successful')
print(ap.ifconfig())


app = Microdot()
Response.default_content_type = 'text/html'


@app.route('/')
async def index(request):
    return render_template('index.html')


@app.route('/update')
def update(request):
    values_kalman_pid = kalman_pid.filter_pid()
    kalman_x_angle = values_kalman_pid[0]
    kalman_y_angle = values_kalman_pid[1]
    
    data = {
    "kalman_x_angle" : kalman_x_angle,
    "kalman_y_angle" : kalman_y_angle    
    }
    response = ujson.dumps(data)
    return response
   

@app.route("/ws")
@with_websocket
async def drone_commands(request, ws):
    while True:
        websocket_message = await ws.receive()
        if "auto_takeoff" in websocket_message:
            motor.auto_takeoff_button()            
            
        if "hover" in websocket_message:
            motor.hover_button()
            
        if "down" in websocket_message:
            motor.down_button()
            
        if "on_manual" in websocket_message:
            motor.on_manual_button()
        
        if "off_manual" in websocket_message:
            motor.off_manual_button()
        
        await ws.send('')
        

def start_server():
    print('Starting microdot app')
    try:
        app.run(port=80)
    except:
        app.shutdown()    

start_server()






