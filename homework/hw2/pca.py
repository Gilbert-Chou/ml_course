def read_dataset():
    f = open("breast-cancer-wisconsin.data", "r")
    cnt = 0
    data = dict()

    for d in f:
        dd = d[:len(d)-1].split(",", 11)
        data[cnt] = (dd[1], dd[2], dd[3], dd[4], dd[5], dd[6], dd[7], dd[8], dd[9], dd[10])
        cnt += 1
        
    f.close()

    #處理dataset有問號的資訊
    return missing_data_handler(data)


def missing_data_handler(data):
    import numpy as np
    data_handled = []

    attribute_T = np.zeros(9)
    attribute_T_cnt = np.zeros(9)
    attribute_F = np.zeros(9)
    attribute_F_cnt = np.zeros(9)

    for d in data:
        if data[d][9] == '2':
            for i in range(0, len(data[d])-1):
                if data[d][i] != '?' :
                    attribute_T[i] += int(data[d][i])
                    attribute_T_cnt[i] += 1
        else:
            for i in range(0, len(data[d])-1):
                if data[d][i] != '?' :
                    attribute_F[i] += int(data[d][i])
                    attribute_F_cnt[i] += 1

    mean_T = attribute_T / attribute_T_cnt
    mean_F = attribute_F / attribute_F_cnt
    mean = (attribute_T + attribute_F) / (attribute_T_cnt + attribute_F_cnt)

    for i in range(0, 9):
        data_handled.append([])
 
    for d in data:
        data_handled[0].append(int(data[d][0]) - mean[0])
        data_handled[1].append(int(data[d][1]) - mean[1])
        data_handled[2].append(int(data[d][2]) - mean[2])
        data_handled[3].append(int(data[d][3]) - mean[3])
        data_handled[4].append(int(data[d][4]) - mean[4])
        data_handled[6].append(int(data[d][6]) - mean[6])
        data_handled[7].append(int(data[d][7]) - mean[7])
        data_handled[8].append(int(data[d][8]) - mean[8])
        # data_handled[9].append(int(data[d][9]) - mean[9])
        if find_missing(data[d]) == -1:
            data_handled[5].append(int(data[d][5]) - mean[5])
        else:
            if data[d][9] == '2':
                data_handled[5].append(round(mean_T[find_missing(data[d])]) - mean[5])
            else:
                data_handled[5].append(round(mean_F[find_missing(data[d])]) - mean[5])


    return data_handled

def find_missing(d):
    for i in range(0, len(d)-1):
        if(d[i] == '?'):
            return i
            
    return -1

def pca(data):
    import numpy as np
    import matplotlib.pyplot as plt

    cov = np.cov(data)

    eigen_value, eigen_vector = np.linalg.eig(cov)

    total = sum(eigen_value)
    var_exp = [(i / total) for i in sorted(eigen_value, reverse=True)]
    cum_var_exp = np.cumsum(var_exp)

    plt.bar(range(1, 10), var_exp, alpha=0.5, align='center', label='individual explained variance')
    plt.step(range(1, 10), cum_var_exp, where='mid', label='cumulative explained variance')
    plt.ylabel('Explained variance ratio')
    plt.xlabel('Principal components')
    plt.legend(loc='best')
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    dataset = read_dataset()
    pca(dataset)

    