class TimeMap:

    def __init__(self):
        self.time_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # initialize an empty dict for key
        if key not in self.time_map:
            self.time_map[key] = {}
    
        self.time_map[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.time_map:
            return ""

        if timestamp in self.time_map[key]:
            return self.time_map[key][timestamp]
        
        l = 0
        r = len(self.time_map[key]) - 1
        times = list(self.time_map[key].keys())
        res = ""

        while l <= r:
            m = l + (r-l)//2
            prev_timestamp = times[m]

            if prev_timestamp <= timestamp:
                res = self.time_map[key][prev_timestamp]
                l = m + 1
            else:
                r = m - 1

        return res
            
        

        
