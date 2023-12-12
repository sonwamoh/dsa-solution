class Solution:
    def totalMoney(self, n: int) -> int:
        """
        1 2 3 4 5 6 7 | 2 3 4 5 6 7 8 | 3 4 5 6 7 8 9 | 4 5 6 7 8 9 10
        28              35              42              49
        """
        div = n // 7
        if div == 0:
            return (n*(n+1))//2
        money = 0
        mod = n % 7
        start = div + 1
        for i in range(mod):
            money += start
            start += 1
        
        for i in range(div):
            money += (i + 4) * 7
        
        return money
        

        
        
        





        