class RequestCreator():
    def __init__(self):
        # Values in tuple (Source, Destination, Bandwidth)
        self.request: tuple

    def problem_request(self):
        self.request = ((1, 3, 3), (2, 3, 7))
        return self.request
