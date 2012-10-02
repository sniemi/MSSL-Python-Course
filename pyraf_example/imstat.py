import pprint
from pyraf import iraf

stats = iraf.imstatistics('../VIS.fits[1]', Stdout=1)
pprint.pprint(stats)
