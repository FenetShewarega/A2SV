class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
          #lambda function to calculate distance
        distance_calculator = lambda x: ((x[0]-0)**2 + (x[1]-0)**2)**1/2
        
        # to store distances
        dist_from_origin = list(map(distance_calculator, points))
        
		# to capture sorted indexes
        sorted_index = sorted(range(len(points)), key = lambda k: dist_from_origin[k])
        sorted_points = [points[i] for i in sorted_index]
        return sorted_points[:k]