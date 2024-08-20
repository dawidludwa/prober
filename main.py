from factory.Director import Director
from factory.ProbeBuilder import ProbeBuilder


probeBuilder = ProbeBuilder()


director = Director(probeBuilder)
probe = director.construct()
probe2 = director.constructRich()


print(probe)
print(probe2)
