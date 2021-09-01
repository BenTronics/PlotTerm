from mittel import Mittel
from median import Median
from ableitung import Ableitung

mittel_filter = Mittel(10)
median_filter = Median(9)
ableitung = Ableitung()

l = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
l2 = [10, 0, 4, 10, 4, 10, 10, 5, 10, 10, 5, 10, 6, 10, 10, 10, 10, 10]

#mittel_filter.filtern(l)
#median_filter.filtern(l2)
print(ableitung.filtern(l2))