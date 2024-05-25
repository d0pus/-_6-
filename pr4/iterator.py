class ExcursionBookingSystem:
    def __init__(self, excursions):
        self.excursions = excursions

    def has_next_excursion(self):
        return len(self.excursions) > 0

    def next_excursion(self):
        excursion = self.excursions.pop(0)
        return excursion
class BookingIterator:
    def __init__(self, booking_system):
        self.booking_system = booking_system

    def has_next(self):
        return self.booking_system.has_next_excursion()

    def next(self):
        if self.has_next():
            return self.booking_system.next_excursion()
        else:
            raise StopIteration
if __name__ == "__main__":
    excursions = ["Музей искусства", "Туристическая прогулка по городу", "Посещение исторического музея"]
    booking_system = ExcursionBookingSystem(excursions)
    iterator = BookingIterator(booking_system)

    while iterator.has_next():
        print(iterator.next())
