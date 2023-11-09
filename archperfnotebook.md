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

在上下文切换时：您可以清空TBL（也可以清空TLB）。然而，这可能非常昂贵。可以添加一个表示翻译上下文的标识符，允许不同线程的多个翻译共存于TLB中。这通常在TLB具有第二级（类似于第二级缓存）时非常有用。

如果我们的入口用尽，大多数情况下我们会随机替换。LRU（最近最少使用）是个好方法，但在硬件中实施它相当困难。其他可以使用的算法包括循环轮询。关键问题在于实施的速度和复杂性。没有时间使用类似操作系统的复杂算法，同样，在硬件中实施复杂算法可能会有很大问题。

处理不同页面大小是一个棘手的问题。通常，不同的TLB专用于不同的页面大小。某些系统将非常大的页面限制为分配在虚拟地址空间的特定区域内。这样，虚拟地址中的一些位可以用于将翻译导向用于翻译的特定TLB。

TLB可以合并，为指令和数据提供服务。然而，由于这两者是内存中的两个独立流，因此从指令和数据分别使用一个单独的TLB是有利的。

是的，操作系统应该有权使TLB失效。例如，如果一个进程被交换出，或者一个页面被映射到不同的帧，所有这些特殊情况都需要由TLB正确处理。因此，操作系统应该有能力根据需要使一个或多个TLB条目失效。

英特尔架构似乎在完全关联模式下使TLB工作超过8个条目存在问题。这并不令人意外。请注意，第二级TLB没有使用完全关联结构。好像它在一个缩小的地址范围内有256个完全关联的TLB。

scoreboard , 可以看计算机体系结构-Tomasulo算法 - 天外飞仙的文章 - 知乎 https://zhuanlan.zhihu.com/p/499978902

## week 6 memory architecture and caching

L1 分别有I cache 和D cache. 

只有高端系统才配备L3缓存。有时，L3缓存位于单独的芯片中，而有时它与处理器一起安装在多芯片模块中。

L1缓存通常在数据和指令之间进行划分。

一个受害者缓存存储所有从L1/L2组合中逐出的缓存行。其思想是，在从进程P1切换到进程P2的上下文切换时，后者将开始清除P1的缓存行，以便为引入P2的缓存行腾出空间。然而，在未来的某个时刻，P1将再次切换回来。在这种情况下，拥有受害者缓存将确保属于P1的所有项目可以从附近的位置（当需要时）加载到缓存中。当然，没有从L3到L2或L1的数据的大规模传输。受害者缓存与包容性缓存之间的决定并不明确。包容式(inclusive)L3缓存设计的支持者指出，L3缓存的大尺寸将使包容式缓存在渐进情况下与受害者结构几乎相同。 原文 : A victim cache stores all the cache lines that are evicted from the L1/L2 combo. The idea is that upon a context switch from process P1 into process P2, the latter will start depopulating the P1 cache lines in favor of bringing the cache lines of P2. At some point though in the future, P1 will be switched back. In this case, having a victim cache will ensure that all the items that belong to P1 can be brought into the cache from a nearby location (on demand, of course. There is no bulk transfer of data from L3 to L2 or L1). The verdict of victim vs. inclusive cache is not clear cut. Proponents of the inclusive L3 cache design point out that the large size of the L3 will make an inclusive cache asymptotically identical to that of a victim structure. 

L2 通常是inclusive的. 包含 L1的所有数据. 

表示缓存行状态的位包括：M（修改），E（独占），V（有效）。如果V=1且E=0，表示其他核心或芯片上的缓存拥有该缓存行的副本。这些位在缓存一致性协议的执行中起着重要作用（详见第7讲）。它们还在替换算法中起作用。例如，具有V=0（空槽位）的缓存行将被视为替换的首选候选项。接下来是V=1且M=0的缓存行，因为我们无需将该缓存行完全刷新到内存。依此类推。

