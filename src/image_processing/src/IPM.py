import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2 
import numpy as np

class IPM_app(Node):

    def __init__(self):
        super().__init__('processor')
        self.publisher_ = self.create_publisher(Image, 'IPM', 10)
        self.bridge = CvBridge()        
        self.s = np.array([[350, 560], [802, 560], [0, 864], [1152, 864]], dtype=np.float32)
# Vertices coordinates in the destination image
        self.t = np.array([[0, 0], [1152, 0], [250, 864], [902, 864]], dtype=np.float32)
        self.M = cv2.getPerspectiveTransform(self.s, self.t)
        self.subscription = self.create_subscription(Image,'Image',self.Image_sub,10)
        # timer_period = 0.5  # seconds
        # self.timer = self.create_timer(timer_period, self.Image_sub)

    def Image_sub(self, msg):
        img = self.bridge.imgmsg_to_cv2(msg , "bgr8")
        warped = cv2.warpPerspective(img, self.M, (img.shape[1], img.shape[0]), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT, borderValue=0)
        warped2=cv2.resize(warped, (int(img.shape[1]/2),int(img.shape[0]/2)), interpolation = cv2.INTER_AREA)
        ros_msg = self.bridge.cv2_to_imgmsg(warped2 , "8UC3")
        self.publisher_.publish(ros_msg)


def main(args=None):
    rclpy.init(args=args)
    processor = IPM_app()
    rclpy.spin(processor)
    processor.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()