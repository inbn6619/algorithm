def solution(numbers, hand):
    answer = ''
    
    leftHand = [9 // 3, 9 % 3]
    rightHand = [11 // 3, 11 % 3]
    
    check = ''
    
    for num in numbers:
        num -= 1
        
        if num in [0, 3, 6]:
            check = 'L'
            
        elif num in [2, 5, 8]:
            check = 'R'
        else:
            if num == -1:
                num = 10
            target = [num // 3, num % 3]

            
            print(num+1, target, rightHand, leftHand)
        
                
            rightDistance = sum([abs(target[0] - rightHand[0]), abs(target[1] - rightHand[1])])
            leftDistance = sum([abs(target[0] - leftHand[0]), abs(target[1] - leftHand[1])])

            
            if rightDistance == leftDistance:
                if hand == "right":
                    check = "R"
                else:
                    check = "L"
            elif rightDistance > leftDistance:
                check = "L"
            else:
                check = "R"
                
        if check == "R":
            rightHand = [num//3, num % 3]
        else:
            leftHand = [num//3, num % 3]
            
        answer += check

    return answer

# LRLLLRLLLRR
# LRLLRRLLLRR