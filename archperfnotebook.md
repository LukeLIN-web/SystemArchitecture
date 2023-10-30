老师是94年的博士, BSEE84,  MCE  87,  MSCS 90. 读了六年的硕士.12-20年的dean.之前在cmu, ut autsin当教授. 在 ibm 有职位. visit过贝尔实验室, meta. 在工业界20年, 在学术界20年.  https://www.cs.cmu.edu/afs/cs/user/mootaz/ftp/html/research.html

博后也可以选课,她是哈萨克斯坦的博士, ms在uk.厂商2015年送了一个手机给老师.

葡萄牙 老哥, 里斯本大学本硕.

homework 30% 

Project 25%

exam 3次,  45%

网上copy答案也可以,  标明出处, 而且要理解是copy了啥.

这个课默认学过体系结构, 作业都是综合大题, 必须熟练掌握体系知识. 问题充满了开放性, 很像企业面试题. 

老师说他没有ps1 游戏机, 但是设计过ps1.

## 第一周

访问L1 cache , 2-5 cycles, L2,  12 cycles. main memory, 5k-6k cycles.

普通的CPU 有几十个寄存器, 有个人提出用60K个寄存器  , 问题在哪里?

1. bandwidth to memory不够
2. 线很长, latency很大. 
3. compiler没法使用好这么多寄存器. 分配寄存器是 np compele 问题.   有个编译器专家调查了一年, 结论是64个寄存器已经很难利用好了.

GPU 和CPU 共用 MEM可以吗?  苹果,  英伟达grace hopper就是这么做的. intel, IBM 这么做失败了, 因为power技术不行,只好用weak 处理器. 技术原因: 

1. GPU 内存 bandwidth 很大, CPU内存需要latency小. 
2. Data movement 用了非常多power.
3. AMD 有能力把GPU 和CPU 共用 MEM, 但是没有这么做, 为了英伟达的软件兼容性.

6 cycles, 需要24 bytes 内存.  频率3GHz.  那么1s 访问12 GB 内存, 但是memory bus只有6GB/s. 会成为bottleneck.

vector instructions. 4way  可以一次处理4个数. 

HBM 是一种立体空间内存.   难点是 发热严重 ,  立体的访问慢. 

高级产品, 可能没有性价比,但是可以树立品牌形象,有广告作用.  

这节课学会了帮公司采购电脑.

每个core一个bus可以吗? 

对于stream的数据, 因为只处理一次,  cache 几乎没啥用, 甚至有害. 

#### stimulations

functional, vs cycle-accurate .

stochastic vs. deterministic .   deterministic 开销大, 因为要存big trace data来得到有用的结果.

Event-based vs time based

event queue vs multithreaded

中国人喜欢riscv , 因为没有license.

多个queue, 一对一 resource好. 还是一个queue,  多个resource好?

一个queue,  多个resource:   适合有个很慢,可以分给一个resource 后面的不用等. resource肯定越多越好. 

 多个queue, 一对一 resource, 需要优秀的load balancing schduler.   最简单的用shortest queue,哪个短放哪个. 

测量不准确怎么办?

1. 多次测量, 用不同的random seeds
2. 报告平均, 标准差和置信区间. 

总共1TB 数据, 服务器用 32 GB 还是64GB双倍价格 的内存? 

设计方案之前先要问 metrics是什么? 

考虑有多少client, client 很多的话, 要多买一些服务器, 所以要买单价低的. 

讨论可以每个人都参与, 但是课程就进行的非常慢, 一个小时就讲一两个知识点. 

因为用户访问量随时间变化非常大, 所以需要云计算,弹性计算. 

如果没有自己的超算,用别人的云计算80k美元发一篇文章.如果要一直用就需要有自己的机器. 

如果要用外部库, 你需要 recompile dynamic lib with debug flag.

以前晶体管不断变小 ->  faster switching, 现在不能无限提高频率了, 因为热效应过大, 晶体管会melt. 

读main memory ,需要50-60 ns.

L1  有32KB.

同步, lock都交给上层硬件. 原则就是, 应该把最底层的东西, 硬件,  做的 as simple as possible, 复杂的都交给上层. 而不是最底层提供大量复杂的功能. 这些功能可能上层用不到. 

硬件多线程的影响

优点:

1. 充分利用cache

缺点

1. 竞争cache
2. tolerate memory latency
3. more state-> more power
4. 增加memory Bandwidth.

## 第二周

vector processor 是非常昂贵的. 

very large instruction , 可以吗? intel 曾经有个processor 做了, 但是行不通.

load vector register, 需要非常多 power .

execution units 不用线性增长, 但是state, bandwidth, 芯片面积,power 都会随thread数量线性增长. 

### multithread

here we talk about **hardware multithread**! 

