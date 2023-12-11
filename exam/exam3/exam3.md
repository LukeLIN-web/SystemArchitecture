## exam3

## question1

#### Assumption

1. page table isn't in cache.
2. tlb access time = L1 cache time  = 2 cycles 
3. when pipeline stall, the data access also stall.

#### Reasoning

1. L1 data cache: 0.85 hit ratio,  miss rate = 0.15
2. For L1 instruction cache,  hit rate = 0.0   Miss rate = 0.05
3. 95% can be found in the L2, miss rate = 0.05

First we calculate **instruction** latency, on average, if we have n accesses:

A hit in the  **instruction** cache = 0.95 n * 2 cycles. = 1.9 cycles
 A miss in L1 but a hit in L2 = 0.05 * 0.95 n * (20) cycles   = 0.95 n cycles

A miss in L2,but a hit in TLB = 0.05 * 0.05  * 0.98 n * (2+ 120) cycles =0.2989 n cycles

A miss in L2,but a miss in TLB = 0.05 * 0.05  * 0.02 n * (6*120) cycles. = 0.09 n cycles 

Average access = (1.9 n + 0.95 n + 0.39 n) / n  

 Average access = 1.9+0.95+0.39=3.24 cycles

Second we calculate **data** latency :

on average, if we have n accesses:

A hit in the  **data** L1 cache = 0.85 n * 2 cycles = 1.7  n cycles
 A miss in L1 but a hit in L2 = 0.15 * 0.95 n * (20) cycles =2.85 cycles

A miss in L2,but a hit in TLB = 0.15 * 0.05  * 0.98 n * (2+ 120) cycles = 0.8967 n cycles

A miss in L2,but a miss in TLB = 0.15 * 0.05  * 0.02 n * (6*120) cycles. =0.27 n cycle (It can be smaller if Page table in the cache)

Average access = ( 1.7  n + 2.85 n + 0.8967  n + 0.27 n) / n  

 Average access = 1.7+2.85+0.9+0.27=5.72 cycles

execute access time :

If an instructions executed by the application require a data access, the Average access = 5.72+ 3.24 =8.96 cycles

If no data access,  Average access time =  3.24 cycles 

so averge per instruction memory access time is 

```
8.96*0.3+3.24*0.7=4.956  cycles
```

So IPC = 1/4.956= 0.20

the SM loses about 20% of its cycles due to pipeline bubbles.  Because we assume when pipeline stall, the data access also stall.  So Adjusted IPC=Initial IPC × Efficiency

So IPC = 0.20*0.8=0.16

#### How to improve performance

We can find L1data cache miss is an important performance bottleneck. Therefore, we need to optimize program, Focus on improving data locality to increase the hit ratio,  to avoid L1 data cache miss.  

We can also use instruction-level optimizations to reduce pipeline bubbles and improve IPC. This includes techniques like instruction scheduling, branch prediction, and loop unrolling.

## Question2

### a

Cores:  Cores are sharing L2 cache. We assume that we have eight processors share one L2 cache. One chip have 8 cores, so one chip have 8 L1 caches.  Each SM cores has it icache and dcache.  

### 1. Cores:

- **Type**: 8 SM cores per chip.
- **Modeling**: Each core operates independently. They issue instructions at a rate determined by the IPC under ideal conditions (0.8 IPC considering pipeline bubbles). There is one process assigned to each core. Therefore, on a chip with 8 cores, there are a total of 8 processes running concurrently.
- **Performance Metrics**: The rate of instruction issue, accounting for pipeline efficiency.

### 2. Caches:

- L1 Cache
  - **Hit Ratio**: 0.95 for instructions, 0.85 for data.
  - **Access Time**: 2 cycles.
- L2 Cache
  - **Hit Ratio**: 0.95.
  - **Access Time**: 20 cycles.

### 3. Bus:

- **Type**: Broadcast bus.
- **Speed**: 6GHz.
- **Modeling**: A shared bus modeled as a single queue. The queue length is infinite, the service time depend on the contention from the cores. Different chip connect same memory with bus. i.e. Different chip share bus. If bus is busy, the core need to wait until the data return from meory.

### 4. Queuing Model Construction:

- **Flow**: Instructions are issued by the cores → Access L1 cache (instruction or data as required) → On L1 miss, access L2 cache → On L2 miss, proceed to memory access.
- **Bus Contention**: Model the bus as a bottleneck, where multiple cores attempting to access memory or synchronize via the bus can lead to contention.

### 5. Simulation Parameters:

- **Instruction Mix**: Account for the 30% of instructions that require data access.
- **Cache and Memory Access Patterns**: Driven by the application's behavior.
- **Pipeline Effects**: Include the impact of 20% cycle loss due to pipeline bubbles in core performance.

Calculation Objective: Our aim is to determine the ratio of bus busy time to the total operational time. we need to track **Bus Request Cycles**: The cycles during which the bus is utilized for memory accesses. We test max_cycles=100000 cycles.  

### b

We need to record bus utilization.

We simulate and find the maximum number of chips is 13 that can be connected to the system while keeping the bus utilization under 80%.

