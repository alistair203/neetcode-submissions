class StockSpanner:

    def __init__(self):
        self.price_spans = []

    def next(self, price: int) -> int:
        span = 1
        while self.price_spans and price >= self.price_spans[-1][0]:
            span += self.price_spans.pop()[1]
        self.price_spans.append((price, span))
        return span

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)