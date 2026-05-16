# Multi-Robot SLAM Architecture

## System Overview

rob0 (DDS 0) -> RTAB-Map -> /robot_0/map + /robot_0/pose
rob1 (DDS 1) -> RTAB-Map -> /robot_1/map + /robot_1/pose
rob2 (DDS 2) -> RTAB-Map -> /robot_2/map + /robot_2/pose

All 3 agents -> Multi-Master Bridge (DDS 10)
             -> Map Merger (occupancy grid max)
                          -> Distributed EKF (<5cm consistency)
                                       -> /merged_map (ROS 2)

                                       ## RTAB-Map Configuration
                                       - Loop closure detection: enabled (ICP-based)
                                       - Map update rate: 1 Hz
                                       - Graph optimization: GTSAM factor graph

                                       ## Communication
                                       - ROS 2 DDS with domain isolation per robot
                                       - Map topics bridged to global namespace
                                       - Multi-master bridge adds ~50ms cross-agent latency
