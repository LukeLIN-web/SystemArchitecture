# How scoreboard works

**Scoreboard** is a centralized method, first used in the [CDC 6600](https://en.wikipedia.org/wiki/CDC_6600) computer, for dynamically scheduling instructions so that they can execute out of order when there are no conflicts and the hardware is available.

CDC6600 maintains a scoreboard, which is actually a store unit. 

It stores **Functional Unit Status**, like the following

1. Busy: Indicates whether the unit is being used or not
2. Op: Operation to perform in the unit (e.g., MUL, DIV, or MOD)
3. Fi: Destination register
4. Fj, Fk: Source-register numbers
5. Qj, Qk: Functional units that will produce the source registers Fj, Fk, such as integer/mult1.
6. Rj, Rk: Flags that indicate when Fj, Fk are ready for and are not yet read.

It stores **Register Status**: Indicates, for each register, which function unit will write results into it.

### **Issue**

Decode the instructions and observe the scoreboard information. The main focus is on observing the status of various functional units and registers in the scoreboard to determine whether the decoded information can be stored in the corresponding unit registers.

**If the corresponding functional unit is available** and **there are no pending writes to the target register the instruction needs to write** (to resolve WAW hazards), then at the end of this stage, the instruction's information can be stored in the register. Simultaneously, the scoreboard is updated with the instruction-related information.

### Operand Fetch

Inspect the scoreboard to understand which register values the current instruction requires, whether these values are ready, and, if not, whether any functional unit is computing them. If the values are not ready (to resolve RAW hazards), the instruction remains in the unit's register, unable to fetch the data.

If all registers are readable, then at the end of this stage, the corresponding register values will be stored in the operand registers. It's important to note that the scoreboard is not modified at this point.

### Execution

Execute the computation process, which may span multiple cycles.

At the end of the first cycle, the content of the scoreboard's read registers (i.e., Rj and Rk) is modified to indicate that the instruction no longer needs to read from registers. At the end of the cycle, when the result is obtained, it is stored in the result register.

### Write Back

At this point, you need to examine the scoreboard. **If no other instruction requires reading the register where the current computation result is about to be written** (to resolve WAR hazards, you need to inspect all Rj and Rk; if the related registers have "Yes" for Rj and Rk, it means some instruction needs to read the register about to be written to, and therefore, you must wait for the preceding instruction to read the register before writing back), then at the end of the cycle, the result is written back to the register file. Simultaneously, the corresponding entry in the scoreboard (such as Integer or mult1) is cleared, indicating that the register has been written and is no longer in a state of "about to be written by the ALU."

### Summary

1. Whether an instruction can be dispatched depends on the availability of functional units, which is indicated in the **functional status**. It also depends on whether the target register to be written by the instruction is about to be written by another instruction, as indicated in the register status. Observing this information is essential to resolve WAW hazards.
2. Whether an instruction can fetch operands depends on whether the scoreboard indicates that the **source registers are not readable**. If they are not readable, it means that the register is about to be modified by a preceding instruction, and the current instruction must wait for the preceding instruction to write back. This observation is crucial for resolving RAW hazards.
3. Once an instruction has completed operand fetch, it can proceed with execution. Execution may span multiple cycles. At the end of the first cycle, the functional status should be updated to indicate that the instruction no longer needs to be read from registers.
4. Whether an instruction can write back depends on whether there are instructions that need to read the register that the current instruction is about to modify. Specifically, it involves observing whether the registers marked "Yes" for Rj and Rk contain the destination register of the current instruction. If they do, it means there are instructions that need to read the old value of the register. In this case, the instruction must wait for these instructions to read the old value before writing back. This observation is crucial for resolving WAR hazards.

### Advantages

It achieves out-of-order instruction execution, resolving data hazards that may occur during out-of-order execution. It implements instruction execution in a dataflow manner, meaning that instructions start execution as soon as their operands are ready, which is different from the control-driven execution in traditional five-stage pipelines. Moreover, it is relatively straightforward to implement.

### Disadvantages

However, the scoreboard algorithm can still encounter blocking due to WAR and WAW hazards. Once blocking occurs, subsequent instructions of the same type cannot be dispatched (during out-of-order execution, the scoreboard dictates that only one instruction of the same type path can exist at a time). Suppose subsequent instructions of the same type cannot be dispatched. In that case, it can have a significant impact on performance, as even instructions that could be executed immediately further down the line may be blocked. 

Furthermore, the scoreboard algorithm does not guarantee sequential completion of instructions (i.e., it doesn't write back in order), which can present challenges for program debugging.

## Tomasulo’s algorithm

### Background

The Scoreboard algorithm is an excellent out-of-order execution algorithm. However, the Scoreboard algorithm itself has some significant drawbacks. Therefore, after IBM introduced the Tomasulo algorithm, the industry generally favored the Tomasulo algorithm.

In the Scoreboard,  if a path is occupied and another instruction for the same path arrives in the instruction stream, that instruction cannot be dispatched to the path, leading to instruction dispatch stagnation and instruction flow interruption. This significantly affects processor performance.

Furthermore, the Scoreboard, in order to handle out-of-order instruction execution, may unnecessarily stall the pipeline when dealing with write-after-write and read-after-write hazards. It does not fully exploit the out-of-order potential of instructions. 

Moreover, the "write-back" operation in the Scoreboard is out of order, which is not favorable for the processor's handling of interrupt exceptions and is also challenging for programmers during program debugging.

### rethink data hazard

#### WAW hazards

If both the first and third instructions need to be written to register R3, they incur a "write-after-write" (WAW) hazard.For example, the subsequent AND instruction cannot be dispatched due to the "write-after-write" hazard with the ADD instruction, causing a pipeline stall during the dispatch phase.

**However, if the destination register of the AND instruction is changed to R10, the hazard is eliminated**, and the AND instruction can be dispatched.

#### WAR Hazards

The first and second instructions encounter a "read-after-write" (RAW) hazard regarding register R3. In the scoreboard, when this situation occurs, the second instruction, during the write-back stage, detects that the first instruction needs to read the old value of R3. As a result, the second instruction stalls in the write-back stage until the first instruction has completed reading R3 and notifies the second instruction.

**If the second instruction changes R3 to R10, the hazard is resolved**, and the first instruction can read R3 while the updated result of the second instruction is stored in R10 without overwriting the old value of R3.

However, **"read after write" (RAW) hazards cannot be resolved** because subsequent instructions read data calculated by preceding instructions. This process involves an explicit data dependency.

The crucial difference among these three hazards lies in "**data dependency**." WAR and WAW can be eliminated by changing the register names, indicating that these two hazards do not involve actual data dependency. In practice, the ultimate goal of program instructions is computation. If you can access all the computed results at any time, where those results are stored becomes less critical.

WAW hazard is a typical case where two instructions write to the same register. What the processor needs is the computed results of these two instructions. 

**In summary, WAW and WAR hazards are not genuine hazards, and there's no need to block the instruction flow because of them**. This is why the scoreboard does not fully exploit the out-of-order potential of instructions.

### Register Renaming

**The primary method for eliminating false data dependencies is register renaming**. In addition to the logical registers (the MIPS instruction set specifies 32 logical registers), there is an extra set of physical registers. If a logical register is about to be written or read, its Busy bit is set to 1, and the Tag indicates which physical register will receive the latest data. Using this method, we can write back immediately when new data is computed. It also allows preceding instructions to read the old value from the logical register (since the old value hasn't been overwritten and still exists in the logical register).

**The essence of register renaming: when a WAW hazard occurs, find a new register to store the new value; when a WAR hazard occurs, also find a new register to store the new value**. Tomasulo handles these two hazards as follows: in the case of WAW hazards, it always writes the latest value into the register. It does not write the slightly older value into the register. Instead, it broadcasts it. If an instruction needs this slightly older value, it can receive the data through broadcasting. 

As for WAR? Note that Tomasulo's algorithm does not encounter WAR hazards because once an instruction is dispatched, it **copies the data it can read**. Once the data is copied, whether the source register has been overwritten is irrelevant to that instruction.

### Tomasulo Architecture

- FP OP Queue, which is the floating-point instruction queue where instructions wait for dispatch.
- Reservation stations for the addition and multiplication units (reservation stations store information about instructions that have been dispatched and buffer incoming data).
- The Address Unit calculates storage addresses before execution.
- The Memory Unit handles storage operations.
- CDB (common data bus), which can directly reach the register file (used for updating general-purpose registers) and the reservation stations for the addition and multiplication units (it transmits data required by instructions in the reservation stations).

#### reservation station

The reservation station is a new structure introduced by the Tomasulo algorithm. It is somewhat similar to the decode information pipeline stage register in the scoreboard. However, the Tomasulo algorithm provides **a set of buffers for each reservation station**. For instance, the floating-point addition unit has reservation stations that can **buffer three instructions**. 

**A buffer is reserved for each reservation station, allowing instructions to be dispatched to the buffer of the reservation station while the addition unit is busy**.

Reservation stations directly buffer the read data, unlike the scoreboard, which only records a register number. Just recording the register number can cause WAR blocking because an instruction continuously monitors its source register before it is officially executed, and the value of the source register cannot change. Consequently, subsequent instructions cannot be written back and can only block the pipeline. 

**Reservation stations adhere to the idea that "once data is ready, execute the instruction immediately." When an instruction finds data to be read, it immediately reads it, and the write or not write to that source register becomes irrelevant**.

Both the scoreboard and reservation stations record Qj and Qk, meaning that as soon as the required data is calculated, it is captured through Qj and Qk broadcast data. **This approach essentially involves renaming, using reservation station numbers rather than register numbers to label data sources**.

#### Issue

**The Tomasulo algorithm dispatches instructions in order**, meaning instructions are dispatched to the reservation stations one after another in the order they appear in the program. **The sole criterion for determining whether an instruction can be dispatched is whether there is space available in the corresponding reservation station**. As long as the reservation station has space available, the instruction can be dispatched to the reservation station.

### Summary

- Whether an instruction can be dispatched depends on whether there is space available in the corresponding reservation station. **As long as there is space available, the instruction can be dispatched to the reservation station and wait for execution. At the time of dispatch, any data that can be read is directly copied to the reservation station**. This eliminates the need to consider WAR hazards. Subsequent instructions can be written back as soon as they are completed without concern for whether preceding instructions need to be read from the register. In other words, every instruction dispatched to the reservation station no longer needs to be read from the register file.
- When an instruction is dispatched, the register status table is updated. If the destination register of a subsequent instruction coincides with that of a preceding instruction, **only the result of the subsequent instruction should be written into the register**. This solves WAW hazards.
- If an instruction is currently being executed in an execution unit, other instructions wait in the reservation station. **If an instruction lacks source data, it remains in the reservation station, constantly monitoring the CDB bus**. If the CDB bus broadcasts the required data, it is immediately copied, and the instruction is then prepared for execution.
