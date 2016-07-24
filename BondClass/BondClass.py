__author__ = 'ivelin.angelov'

# -------------------------------------------------------------------------------
# Author:       Ivelin Angelov
# Written:      23/03/2015
# Last Updated: 26/03/2015

# Filename:     BondClass.py
# Python used:  2.7
#-------------------------------------------------------------------------------
# Description:  Set of classes and methods to represent bonds and their operations.
#-------------------------------------------------------------------------------
# Log of changes:
# Date          Author             Change
# 26/03/2015    Ivelin Angelov
#-------------------------------------------------------------------------------

import datetime

from Descriptors.DescriptorClass import typeassert


#---------------------------------------------------------------------------------
# BOND CLASS
#---------------------------------------------------------------------------------

# @typeassert is a decorator that uses a descriptor to use getters and setters to check the correct type inputs for attributes of class Bond
@typeassert(calcDate=datetime.datetime,
            rebDate=datetime.datetime,
            isdBond=str,
            isin=str,
            weight=float,
            coupon=float,
            couponFrequency=int,
            nextCoupon=float,
            maturity=datetime.datetime,
            workoutdate=datetime.datetime,
            nextCouponDate=datetime.datetime,
            firstSettleDate=datetime.datetime,
            firstCouponDate=datetime.datetime,
            penultimateCouponDate=datetime.datetime,
            nextCallDate=datetime.datetime,
            isCallable=bool,
            isSinkable=bool,
            isMultiCoupon=bool,
            isZeroCoupon=bool,
            isPerpetual=bool,
            isFixToFloat=bool,
            isFloater=bool,
            isIndexLink=bool,
            isPIKbond=bool,
            isRatingSensitive=bool,
            isRegisterSensitiv=bool,
            isPutable=bool,
            isDtcEligible=bool,
            isTraceEligible=bool,
            isCreditLinked=bool,
            isHybridCapital=bool,
            isConvertible=bool,
            isMatured=bool,
            isCalled=bool,
            dcc=str,
            bidPrice=float,
            askPrice=float,
            indexPrice=float,
            midPrice=float,
            accruedInterest=float,
            redemptionFactor=float,
            PIK_Factor=float,
            coupAdjustment=int,
            xdFactor=int,
            level1=str,
            level2=str,
            level3=str,
            level4=str,
            level5=str,
            level6=str,
            level7=str,
            level8=str,
            iBoxxRating=str,
            iBoxxRatingScore=int,
            principal=float,
            currency=str,
            notional=float,
            minIncrement=float,
            minPiece=float,
            ticker=str,
            debt=str,
            tier=str,
            countryOfRisk=str,
            issuerCountry=str
            )
