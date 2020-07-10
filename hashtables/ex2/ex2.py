#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source    # Current Airport
        self.destination = destination  # Next Airport

        # Ticket Format: [self.source, self.destination]
        # First Ticket: source = None, destination = next
        # Last Ticket: source = prev, destination = None


def reconstruct_trip(tickets, length):
    route = []
    cache = {s.source: s for s in tickets}

    destination = "NONE"

    for i in range(length):
        destination = cache[destination].destination

        route.append(destination)

    # print("Final Route: ", route)
    return route
