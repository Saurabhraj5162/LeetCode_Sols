class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
#         ld = []
#         if n > 1:
#             for i in range(n-1,0,-1):

#                 cmax = prices[i] - prices[i-1]
#                 for j in range(i-1,-1,-1):
#                     cmax = max(cmax, (prices[i]-prices[j]))
#                 ld.append(cmax)

#             profit = max(ld)
#         else:
#             profit = 0

        if n>1 :
            pmin = [0]*n
            smax = [0]*n
            pmin[0] = prices[0]
            smax[n-1] = prices[n-1]

            for i in range(1,n):
                
                pmin[i] = min(prices[i],pmin[i-1])

            for i in range(n-2,-1,-1):
                smax[i] = max(prices[i],smax[i+1])

            profit = smax[0] - pmin[0]
            for j in range(1,n):
                if ((smax[j] - pmin[j]) > profit):
                    profit = smax[j] - pmin[j]
            print(pmin)
            print(smax)
        
        else:
            profit = 0
            
        if profit>0:
            return profit
        else:
            return 0
       
