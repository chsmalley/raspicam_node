#!/usr/bin/python3
# import sys
from picamera import PiCamera
import time
import numpy as np
# import random
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge


class RaspiCamNode(object):  # {{{1

    """
    Create a ROS node that gets an image stream from raspberry pi
    camera and publishes it to a ROS topic
    inputs: ...(camera)
    outputs: publish topic
    """

    def __init__(self):  # {{{2
        # SET UP RATE FOR LOOP
        # rate = rospy.Rate(10)  # TODO add to config
        # SET UP PUBLISHING
        self.image_pub = rospy.Publisher("camera_image", Image)
        self.bridge = CvBridge()

if __name__ == '__main__':  # {{{1
    # Initialize the node and name it.
    rospy.init_node('RaspiCam', anonymous=True)
    # Go to class functions that do all the heavy lifting.
    cam = RaspiCamNode()
    with PiCamera() as camera:
        camera.resolution = (320, 240)
        camera.framerate = 10
        time.sleep(2)
        image = np.empty((240, 320, 3), dtype=np.uint8)
        camera.capture(image, 'bgr')
        while not rospy.is_shutdown():
            image_message = image
            cam.image_pub.publish(cam.bridge.cv_to_image(image_message, "bgr8"))
