# Multi-Robot vs Single Robot Mapping Speed

## Coverage vs Time
| Configuration | 100% Coverage |
|---------------|-|
| Single robot | 24.3 min |
| 2 robots | 16.8 min |
| **3 robots** | **14.5 min** |

**3-robot vs single: 40% faster**

## Inter-Agent Consistency
| Pair | Mean | Max |
|------|------|-----|
| r0-r1 | 2.3cm | 4.8cm |
| r0-r2 | 2.7cm | 4.9cm |
| r1-r2 | 2.1cm | 4.3cm |

All pairs less than 5cm - PASS

## Map Quality
- Loop closures: 31 (vs 12 single robot)
- Merge artifacts: <2% cells
