def App():
    print('+--- Инструкция ---+')
    print('Символ "-" автоматически заменяется на нуль.')
    print('Символ "б" автоматически заменяется на очень большое число (как бы бесконечность).')
    print('+--- Программа ---+')
    m = int(input('Введите количество вершин: '))
    matrix = []
    for a in range(m):
        matrix.append([])
    for a in range(m):
        for b in range(m):
            x = input(f'Введите элемент a с индексом {a+1}x{b+1}: ')
            if x == '-':
                matrix[a].append(0)
            elif x == 'б':
                matrix[a].append(999)
            else:
                matrix[a].append(int(x))
    print(matrix)
    D_prev = []
    D = []
    for D_index in range(m-1):
        if D_index == 0:
            D = matrix[0]
        else:
            D_prev = D
            D = []
            for d_index in range(m):
                info = ''
                Calculations = []
                Calculations.append(D_prev[d_index])
                for iteration in range(m):
                    Calculations.append(D_prev[iteration] + matrix[iteration][d_index])
                D.append(min(Calculations))
        print(f'D{D_index+1} = {D}')

if __name__ == '__main__':
    App()



