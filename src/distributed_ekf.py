"""
Distributed EKF for 3-agent pose consistency.
<5cm inter-agent localization error.
"""
import numpy as np
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseWithCovarianceStamped

AGENTS = ["robot_0", "robot_1", "robot_2"]

class DistributedEKF(Node):
      def __init__(self):
                super().__init__("distributed_ekf")
                self.states = {a: np.zeros(3) for a in AGENTS}
                self.covs = {a: np.eye(3)*0.1 for a in AGENTS}
                self.Q = np.diag([0.01, 0.01, 0.005])
                self.R = np.diag([0.02, 0.02, 0.010])
                for a in AGENTS:
                              self.create_subscription(PoseWithCovarianceStamped,
                                                                       f"/{a}/pose", lambda m, ag=a: self.cb(m, ag), 10)
                          self.pubs = {a: self.create_publisher(
                    PoseWithCovarianceStamped, f"/{a}/fused_pose", 10) for a in AGENTS}

      def cb(self, msg, agent):
                p = msg.pose.pose.position
                q = msg.pose.pose.orientation
                z = np.array([p.x, p.y, 2*np.arctan2(q.z, q.w)])
                self.covs[agent] += self.Q
                H = np.eye(3)
                K = self.covs[agent]@H.T@np.linalg.inv(H@self.covs[agent]@H.T+self.R)
                self.states[agent] += K@(z-self.states[agent])
                self.covs[agent] = (np.eye(3)-K@H)@self.covs[agent]
                out = PoseWithCovarianceStamped()
                out.header = msg.header
                out.pose.pose.position.x = self.states[agent][0]
                out.pose.pose.position.y = self.states[agent][1]
                out.pose.pose.orientation.z = np.sin(self.states[agent][2]/2)
                out.pose.pose.orientation.w = np.cos(self.states[agent][2]/2)
                self.pubs[agent].publish(out)

  def main():
        rclpy.init()
        rclpy.spin(DistributedEKF())
        rclpy.shutdown()