•What?

•Abstractions of independent instruction streams implemented in hardware, equivalent to a CPU from a software perspective

User thread, kernel thread (也就是操作系统的 thread),  hypervisor thread, hard ware thread. 这四个都是不一样的. 一层层往下都要映射. 

一个core 可能有多个 hardware thread.  大部分都是1个或者2个thread.  有的单核有4个thread, IBM 有过单核8 thread. 

•Implications for the operating system: Scheduling

•Implications for performance: More throughput, but not faster!

•Implications for the software writer: May want to exploit by assist threads, etc.

•A confusing concept: Program level threads can be multiplexed on the hardware threads

#### loop unrolling

HPC 常用的技术, 为了减少bubble. 循环步长不为1, 而是在循环中修改变量i. 可以在循环中省下一两条指令的时间. 

## 第三周

五个阶段: IF ID Reg  EX  L/S

data从寄存器到ALU也需要一个cycle.

Control induced bubble. 不知道要不要跳转. 

多线程可以 填补bubble

structural hazard 的解决方案:  增加资源. 比如 two ported register file

现在实际上有200多个寄存器, 指令集的32个寄存器会映射过去. 

single-ported integer register file , file就是寄存器array. 

### 第四周

arm(包括Apple) , risc, 和 power pc 都属于risc,  no translation.  

x86 , 是intel 和amd 用的, 有translator, 把 cisc 翻译成 risc.

pipeline 不能太深, 否则时钟电平有问题. 

标准的REG stage, 可以同时读两个写一个.

这门课的reg不能同时read write.第三个是read reg, 最后是write back.

st操作,st r3, (r6) 需要读两个,  r3和r6都要读reg.

#### superscalar (multi-issue) pipeline

需要增加更多资源

#### 乱序执行

可以把下一个loop 前几个cycles 和前一个loop overlap起来. 

如果memory fault了怎么办?  前面的都写入内存了,撤不回了怎么办?   IBM的解决办法是把前面的写入一个buffer, 比如写入register33,  如果整个完成了再commit.

#### 寄存器重命名

加速和乱序执行差不多, register renaming works better with larger codes.

实际上的register比 32个architecture register多很多, 用来 renaming 或者暂存 etc.  

IF, ID 之后, instruction issue & scheduling  是非常重要的, 

pipeline 有n 个stage, 就有n个control register, 课程project 需要implement it. 有一个active的control register. 

## L05 Virtual memory and TLB

vector 声明的数组在heap,  普通的变量在stack.  **heap：是由malloc之类函数分配的空间所在地。** **地址是由低向高增长的。** **stack：是自动分配变量，以及函数调用的时候所使用的一些空间。** **地址是由高向低减少的**。

Buddy Allocation : 分配内存, 不断减半, 直到最小的一块, smallest block its size 满足需求. 

TLB, 就是虚拟地址的cache 

物理地址比虚拟地址空间大或者小都行, 是独立的. 

#### 页表

用MMU来翻译, 从virtual page map 到 实际page. 

对于每个frame 还会存protection bits 和reference bit.

如果只有一个页表,  2^52次 * 6Byte,  6Byte 48bit 是physical address , 这需要的virtual address太大了.

8bit , Index1, 找到page table level1 查找下一级的页表基地址. Index2 6bit, Index3 6bit,  offset 12bit.

large page, 1个页有2MB.    之前都是在HPC用,   AI 可能推动很大的page, 因为数据非常多非常大. 

表示large 页表的方法

1. 可以加indicator, 表现page有多大
1. 专门用index 1 来索引大page. 

TLB miss 的代价是非常大的. 

what if a page is swapped out? 

先cache, 再TLB, 可以更多吞吐. 因为可能不用经过TLB.  而且可以用id,  标记是哪个进程在用. 

增加 associativity：访问时间hit 时间增加， miss 时间减少。

全相连fully associate: 增加了hit时间,减小了miss rate 

组相连: 

直接连接:

random :cheap , 

LRU:  成本高. 

有指令TLB和 Data TLB .

Solution 1: Multi-Level Page Tables

context table 在MMU中. 

谁翻译这个地址? 

Solution 2: zero-Level Page Table

•Only a TLB inside processor

•No page table support in MMU

•On a TLB miss, trap to software and let the OS deal with it (MIPS 3000/4000)

Advantages:  Simpler hardware , Flexibility for OS 

Disadvantages: Trap to software,  may be slow

The MIPS architecture used to have this feature. This enabled maximum flexibility to the software and simplified the implementation of the hardware. Unfortunately, the cost of a TLB miss can be substantial (although you may argue that it is not much better if done in hardware because of the memory accesses).

问题 

•What to do on a context switch?   每次switch都要flash TLB.  有的一个thread一个TLB,  有的多个thread共享一个TLB

