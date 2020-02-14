#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = []
    for i in range (len(tickets)):
      source = tickets[i].source
      destination = tickets[i].destination
      #insert tickets in to hashtable
      hash_table_insert(hashtable, source, destination)
    
    #find the beginning
    step = hash_table_retrieve(hashtable, "NONE")
    #while we haven't reached the last ticket
    while step is not "NONE":
    # add ticket to route
      route.append(step)
      #move to the next ticket
      step = hash_table_retrieve(hashtable, step)
    return route
