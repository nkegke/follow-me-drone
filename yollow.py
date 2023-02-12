#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from darknet_ros_msgs.msg import BoundingBoxes
import numpy as np

class CameraMonitor(object):
	def __init__(self, pub, pos):
		self.pub = pub
		self.pos = pos

	def callback(self, msg, ang):
		person = -1
		for i, det in enumerate(msg.bounding_boxes):
			if det.Class=="person":
				person = i
				break
		if person == -1:
			return

		xmin = msg.bounding_boxes[person].xmin
		ymin = msg.bounding_boxes[person].ymin
		xmax = msg.bounding_boxes[person].xmax
		ymax = msg.bounding_boxes[person].ymax
		center = [(xmin+xmax)/2, (ymin+ymax)/2]

		move_val = Twist()
		if center[1] < 240:
			move_val.linear.x = 0.5
		elif center[1] > 240:
			move_val.linear.x = -0.5
		if center[0] < 320:
			move_val.linear.y = 0.5
		elif center[0] > 320:
			move_val.linear.y = -0.5
		else:
			move_val.linear.x = 0.000001
			move_val.linear.y = 0.000001
			move_val.linear.z = 0.000001

		self.pub.publish(move_val)


def main():
	rospy.init_node('image_reader', anonymous=True)
	pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
	pos = [-4.66, 1.4, 0.8]
	monitor = CameraMonitor(pub, pos)

	rate = rospy.Rate(15)
	while not rospy.is_shutdown():
		msg = rospy.wait_for_message('/darknet_ros/bounding_boxes', BoundingBoxes, timeout=None)
		monitor.callback(msg, ang)
		rate.sleep()


if __name__ == '__main__':
	try:
		main()
	except rospy.ROSInterruptException:
		pass
