class Solution:
    def trap(self, height: list[int]) -> int:
        import heapq

        # initial thought: keep track of peak, end
        # need to go peak to peak
        # if I find a peak higher than the first, pool is over
        # can start new pool


        # if height ascends, potential area added but only if matching descent exists
        # therefore, must record previous descents
        # dict with format id: [height, filled]
        descents = {}
        d_heap = []
        heapq.heapify(d_heap)

        # each descent has index, height, and amount filled
        # ascent also has index, height
        # ascents apply to all open descents where a-height >= d-filled
        # total area increases by min(d-height - d-filled, a-height - d-filled) * (a-index - d-index)
        # close descent if a-height > d-height, otherwise d-filled = a-height

        total = 0
        last_height = 0

        # potential optimization: pre-filter to only check descents with lower fill than height
        # would need to sort descents by filled
        # minheap of lowest filled descents?

        # populate descents
        for i, h in enumerate(height):

            if h < last_height: # descent. amount filled starts new height
                descents[i] = [last_height, h]
                heapq.heappush(d_heap, (h, i)) # update heap with (filled, index)
            
            # handle ascent? attempt to fill all open descents
            else:
                while d_heap:
                    d_id = d_heap[0][1]
                    data = descents[d_id]

                    d_height = data[0]
                    d_filled = data[1]

                    if h > d_filled: # updateable
                        heapq.heappop(d_heap)
                        total += min(d_height - d_filled, h - d_filled) * (i - d_id)

                        if h >= d_height: 
                            descents.pop(d_id)
                        else: # update filled
                            descents[d_id][1] = h
                            heapq.heappush(d_heap, (h, d_id))
                    else:
                        break

            last_height = h
        return total
        