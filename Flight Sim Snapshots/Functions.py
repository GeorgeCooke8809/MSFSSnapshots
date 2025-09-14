from SimConnect import *

sm = SimConnect()
aq = AircraftRequests(sm)

class snapshot:
    def __init__(self):
        self.altitude = aq.get("PLANE_ALTITUDE")
        self.latitude = aq.get("PLANE_LATITUDE")
        self.longitude = aq.get("PLANE_LONGITUDE")
        self.track = aq.get("GPS_GROUND_TRUE_TRACK")
        self.speed = aq.get("AIRSPEED_INDICATED")
        self.pitch = aq.get("PLANE_PITCH_DEGREES")
        self.roll = aq.get("PLANE_BANK_DEGREES")
        self.flaps = aq.get("FLAP_POSITION_SET")
        #TODO: Engines %
        #TODO: Acceleration Vectors
        #DEBUG - print("Snapshot Saved")

def save_location():
    global snapshot_one

    snapshot_one = snapshot()

def set_location():
    global snapshot_one
    try:
        aq.set("PLANE_ALTITUDE", snapshot_one.altitude)
        aq.set("PLANE_LATITUDE", snapshot_one.latitude)
        aq.set("PLANE_LONGITUDE", snapshot_one.longitude)
        aq.set("GPS_GROUND_TRUE_TRACK", snapshot_one.track)
        aq.set("AIRSPEED_INDICATED", snapshot_one.speed)
        aq.set("PLANE_PITCH_DEGREES", snapshot_one.pitch)
        aq.set("PLANE_BANK_DEGREES", snapshot_one.roll)
        aq.set("FLAP_POSITION_SET", snapshot_one.flaps)

        #DEBUG - print("Snapshot Enacted")

    except:
        #DEBUG - print("No Snapshot Was Saved")