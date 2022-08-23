# Xin Xu #2194517

import random

class Des:
    def __init__(self, nb_faces, valeur1 = 0, valeur2 = 0) -> None:
        self.nb_faces = nb_faces
        self.de_1 = valeur1
        self.de_2 = valeur2

    def brasser(self):
        self.de_1 = random.randint(1, self.nb_faces)
        self.de_2 = random.randint(1, self.nb_faces)







d = Des(24)
print(d.nb_faces)
print(d.de_1)
print(d.de_2)

for i in range(30):
    d.brasser()
    print(d.de_1, end = "\t")
    print(d.de_2)


