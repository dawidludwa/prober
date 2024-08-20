class Director:
    def __init__(self, builder):
        self.builder = builder

    def construct(self):
        return (
            self.builder.set_name("probe")
            .set_port(80)
            .set_timeout(10)
            .set_interval(5)
            .set_threshold(3)
            .build()
        )

    def constructRich(self):
        return (
            self.builder.set_name("probe")
            .set_port(80)
            .set_timeout(10)
            .set_interval(5)
            .set_threshold(3)
            .build()
        )
