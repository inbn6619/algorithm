def solution(new_id):
    import re
    
    sqecial_characters = r"~!@#$%^&*()=+[{]}:?,<>/"
    
    pattern = "[" + re.escape(sqecial_characters) + "]"
        
    answer = ''
    
    lowerId = new_id.lower()
        
    reId = re.sub(pattern, "", lowerId)
        
    reDotId = re.sub(re.escape(".") + r"{2,}", ".", reId)
        
    removedDotFrontBack = re.sub(r"^\.*|\.*$", "", reDotId)
        
    if not removedDotFrontBack:
        removedDotFrontBack = "a"
    Id = removedDotFrontBack[:15]
    
    answer = re.sub(r"\.*$", "", Id)
    
    while len(answer) <= 2:
        answer += answer[-1]
    
    
    return answer