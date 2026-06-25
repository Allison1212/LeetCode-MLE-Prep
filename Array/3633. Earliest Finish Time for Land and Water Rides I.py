class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        land_end = [999]*len(landStartTime)
        water_end = [999]*len(waterStartTime)
        new_land_end = [999]*len(landStartTime)
        new_water_end = [999]*len(waterStartTime)
        # Land start 
        for i in range(0,len(land_end)):
            land_end[i] = landStartTime[i] + landDuration[i]
        min_land_end = min(land_end)
        new_water_start = [max(min_land_end,i) for i in waterStartTime]

        for i in range(0,len(water_end)):
            new_water_end[i] = new_water_start[i] + waterDuration[i]
        print(new_water_end)

        # Water start 

        for i in range(0,len(water_end)):
            water_end[i] = waterStartTime[i] + waterDuration[i]
        min_water_end = min(water_end)
        new_land_start = [max(min_water_end,i) for i in landStartTime]

        for i in range(0,len(land_end)):
            new_land_end[i] = new_land_start[i] + landDuration[i]

        return (min(min(new_water_end),min(new_land_end)))
