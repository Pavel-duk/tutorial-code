def matrix_pruf(matrix,i,j):
    if len(matrix) == (len(matrix[i])):
        stroka_matrix = [element for element in matrix[i]]
        stolb_matrix = []
        for ind in range(len(matrix)):
            stolb_matrix.append(matrix[i][ind])
        print(stolb_matrix)
        index = 0
        for i1 in range(len(matrix)):
            matrix[i1].insert(j,stroka_matrix[index])
            matrix[i1].pop(j-1)
            index += 1
        index1 = 0
        for j1 in range(len(matrix[i])):
            matrix[i].insert(j1,stolb_matrix[index1])
            index1 += 1
            matrix[i].pop(i1+1)
    return matrix
____________________________________________





