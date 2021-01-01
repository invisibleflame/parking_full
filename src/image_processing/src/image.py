

import rclpy
from rclpy.node import Node
from std_msgs.msg import UInt8MultiArray
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2 
import numpy as np
class Image_trans(Node):
    def __init__(self):
        super().__init__('mela_publisher')
        self.publisher_ = self.create_publisher(Image, 'Image', 10)
        self.bridge = CvBridge()        
        self.cv_image = cv2.imread("/home/bhuvan/ros2_ws/src/image_processing/src/lol.jpg")
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.read_image)
       
        

    def read_image(self):
        img = np.array(self.cv_image)
        ros_msg = self.bridge.cv2_to_imgmsg(img , "bgr8")
        self.publisher_.publish(ros_msg)

def main(args=None):
    rclpy.init(args=args)
    
    mela_publisher = Image_trans()
    rclpy.spin(mela_publisher)
    mela_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()



