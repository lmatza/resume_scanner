keywords = ['Python', 'Java']

try:
    with open('resume_test.txt', 'r', encoding = 'utf-8') as file:
        for line in open('resume_test.txt'):
            for k in keywords:
                if k in line:
                    print(k)

finally:
    file.close()