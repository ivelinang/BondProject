__author__ = 'ivelin.angelov'

#-------------------------------------------------------------------------------
# Author:       Ivelin Angelov
# Written:      23/03/2015
# Last Updated: 23/03/2015

# Filename:     IndexAnalyticsMapper.py
# Python used:  3.4
#-------------------------------------------------------------------------------
# Description:  maps analytics index attributes to sql column names
#-------------------------------------------------------------------------------
# Log of changes:
# ...
#-------------------------------------------------------------------------------

from DataGetter.ResultWrapper import ResultSetWrapper
from IndexClass.IndexAnalytics import IndexAnalytics


class IndexAnalyticsMapper(object):

    def __init__(self):
        pass

    def createIndexAnalytics(self, ResultSet, row):
        ''' map the indexattributes to sql column names + return
        :param ResultSet:
        :param row:
        :return:
        '''

        #create resultWrapper - wrapper around sql resultset to force type conversion
        rs=ResultSetWrapper(ResultSet)

        #create new bond
        analytics=IndexAnalytics()

        #feed the attributes from the SQL resultSet
        analytics.calcDate = rs.getDatetime('CalcDate', row)
        analytics.rebDate = rs.getDatetime('RebalanceDate', row)
        analytics.isdIndex = rs.getString('isdIndex', row)
        analytics.costFactor = rs.getFloat('costFactor', row)
        analytics.accruedCashFactor = rs.getFloat('accruedCashFactor', row)
        analytics.rebCash = rs.getFloat('RebalanceCash', row)
        analytics.calcCash = rs.getFloat('calcCash', row)
        analytics.indexMTD = rs.getFloat('indexMTD', row)
        analytics.indexBMV = rs.getFloat('indexBMV', row)
        analytics.indexMV = rs.getFloat('indexMV', row)

        #return object
        return analytics

def Main():

   print('test')



'Run the Main function if the module is open(vs. imported)'
if __name__ == "__main__":
    Main()


