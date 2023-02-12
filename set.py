#!/usr/bin/env python

import rospy
import time
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
import numpy as np

class VelocityMonitor(object):
    def __init__(self, pub, goal):
        self.pub = pub
        self.goal = goal


    def callback(self, msg):
        x = msg.pose.pose.position.x
        y = msg.pose.pose.position.y
        z = msg.pose.pose.position.z
        o1 = msg.pose.pose.orientation.w
        o2 = msg.pose.pose.orientation.z

        if np.abs(self.goal[2] - z) >= 0.1:
            if self.goal[2] > z:
                move_val = Twist()
                move_val.linear.z = 1
                self.pub.publish(move_val) 
            else:
                move_val = Twist()
                move_val.linear.z = -1
                self.pub.publish(move_val) 

        elif x >= self.goal[0] + 0.1:
            move_val = Twist()
            move_val.linear.x = -1
            self.pub.publish(move_val)

        elif y >= self.goal[1] + 0.001:
            move_val = Twist()
            move_val.linear.y = -1
            self.pub.publish(move_val)

        elif o1 >= 0.707 + 0.01 and o2 >= -0.707 + 0.01:
            move_val = Twist()
            move_val.angular.z = -1
            self.pub.publish(move_val)

        else:
            hover = Twist()
            hover.linear.z = 0.0000001
            hover.linear.y = 0.0000001
            hover.linear.x = 0.0000001
            self.pub.publish(hover)



def main():
    rospy.init_node('set_location')
    #goal = [-4.76, 0.4, 2.10]
    goal = [-4.66, 1.4, 2.30]

    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    monitor = VelocityMonitor(pub, goal)

    rospy.Subscriber('/ground_truth/state', Odometry, monitor.callback)
    rospy.spin()


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
