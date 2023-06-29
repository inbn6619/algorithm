company = dict()

for i in range(int(input())):
    name, case = input().split()

    company[name] = case

company = sorted(company.items(), reverse=True)

for k, v in company:
    if v == "enter":
        print(k)
