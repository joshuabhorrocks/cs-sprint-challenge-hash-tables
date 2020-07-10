#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source    # Starting Airport
        self.destination = destination # Next Airport
        self.tickets = {self.destination, self.source}
        print(self.tickets)
        # First Ticket: source = None, destination = next
        # Last Ticket: source = prev, destination = None


def reconstruct_trip(tickets, length):
    route = []

    return route


if __name__ == "__main__":

    ticket_1 = Ticket("NONE", "PDX")
    ticket_2 = Ticket("PDX", "DCA")
    ticket_3 = Ticket("DCA", "NONE")