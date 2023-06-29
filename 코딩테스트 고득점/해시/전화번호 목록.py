def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
                answer = False
                break

    return answer


book1 = ["119", "97674223", "1195524421"]
book2 = ["123","456","789"]
book3 = ["12","123","1235","567","88"]

print(solution(book1))
print(solution(book2))
print(solution(book3))