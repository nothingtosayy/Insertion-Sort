def insertionsort(sequence):
    sorted_sequence = []
    sorted_sequence.append(sequence.pop(0))
    for i in range(len(sequence)):
        sorted_sequence.append(sequence[i])
        for j in range(len(sorted_sequence)-1, 0, -1):
            if sorted_sequence[j-1] > sorted_sequence[j]:
                sorted_sequence[j-1], sorted_sequence[j] = sorted_sequence[j], sorted_sequence[j-1]
    return sorted_sequence
    
print(insertionsort(sequence=[7,7,5,6,7,8,9,3,2,1,4,5,6,7,9,8]))