缓存行大小一直是一个引人入胜的问题，因为没有明确的答案来确定最佳大小。较大的缓存行将需要较小的地址标签，较少的取操作，并且如果遵守局部性原则，每次取操作将使用更多的数据。这可以降低缓存结构的开销。但这也是有代价的。如果代码没有显示出良好的访问局部性，较大的缓存行性能将较差。实际上，您可能会将不太可能使用的数据放入缓存。它还增加了总线操作的压力，因为我们需要每次获取更多的数据，这可能需要更宽的总线，或者我们将不得不在多个内存总线周期内拆分获取。较大的缓存行还可能会逐出更多的行，这可能会降低性能。

需要注意：在一些文献中，有时将缓存行称为“缓存块”。

需要注意：不合理大的缓存行可能会加剧“虚假共享”的问题，请参见第7讲。

我们在地址标签中存储多少位？数据项中用于表示行内偏移的位与比较无关。因此，最好只存储必要的内容，以节省空间、功耗和时间。有人可能会质疑我们是否真的在位操作中深入探讨这个问题。答案是否定的。考虑一个具有64字节缓存行的44位地址空间。偏移量的6位大约占地址的14%。在地址标签数组中节省这个量将减少14%的面积和功耗。这是一个很大的收益。

Cache size 一般都是Stimulate 出来的, 都是工程调试, 没有准则. 

### directly associative

只对一个item比较

### set associative

44 bit address space

7 bit offset 

### fully  associative

Any line can be stored In any address

Need to compare all items

**Write Through**）场景中，数据同时更新到缓存和内存（**simultaneously updated to cache and memory**）

#### write back

支持回写的缓存实现起来比较复杂，因为它需要跟踪哪些位置已被覆盖，并将它们标记为变脏，以便稍后写入memory中。出于这个原因，回写缓存中的读取未命中（需要一个块被另一个块替换）通常需要两次内存访问来服务：一次将替换的数据从缓存写回存储，一次检索所需的数据。

### page coloring

"在这个示例中，操作系统最好保持2的9次方，也就是512个空闲页面队列，并以轮询的方式从这些页面队列中为请求的进程分配页面。这样，页面分配是均衡的。当可用内存开始变得紧缺时，一些这些队列可能会变为空。然后，新的分配变得不够理想。过度分配内存的系统运行通常不是一个好主意。"

## memory

存储芯片通常是根据存储的位数与读取的位数相乘来报的。例如，一个4Gb×1是一款非常流行的DRAM芯片（约2020年左右），它表示该芯片具有4G位，并且一次读取或写入操作在1位单位上进行。还有其他配置，比如4Gb×4等。

请注意，单独的存储芯片通常是以位（b）而不是字节（B）为单位报价。

请注意，为了形成一个字节的存储，我们通常会将8个xxMb×1位的芯片组合在一起，这就是所谓的DIMM（双排内存模块）

请注意，通常会添加额外的芯片到数组中以存储奇偶校验。它本质上是8个芯片上所有数据的异或值。奇偶校验可以检测到由宇宙射线或周围环境中的噪声引起的内存内容损坏的情况。在高海拔地区运行的计算机更容易出现内存错误。

有时，在高端系统或任务关键系统中，会添加额外的芯片以提供更多的保护。2个汉明码排列可以检测两个同时发生的错误并纠正单位错误。

实际上，宇宙射线不会挑剔，它们可能同时影响多个芯片，引发灾难性错误。我们称这些为瞬态错误。

实际上，瞬态错误要么被检测到，此时操作系统通常会发出“紧急”消息并关闭系统，要么瞬态错误未被检测到，此时我们将面对“静默错误”。静默错误可能会影响到我们当前未使用或即将覆盖的存储区域，这是幸运的情况。不幸的情况是，瞬态错误可能导致数据损坏，而这种损坏很难（如果有可能）恢复。"

#### 内存控制器