class Bond(object):
    ''' Bond Class:
        main building block. Each bond feeds
        an instance of a subclass to this superclass.
        Attributes: static data + analytics object that holds analytics for the bond
    '''

    #NOT abstract class
    #__metaclass__ = ABCMeta

    def __init__(self,
                 cdate = datetime.datetime(2100,1,1),
                 rebdate = datetime.datetime(2100,1,1),
                 isin = 'X',
                 isdBond = 'X',
                 weight = 0.03,
                 coupon = 4.5,
                 nextCoupon = 4.5,
                 cpn_freq = 1,
                 maturity = datetime.datetime(2100,1,1),
                 workoutdate = datetime.datetime(2100,1,1),
                 firstSettleDate = datetime.datetime(2100,1,1),
                 firstCouponDate = datetime.datetime(2100,1,1),
                 penultimateCouponDate = datetime.datetime(2100,1,1),
                 nextCouponDate = datetime.datetime(2100,1,1),
                 nextCallDate = datetime.datetime(2100,1,1),
                 callable = False,
                 sinkable = False,
                 zero_copoun = False,
                 perpetual = False,
                 multiCoupon = False,
                 fixtofloat = False,
                 floater = False,
                 indexlink = False,
                 is_PIKbond = False,
                 isMatured = False,
                 isCalled = False,
                 isRatingSensitive = False,
                 isRegisterSensitive = False,
                 isPutable = False,
                 isDtcEligible = False,
                 isTraceEligible = False,
                 isCreditLinked = False,
                 isHybridCapital = False,
                 isConvertible = False,
                 dcc = 'ACT/ACT',
                 bidprice=99.9,
                 askprice = 99.9,
                 indexPrice = 99.9,
                 midPrice = 99.9,
                 accruedInterest = 0.34,
                 coupAdjustment = 0,
                 xdFactor = 1,
                 redemptionFactor = 1.0,
                 PIK_Factor = 1.0,
                 notional = float(1000000),
                 minIncrement = float(3000),
                 minPiece = float(100000),
                 ticker = 'GOOG',
                 currency = 'USD',
                 debt = 'SEN',
                 tier = 'T1',
                 iBoxxRating = 'A',
                 iBoxxratingScore = 5,
                 countryOfRisk = 'US',
                 issuerCountry = 'US',
                 level1='X',
                 level2='X',
                 level3='X',
                 level4='X',
                 level5='X',
                 level6='X',
                 level7='X',
                 level8='X',
                 principal = 100.0
                 ):

        self.calcDate = cdate
        self.rebDate = rebdate
        self.isin = isin
        self.isdBond = isdBond
        self.weight = weight
        self.coupon = coupon
        self.nextCoupon = nextCoupon
        self.couponFrequency = cpn_freq
        self.maturity = maturity
        self.workoutdate = workoutdate
        self.nextCouponDate = nextCouponDate
        self.firstSettleDate = firstSettleDate
        self.firstCouponDate = firstCouponDate
        self.penultimateCouponDate = penultimateCouponDate
        self.nextCallDate = nextCallDate
        self.isCallable = callable
        self.isMultiCoupon = multiCoupon
        self.isSinkable = sinkable
        self.isZeroCoupon = zero_copoun
        self.isPerpetual = perpetual
        self.isFixToFloat = fixtofloat
        self.isFloater = floater
        self.isIndexLink = indexlink
        self.isPIKbond = is_PIKbond
        self.isRatingSensitive = isRatingSensitive
        self.isRegisterSensitive = isRegisterSensitive
        self.isPutable = isPutable
        self.isDtcEligible = isDtcEligible
        self.isTraceEligible = isTraceEligible
        self.isCreditLinked = isCreditLinked
        self.isHybridCapital = isHybridCapital
        self.isConvertible = isConvertible
        self.isMatured = isMatured
        self.isCalled = isCalled
        self.dcc = dcc
        self.bidPrice = bidprice
        self.askPrice = askprice
        self.indexPrice = indexPrice
        self.midPrice = midPrice
        self.accruedInterest = accruedInterest
        self.redemptionFactor = redemptionFactor
        self.PIK_Factor = PIK_Factor
        self.coupAdjustment = coupAdjustment
        self.xdFactor = xdFactor
        self.level1 = level1
        self.level2 = level2
        self.level3 = level3
        self.level4 = level4
        self.level5 = level5
        self.level6 = level6
        self.level7 = level7
        self.level8 = level8
        self.iBoxxRating = iBoxxRating
        self.iBoxxRatingScore = iBoxxratingScore
        self.principal = principal
        self.currency = currency
        self.notional = notional
        self.minIncrement = minIncrement
        self.minPiece = minPiece
        self.ticker = ticker
        self.debt = debt
        self.tier = tier
        self.countryOfRisk = countryOfRisk
        self.issuerCountry = issuerCountry
        self.analytics = None
        self.marketValue = None
        self.baseMarketValue = None
        self.MTDreturn = None


    def calcMarketValue(self):
        ''' calc bond market value
            formula: Notional*(bidPrice + Accrued +XDfactor*CoupAdj)*RedemptionFactor*PIK_factor/100
        :return: self.MarketValue
        '''

        marketValue = self.notional*(self.bidPrice + self.accruedInterest + self.xdFactor*self.coupAdjustment)*\
                           self.redemptionFactor*self.PIK_Factor/100.0

        return marketValue

    def calcBaseMarketValue(self):
        ''' calc base market value
            formula: Notional*(indexPrice + Accrued +XDfactor*CoupAdj)*RedemptionFactor*PIK_factor/100
        :return: self.baseMarketValue
        '''

        baseMarketValue = self.notional*(self.bidPrice + self.accruedInterest + self.xdFactor*self.coupAdjustment)*\
                               self.redemptionFactor*self.PIK_Factor/100.0

        return baseMarketValue

    def calcCashPayment(self):
        ''' calc cash payment for bond
        :return:
        '''

        cashpay = self.analytics.cashPayment*self.notional/100

        return cashpay




def Main():

    bond=Bond()
    #bond.bidPrice=1
    #bond.isin=3
    bond.isCallable=True
    bond.constituentDate=datetime.datetime(2011,1,1)
    print(bond.isin)


'Run the Main function if the module is open(vs. imported)'
if __name__ == "__main__":
    Main()
