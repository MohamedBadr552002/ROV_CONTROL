from calculation import translate
from calculation import Vectorize
class Truster:
    def __init__(self,chanel):
        self.speed = 1500
        self.chanel = chanel
        #Linear Range
        self.linear_limit_max = 1900 
        self.linear_limit_min = 1100
        #Angular Range
        self.angular_limit_max = 1600
        self.angular_limit_min = 1400
        #Horizontal Range
        self.h_limit_max = 1900
        self.h_limit_min = 1100
        #Pitch Range
        self.pitch_limit_max = 1900
        self.pitch_limit_min = 1100
        self.pitch_increment = 10
        self.pitch_speed = 1500

    def get_chanel(self):
        return self.chanel
    
    def set_chanel(self,chanel):
        self.chanel = chanel

    def stop(self):
        self.speed = 1500



class DriveRovVector:

    def __init__(self):
        #horizontal thrusters
        self.motor1 = Truster(1)
        self.motor2 = Truster(1)
        self.motor3 = Truster(1)
        self.motor4 = Truster(1)
        #vertical thrusters
        self.motor5 = Truster(1)
        self.motor6 = Truster(1)

        self.motors = [self.motor1.speed, self.motor2.speed, self.motor3.speed, self.motor4.speed, self.motor5.speed,
         self.motor6.speed, 0]

        
    


    def _speed_windup(self, speed, minlimit, maxlimit):

        return translate(round(speed, 2), minlimit, maxlimit)

    def move_forword(self, value):
        speed = self._speed_windup(
            value, self.motor1.linear_limit_min, self.motor1.linear_limit_max)
        
        """
        
        WHY YOU REDECLARE THE CAHNNELS ?
        
        """
        #set the direction of hirozintal thrusters
        self.motor1.chanel = 1
        self.motor2.chanel = 1
        self.motor3.chanel = 1
        self.motor4.chanel = 1
        dircs = [self.motor1.chanel, self.motor2.chanel, self.motor3.chanel, self.motor4.chanel]

        motors = [self.motor1.speed,self.motor2.speed,self.motor3.speed,self.motor4.speed]

        for index, dirc in enumerate(dircs):

            if dirc:
                self.motors    """  !!!!!!!! """
                motors[index] = speed
            else:
                motors[index] = 3000 - speed
        
        return motors

    def move_latrially(self, value):
        speed = self._speed_windup(
            value, self.motor1.linear_limit_min, self.motor1.linear_limit_max)

        #set the direction of hirozintal thrusters
        self.motor1.chanel = 0
        self.motor2.chanel = 1
        self.motor3.chanel = 0
        self.motor4.chanel = 1
        dircs = [self.motor1.chanel, self.motor2.chanel, self.motor3.chanel, self.motor4.chanel]

        motors = [self.motor1.speed,self.motor2.speed,self.motor3.speed,self.motor4.speed]
        for index, dirc in enumerate(dircs):

            if dirc:
                motors[index] = speed
            else:
                motors[index] = 3000 - speed
        
        return motors

    def rotate(self, value):
        
        speed = self._speed_windup(
            value,self.motor1.angular_limit_min, self.motor1.angular_limit_max)

        #set the direction of hirozintal thrusters
        self.motor1.chanel = 0
        self.motor2.chanel = 1
        self.motor3.chanel = 1
        self.motor4.chanel = 0
        dircs = [self.motor1.chanel, self.motor2.chanel, self.motor3.chanel, self.motor4.chanel]

        motors = [self.motor1.speed,self.motor2.speed,self.motor3.speed,self.motor4.speed]

        for index, dirc in enumerate(dircs):

            if dirc:
                motors[index] = speed
            else:
                motors[index] = 3000 - speed
        
        return motors

    def move_up_down(self, value):
        speed = self._speed_windup(
            value, self.motor1.h_limit_min, self.motor1.h_limit_max)
        
        motors = [self.motor5.speed,self.motor6.speed]

        #set the direction of vertical thrusters
        self.motor5.chanel = 1
        self.motor6.chanel = 0
        dircs = [self.motor5.chanel, self.motor6.chanel]
        for index in range(2):
            if dircs[index]:
                motors[index] = speed
            else:
                motors[index] = 3000 - speed
        return motors

    def pitch(self, value):
        speed = self._speed_windup(
            value, self.motor1.h_limit_min, self.motor1.h_limit_max)

        motors = [self.motor5.speed,self.motor6.speed]

        #set the direction of vertical thrusters
        self.motor5.chanel = 1
        self.motor6.chanel = 1

        dircs =[self.motor5.chanel , self.motor6.chanel]
        for index in range(2):
            if dircs[index] :
                motors[index] = speed

            else :
                motors[index] = 3000 - speed
        
        return motors

        
    def stop(self):
        self.motor1.stop()
        self.motor2.stop()
        self.motor3.stop()
        self.motor4.stop()
        self.motor5.stop()
        self.motor6.stop()
        return [self.motor1.speed,self.motor2.speed,self.motor3.speed,self.motor4.speed,self.motor5.speed,self.motor6.speed]
    


        
    def control(self, data):

         #to generate the PWM signals for the motors that control the ROV's forward/backward movement, lateral movement, and rotation, respectively
        up = Vectorize([self.move_up_down(data[3]),self.pitch(data[4])])
        

        #to generate the PWM signals for the motors that control the ROV's forward/backward movement, lateral movement, and rotation, respectively

        Direction =Vectorize([self.move_forword(data[1]) ,self.move_latrially(data[2]) , self.rotate(data[0]) ])

        Direction.extend(up)
        # maxAxis = data.index(max(data[:3], key=abs))
        # if maxAxis == 0 :
        #     self.rotate(data[0])
        # elif maxAxis == 1:
        #     self.move_forword(data[1])
        # elif maxAxis == 2:
        #     self.move_latrially(data[2])
        
        
        return Direction