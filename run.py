from models import Bioreactor
from calculations import pandas_array, generate_od_plot, generate_ln_plot

reactor = Bioreactor(input('Please add the reactor number: '))
reactor.set_data()
pandasreactor = reactor.pandas_subreactor()
numpyreactor = reactor.make_subreactor()
generate_od_plot(numpyreactor)
generate_ln_plot(numpyreactor)


