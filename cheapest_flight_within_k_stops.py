from collections import defaultdict
import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = collections.defaultdict(list)
        pq = []
        for u, v, w in flights: graph[u].append((w, v))
        heapq.heappush(pq, (0, K+1, src))
        while pq:
            price, stops, city = heapq.heappop(pq)
            if city is dst: return price
            if stops>0:
                for price_to_nei, nei in graph[city]:
                    heapq.heappush(pq, (price+price_to_nei, stops-1, nei))
        return -1