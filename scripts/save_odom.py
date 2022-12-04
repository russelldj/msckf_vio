#!/usr/bin/env python
from nav_msgs.msg import Odometry
import numpy
import rospy
import time


FILENAME = "/root/data/results/odom_{}.npy".format(int(time.time() * 1e6))
POSES = []


def callback(data):
    # GT format is [time, x, y, z, qx, qy, qz, qw]
    # So we should match for the first 8, and then it's okay to diverge by
    # adding covariances
    POSES.append(
        [
            data.header.stamp.secs + 1e-9 * data.header.stamp.nsecs,
            data.pose.pose.position.x,
            data.pose.pose.position.y,
            data.pose.pose.position.z,
            data.pose.pose.orientation.x,
            data.pose.pose.orientation.y,
            data.pose.pose.orientation.z,
            data.pose.pose.orientation.w,
        ] + [
            cov for cov in data.pose.covariance
        ]
    )


def listener():
    rospy.init_node("listener", anonymous=True)
    rospy.Subscriber("/firefly_sbx/vio/odom", Odometry, callback)
    rospy.spin()
    poses = numpy.array(POSES)
    numpy.save(FILENAME, poses)


if __name__ == "__main__":
    listener()
