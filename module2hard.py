# Дополнительное практическое задание по модулю: "Основные операторы"
# Задание "Слишком древний шифр":
def password(n):
    result_ = ''
    for i in range(1, n):
        for j in range(i + 1, n):
            if n % (i + j) == 0:
                result_ += str(i) + str(j)
    return result_


print(password(int(input("Введите число от 3 до 20: "))))

