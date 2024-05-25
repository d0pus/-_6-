from abc import ABC, abstractmethod

class AbstractTicket(ABC):
    @abstractmethod
    def get_ticket_type(self) -> str:
        pass

    @abstractmethod
    def add_service(self, service: str) -> None:
        pass

class AbstractService(ABC):
    @abstractmethod
    def get_description(self) -> str:
        pass

class RegularTicket(AbstractTicket):
    def __init__(self):
        self.services = []

    def get_ticket_type(self) -> str:
        return "Обычный"

    def add_service(self, service: str) -> None:
        self.services.append(service)

class VipTicket(AbstractTicket):
    def __init__(self):
        self.services = []

    def get_ticket_type(self) -> str:
        return "VIP"

    def add_service(self, service: str) -> None:
        self.services.append(service)

class Popcorn(AbstractService):
    def get_description(self) -> str:
        return "Попкорн"

class Drink(AbstractService):
    def get_description(self) -> str:
        return "Напиток"

class TicketFactory(ABC):
    @abstractmethod
    def create_ticket(self, ticket_type: str) -> AbstractTicket:
        pass

    @abstractmethod
    def add_service_to_ticket(self, ticket: AbstractTicket, service: Ab-stractService) -> None:
        pass

class MovieTicketFactory(TicketFactory):
    def create_ticket(self, ticket_type: str) -> AbstractTicket:
        if ticket_type.lower() == "regular":
            return RegularTicket()
        elif ticket_type.lower() == "vip":
            return VipTicket()
        else:
            raise ValueError("Неизвестный тип билета")

    def add_service_to_ticket(self, ticket: AbstractTicket, service: Ab-stractService) -> None:
        ticket.add_service(service.get_description())

def main():
    factory = MovieTicketFactory()
    regular_ticket = factory.create_ticket("Regular")
    vip_ticket = factory.create_ticket("Vip")

    popcorn = Popcorn()
    drink = Drink()

    factory.add_service_to_ticket(regular_ticket, popcorn)
    factory.add_service_to_ticket(vip_ticket, drink)

    print(f"{regular_ticket.get_ticket_type()} билет: {', '.join(regular_ticket.services)}")
    print(f"{vip_ticket.get_ticket_type()} билет: {', '.join(vip_ticket.services)}")

if __name__ == "__main__":
    main()
