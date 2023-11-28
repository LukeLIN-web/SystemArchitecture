## Question	1

​	(5	points)		Consider	the	following	code:			

```cpp
{		 double	array[2^20];		 
array[0]	=	(double)	0;		
array[1]	=	(double)	1;	
for(i	=	0;	i	<	2^20	–	3;	i++)				
array[i	+2]	=	array[i]	+	array[i	+	1];	
}		
```

a. If	the	cache	line	size	is	64	bytes,	estimate	the	hit	ratio	at	the	data	L1	cache.	Assume	a	cold	start.	State	your	assumptions	clearly.

### Assumption

1.  neighbor array number is  contiguous in memory.
2. replacement policy is FIFO
3. we use Write Through,simultaneously updated to cache and memory

each double type is 8 bytes.

**Cold Start Assumption**: This means that at the start, the cache is empty, so the initial accesses will be cache misses. Array[0] miss, load  64bytes, so the cache has 8 double numbers.

array[1] , hit

Array[2], calculated.

Array[1], hit

 Array[2],hit 

array[3], calculated.

....   23, 34, 45,56,67,  ten hits

array[8], calculated.

now we want to store array[8], we need to evict the array[0],  and assume we clear the cache line.

Array[7], miss

array[8], hit.

then repeat the first cycle.

Therefore ,the hit rate is  13/14=0.928571428571







## **Question 2 (5 points)**

a. For problem 1, assume a page size of 4KB and a fully associative data TLB with 8 entries. Compute the TLB hit ratio. State your assumptions clearly.

Total number of pages required for the array: 8 bytes * 2^20 / 4KB =   2^23/ 2^12 =  2^11

### Assumption

1. **Cold Start**: Initially, the TLB is empty, so the first few accesses will definitely be TLB misses.
2. For simplicity, we'll assume that once a page is loaded into the TLB, it stays there as long as needed
3. replacement policy is FIFO

since there are more pages  2048 than the TLB can hold (8), each new page accessed beyond the first 8 will replace an existing entry in the TLB.

because we are doing **Subsequent Accesses**: Beyond the first 8 pages, each new page access is likely a miss, as it replaces an existing entry in the TLB.

Therefore, TLB hit rate =  0%

page[0] miss 

page[1] , miss

page[2] , miss

错了 !  这个程序是一个page访问几百下, TLB是hit rate是99%接近1001.5k hit 1 miss



答案:

 (3*511 +2  )/3/ 512 

b. If the page table consists of a 6-level page table, would this change the answer to question 1? If so, how? If not, why?

No, The TLB is a cache that stores recent translations from virtual to physical memory addresses. It serves to speed up this translation process. A TLB hit occurs when the translation for a given virtual address is already in the TLB, regardless of how deep or complex the page table structure is. The TLB hit ratio is primarily a function of the access pattern to the data (in this case, sequential access to the elements of an array) and the TLB's characteristics (size, associativity). Whether the underlying page table is 1-level or 6-level, the pattern of memory accesses (and thus TLB accesses) remains the same.

6次memory load, 512 op出现一次, 不会有很大的变化.



### **Question 3 (5 points)**

Consider a system where the base address of the page table is stored in a privileged register. The page table is a 6-level tree structured page table. When the operating system runs a user process, it loads the register with the starting address of the process. Loading and setting the value in the register are two privileged instructions that run only when the processor is in supervisor mode (the mode that allows access to privileged instructions). Now, it is desired to run a virtualized environment with a hypervisor and several operating systems. Answer the following questions:

1 Is the value in the register described above a virtual address or a real one? Justify your answer.

#### Ans

It should be a real address.

Firstly, because page table is used by MMU for translating virtual daddress, if base address is a virtual address, it is difficult to translate it to physical address because we create a circular dependency.

Secondly, User processes typically cannot directly modify real address, so the value  in the register  would have security and integrity.

Thirdly, by storing the physical base address of each guest OS's page table, the hypervisor can ensure proper isolation and manage the memory resources among different virtual machines.

2 How can the hypervisor allow multiple operating systems to run on the system? How can it organize access to the privileged register? Assume no hardware change is possible.

答案: 触发异常, 

#### Answer

#### **Virtualization of the Privileged Register**

The hypervisor can create virtualized instances of the privileged register for each guest OS. Each OS believes it has control over the actual register, but in reality, it's interacting with a virtualized version managed by the hypervisor. When an OS tries to load a value into this register, the hypervisor intercepts this operation. The hypervisor then maps this virtualized register's value to a location in a real page table that it maintains for the virtual machine (VM).

#### **Context Switching Between VMs**

When switching from one VM to another, the hypervisor saves the current state of the VM, including the value of its virtualized privileged register. Before running a different VM, the hypervisor restores its state, including setting the real privileged register to point to the base of the page table for the next VM.

#### **Managing Memory Translations**

The hypervisor maintains a separate page table for each VM, effectively mapping the VM's virtual addresses to the machine's physical addresses. This allows each OS to have its own isolated virtual memory space while sharing the same physical hardware.

#### **Handling Privileged Instructions**

The hypervisor must handle every privileged instructions, like accessing or modifying the priviledged register, as these cannot be executed directly by the guest OSes.

The hypervisor can use binary translation or paravirtualization. In binary translation, the hypervisor translate privileged instructions into a sequence of safe instructions. In paravirtualization, the guest OS is modified to call hypervisor functions for privileged operations.

## **Question 4 (5 points)**

You have been tasked to design *a system* that works well for both cloud workloads and high-performance computing workloads. The processor chip you have is contains eight core, where each core is multithreaded among four symmetric hardware threads (symmetric hardware threads are identical threads in terms of priority and access to the processor resources). Each thread has a direct-mapped instruction and data L1 caches, whereas they share the L2 cache which is 4-way set- associative.

The cloud workloads consist of threads that run independently and belong to different contexts (or processes). The HPC workloads consists of threads that run cooperatively and belong to a single context (or a process).

For cloud workloads, we would like to get a level of performance isolation between the threads, whereas in HPC workloads we would like the threads to cooperate. How would you solve this problem?

#### Ans:

#### Resource allocation

For cloud workloads, allocate separate cores or hardware threads to different processes to ensure isolation. This minimizes interference and contention for shared resources like the L2 cache.

For HPC workloads, allow threads from the same process to share cores or cluster them on adjacent cores to facilitate cooperation and efficient cache utilization.

make full use of shared L2 cache for HPC workloads. Since L2 is 4-way set-associative, it can efficiently handle cache lines used by multiple threads from the same context. This setup can improve data sharing and reduce memory latency for HPC workloads.

#### **Scheduling Policies**

For cloud workloads, the scheduler should prioritize context switching and load balancing across different cores to maintain performance isolation.

For HPC workloads, the scheduler should keep threads of the same process on the same or nearby cores to enhance data sharing and reduce synchronization overhead. consider dynamic prioritization based on the workload characteristics, like dependency among threads or critical sections, to optimize performance.

#### **Memory Management**

Implement efficient memory management techniques that cater to the specific needs of each workload type

For cloud workloads, ensure that memory allocation minimizes contention and cross-process interference

For HPC workloads, optimize memory allocation to facilitate data sharing and reduce memory access times

