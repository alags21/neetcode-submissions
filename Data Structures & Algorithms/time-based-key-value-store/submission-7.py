class TimeMap:

    def __init__(self):
        self.timestamps = {} # object : {timestamp : state}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timestamps:
            self.timestamps[key] = []
        self.timestamps[key].append([timestamp, value])
        

    def get(self, key: str, timestamp: int) -> str:
        curr_max = -1
        curr_state = ""
        if key not in self.timestamps:
            return ""
        L=0
        R = len(self.timestamps[key]) - 1
        while (L <= R):
            mid = (L+R) // 2
            t, s = self.timestamps[key][mid]
            if (t > timestamp):
                R = mid - 1
            else:
                if t > curr_max:
                    curr_max = t
                    curr_state = s
                L = mid + 1
        return curr_state
