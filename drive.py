import rospy
from control.msg import Axis , PWM
#from modules.driveRovVector import DriveRovVector
from thruster import DriveRovVector

control = DriveRovVector()

pub = rospy.Publisher('PWM', PWM, queue_size=10)

def callback(msg):
    x,y,z,r,p = msg.x,msg.y,msg.z,msg.r,msg.p
    motors = control.control([r,x,y,z,p])
    msg = PWM()
    # rospy.loginfo(motors)
    msg.ch0 = int(motors[0])
    msg.ch1 = int(motors[1])
    msg.ch2 = int(motors[2])
    msg.ch3 = int(motors[3])
    msg.ch4 = int(motors[4])
    msg.ch5 = int(motors[5])
    pub.publish(msg)

def subscriber():
    
    rospy.init_node("Drive_Node", anonymous=True)
    rospy.Subscriber("pid_axis", Axis,callback)
    rospy.spin()


if __name__ == "__main__":
    try:
        subscriber()
    except rospy.ROSInterruptException:
        pass