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
