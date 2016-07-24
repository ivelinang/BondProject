__author__ = 'ivelin.angelov'

# -------------------------------------------------------------------------------
# Author:       Ivelin Angelov
# Written:      23/03/2015
# Last Updated: 26/03/2015

# Filename:     BondAnalyticsClass.py
# Python used:  2.7
#-------------------------------------------------------------------------------
# Description:  contain bond level analytics.
#-------------------------------------------------------------------------------
# Log of changes:
# Date          Author             Change
# 26/03/2015    Ivelin Angelov
#-------------------------------------------------------------------------------

import datetime

from Descriptors.DescriptorClass import typeassert


#---------------------------------------------------------------------------------
# ABSTRACT BOND CLASS
#---------------------------------------------------------------------------------

# @typeassert is a decorator that uses a descriptor to use getters and setters to check the correct type inputs for attributes of class Bond
@typeassert(calcDate=datetime.datetime,
            rebDate=datetime.datetime,
            isdBond=str,
            isin=str,
            annualYield=float,
            annualModDuration=float,
            annualConvexity=float,
            annualBenchSpread=float,
            zSpread=float,
            oaSpread=float,
            assetSwapSpread=float,
            effectiveDuration=float,
            discountMargin=float,
            floaterDuration=float,
            erl=float,
            cashPayment=float,
            fxrateUSDvLCY=float,
            fxrateEURvLCY=float,
            fxrateGBPvLCY=float,
            )
class BondAnalytics(object):
    ''' BondAnalytics Class:
        hold analytics for bonds.
        Attributes: static data + analytics object that holds analytics for the bond
    '''

    #NOT abstract class
    #__metaclass__ = ABCMeta

    def __init__(self,
                 cdate = datetime.datetime(2100,1,1),
                 rebdate = datetime.datetime(2100,1,1),
                 isin = 'X',
                 isdBond = 'X',
                 annualYield = 2.3,
                 annualModDuration = 4.3,
                 annualConvexity = 23.2,
                 annualBenchSpread = 312.3,
                 zSpread = 312.3,
                 oaSpread = 312.3,
                 assetSwapSpread = 312.3,
                 effectiveDuration = 4.3,
                 discountMargin = 351.3,
                 floaterDuration = 3.2,
                 erl = 3.4,
                 cashPayment = 340.3,
                 fxrateUSDvLCY = 1.54,
                 fxrateEURvLCY = 1.34,
                 fxrateGBPvLCY = 1.65,
                 ):
        self.calcDate = cdate
        self.rebDate = rebdate
        self.isin = isin
        self.isdBond = isdBond
        self.annualYield = annualYield
        self.annualModDuration = annualModDuration
        self.annualConvexity = annualConvexity
        self.annualBenchSpread = annualBenchSpread
        self.zSpread = zSpread
        self.oaSpread = oaSpread
        self.assetSwapSpread = assetSwapSpread
        self.effectiveDuration = effectiveDuration
        self.discountMargin = discountMargin
        self.floaterDuration = floaterDuration
        self.erl = erl
        self.cashPayment = cashPayment
        self.fxrateUSDvLCY = fxrateUSDvLCY
        self.fxrateEURvLCY = fxrateEURvLCY
        self.fxrateGBPvLCY = fxrateGBPvLCY

