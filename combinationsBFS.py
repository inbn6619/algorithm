from collections import deque

def combinations_bfs(iterable, r):
    queue = deque([(i,) for i in iterable])
    
    while queue:
        current_combination = queue.popleft()
        
        if len(current_combination) == r:
            yield current_combination
        else:
            last_index = current_combination[-1] if current_combination else 0
            for i in range(last_index, len(iterable)):
                new_combination = current_combination + (i,)
                queue.append(new_combination)

# 예시 사용
my_string = "abcd"
result = list(combinations_bfs(my_string, 2))

print(result)

# O(n*r!) // 내가 짯던 코드 BFS == O(n!)

# def makeStringByStrElements(string, length):
#     from collections import deque
    
#     deq = deque(i for i in string)

#     checkSet = set()

#     while deq:
#         target = deq.popleft()

#         if len(target) > length:
#             break
        
#         for s in string:
#             if s not in target:
#                 t = target + s
#                 t = ''.join(sorted(list(t)))
#                 deq.append(t)
#                 if len(t) == length:
#                     checkSet.add(t)
        
#     return list(checkSet)