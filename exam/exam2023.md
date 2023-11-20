## 讲解





unrolling不是写代码的, 是编译器做的

除法很慢, 把除法展开快很多.





## 第一次期中考

### **Question 1** 

Each request is guaranteed not to exceed 5msec in processing time.

 a request’s response time cannot exceed 10 msec.

Web requests arrive at random according to an exponential distribution, with average inter-arrival time of 50 msec. one second average 20 request averge.  means lambda = 20.

Since response time cannot exceed 10 ms, we need to calculate the possiblity,  If, within a 5 ms duration, we have 2 requests arriving, it would indeed exceed the 10 ms response time requirement. 

From https://homepage.divms.uiowa.edu/~mbognar/applets/exp-like.html we can get Possiblity is 9.5%,  it is not small since our server is run long time.   

Therefore, considering the potential risk of violating the Service Level Agreement and the associated penalties, we should reject this contract.

答案 : 电子表格模型只能捕获对资源的聚合需求，但无法解释到达率随机时不可避免的排队延迟和影响。尽管中本聪先生的合理假设是到达率非常低，但现实情况是，由于到达率是随机的，因此会出现此类请求彼此距离太近的情况，此时排队延迟将阻止系统履行其响应时间义务。

### Question2

### 1)

for one core, the peak floating-point performance in FLOP (Floating Point Operations Per Second) would be: 2 * 10^9 Hz * 2 = 4 * 10^9 FLOP/s

Since there are 16 cores in total, the peak performance of the entire chip would be: 16 cores * 4 * 10^9 FLOP/s = 64 * 10^9 FLOP/s = 64 GFLOP/s

正确

### 2)

without memory bottleneck, the peak rate of floating-point operations is 64 GFLOP/s.

However one floating point is 4Bytes.  The memory bandwidth of the entire chip is 4GB/sec. Therefore one second chip can go throught 1G floating point.  

If we want to reach peak rate, we cannot move data throught memory, only calculate them on chip during this second.

what's more, all 16 cores need to run floating point operations, and use two floating point units simutaeiously. 

错误, 一个flop 需要两个op和一个result. 峰值速率出现在一种不太可能的情况下，即流水线已满，并且没有出现缓存未命中、数据依赖冲突、控制或结构性危险等停滞。要达到峰值速率，数据很可能必须驻留在高速缓存中。

#### 3)

Peak floating-point operations per second (GFLOP/s) is a useful metric for characterizing the theoretical maximum floating-point performance of a processor.  This metric represents an ideal scenario that may not always be achievable in real-world applications.

The suitability of this metric depends on the type of workload or application:

- For highly parallel and compute-intensive tasks that fully utilize all available cores and floating-point units, the peak GFLOP/s can be a meaningful indicator of performance potential.
- However, many real-world applications may not fully saturate all cores and units simultaneously. Memory access patterns, data dependencies, and other factors can limit actual performance.
- In practice, sustained and achievable performance may be lower than the peak due to various bottlenecks, such as memory bandwidth limitations. --reference:  chatgpt.

峰值速率一直是数据表（销售人员和行业杂志使用）中评定处理器性能的标准方法。在更现实的应用中，由于管道危险和高速缓存缺失会频繁发生，因此峰值速率具有相当大的误导性。Linpack 标准试图通过提供一些有用的代码来改善这种情况，这些代码仍然具有很好的引用局部性。该基准是一些线性代数代码的代表。设计良好的系统应能在 Linpack 基准上达到峰值性能的 75% 至 90%。

### Question3

### 1)

Yes. It happens when a store instruction in Q1 and a speculative instruction also write the same address(may next loop).

### 2)

1. If the cache is hit, then LS can load data directly. 

2. If cache miss and data can be found in Q1, then LS can load data from Q1 because Q1 has not write back, but it will be.

3. If cache miss and Q1 miss, if we find it in Q2. It means data is related to uncommitted instruction. LS unit should check whether this speculative instruction is committed. It has two situation:

4. 1. If speculative instruction committed, then LS can load data from Q2. 
   2. If speculative instruction not committed, then LS needs to stall. 

错误

答案: 

There are two cases to consider:

1. The load instruction is not speculative:
    o Then, we must first search Q1 in case if a previous update is still pending in the queue and has yet to be written in the cache. If the data item is absent from Q1, then we issue the request to search the cache. We do not approach Q2 at all in this case.

2. The load instruction is speculative:
    o This case is tricky, because we have to rely on the instruction

   scheduler to ensure that the data hazards are taken care of even in speculative execution. In this case, we search Q2 first, then if not found, we revert to the previous case.

### Question4

```cpp
double a[N], b[N], c[N], d[N], e[N];// N is a constant int i;
double u, v;
for(i = 0; i < N; i++) { 
  u = a[i] / b[i]; 
  v =  c[i]/ d[i];
  e[i]= u + v;
}
```

Reasons:

1. `u` and `v` can be computed independently in each iteration, so they don't have a data dependency.

错误

答案

As discussed in class, division operations are very expensive and are very difficult to pipeline. The loop contains two divisions. A rewrite of this code could be 

```cpp
for(i = 0; i < N; i++)
e[i] = (a[i] * d[i] + c[i] * b[i]) / (b[i] * d[i]);
```

On an M2 processor, the running time of the second version of the loop is 37% faster than the original one! Even if we have added three floating-point multiplications, the code still ran faster than with two divisions! Note that this case benefits from the M2 having more than one floating-point unit which masks the penalty of the added multiplications.
Note that the incorrect answer is to rewrite the code so that the loop is unrolled by hand. Please remember that loop unrolling is performed by the compiler. Forcing the programmers to rewrite the code to unroll the loops by hand will provide ugly code that is difficult to maintain. Keep in mind performance is importance, but programmer’s time and code maintainability should never be sacrificed for performance. Elegant solutions usually perform best!

### Question5

答案:

IF: Instruction fetch, ID: Instruction Decode, Reg: Reading integer register file
 L/S: Load store, WI: write result into integer register file
 Freg: Reading floating point register file, FPA0: Stage 0 of the adder, FPM0: Stage 0 of the multiplier.





## 第二次期中考





