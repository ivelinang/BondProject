__author__ = 'ivelin.angelov'

#-------------------------------------------------------------------------------
# Author:       Ivelin Angelov
# Written:      23/03/2015
# Last Updated: 23/03/2015

# Filename:     ResultSet.py
# Python used:  2.7
#-------------------------------------------------------------------------------
# Description:  map SQL results with bond attributes
#-------------------------------------------------------------------------------
# Log of changes:
# ...
#-------------------------------------------------------------------------------

from DataGetter.ResultWrapper import ResultSetWrapper
from BondClass.BondClass import Bond


class BondMapper(object):

    def __init__(self):
        pass

    def createBond(self, ResultSet, row):
        ''' map the bond attributes to sql column names + return bond object
        :param ResultSet:
        :param row:
        :return: bond object with the new attributes
        '''

        #create resultWrapper - wrapper around sql resultset to force type conversion
        rs=ResultSetWrapper(ResultSet)

        #create new bond
        bond=Bond()

        #feed the attributes from the SQL resultSet
        bond.calcDate = rs.getDatetime('CalcDate', row)
        bond.rebDate = rs.getDatetime('RebalanceDate', row)
        bond.isdBond = rs.getString('ISD_BOND', row)
        bond.isin = rs.getString('ISIN', row)
        bond.weight = rs.getFloat('Weight', row)
        bond.coupon = rs.getFloat('Coupon', row)
        bond.couponFrequency = rs.getInteger('CouponFreq', row)

        bond.maturity = rs.getDatetime('Maturity', row)
        bond.workoutdate = rs.getDatetime('Workoutdate', row)
        bond.nextCouponDate = rs.getDatetime('NextCouponDate', row)
        bond.firstCouponDate = rs.getDatetime('FirstCpnDate', row)
        bond.firstSettleDate = rs.getDatetime('FirstSettleDate', row)
        bond.penultimateCouponDate = rs.getDatetime('PenultimateCpnDate', row)
        bond.nextCallDate = rs.getDatetime('NextCallDate', row)

        bond.isCallable = rs.getBoolen('IsCallable', row)
        bond.isMultiCoupon = rs.getBoolen('IsMultiCpn', row)
        bond.isSinkable = rs.getBoolen('IsSinkable', row)
        bond.isZeroCoupon = rs.getBoolen('IsZeroCoupon', row)
        bond.isPutable = rs.getBoolen('IsPutable', row)
        bond.isPerpetual = rs.getBoolen('IsPerpetual', row)
        bond.isPIKbond = rs.getBoolen('Is_PIK', row)
        bond.isFloater = rs.getBoolen('IsFloater', row)
        bond.isFixToFloat = rs.getBoolen('IsFixedToFloat', row)
        bond.isIndexLink = rs.getBoolen('IsIndexLinked', row)
        bond.isRatingSensitive = rs.getBoolen('IsRatingSensitive', row)
        bond.isRegisterSensitive = rs.getBoolen('IsRegisterSensitive', row)
        bond.isDtcEligible = rs.getBoolen('IsDtcEligible', row)
        bond.isHybridCapital = rs.getBoolen('IsHybridCapital', row)
        bond.isTraceEligible = rs.getBoolen('IsTraceEligible', row)
        bond.isConvertible = rs.getBoolen('IsConvertible', row)
        bond.isCreditLinked = rs.getBoolen('IsCreditLinked', row)
        bond.isMatured = rs.getBoolen('Is_matured', row)
        bond.isCalled = rs.getBoolen('Is_called', row)

        bond.dcc = rs.getString('DCC', row)
        bond.bidPrice = rs.getFloat('bidPrice', row)
        bond.askPrice = rs.getFloat('askPrice', row)
        bond.indexPrice = rs.getFloat('indexPrice', row)
        bond.midPrice = rs.getFloat('midPrice', row)
        bond.accruedInterest = rs.getFloat('AccruedInterest', row)
        bond.redemptionFactor = rs.getFloat('RedemptionFactor', row)
        bond.PIK_Factor = rs.getFloat('PIK_Factor', row)
        bond.coupAdjustment = rs.getInteger('CoupAdjustment', row)
        bond.xdFactor = rs.getInteger('XDFactor', row)

        bond.level1 = rs.getString('Level1', row)
        bond.level2 = rs.getString('Level2', row)
        bond.level3 = rs.getString('Level3', row)
        bond.level4 = rs.getString('Level4', row)
        bond.level5 = rs.getString('Level5', row)
        bond.level6 = rs.getString('Level6', row)
        bond.level7 = rs.getString('Level7', row)
        bond.level8 = rs.getString('Level8', row)
        bond.debt = rs.getString('Debt', row)
        bond.tier = rs.getString('Tier', row)
        bond.principal = rs.getFloat('Principal', row)
        bond.notional = rs.getFloat('Notional', row)
        bond.minIncrement = rs.getFloat('MinIncrement', row)
        bond.minPiece = rs.getFloat('MinPiece', row)
        bond.ticker = rs.getString('Ticker', row)
        bond.currency = rs.getString('Currency', row)
        bond.countryOfRisk = rs.getString('CountryOfRisk', row)
        bond.issuerCountry = rs.getString('IssuerCountry', row)
        bond.iBoxxRating = rs.getString('iBoxxRating', row)
        bond.iBoxxRatingScore = rs.getInteger('FinalScore', row)

        #return bond object
        return bond

def Main():

    from DataLoader.DataLoader import DataLoaderProd

    dataload=DataLoaderProd()
    print(dataload.CONNECTION_STRING)
    #get calc data
    CalcDate='2015-07-31'
    IndexID='MKT.xxx'
    result=dataload.getCalcDayRefData(CalcDate, IndexID)



'Run the Main function if the module is open(vs. imported)'
if __name__ == "__main__":
    Main()
