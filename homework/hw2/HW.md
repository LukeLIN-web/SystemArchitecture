



Q1:

a has  100/8 = 12.5 GB/s,  128/12.5=10.24 ns 

a send a message of 128 Bytes  needs 5microsecond + 10.24ns  =5012ns

Network thourghtput = 128/5012=0.0255GB/s 

b has bandwidth 125/8=15.625 GB/s , 128/15.625=8.192 ns

b send a message of 128 Bytes  needs  6 microsecond + 8.192ns  =6008 ns

Network thourghtput = 128/6008=0.0213GB/s

I use b, because it has better bandwidth.

Q2

The critical path in this pipeline is the longest sequence of stages, which in this case is from "Instruction decode" to "Execution unit," with a total time of 

400 + 500 + 400 = 1700ps

To choose a good frequency for the processor, we want to ensure that the critical path can be completed within one clock cycle. Let's calculate the frequency (F) using the formula:

F = 1 / Clock cycle time

F = 1 / 1700 picoseconds F ≈ 0.588 GHz

Q4:

ld f1  1cycle 

mul f4,f2,f0  7 cycle

ld f6 1 cycle  

add f6   4 cycle 写后读, 不能改. 

st f6 1 cycle

add r1, r1, 8  1 cycle

add r2, r2, 8 1 cycle

add r3, -1  1 cycle

bnz  1cycle, 但是可以都预测为跳转,  循环次数很大的时候 约等于0 

总共17个cycle, 9个instruction 

不能同时读取两个浮点数.  我们也不能重命名寄存器.

IPC :  17/9=1.88888888889 

这样可能不对? 需要excel 一个个stage算吗?  
