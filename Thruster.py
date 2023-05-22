import rospy
from control.msg import PWM

class THRUSTER:

    def __init__(self, motor_channel):
        self.thruster_channel = motor_channel
        self.thruster_speed = 1500              #stop value (initial)
        self.pwm_limit_max = 1900
        self.pwm_limit_min = 1100
        
        self.pub = rospy.Publisher('PWM', PWM, queue_size=10)

    def set_speed(self, speed):
        #The method ensures that the speed is within the allowable range of PWMvalues
        self.thruster_speed = max(self.pwm_limit_min, min(self.pwm_limit_max, speed))

    def stop(self):
        self.thruster_speed = 1500

    def publish_pwm(self):
        msg = PWM()
        msg.channels = [1500, 1500, 1500, 1500, 1500, 1500, 0]
        msg.channels[self.thruster_channel] = self.thruster_speed
        self.pub.publish(msg)




rospy.init_node("Drive_Node", anonymous=True)

motor1 = THRUSTER(0) # create instance for motor 1
motor2 = THRUSTER(1) # create instance for motor 2

# set the speed of motor 1 to 1200
motor1.set_speed(1200)
motor1.publish_pwm()

# stop motor 1
motor1.stop()
motor1.publish_pwm()

# set the speed of motor 2 to 1800
motor2.set_speed(1800)
motor2.publish_pwm()
