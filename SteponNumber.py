# input list awal
list_awal = [[4,2],[6,6],[3,4]]

# pattern yang ditemukan di graph adalah:
# condition 1 ( jika value x dan y genap = x + y )
# condition 2 ( jika value x dan y ganjil = x + y - 1 )
# condition 3 ( jika value x dan y tidak dua duanya genap atau ganjil value = 0 )

# function untuk tarik value dari graph
def steponNumber(x):
    # temporary list untuk simpan jawaban
    temp_list = []
    for i in range(len(x)): # for loop iterasi if statement untuk semua input list
        if x[i][0] % 2 == 0 and x[i][1] % 2 == 0: # jika condition 1 terpenuhi
            temp_list.append(x[i][0] + x[i][1]) # append x + y
        elif x[i][0] % 2 != 0 and x[i][1] % 2 != 0: # jika condition 2 terpenuhi
            temp_list.append((x[i][0] + x[i][1]) - 1) # append (x + y) - 1
        else: # jika condition 3 terpenuhi
            temp_list.append('No Number') # append 'No Number'
    return temp_list

# print jawaban
print(steponNumber(list_awal))