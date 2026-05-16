# Multi-Robot Collaborative SLAM

> 3-agent cooperative mapping with ROS 2, RTAB-Map, and distributed EKF. Real-time occupancy grid merging via multi-master DDS bridge. **40% faster full-environment mapping vs single robot. <5cm inter-agent localization consistency.**
>
> **Researcher:** Krishna Digamarthi | University of Delaware
>
> ---
>
> ## Results
> | Metric | Value |
> |--------| ------|
> | Mapping speedup | **40% faster** vs single robot |
> | Inter-agent consistency | **<5cm** across all agent pairs |
> | Full coverage time | **14.5 min** (3 robots) vs 24.3 min (1 robot) |
> | Loop closures | **31** (vs 12 single robot) |
> | Map merge artifacts | **<2% cells** |
>
> ## How to Run
> ```bash
> ROS_DOMAIN_ID=0 ros2 launch multi_robot robot_0.launch.py
> ROS_DOMAIN_ID=1 ros2 launch multi_robot robot_1.launch.py
> ROS_DOMAIN_ID=2 ros2 launch multi_robot robot_2.launch.py
> ROS_DOMAIN_ID=10 ros2 launch multi_robot map_merger.launch.py
> ```
>
> ## Proof Materials
> | Type | Location |
> |------|---------|
> | Mapping comparison | evaluation/mapping_speed_comparison.md |
> | Comm config | coordination/multi_master_config.yaml |
> | Architecture | docs/architecture.md |
> | Proof guide | docs/proof_guide.md |
>
> ## Limitations
> - Tested in controlled warehouse environment
> - - Map merging assumes overlapping coverage between agents
>   - - Multi-master bridge adds ~50ms latency to cross-agent topics
>    
>     - ## Future Work
>     - - Task allocation for optimal coverage planning
>       - - Dynamic team size (add/remove robots at runtime)
>         - - 3D multi-robot SLAM with voxel map merging
