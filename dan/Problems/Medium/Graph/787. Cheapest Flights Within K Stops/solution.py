import heapq
class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        airlines = [dict() for _ in range(n)]
        known = [False for _ in range(n)]
        for u, v, w in flights:
            airlines[u][v] = w
        heap = []
        heapq.heappush(heap, (0, src, -1))
        while heap:
            dist, node, k = heapq.heappop(heap)
            if k <= K:
                known[node] = True
                if node == dst:
                    return dist
                for next in airlines[node]:
                    if not known[next]:
                        heapq.heappush(heap, (dist + airlines[node][next], next, k+1))
        return -1



