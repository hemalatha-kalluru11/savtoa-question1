from abc import ABC, abstractmethod
# Base Device class (Abstract)
class Device(ABC):
    def __init__(self):
        self._is_on = False   

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    def is_on(self):
        """Allows external code to check device status"""
        return self._is_on


# Motor device
class Motor(Device):
    def start(self):
        if not self._is_on:
            self._is_on = True
            print("Motor has started")

    def stop(self):
        if self._is_on:
            self._is_on = False
            print("Motor has stopped")


# Light device
class Light(Device):
    def start(self):
        if not self._is_on:
            self._is_on = True
            print("Light switched on")

    def stop(self):
        if self._is_on:
            self._is_on = False
            print("Light switched off")


# Controller class (device-independent)
class Controller:
    def operate(self, device: Device):
        device.start()
        device.stop()


#------ Testing / Driver Code ------

if __name__ == "__main__":
    motor = Motor()
    light = Light()

    motor_controller = Controller()
    light_controller = Controller()

    motor_controller.operate(motor)
    light_controller.operate(light)


