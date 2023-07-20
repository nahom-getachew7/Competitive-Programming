class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        collide = [asteroids[0]]
        i= False
        j= 1
        while j < len(asteroids):
            while collide and collide[-1] > 0 and asteroids[j] < 0:
                if collide[-1] < abs(asteroids[j]):
                    collide.pop()
                elif collide[-1] == abs(asteroids[j]):
                    collide.pop()
                    i = True
                    break
                else:
                    i = True
                    break
                        
            if not i:
                collide.append(asteroids[j])
            i= False
            j += 1
        return collide