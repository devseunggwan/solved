from collections import Counter
    
def solution(a, b, c, d):
    nums = Counter([a, b, c, d])
    
    if len(nums) == 4:
        return min([a, b, c, d])
    if len(nums) == 3:
        q, r = [key for key, value in nums.items() if value == 1] 
        return q * r
    if len(nums) == 2:
        p, q = [item[0] for item in sorted(nums.items(), key=lambda x: x[1], reverse=True)]
        return (p + q) * abs(p-q) if nums[p] == 2 else ((10 * p) + q) ** 2
    if len(nums) == 1:
        return 1111 * a
    

        