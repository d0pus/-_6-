from abc import ABC, abstractmethod

class DeliveryProcessor(ABC):

    @abstractmethod
    def choose_transport(self):
        pass

    @abstractmethod
    def plan_route(self):
        pass

    @abstractmethod
    def deliver_goods(self):
        pass

    @abstractmethod
    def confirm_delivery(self):
        pass

    def process_delivery(self):
        self.choose_transport()
        self.plan_route()
        self.deliver_goods()
        self.confirm_delivery()
class CourierDeliveryProcessor(DeliveryProcessor):

    def choose_transport(self):
        print("Выбор курьерской доставки...")

    def plan_route(self):
        print("Планирование маршрута курьером...")

    def deliver_goods(self):
        print("Доставка товаров курьером...")

    def confirm_delivery(self):
        print("Подтверждение доставки курьером...")

class SelfPickupDeliveryProcessor(DeliveryProcessor):

    def choose_transport(self):
        print("Выбор самовывоза...")

    def plan_route(self):
        print("Планирование маршрута для самовывоза...")

    def deliver_goods(self):
        print("Уведомление о готовности к самовывозу...")

    def confirm_delivery(self):
        print("Подтверждение самовывоза...")
if __name__ == "__main__":
    courier_processor = CourierDeliveryProcessor()
    courier_processor.process_delivery()

    pickup_processor = SelfPickupDeliveryProcessor()
    pickup_processor.process_delivery()
