#!/usr/bin/env python3

import rospy
import cv2
import numpy as np
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from geometry_msgs.msg import Twist

class RedDetector:
    def __init__(self):
        rospy.init_node('red_detector', anonymous=True)
        self.bridge = CvBridge()
        self.cmd_vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        self.image_sub = rospy.Subscriber('/cv_camera/image_raw', Image, self.image_callback)
        self.twist = Twist()

    def image_callback(self, msg):

        cv_image = self.bridge.imgmsg_to_cv2(msg, "bgr8")

        hsv = cv2.cvtColor(cv_image, cv2.COLOR_BGR2HSV)

        lower_red1 = np.array([0, 120, 70])
        upper_red1 = np.array([10, 255, 255])
        lower_red2 = np.array([170, 120, 70])
        upper_red2 = np.array([180, 255, 255])
        
        mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
        mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
        mask = mask1 + mask2

        red_pixels = cv2.countNonZero(mask)

        # Si hay suficiente rojo, mover hacia adelante
        if red_pixels > 1000:  # Umbral
            self.twist.linear.x = 0.2  # Velocidad hacia adelante
        else:
            self.twist.linear.x = 0.0  # Detenerse

        self.twist.angular.z = 0.0
        self.cmd_vel_pub.publish(self.twist)

    def run(self):
        rospy.spin()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    try:
        detector = RedDetector()
        detector.run()
    except rospy.ROSInterruptException:
        pass
