ln = len(nums)
    if ln < 4:
        return []
    
    nums.sort()
    ans = set()
    for i in range(ln-3):
        
        if i>0 and nums[i-1]==nums[i]:
            continue
        
        ctarget1 = target - nums[i]
        for j in range(i+1,ln-2):
            if j > i+1 and nums[j-1]==nums[j]:
                    continue
            t = {}
            for k in range(j+1,ln):
                    ctarget2 = ctarget1-nums[j]-nums[k]
                    if nums[k] in t:
                        elem = (nums[i],nums[j],ctarget2,nums[k])
                        ans.add(elem)
                    else:
                        t[ctarget2] = 1
                        
    return sorted(list(ans))