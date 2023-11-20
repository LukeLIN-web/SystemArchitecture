# System Architecture and Performance

Brad 声称该代码可以实现大约 1 个每周期指令 (IPC) 的说法并不准确，并且有多种原因可以解释为什么使用给定的代码和硬件配置无法实现这一点。

1. 内存访问限制：该代码涉及 2.56 亿 (0x10000000) 个条目的大型数组。该数组比缓存所能容纳的要大得多，并且与 ALU 操作相比，内存访问时间要慢得多。在流水线处理器中，内存访问是一个主要瓶颈，并且可能需要多个周期才能完成。高内存访问延迟会显着降低 IPC。 (如果有优秀的提前读取就可以,在给定的代码中，内存访问是随机的（因为它取决于 的结果`random()`），预取可能无法有效工作)
2. 数据依赖性：代码执行内存读取和写入，并且写入取决于从内存读取的值。这会产生数据依赖性，并可能限制并行发出多个指令的能力。在双发射处理器中，如果指令之间存在数据依赖性，则可能会导致流水线停顿。
3. 随机内存访问：代码使用随机内存访问（使用函数`random()`）来访问数组元素。随机内存访问模式对缓存系统不友好，可能导致缓存未命中，进一步增加内存访问延迟。
4. 内存带宽限制：即使使用四端口寄存器文件，在访问如此大的阵列时，内存带宽也可能成为瓶颈，特别是在同时进行多个访问的情况下。
5. 有限的并行性：虽然处理器能够进行双发射，但每个周期实现两条指令需要代码中具有高度的指令级并行性 (ILP)。由于随机内存访问和数据依赖性的性质，所提供的代码没有表现出明显的 ILP。

实际上，由于内存访问延迟和依赖性，代码可能会在流水线中遇到严重的停顿，从而无法实现 IPC 为 1，更不用说每个周期两条指令了。实际的 IPC 会低得多，并且很大程度上取决于特定处理器的架构和内存层次结构。

A processor’s execution unit consists of 5 functional subsystems S1 through S5 with the following timing characteristics:

S1: 100 pico-seconds S2: 150 pico-seconds S3: 150 pico-seconds. S4: 200 pico-seconds. S5: 200 pico-seconds.

You also have access to latches, where a latch introduces 20 pico-seconds of delay.

1. What is the highest frequency an in-order, single issue processor can run at with the above design? 

   f = 1 / (800 * 10^(-12)) Hz ≈ 1.25 GHz

2. If we pipeline this execution unit by adding a latch after every subsystem, what is the highest frequency at which the processor can run?

   f = 1 / (220 * 10^(-12)) Hz ≈ 4.55 GHz

3. You are given an alternative pipeline structure in which S1-S2-S3 are considered one stage and S4-S5 are considered another stage, with an intervening latch between the two stages. What is the highest frequency that you can run the pipeline at?

   第一个stage, 400, 第二个stage 400, 所以我是 2.38GHz

4. Between the design in (b) and (c), which one would you pick? Why?

Given the choice, it would be preferable to pick the design with a latch after every subsystem (design in b) because it allows the processor to operate at a significantly higher clock frequency. Higher clock frequencies can lead to better overall performance, provided that the workload can be effectively parallelized and benefits from pipelining. However, it's important to consider other factors such as power consumption, area, and the specific requirements of the target application.

6/8 GB/s  内存可以. 21.3333333333

network 可以10个,

cpu可以 9个

所以最多9个同时. 

pick CPU. 强化到10个stream 并发. 

#### quiz03

1 He suggested changing the 4-way set associate l2 cache to a direct-mapped cache can reduce power consumption and keep the chip within the power envelope of the design targets. He admitted that there will be a loss in performance, but since each cache access requires four comparisons and a complex replacement algorithm to beimplemented, that the reduction in power was a fair tradeoff between performance and feasibility.

In HPC, performance is more important, a more associative cache might be preferred despite its higher power consumption. In power-sensitive designs like mobile device, maybe we can use direct-mapped cache to reduce power consumption 

2 What is the size of an 8-entry TLB if the system has a 64-bit address space, a 44-bit physicaaddress space, and a 4KB page?

4KB,  12 bit for offset, 52 bit  VPN

physical 44, 12 bit for offset, 32 for  PFN

Each TLB entry must store both a VPN and a PFN  =>one TLB entry , 84 bit, 

so the size of an 8-entry TLB = Total Size=Number of Entries×(Size of VPN+Size of PPN) = 84 bytes

 3  Consider the stream benchmark. If we have a 4-way set associative cache, compare theperformance of the following replacement algorithms:

LRU, FIFO, random

不同的replacement 策略不会改变. 

#### quiz04

1. Consider a workload that finds about 90% of its data in Level 1 cache, and 95% of its data in Level 2 cache. Compute the average time to load an item from memory as seen by the processor, given that the L1 cache requires 1 cycle to load, the L2 requires 10 cycles to load, and the main memory requires 65 cycles to load.

= (90% * 1 )  +(10 %*  95% * 10) + (10 %*  5% *65 ) 

2. Reconsider Problem 1. A brilliant engineer working with you comes up with the idea of adding an L3 cache. Using simulation, you discover that the workload in problem 1 now finds its data in the L3 98% of the time. What is the average time to load an item from memory as seen by the processor. If the addition of the L3 will increase the cost of the processor by 50%, do you believe that this is worth doing?

Regarding the second part of your question, whether the addition of the L3 cache is worth the 50% increase in processor cost depends on the specific requirements and constraints of your application. If the application is highly sensitive to data access times and the performance improvement justifies the cost, then it could be worth it. However, if cost efficiency is more critical or if the performance gains are not substantial for the application's needs, the additional cost might not be justified. This decision often depends on factors like the specific use case, budget constraints, and performance requirements.

关于问题的第二部分，添加 L3 缓存是否值得处理器成本增加 50% 取决于应用程序的具体要求和限制。如果应用程序对数据访问时间高度敏感，并且性能改进证明了成本的合理性，那么它可能是值得的。但是，如果成本效益更为关键，或者性能提升对于应用程序的需求来说并不显著，则额外的成本可能不合理。此决策通常取决于特定用例、预算限制和性能要求等因素。

5

Consider the following code: double a[2 << 20]; double b[2 << 20]; double c[2 << 20];

for(i = 0; i < n; i++) { a[i] = b[i] * c[i];

}
Assume that the cache line is 64 bytes. The processor runs at 2GHz. Calculate the necessary memory bandwidth that the processor needs to enable computation at 2GF/sec.

一次读64bytes, 8 cycle之后会有一次miss.

一秒计算需要 3* 64bit = 192 bit  x 2 G  的数据

所以带宽 为 3 x8 x2 / 8 = 6 GB/s

