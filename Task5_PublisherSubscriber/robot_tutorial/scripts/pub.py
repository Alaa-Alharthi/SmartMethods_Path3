#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def h_talker():
  h_pub = rospy.Publisher('hello', String, queue_size=10)
  rospy.init_node('talker', anonymous=True)
  rate = rospy.Rate(10)
  while not rospy.is_shutdown():
    hello_str = "hello world"
    rospy.loginfo(hello_str)
    h_pub.publish(hello_str)
    rate.sleep()

if __name__ == '__main__':
  try:
    h_talker()
  except rospy.ROSInterruptException:
    pass

