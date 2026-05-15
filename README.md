# Multi-Robot Collaborative SLAM

> **Project** | 3-Agent Cooperative Mapping with ROS 2 + RTAB-Map
> > Distributed EKF · Multi-Master Topic Bridge · Occupancy Grid Merging
> >
> > ---
> >
> > ## Overview
> >
> > A **3-agent cooperative SLAM system** using ROS 2 and RTAB-Map for real-time occupancy grid merging. Implements a distributed EKF for multi-agent pose estimation, achieving consistent localization within 5 cm of ground truth, and demonstrates 40% faster full-environment mapping compared to a single-robot baseline.
> >
> > ---
> >
> > ## Key Results
> >
> > | Metric | Value |
> > |---|---|
> > | Agents | 3 cooperative robots |
> > | Localization Accuracy | Within **5 cm** of ground truth |
> > | Mapping Speed Improvement | **40% faster** vs single-robot |
> > | Map Merging | Real-time occupancy grid merging |
> > | Application | Warehouse coverage planning |
> >
> > ---
> >
> > ## System Architecture
> >
> > ```
> > Robot 1 (RTAB-Map SLAM)    Robot 2 (RTAB-Map SLAM)    Robot 3 (RTAB-Map SLAM)
> >        ↓                           ↓                           ↓
> >   Local Map + Pose           Local Map + Pose           Local Map + Pose
> >        ↓                           ↓                           ↓
> >                     Multi-Master ROS 2 Topic Bridge
> >                               ↓
> >                     Distributed EKF (Multi-Agent Pose Estimation)
> >                               ↓
> >                     Occupancy Grid Map Merging
> >                               ↓
> >                     Unified Global Map (Real-Time)
> > ```
> >
> > ---
> >
> > ## Features
> >
> > - **3-agent cooperative SLAM** with RTAB-Map for each agent
> > - - **Real-time occupancy grid merging** via multi-master ROS 2 topic bridge
> >   - - **Distributed EKF** for multi-agent pose estimation within 5 cm of ground truth
> >     - - **40% faster** full-environment mapping vs single-robot baseline
> >       - - Demonstrated for **warehouse coverage planning** scenarios
> >         - - Scalable architecture supporting N robot agents
> >          
> >           - ---
> >
> > ## Tech Stack
> >
> > | Category | Tools / Libraries |
> > |---|---|
> > | SLAM | RTAB-Map |
> > | Middleware | ROS 2 (Humble) |
> > | Multi-Robot | Multi-master topic bridge, ROS 2 namespacing |
> > | State Estimation | Distributed EKF |
> > | Map Merging | Custom occupancy grid merging |
> > | Programming | Python, C++ |
> >
> > ---
> >
> > ## Package Structure
> >
> > ```
> > multi_robot_slam_ws/
> > ├── src/
> > │   ├── robot_slam/
> > │   │   ├── robot_slam/
> > │   │   │   └── rtabmap_agent.py             # Per-robot RTAB-Map SLAM node
> > │   │   ├── config/
> > │   │   │   └── rtabmap_params.yaml
> > │   │   └── launch/
> > │   │       └── single_robot_slam.launch.py
> > │   ├── multi_robot_bridge/
> > │   │   ├── multi_robot_bridge/
> > │   │   │   ├── topic_bridge.py              # Multi-master topic bridge
> > │   │   │   └── pose_aggregator.py           # Multi-agent pose collection
> > │   │   └── launch/
> > │   │       └── multi_master_bridge.launch.py
> > │   ├── distributed_ekf/
> > │   │   ├── distributed_ekf/
> > │   │   │   ├── ekf_multi_agent.py           # Distributed EKF implementation
> > │   │   │   └── covariance_intersection.py   # CI-based fusion
> > │   │   └── config/
> > │   │       └── ekf_params.yaml
> > │   ├── map_merging/
> > │   │   ├── map_merging/
> > │   │   │   ├── grid_map_merger.py           # Real-time occupancy grid merging
> > │   │   │   └── map_alignment.py            # Inter-map alignment
> > │   │   └── launch/
> > │   │       └── map_merger.launch.py
> > │   └── multi_robot_bringup/
> > │       └── launch/
> > │           ├── 3_robot_slam.launch.py       # Launch all 3 agents
> > │           └── warehouse_coverage.launch.py  # Warehouse planning scenario
> > ├── evaluation/
> > │   ├── mapping_speed_benchmark.py
> > │   └── localization_accuracy.py
> > └── README.md
> > ```
> >
> > ---
> >
> > ## Installation
> >
> > ```bash
> > # Clone the repository
> > git clone https://github.com/DKrishna007/multi-robot-collaborative-slam.git
> > cd multi-robot-collaborative-slam
> >
> > # Install dependencies
> > rosdep install --from-paths src --ignore-src -r -y
> > sudo apt-get install ros-humble-rtabmap-ros
> >
> > # Build
> > colcon build --symlink-install
> > source install/setup.bash
> > ```
> >
> > ---
> >
> > ## Usage
> >
> > ```bash
> > # Launch 3-robot collaborative SLAM
> > ros2 launch multi_robot_bringup 3_robot_slam.launch.py
> >
> > # Launch single robot (for baseline comparison)
> > ros2 launch robot_slam single_robot_slam.launch.py robot_id:=robot1
> >
> > # Run warehouse coverage planning scenario
> > ros2 launch multi_robot_bringup warehouse_coverage.launch.py
> >
> > # Evaluate localization accuracy
> > python3 evaluation/localization_accuracy.py \
> >   --ground_truth data/gt_poses.csv \
> >   --estimated data/estimated_poses.csv
> > ```
> >
> > ---
> >
> > ## Multi-Robot Coordination
> >
> > Each robot runs its own RTAB-Map instance with a unique namespace (`/robot1`, `/robot2`, `/robot3`). The multi-master bridge relays pose and map data across namespaces. The distributed EKF uses covariance intersection to fuse pose estimates without requiring cross-covariances.
> >
> > ---
> >
> > ## Author
> >
> > **Krishna Digamarthi** | Robotics Engineer | University of Delaware
> > 📧 shivasaikrishna23@gmail.com | [GitHub](https://github.com/DKrishna007)
