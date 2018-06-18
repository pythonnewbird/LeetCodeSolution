class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        start=sums=0
        for i in range(len(gas)):
            sums+=gas[i]-cost[i]
            if sums<0:
                sums,start=0,i+1
        return start if sum(gas)>=sum(cost) else -1

结论1：若从加油站A出发，恰好无法到达加油站C（只能到达C的前一站）。则A与C之间的任何一个加油站B均无法到达C。

结论1的证明：反证法

假设从加油站A出发恰好无法到达加油站C，但是A与C之间存在加油站B，从B出发可以到达C。

而又因为从A出发可以到达B，所以A到B的油量收益（储油量 - 耗油量）为正值，进而可以到达C。

推出矛盾，假设不成立。
结论2：若储油量总和sum(gas) >= 耗油量总和sum(cost)，则问题一定有解。

结论2的证明：反证法

假设sum(gas) >= sum(cost)时，从环形内任意加油站出发，均无法走完一圈。

则从任意加油站A出发绕行一圈返回A之前，油量增益减为负值，假设恰好无法到达加油站B。

亦即：sum(gas[A~B]) < sum(cost[A~B])

而又因为加油站B出发绕行一圈返回B之前，油量增益减为负值，假设恰好无法到达加油站C。

亦即：sum(gas[B~C]) < sum(cost[B~C])

以此类推，最终将进入循环，假设循环的起点为P，中间点为M1, M2 ... Mk

则有：

储油量总和：sum(gas[P~M1] + ... + gas[Mk ~ P]) = c * sum(gas)

耗油量总和：sum(cost[P~M1] + ... + cost[Mk ~ P]) = c * sum(cost)

亦即：

c * sum(gas) < c * sum(cost) 等价于 sum(gas) < sum(cost)

推出矛盾，假设不成立。