#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    answer = None
    for i in range(len(weights)):
    #insert weights into hashtable
      hash_table_insert(ht, weights[i], i)
      #find the weight needed to add to i to equal limit
      needed = limit - weights[i]
      retrieved = hash_table_retrieve(ht, needed)
      #if needed is in the hashtable
      if retrieved:
        #organize answer
        if i == retrieved:
          answer = (i, i-1)
        elif i < retrieved:
          answer = (retrieved, i)
        else:
          answer = (i, retrieved)
    print(answer)
    return answer


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")


