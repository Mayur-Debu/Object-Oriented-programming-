class ElectrnoicDevice:
    def electronicDeviceFunction(self):
        return f"Mobile phone is a Electronic Device"

class PocketGadget(ElectrnoicDevice):
    def pocketGadgetFunction(self):
        return f"Mobile phone is a Pocket device"

class Phone(PocketGadget):
    pass

mobile=Phone()
print(mobile.electronicDeviceFunction())
print(mobile.pocketGadgetFunction())