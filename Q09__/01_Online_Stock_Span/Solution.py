class StockSpanner:

    def __init__(self):
        self.stackNum = []
        self.stackCnt = []

    def next(self, price: int) -> int:
        if len(self.stackNum) == 0:
            self.stackNum.append( price )
            self.stackCnt.append( 1 )
            return 1
        else:
            outNum = 0
            while True:
                if len(self.stackNum) == 0:
                    self.stackNum.append( price )
                    self.stackCnt.append( outNum + 1 )
                    break
                else:
                    if self.stackNum[-1] <= price:
                        self.stackNum.pop()
                        outNum += self.stackCnt.pop()
                    else:
                        self.stackNum.append( price )
                        self.stackCnt.append( outNum + 1 )
                        break
            return outNum + 1


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)