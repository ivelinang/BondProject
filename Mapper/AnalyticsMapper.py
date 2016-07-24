__author__ = 'ivelin.angelov'

#-------------------------------------------------------------------------------
# Author:       Ivelin Angelov
# Written:      23/03/2015
# Last Updated: 23/03/2015

# Filename:     AnalyticsMapper.py
# Python used:  2.7
#-------------------------------------------------------------------------------
# Description:  maps analytics bond attributes to sql column names
#-------------------------------------------------------------------------------
# Log of changes:
# ...
#-------------------------------------------------------------------------------

from DataGetter.ResultWrapper import ResultSetWrapper
from BondClass.BondAnalyticsClass import BondAnalytics


class AnalyticsMapper(object):

    def __init__(self):
        pass

    def createAnalytics(self, ResultSet, row):
        ''' map the bond attributes to sql column names + return analytics object
        :param ResultSet:
        :param row:
        :return: bond object with the new attributes
        '''

        #create resultWrapper - wrapper around sql resultset to force type conversion
        rs=ResultSetWrapper(ResultSet)

        #create new bond
        analytics=BondAnalytics()

        #feed the attributes from the SQL resultSet
        analytics.calcDate = rs.getDatetime('CalcDate', row)
        analytics.rebDate = rs.getDatetime('RebalanceDate', row)
        analytics.isdBond = rs.getString('ISD_BOND', row)
        analytics.isin = rs.getString('ISIN', row)
        analytics.annualYield = rs.getFloat('ANNUAL YIELD', row)
        analytics.annualConvexity = rs.getFloat('ANNUAL CONVEXITY', row)
        analytics.annualModDuration = rs.getFloat('ANNUAL MODIFIED DURATION', row)
        analytics.annualBenchSpread = rs.getFloat('ANNUAL BENCHMARK SPREAD', row)
        analytics.assetSwapSpread = rs.getFloat('ASSET SWAP SPREAD', row)
        analytics.effectiveDuration = rs.getFloat('EffectiveDuration', row)
        analytics.floaterDuration = rs.getFloat('FloaterDuration', row)
        analytics.zSpread = rs.getFloat('Z_SPREAD', row)
        analytics.oaSpread = rs.getFloat('OA_SPREAD', row)
        analytics.floaterDuration = rs.getFloat('FloaterDuration', row)
        analytics.discountMargin = rs.getFloat('DISCOUNTED_MARGIN', row)
        analytics.cashPayment = rs.getFloat('CASHPAYMENT', row)
        analytics.fxrateUSDvLCY = rs.getFloat('USDvsLCY', row)
        analytics.fxrateEURvLCY = rs.getFloat('EURvsLCY', row)
        analytics.fxrateGBPvLCY = rs.getFloat('GBPvsLCY', row)

        #return analytics object
        return analytics

def Main():

   print('test')

'Run the Main function if the module is open(vs. imported)'
if __name__ == "__main__":
    Main()
