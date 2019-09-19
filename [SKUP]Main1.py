import Controls as c
import rospy
#import Map as m
import numpy as np
#import Navigation as nav
#import Lidar as Lidar
import time

from nav_msgs.msg import Odometry as odom
from sensor_msgs.msg import LaserScan

def run():
    print("run method go plz?")

def get_data_array(data, a=0, b=240):
    PPD = 4.5  # points per degree
    data = data[int(a * PPD):int(b * PPD)]
    arr = np.array(data)
    return arr

def printData(data):
    #print(data)
    dataFront = get_data_array(data.ranges, 100, 140)
    distInFront=dataFront.mean()
    print(distInFront)
    go=True

    if(distInFront<2):
        go=False

    x= 1 if go else 0
    speed=5 if go else 0
    c.move(x,0,speed)

if __name__ == "__main__":
    print ("go")
    rospy.init_node('keyop')  # vesc/ackermann_cmd_mux/input/navigation ackermann_msgs/AckermannDriveStamped
    #mpo=rospy.Subscriber('main', LaserScan,run , queue_size=2)
    #pub = rospy.Subscriber('odom', odom, nav.print_odata, queue_size=2)
    lidarsub = rospy.Subscriber('scan', LaserScan, printData, queue_size=2)

lrender=0
dt=0
lastsave=rospy.get_time()
imgnum=0
lrtime=rospy.get_time()


while not rospy.is_shutdown():
    #m.update(Lidar.getOrient())
    '''if(rospy.get_time()-lrtime>.5 and m.route!=None):
        m.updateRoute()
        lrtime=rospy.get_time()
    if (rospy.get_time()>lrender+1.5):
        st=time.time()
        lrender=rospy.get_time()
        m.render(dt)
        dt=time.time()-st
        #print ('render time : ',dt)
    if (rospy.get_time() - lastsave > 8):
        st1=time.time()
        m.saveImg(imgnum)
        lastsave = rospy.get_time()
        imgnum = imgnum + 1
        print ('img saved in ',(time.time()-st1),' sec')'''

    pass
