#! /usr/bin/env python

# Assignment 1 for Week1: In this assignment you will subscribe to the topic that
# publishes sensor information. Then, you will transform the sensor reading from
# the reference frame of the sensor to compute the height of a box based on the
# illustration shown in the assignment document. Then, you will publish the box height
# on a new message type ONLY if the height of the box is more than 10cm.

# All necessary python imports go here.
import rospy
import time
from hrwros_msgs.msg import SensorInformation, BoxHeightInformation
def sensor_info_callback(data, bhi_pub):
    #rospy.loginfo('%f is what i heard in sensinfocal', data.sensor_data.range)
    height_box = 2-data.sensor_data.range
    #print(height_box)
    #print(data)ros
    #time.sleep(2)
    

    # Compute the height of the box.
    # Boxes that are detected to be shorter than 10cm are due to sensor noise.
    # Do not publish information about them.
    if (height_box==0.0 and height_box<=0.1):
	#print("Box is not there")  
	pass
    else:
        # Declare a message object for publishing the box height information.
        box_height_info = BoxHeightInformation()
        # Update height of box
        box_height_info.box_height=height_box
        # Publish box height using the publisher argument passed to the callback function.
        bhi_publisher.publish(box_height_info)
	#print(height_box)

if __name__ == '__main__':
    # Initialize the ROS node here.
    rospy.init_node('compute_box_height', anonymous = False)

    # Wait for the topic that publishes sensor information to become available - Part1
    rospy.loginfo('Waiting for topic %s to be published...', 'sensor_info')
    rospy.wait_for_message('sensor_info', SensorInformation)
    rospy.loginfo('%s topic is now available!', 'sensor_info')

    # Create the publisher for Part3 here
    bhi_publisher = rospy.Publisher('box_height_info', BoxHeightInformation, queue_size=10)
    #rospy.init_node('box_height_info', anonymous=True)
    #rate = rospy.Rate(10) # 10hz
    # Note here that an ADDITIONAL ARGUMENT (bhi_publisher) is passed to the subscriber. This is a way to pass
    # ONE additional argument to the subscriber callback. If you want to pass multiple arguments,
    # you can use a python dictionary. And if you don't want to use multiple arguments to the
    # subscriber callback then you can also consider using a Class Implementation like we saw in
    # the action server code illustration.

    # Create the publisher for Part1 here
    rospy.Subscriber('sensor_info', SensorInformation, sensor_info_callback, bhi_publisher)

    # Prevent this code from exiting until Ctrl+C is pressed.
    rospy.spin()
