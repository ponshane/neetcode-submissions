class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        mem = {0: 0}

        for i in range(1, amount + 1):
            for coin in coins:
                sub_amount = i - coin

                if sub_amount < 0:
                    continue # move to next coin
                
                if sub_amount not in mem:
                    continue

                candidate = mem[sub_amount] + 1 # use the current coin so + 1

                if i not in mem:
                    mem[i] = candidate
                else:
                    mem[i] = min(mem[i], candidate)
        
        return mem.get(amount, -1)