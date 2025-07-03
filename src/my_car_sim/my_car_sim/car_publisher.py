import rclpy
from rclpy.node import Node
from visualization_msgs.msg import Marker

class CarPublisher(Node):
    def __init__(self):
        super().__init__('car_publisher')
        self.publisher = self.create_publisher(Marker, 'car_marker', 10)
        self.timer = self.create_timer(0.1, self.timer_callback)
        self.positionx = 0.0
    def timer_callback(self):
        marker = Marker()
        marker.header.frame_id = "map"
        marker.header.stamp = self.get_clock().now().to_msg()
        marker.ns = "car"
        marker.id = 0
        marker.type = Marker.CUBE
        marker.action = Marker.ADD
        self.positionx += 0.01
        marker.pose.position.x = self.positionx
        marker.pose.position.y = 2.0
        marker.pose.position.z = 0.1
        marker.scale.x = 1.0
        marker.scale.y = 0.5
        marker.scale.z = 0.2
        marker.color.r = 0.0
        marker.color.g = 0.5
        marker.color.b = 1.0
        marker.color.a = 1.0
        self.publisher.publish(marker)

def main(args=None):
    rclpy.init(args=args)
    node = CarPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
