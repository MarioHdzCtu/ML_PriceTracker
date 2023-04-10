class StoreNotRegistered(Exception):
    """
    Exception raised when class not considered in the logic of tracker module

    Attributes:
        store -- Web store that will be tracked (eg. Mercado Libre)
        message -- explanation of the error
    """

    def __init__(self, store, message='Store not regitered in logic') -> Exception: # type: ignore
        self.store = store
        self.message = message
        super().__init__(self.message)