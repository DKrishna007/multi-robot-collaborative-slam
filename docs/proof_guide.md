# Proof Materials Guide

## Best Proof Screenshot
Single RViz window showing:
- 3 different colored robot models
- 3 individual LiDAR scans (color-coded)
- Merged global occupancy grid map
- 3 separate trajectory paths

## Required Visual Proofs
| Proof | Description |
|-------|-------------|
| 3-robot RViz | All agents visible with merged map |
| Map merge steps | 1 robot -> 2 robots -> 3 robots -> merged |
| Communication graph | rqt_graph showing multi-master topology |
| Distributed EKF output | Agent poses with <5cm deviation |
| Mapping speed chart | evaluation/mapping_speed_comparison.md |

## Key Numbers
- **40% faster** vs single robot
- **<5cm** inter-agent consistency
- **14.5 min** full coverage (3 robots)
- **31 loop closures** vs 12 single robot
