## exam3

## question1

1. An access has a probability of 0.85 of finding the data item in the L1. If the item is not in the level one cache, then it is among the 15% of accesses that miss in L1.

2. For L1 instruction cache,  An access has a probability of 0.95 of finding the data item in the L1. If the item is not in the level one cache, then it is among the 5% of accesses that miss in L1.

3.  For these, about 95% can be found in the L2, while the others will miss in L2. 

4. 30% need data access.  So 70% only need instruction access.

#### Assumption:

1. page table isn't in cache.
2. tlb access time = L1 cache time  = 2 cycles 
3. when pipeline stall, the data access also stall.

First we calculate **instruction** latency :

on average, if we have n accesses:

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

30%  instructions executed by the application require a data access. so Average access = 5.72+ 3.24 = 5.72+3.24=8.96 

70% no data access,  Average access =  3.24 cycles 

so averge per instruction memory access time is 

```
3.24+5.72*0.3=4.956 cycles
```

So IPC = 1/4.956=0.20

the SM loses about 20% of its cycles due to pipeline bubbles.  Because we assume when pipeline stall, the data access also stall.  So Adjusted IPC=Initial IPC × Efficiency

So IPC = 0.20*0.8=0.16 

How to improve performance:

We can find L1data cache miss is an important performance bottleneck. Therefore, we need to optimize program, Focus on improving data locality to increase the hit ratio,  to avoid L1 data cache miss.  

We can also use instruction-level optimizations to reduce pipeline bubbles and improve IPC. This includes techniques like instruction scheduling, branch prediction, and loop unrolling.

## Question2

### a

cores:  cores are sharing L2 cache. We assume that we have eight processors share one L2 cache. One chip have 8 cores, so one chip have 8 L1 caches.  Each SM cores has it icache and dcache. 

Bus: And different chip connect same memory with bus.

There is one process per core. So one chip has 8 process.

we need to calculate bus busy time/ total time.

we need to track **Bus Request Cycles**: The cycles during which the bus is utilized for memory accesses.

For simplification, use a uniform distribution. So we assume each cycle, each core has 10% possibilities issue an insturction. We test max_cycles=100000 cycles. 

if bus is busy, the core need to wait until the data return from meory.

### b

We only need to record bus utilization.

We simulate and find the maximum number of chips is 11 or 12 that can be connected to the system while keeping the bus utilization under 80%.
