class ProbeBuilder:

    def __init__(self):
        self.probe = Probe()

    def set_name(self, name):
        self.probe.name = name
        return self

    def set_port(self, port):
        self.probe.port = port
        return self

    def set_timeout(self, timeout):
        self.probe.timeout = timeout
        return self

    def set_interval(self, interval):
        self.probe.interval = interval
        return self

    def set_threshold(self, threshold):
        self.probe.threshold = threshold
        return self

    def build(self):
        return self.probe
