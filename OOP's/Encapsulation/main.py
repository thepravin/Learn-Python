# Don't expose variables directly. Use property.

class Order:
    def __init__(self):
        self._status = "PLACED" # protected state

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, new_status):
        if new_status not in ["PLACED", "COOKING", "OUT_FOR_DELIVERY", "DELIVERED"]:
            raise ValueError("Invalid status")
        self._status = new_status

o = Order()
o.status = "COOKING" # calls setter
# o.status = "RANDOM" # raises error