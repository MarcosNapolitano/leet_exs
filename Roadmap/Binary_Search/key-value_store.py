class TimeMap:

    def __init__(self):
        self.dict = {}

    def set(self, key: str, value: str, timestamp: int) -> None:

        try:
            self.dict[key].append((value,timestamp))  
            
        except:
            self.dict[key] = [(value, timestamp)]
        

    def get(self, key: str, timestamp: int) -> str:

        try:
            arr = self.dict[key]

            length = len(arr)

            if length == 1:
                return arr[0][0]

            l, r = 0, length-1

            while l<r:

                mid_point = (r-l)//2

                if arr[l][1] == timestamp: return arr[l][0]
                if arr[r][1] == timestamp: return arr[r][0]

                if not mid_point:
                    break

                if arr[l+mid_point][1] == timestamp: return arr[mid_point+l][0]

                if arr[l+mid_point][1] < timestamp:
                    l+=mid_point
                else:
                    r-=mid_point


            if arr[r][1]> timestamp > arr[l][1]:
                return arr[l][0]
            elif timestamp > arr[r][1]:
                return arr[r][0]
            else:
                return ""

            
        except:
            return ""
        


# Your TimeMap object will be instantiated and called as such:
obj = TimeMap()
obj.set("love","high",10)
obj.set("love","low",20)
print(obj.get("love",5))
print(obj.get("love",10))
print(obj.get("love",15))
print(obj.get("love",20))
print(obj.get("love",25))


#tengo que devolver el valor con el timestamp mas alto ej ("Hola",1), ("chau",4) si pregunto por menos de 4 tengo que devolver hola y si pregunto x mas de 4 es chau