•What if we run out of entries? What is the replacement policy?  LRU, or random 

•How to handle the page size issue? (e.g., Intel specifies 4K, 2MB and 1GB as valid page sizes)

•Do we differentiate between instruction and data?

•Should the operating system have the right to invalidate the TLB?

On a context switch: You can flush the TBL (also, shoot down the TLB). On the other hand, this can be very costly. One can add an id that signifies the context of the translation, allowing multiple translations belonging to different threads to co-exist in the TLB. This is typically useful if the TLB has a second level (like a second level cache).

If we run out of entry, most of the time we do a replacement at random. LRU would be great, but implementing it in hardware is quite difficult. Other algorithms that could be used is round-robin. The key issue here is speed and complexity of the implementation. There is no time to go into an elaborate algorithm like what the operating system would do, and similarly, implementing an elaborate algorithm in hardware could be very problematic.

Handling different page sizes is a tricky issue. Typically, different TLB’s are devoted to different page sizes. Some systems would restrict the very large pages to be allocated within a certain region within the virtual address space. This way, some bits in the virtual address that is to be translated can be used to steer the translation toward the specific TLB that can be used for translation. 

A TLB can be combined, providing service for both instructions and data. However, since these are two independent streams into the memory, it is profitable to have a separate TLB for instructions from the one that is used for the data.

Yes, the operating system should have the right to invalidate the TLB. For instance, if a process is swapped out, or if a page is remapped to a different frame, all of these special cases need to be properly handled by the TLB. The operating system therefore should have the ability to invalidate one or more TLB entries as necessary.

The Intel architecture seems to have an issue getting the TLB to work beyond 8 entries in fully associative mode. This is not surprising. Notice how the second level TLB is not using a fully associative structure. It is as if it has 256 TLB fully associative TLB within a reduced address range. 

scoreboard , 可以看计算机体系结构-Tomasulo算法 - 天外飞仙的文章 - 知乎 https://zhuanlan.zhihu.com/p/499978902

## week 6 memory architecture and caching



L1 分别有I cache 和D cache. 

Only high-end systems sport an L3 cache. Sometimes, the L3 cache is in a different chip by itself, and sometimes it is mounted with the processor in a multichip module. 

The L1 is typically split between data and instructions.

A victim cache stores all the cache lines that are evicted from the L1/L2 combo. The idea is that upon a context switch from process P1 into process P2, the latter will start depopulating the P1 cache lines in favor of bringing the cache lines of P2. At some point though in the future, P1 will be switched back. In this case, having a victim cache will ensure that all the items that belong to P1 can be brought into the cache from a nearby location (on demand, of course. There is no bulk transfer of data from L3 to L2 or L1). The verdict of victim vs. inclusive cache is not clear cut. Proponents of the inclusive L3 cache design point out that the large size of the L3 will make an inclusive cache asymptotically identical to that of a victim structure.

L2 通常是inclusive的. 包含 L1的所有数据. 

The bits that indicate the state of the cache line are: M: Modified, E: Exclusive, V: Valid. If V=1 and E=0, it means that there are other caches on other cores or chips that have a copy of this cache line. These bits play an important role in the execution of cache coherence protocols (see L-07). They also play a role in the replacement algorithm. For instance, a cache line with V=0 (an empty slot) will be most beneficiary as a candidate for replacement. Next would be a cache line with V=1 and M=0, because we will not need to flush this cache line all the way to memory. And so on.

The cache line size has been always a fascinating problem, as there is no definitive answer as to what is the optimal size. A larger cache line will require smaller address tags, fewer fetch operations, and if the principle of locality is respected, more data will be used per a single fetch operation. This can be great for reducing the overhead of the cache structure. But it comes with a price. A large cache line will perform poorly if the code does not show good locality of access. In fact, you are bound to bring into the cache data that may not likely to be used. It also puts more pressure on the bus operation, as we need to bring in a larger amount of data per fetch, and this may need for the bus to be wider, or we will have to split the fetch over more than one memory bus cycle. A large cache line also has the potential of bumping out more lines, which can reduce performance.

Please note: Sometimes a cache line is called “cache block” in some literature.

Please note: An unreasonably large cache line can exacerbate the problem of “False sharing”, please see L-07.

How many bits do we store in the address tag? The bits indicating the offset within the line for a data items are not relevant to the comparisons. Therefore it is better to conserve space, power and time by only storing what is necessary. One may argue if we are really down there in the bit twiddling department. The answer is no. Consider a 44-bit address space with a 64-byte cache line. The 6 bits of the offset are about 14% of the address. Saving this amount in the address tag array will yield 14% less area and power. A good deal to have.



Cache size 一般都是Stimulate 出来的, 都是工程调试, 没有准则. 

