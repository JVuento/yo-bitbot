import yobit

'''
Routes you want bot to try. First index is where to start.
Note naming in yobit (ex eth_btc not btc_eth) when desiding routes. More than one routes for easier reading
'''

routes = [['btc', '1337', 'eth'], ['btc', '1337', 'doge'],['btc', 'xt', 'eth'], ['btc', 'xt', 'doge']]
routes2 = [['btc', 'carbon', 'eth'], ['btc', 'carbon', 'doge']]
routes = routes + routes2

'''Get only buy price from ticker call. Will be changed, waste of time but works for testing '''
def getBuyPrice(pari):
    kutsut = yobit.YoBit()
    palautus = kutsut.ticker(pari)
    return palautus[pari]['buy']

'''Get only buy sell from ticker call. Will be changed, waste of time but works for testing '''
def getSellPrice(pari):
    kutsut = yobit.YoBit()
    palautus = kutsut.ticker(pari)
    return palautus[pari]['sell']

'''
Repeat for all the routes desided. Tries the route both ways.
voitto = how much you get with 1 starting currency
'''
for i in range(len(routes)):
    pr1 = getSellPrice(routes[i][1] + '_' + routes[i][0])
    pr2 = getBuyPrice(routes[i][1] + '_' + routes[i][2])
    pr3 = getBuyPrice(routes[i][2] + '_' + routes[i][0])
    voitto = (1 / pr1) * pr2  * pr3
    print str(routes[i]) + ' direction 1: ' + str(voitto)
    pr1 = getSellPrice(routes[i][2] + '_' + routes[i][0])
    pr2 = getSellPrice(routes[i][1] + '_' + routes[i][2])
    pr3 = getBuyPrice(routes[i][1] + '_' + routes[i][0])
    voitto = (1 / pr1) / pr2  * pr3
    print str(routes[i]) + ' direction 2: ' + str(voitto)
