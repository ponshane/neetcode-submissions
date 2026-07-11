class TimeMap:

    def __init__(self):
        self.time_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # initialize an empty dict for key
        if key not in self.time_map:
            self.time_map[key] = []
    
        self.time_map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.time_map:
            return ""
        
        l = 0
        r = len(self.time_map[key]) - 1
        # if time_map is dict(dict), then the following operation creates O(n)
        # times = list(self.time_map[key].keys())
        res = ""

        while l <= r:
            m = l + (r-l)//2
            prev_timestamp = self.time_map[key][m][1]

            if prev_timestamp <= timestamp:
                res = self.time_map[key][m][0]
                l = m + 1
            else:
                r = m - 1

        return res
            
        

        
