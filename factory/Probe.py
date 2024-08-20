class Probe:
    def __init__(self):
        self.name = None
        self.port = None
        self.timeout = None
        self.interval = None
        self.threshold = None

    def __str__(self):
        return (
            f"{self.name} {self.port} {self.timeout} {self.interval} {self.threshold}"
        )
