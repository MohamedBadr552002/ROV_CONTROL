def translate( value, rightMin, rightMax):
        leftMax = -1
        leftMin = 1
        # Figure out how 'wide' each range is
        leftSpan = leftMax - leftMin
        rightSpan = rightMax - rightMin

        # Convert the left range into a 0-1 range (float)
        valueScaled = float(value - leftMin) / float(leftSpan)

        # Convert the 0-1 range into a value in the right range.
        return rightMin + (valueScaled * rightSpan)



def Vectorize(axes):
        motors  = [0 for i in range(len(axes[0]))]  
        for axis in axes :
            for index ,motor in enumerate(axis) :
                motors[index] += motor - 1500
        
        for index,value in enumerate(motors):
            motors[index] = 1500 + value
            
        for i, v in enumerate(motors):
            motors[i] = max (1100, min(1900, v))
        
        return motors