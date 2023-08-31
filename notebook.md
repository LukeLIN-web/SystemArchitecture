老师是94年的博士, BSEE84,  MCE  87,  MSCS 90. 读了六年的硕士.12-20年的dean.之前在cmu, ut autsin当教授. 在 ibm 有职位. visit过贝尔实验室, meta. 在工业界20年, 在学术界20年.  

博后也可以选课,她是哈萨克斯坦的博士, ms在uk

葡萄牙 老哥, 里斯本大学本硕.

homework 30% 

Project 25%

exam 3次,  45%

网上copy答案也可以,  标明出处, 而且要理解是copy了啥.

2015年送了一个手机给老师.

## class1

访问L1 cache , 2-5 cycles, L2 12 cycles. main memory 5k-6k cycles.

普通就几十个寄存器, 有个人提出用60K个寄存器  , 问题在哪里?

1. bandwidth to memory不够
2. 线很长, latency很大. 
3. compiler没法使用好这么多寄存器. 分配寄存器是 np compele 问题.   有个编译器专家调查了一年, 结论是64个寄存器 已经很难利用好了.

GPU 和CPU 共用 MEM可以吗?  苹果,  grace hopper就是这么做的. intel, IBM 这么做, 失败了, 因为power技术不行,只好用weak 处理器. 

1. GPU 内存 bandwidth 很大, CPU内存需要latency小. 
2. Data movement 用了非常多power.
3. AMD 有能力把GPU 和CPU 共用 MEM, 但是没有这么做, 为了英伟达的软件兼容性.

老师说他没有ps1 游戏机, 但是设计过ps1.

## class2

6 cycles, 需要24 bytes 内存.  频率3GHz. 那么1s 访问12 GB 内存, 但是memory bus只有6GB/s. 那么就会成为bottleneck.

vector instructions. 4way  可以一次处理4个数. 



HBM 是一种立体空间内存.   难点是 发热严重 ,  立体的访问慢. 

高级产品, 可能没有性价比,但是可以树立品牌形象,有广告作用.  

