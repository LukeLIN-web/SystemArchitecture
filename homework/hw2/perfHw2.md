



## Q1

**For Device A:**

$100\mathrm{Gb/s} = 12.5\mathrm{GB/s}$

Transmission Latency: $\frac{128\mathrm{B}}{12.5\mathrm{GB/s}}=10.24ns$

Total Latency: $10.24ns+5ms=5010.24ns$

**For Device B:**

$125\mathrm{Gb/s} = 15.625\mathrm{GB/s}$

Transmission Latency: $\frac{128\mathrm{B}}{15.625\mathrm{GB/s}}=8.192ns$

Total Latency: $8.192\mathrm{ns}+6\mathrm{ms}=6008.192\mathrm{ns}$

Thus, **Device A is better**, because its total latency is smaller.

## Q2

We could build a 5-stage pipelined processor. In this case, the latency is determined by the component took the longest time.

We noticed `Operand fetch` may become the most time-consuming stage, which took up to 500ps if fetching an operand from the cache.

However, for the processor, it is much more frequent to operate on registers compared to caches. Thus, we could let `Operand fetch from cache` take 2 cycles to complete. So, right now, `Instruction decode` and `Execution unit` determine the processing frequency, which is

$f = \frac{1}{400\mathrm{ps}} = 2.5\mathrm{GHz}$

## Q3

Since the webserver speed most of the time on waiting connection if the webserver is idle. Here we simulate this scenario.

1. We measure the time starting at the server start
2. We generate 1000 requests in POST method to avoid cache.
3. We measure the time when the server finished all the requests and quit.
4. We manually set a time counter to compare the running time of the server with/without profiler.

The result of default output is shown in `q3_output.txt`, and the svg is shown below

From the text result, it's not clear about the invoking relationship. But in the flame graph, it's more clear. There's the result analysis

1. The overhead time (socket initial time) is trivial, which is 0.15% of the total time.
2. The server spend 20% of the time on `select` function, which is used to wait for the connection.
3. We there's a request, the server spend 53.75% of the time on `parse_request` function, which is used to read the request and parse the header. The time for handling the request is only 11.68%, compared with the time for parsing the request, it's much smaller. So the header parser is the bottleneck of the server.
4. If we enable the profiler, the execution time is 9.48s, but without the profiler, the execution time is 2.39s. The profiler takes 7.09s, which is 296.23% of the execution time. The overhead is huge, but it's acceptable since the profiler is used for debugging only once or twice.


## Q4

Juyi 

####  数据依赖

L2 和L1 

L4 和L2, L3 

L5 和L4 

L9 和L8控制依赖

假设不用经过ALU可以直接bypass到mem.

还假设了 floating point adder 和integer adder 可以并行. 

L3不能在L2之前IF. 取指和解码只能顺序解 ,解完以后看指令是否满足条件运行, Fetch和decode必须in order的. 先前的指令不满足条件延后执行，之后的指令满足条件先执行

同舟的是14个cycle  9个instr,  但是23个cycle有两次bnz. 到底怎么数 ipc呢? 可能要自己定义. 



an instruction fetch stage that can fetch up to two instructions in a cycle, an instruction decode that can issue up to two instructions in a cycle, 

an integer register file and a floating-point register file, each with four read ports and two write ports. 

A load-store unit can load a data item from the cache in two cycles and stores in one cycle. Assume that the integer ALU computes in one cycle, a floating-point multiplier that is pipelined over 3 stages, and a floating-point adder that is pipelined over 2 stages.