内存控制器负责执行内存总线事务。事务可以是原子事务，也可以是分割(split)事务。原子事务在完成之前不会释放总线。分割事务通过将事务分成每个都是原子运行的子事务，从而提供了更高的性能。分割事务的实现可能会很复杂。总线协议在实施和验证方面非常困难。您会发现，在行业中，内存总线技术在设计方面变化非常缓慢，尽管受益于总线宽度和频率的增加。设计新总线的复杂性是设计新协议的障碍，更改协议通常需要更改连接到总线的所有设备，这是一项非常昂贵的操作。

#### Memory Architecture

广播总线是连接的最简单形式。早期的共享内存多处理器系统，以保持处理器之间的内存一致性，都是采用广播总线技术实现的。所有参与者都能监听所有事务，这简化了缓存协议的实现，同时还允许通过锁定总线进行同步，以使处理器能够同时与多个实体通信。总线不像需要复杂路由的更复杂结构那样复杂。总线结构的问题既存在于性能方面，也存在于物理方面。在性能方面，总线带宽被所有参与者共享，这意味着随着我们在总线上添加更多参与者，每个参与者的带宽份额将减少。在物理方面，总线的长度有限，信号衰减会使其操作变得不切实际。这限制了总线结构的可扩展性，通常只能支持少数处理器，如果要获得良好的性能，通常不会超过十几个处理器。  

NUMA（非统一内存访问）结构与支撑所有已知算法和理论发展的RAM（随机访问机器）模型的抽象存在巨大差异。当我们编写程序时，我们通常假设所有数据都能以相同性能均匀访问。然而，NUMA系统违反了这一原则，具体取决于内存分配给进程的方式。操作系统需要付出一些努力，以确保将内存分配给进程，使得所有数据来自同一节点。然后，操作系统会安排这些进程在最接近内存的芯片上运行。一般来说，在NUMA系统中编写具有可预测性性能的代码是困难的。

需要注意的是，Elnozahy等人在21世纪初的一篇论文中提出，使用NUMA系统的正确方式是将每个具有独立内存的芯片视为独立单元，并在程序级别的节点之间使用消息传递。然后，共享内存用于加速消息传递的性能。他们证明，采用这种方式使用的系统可以优于将内存暴露给程序员的系统。

此外，NUMA系统通常以比例形式引用，如1:2 NUMA，这意味着远程内存在访问周期数上比本地内存远两倍。

#### NUMA issue

•Memory allocation policies

•Process scheduling

•Cache affinity

•Performance stability

New Concept: Memory Interleaving

Memory interleaving指的是内存寻址，使得连续的字节分布在多个模块（DIMM）上，而不是来自同一个DIMM。这样，如果我们想读取缓存行，我们可以在获取大量字节时实现并行，而不是一次拉取一个字节。

#### High Bandwidth Memory

HBM可以作为缓存系统的扩展，提供非常大的L3缓存。这样，不需要程序员或操作系统智能来从HBM中获益。或者，它们可以被提供给程序员作为临时存储区。这类似于早期系统使用的一种称为page-0-addressing的地址模式。这使软件变得复杂，不易移植，并且使虚拟化和上下文切换变得昂贵或不可能。第三个选择是将HBM视为地址空间的一部分，并让操作系统控制如何分配这些页面。这种技术的理论基础是，操作系统可以智能地使用这宝贵的内存，优先考虑某些进程，或存储性能敏感的信息，如页表或内核数据结构。然而，使操作系统能够胜任执行这些功能所需的修改远非简单。

#### Persistent memory

持久内存允许以字节级别访问内存中的数据，并可以与加载和存储指令一起使用。这与以磁盘块大小访问的闪存存储设备不同。写入仍然很昂贵，因为它们需要烧掉材料以留下无法忘记的印记。这使得这些设备非常适合读取。计划使用良好尺寸的缓存来吸收大多数写入，以便这项技术的写入挑战不会对性能产生严重影响。
