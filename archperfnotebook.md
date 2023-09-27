老师是94年的博士, BSEE84,  MCE  87,  MSCS 90. 读了六年的硕士.12-20年的dean.之前在cmu, ut autsin当教授. 在 ibm 有职位. visit过贝尔实验室, meta. 在工业界20年, 在学术界20年.  

博后也可以选课,她是哈萨克斯坦的博士, ms在uk

葡萄牙 老哥, 里斯本大学本硕.

homework 30% 

Project 25%

exam 3次,  45%

网上copy答案也可以,  标明出处, 而且要理解是copy了啥.

2015年送了一个手机给老师.

## 第一周

访问L1 cache , 2-5 cycles, L2 12 cycles. main memory 5k-6k cycles.

普通就几十个寄存器, 有个人提出用60K个寄存器  , 问题在哪里?

1. bandwidth to memory不够
2. 线很长, latency很大. 
3. compiler没法使用好这么多寄存器. 分配寄存器是 np compele 问题.   有个编译器专家调查了一年, 结论是64个寄存器已经很难利用好了.

GPU 和CPU 共用 MEM可以吗?  苹果,  grace hopper就是这么做的. intel, IBM 这么做, 失败了, 因为power技术不行,只好用weak 处理器. 

1. GPU 内存 bandwidth 很大, CPU内存需要latency小. 
2. Data movement 用了非常多power.
3. AMD 有能力把GPU 和CPU 共用 MEM, 但是没有这么做, 为了英伟达的软件兼容性.

老师说他没有ps1 游戏机, 但是设计过ps1.

6 cycles, 需要24 bytes 内存.  频率3GHz. 那么1s 访问12 GB 内存, 但是memory bus只有6GB/s. 那么就会成为bottleneck.

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

以前晶体管不断变小, ->  faster switching, 现在不能无限提高频率了, 因为热效应过大, 会melt. 

读main memory ,需要50-60 ns.

L1  有32KB.

同步, lock都交给上层硬件. 原则就是, 应该把最底层的东西, 硬件,  做的 as simple as possible, 复杂的都交给上层. 而不是最底层提供大量复杂的功能. 这些功能可能上层用不到. 

硬件多线程的影响

优点:

1. 充分利用cache
2. 

缺点

1. 竞争cache
2. tolerate memory latency
3. more state-> more power
4. 增加memory Bandwidth.

## 第二周

vector processor , 是非常昂贵的. 

very large instruction , 可以吗? intel 一个processor 做了, 但是行不通, 

load vector register, 需要非常多 power .

execution units 不用线性增长, 但是state, bandwidth, 芯片面积,power 都会随thread数量线性增长. 

### multithread

here we talk about hardware multithread ! 

•What?

•Abstractions of independent instruction streams implemented in hardware, equivalent to a CPU from a software perspective

User thread, kernel thread (也就是操作系统的 thread),  hypervisor thread, hard ware thread. 这四个都是不一样的. 一层层往下都要映射. 

一个core 可能有多个 hardware thread.  大部分都是1个 或者2个thread.  有的单核有4个thread, IBM 有过单核8 thread. 

•Implications for the operating system: Scheduling

•Implications for performance: More throughput, but not faster!

•Implications for the software writer: May want to exploit by assist threads, etc.

•A confusing concept: Program level threads can be multiplexed on the hardware threads



#### loop unrolling

是HPC非常常用的, 为了减少bubble, 循环步长不要设置为1, 而是在循环中修改变量i. 可以在循环中省下一两条指令的时间. 

## 第三周



IF ID Reg  EX  L/S

data从寄存器到ALU也需要一个cycle.

Control induced bubble. 不知道要不要跳转. 

多线程可以 填补bubble

structural hazard 的解决方案:  1.  增加资源. 

2 ported register file

现在实际上有200多个寄存器, 指令集的32个寄存器会映射过去. 

single-ported integer register file , file就是寄存器array. 

感觉这个课就是默认学过体系结构, 作业都是综合大题, 必须熟练掌握体系知识. 问题充满了开放性, 很像企业面试题. 



2号考试, 可以搜索网络, 但是不能talk, 可以用chatgpt.



### 第四周

arm(包括Apple) , risc, 和 power pc 都属于risc,  no translation.  

x86 , 是intel 和amd 用的, 有translator, 把 cisc 翻译成 risc.

pipeline 不能太深, 否则时钟电平有问题. 

标准的REG stage, 可以同时读两个写一个.

这门课的reg不能同时read write.第三个是read reg, 最后是write back.

st操作,st r3, (r6) 需要读两个,  r3和r6都要读reg.

#### superscalar (multi-issue) pipeline

需要增加更多资源, 

#### 乱序执行

可以把下一个loop 前几个cycles 和前一个loop overlap起来. 

如果memory fault了怎么办?  前面的都写入内存了,撤不回了怎么办?   IBM的解决办法是把前面的写入一个buffer, 比如写入register33,  如果整个完成了再commit.

#### 寄存器重命名

加速和乱序执行差不多, register renaming works better with larger codes.

