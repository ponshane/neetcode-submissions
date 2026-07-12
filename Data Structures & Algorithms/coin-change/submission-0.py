class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {0: 0}

        for i in range(1, amount + 1):
            for coin in coins:
                subproblem = i - coin

                if subproblem < 0:
                    continue

                # We cannot build i from an unreachable subproblem.
                if subproblem not in memo:
                    continue

                candidate = memo[subproblem] + 1

                if i not in memo:
                    memo[i] = candidate
                else:
                    memo[i] = min(memo[i], candidate)

        if memo.get(amount) is None:
            return -1
        else:
            return memo.get(amount)