



Your grade for the HW1 submission is 79.5/100.



Below, you will find comments for each question. Please review them and reach out in case you have any questions. For any rebuttal, please reach out before Thursday 5 pm. Any rebuttal request after Thursday will not be guaranteed to be held.



**//START OF COMMENTS**

Q1 7.5/10: The quoted argument from the StackExchange thread is not explained and taken as is. It does not contribute to the explanation given afterwards regarding the problem of having the main memory unable to accommodate the whole dataset and, therefore, the need for swapping from the disk. However, the swapping problem is correct and explained. The cache problem is correct but not well explained. There is no explanation indicating why specifically the cache size would be a problem only when the dataset is large (which is the case when the algorithm chooses to access a location far enough from those who are already in the cache). The problem of stacking an enormous number of recursion states, given the recursion nature of the qsort algorithm, is missing.



Q2 2/15: Your solution is valid only if we assume that first of all, the data is already in the cache levels, including the added L3, and second, that it is distributed in a manner that the random index will uniformly choose from one of the 16MB. However, this benchmark randomly accesses a data point from a large array (here of integers), and even by adding an L3, the chances to sample an element randomly from one of the previous cached lines is still low as randomly picking an element from 0 to 1 << 24 will almost always surely going to access an element far from the previously fetched ones in a sense that the locality buys us nothing.



Q3 5/5: Correct.



Q4 10/10: Correct.



Q5-a 5/5: Correct.



Q5-b 7/9: You have not segregated the measurements for the two types of requests. The rest is correct and clear.



Q5-c 9/9: Correct.



Q5-d 9/9: Correct.



Q5-e 6/9: You have not provided any explanation whatsoever and just gave the average response time and the std deviation time.



Q5-f 9/9: Correct.



Q5-g 10/10: Fair enough.

***//END OF COMMENTS\***



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
