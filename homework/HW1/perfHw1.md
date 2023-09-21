



Q1:

Consider the famous qsort() algorithm for a very large dataset. What would you consider the bottleneck in the system performance to be from a qualitative viewpoint?

1. Memory, According to https://cs.stackexchange.com/questions/138335/what-is-the-space-complexity-of-quicksort,  If the pivot can be chosen adversarially, causing the worst-case space complexity to be Θ(𝑛).  Therefore, If the available memory is limited and the dataset is large, it can lead to increased disk swapping, which severely impacts performance.
2. **Cache Efficiency**: Access patterns during sorting can impact cache efficiency. Large datasets may not fit entirely in cache, leading to cache misses and slower performance.

Q2: 

The GUPS benchmark can be summarized in the following simplified code:

```cpp
          i = random(1, 1<<24);    // Generate a random integer between 0 and 1<<24
          hist[i]++;               // i and hist are of type integer
```

The L1 cache is 32KB, and the L2 cache is 2MB. How do you expect the code to perform? Would it benefit from adding another layer of caching of 16MB size?

1. The code snippet generates a random integer `i` and increments `hist[i]`, which suggests random memory accesses to the `hist` array.With random memory accesses, the L1 cache may suffer from cache misses, leading to frequent fetching of data from slower levels of memory.
2. The L2 cache is larger than the L1 cache, which can help in mitigating cache misses to some extent. However,  A integer in cpp is 4 bytes.  32k/4=8k, So when we have 8k number,  the L2 cache may also experience cache misses.
3. Thus adding another layer of caching of 16MB size would benefit. Because 1<<24 leads 2^24= ~16M possible numbers . Adding an additional layer of caching with a 16MB size could potentially benefit the code's performance. A larger cache can hold more data, reducing the likelihood of cache misses and improving memory access times.



Q4:

Write a program to generate a Poisson distribution of a mean value of *l.*





Q5

第一个任务到达的时间是0时刻, 每个服务到达的时间，和之前的那个时间对比,如果之前的没处理完，就等之前的处理完了再处理自己的





If we would like to have the average response time to be thirty milliseconds and a standard deviation of +/- 10%, estimate the number of necessary servers. Use a single queue/multiple server paradigm.

不断尝试参数? 20个可以吗? 





multiple queues with one server per queue. 
