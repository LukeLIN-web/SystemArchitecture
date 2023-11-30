#### install gem5

```
scons build/X86/gem5.opt -j 16
```

trace有什么用? 







https://github.com/bhavin392/Two-Level-Cache-Simulator-with-Translation-Lookaside-Buffer-TLB-/tree/master





该分析主要针对一个且仅有一个跟踪文件 000.espresso.din 进行，并且有人认为（与一名团队成员面对面，但未书面）其他跟踪文件给出的结果没有意义。然而，任务是对所有跟踪运行模拟，并广泛了解它们的行为，以及广义上工作负载可能执行的操作如何影响性能。因此，分析结果仅局限于底层跟踪文件 008.esperesso 的原始行为。另外，开头提供了一个假设，即高速缓存行大小和高速缓存大小在很大程度上与分析无关，因为底层跟踪文件仅使用三个地址，这是一个错误的陈述，仅查看即可看出跟踪文件中的前四行。此外，即使是这种情况，作业的目标是理解/可视化/运行内存系统行为表现的模拟，而给定的假设大量忽略了这一点。 

整体分析，都是用数字总结的，包括L1和L2的命中率与缓存线大小的关系。为此涵盖了所需的所有配置。然而，几乎没有围绕这些数字进行任何分析（大多数案例不包括任何分析线，而只是一个数字）。也没有关于平均访问时间的分析、数字或报告值。也没有直接分析来比较 TLB 未命中与高速缓存未命中的影响（仅提供了不同 TLB 大小的高速缓存未命中的数据）。

对于情况2，三种缓存替换策略之间没有可比性；这只是 FIFO 案例中的一行分析提供的数字。案例3本来是要分析集合关联数之间的比较，但对于任何案例都没有提供任何分析，只是给出了数字。通过对观察到的行为提供的分析，以下陈述的正确性尚不清楚，并且没有有效的论据“我们可以发现 TLB 条目增加，L1 命中减少，这是因为 L1 命中经常进行页表遍历，因此 TLB 条目增加，页面行走减少，因此 L1 命中减少。” 以及“我们可以发现TLB条目增加，L1命中减少”的陈述。

另外，没有任何分析可以辅助这样的说法：“从上图可以看出，Line size=32Bytes，TLB=16个entry，L2命中率几乎为零”。在使用直接映射的情况 3 中，这在某些方面是直接映射的预期行为，但问题是为什么在相同数字后面使用较小的 TLB 时情况并非如此？另一方面，模拟器的构建受到赞赏，并且在图中紧凑地暴露大量配置的方式做得很好。 

总的来说，只构建了模拟器，并给出了数据，但几乎没有提供分析（这是硬件的目标，因为任何工具都可以用来执行模拟），并且一开始就给出了严重违反的假设同时只处理一个且仅一个跟踪文件。

Your grade for the HW4 submission is 50/100.



Below, you will find comments for your submission. Please review them and reach out in case you have any questions. For any rebuttal, please reach out before Monday 5 pm. Any rebuttal request after Monday will not be guaranteed to be held.



**//Comments start**

The analysis was done primarily on one and only one trace file, 000.espresso.din, and it was argued (in person with one team member, but not written) that the other trace files gave results that did not make sense. However, the task was to run the simulation over all the traces and have a broad look at their behaviour, and how performance would be affected by operations a workload may perform in a broad sense. For this reason, the analysis results are only restrictive to what the primitive behaviour of the underlying trace file 008.esperesso is. In addition, an assumption was provided by the beginning stating that the cache line size and cache size are largely irrelevant factors to the analysis since the underlying trace file only uses three addresses, which is a wrong statement, as could be seen by only looking at the first four lines in the trace file. In addition, even if this is the case, the goal of the assignment is to understand/visualise/run a simulation where the behaviour of the memory system manifests, which is heavily omitted by the given assumption. 



Regarding the overall analysis, it was all summarised in figures that include the hit rate of L1 and L2 in relation to the cache line size. All the configurations required were covered for that. However, nearly no analysis was done around those figures (most of the cases do not include any line of analysis and it is just a figure). There is also no analysis, figure, or reported value whatsoever of the average access time. There is also no direct analysis that compares the effect of a TLB miss compared to the cache miss (it is just the figures for the cache misses with different TLB sizes that were provided).



For case 2, there is no comparison between the three cache replacement policies; it was just figures provided with one line of analysis in the FIFO case isolatedly. Case 3 is supposed to analyse the comparison between the number of set associativity, whereas there was no analysis provided at all regarding any of the cases, and just figures were given. Going through the provided analysis of the observed behaviour, the correctness of the following statements is unclear and have no valid argument "We can find TLB entries incerase, L1 hit decrease, this is because L1 hit often doing page table walk, so TLB entries increase, page walk decrease, so L1 hit decrease." and the statement "We can find TLB entries incerase, L1 hit decrease.".



In addition, there is no analysis that assists the statement," From the figure above, we can see Line size =32 Bytes, TLB = 16 entries, L2 hits nearly zero." in case 3 with direct mapping, which is the expected behaviour for direct mapping in some ways but the question is why is it not the case with a smaller TLB following the same figure? _On the other hand, the simulator building is appreciated, and the way of compactly exposing a large number of configurations in figures is well done. 



Overall, only the simulator was built, and figures were given, but nearly no analysis was provided (which is the goal of the HW as any tool could have been used to perform the simulations), and a heavily violated assumption was given in the beginning while only handling one and only one trace file.
