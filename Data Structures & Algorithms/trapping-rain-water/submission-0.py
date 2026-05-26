class Solution:
    def trap(self, height: List[int]) -> int:
        level = 0
        water = 0
        idx, lid, rid = 0, 0, len(height) - 1

        while lid < rid:
            if height[lid] == 0:
                lid += 1
                idx = lid
                continue
            elif height[rid] == 0:
                rid -= 1
                idx = rid
                continue
            h = min(height[lid],height[rid])
            #print(f"calc for:{lid},{rid}, vals: {height[lid]},{height[rid]}, h:{h}")

            if level > 0:
                water -= min(level,height[idx])
                #print(f"removing water: {level}")
            if h > level:
                water += (h - level) * (rid - lid - 1)
                #print(f"adding water: {(h - level) * (rid - lid - 1)}")
                level = h

            if height[lid] > height[rid]:
                rid -= 1
                idx = rid
            else:
                lid += 1
                idx = lid
        return water