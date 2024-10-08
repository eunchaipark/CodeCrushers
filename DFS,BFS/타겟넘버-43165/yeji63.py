def solution(numbers, target):
    answer = 0
    # numbers = [4,1,2,1]
    # target = 4
  
    def dfs(idx, sum):
        nonlocal answer
        if idx == len(numbers):
            answer+=1 if sum==target else 0
            return answer
        
        sum1 = sum + numbers[idx]
        sum2 = sum + numbers[idx]*(-1)
        dfs(idx+1, sum1)
        dfs(idx+1, sum2)
        
    dfs(0, 0)
    
    return answer
