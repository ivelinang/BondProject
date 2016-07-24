__author__ = 'ivelin.angelov'

# -------------------------------------------------------------------------------
# Author:       Ivelin Angelov
# Written:      23/03/2015
# Last Updated: 26/03/2015

# Filename:     IndexClass.py
# Python used:  3.4
#-------------------------------------------------------------------------------
# Description:  Index class holds bond objects and performs operations on them.
#-------------------------------------------------------------------------------
# Log of changes:
# Date          Author             Change
# 26/03/2015    Ivelin Angelov     Change the AddMonth function to use dateutil module
#-------------------------------------------------------------------------------

from abc import ABCMeta, abstractmethod
from BondClass.BondClass import Bond
from Descriptors.DescriptorClass import typeassert
import datetime

#---------------------------------------------------------------------------------
# Index Analytics CLASS
#---------------------------------------------------------------------------------

# @typeassert is a decorator that uses a descriptor to use getters and setters to check the correct type inputs for attributes of class Bond
@typeassert(calcDate=datetime.datetime,
            rebDate=datetime.datetime,
            isdIndex=str,
            costFactor=float,
            rebCash=float,
            accruedCashFactor=float,
            calcCash=float,
            indexBMV=float,
            indexMV=float,
            indexMTD=float,
            )
class IndexAnalytics(object):
    """
    interface for index classes
    """


    #@abstractmethod
    def __init__(self,
                 cdate = datetime.datetime(2100,1,1),
                 rebdate = datetime.datetime(2100,1,1),
                 isdIndex = 'X',
                 costFactor = 0.99,
                 rebCash = 123000.0,
                 accruedCashFactor = 1.03,
                 calcCash = 123000.0,
                 indexBMV = 123000.0,
                 indexMV = 123000.0,
                 indexMTD = 1.034
                 ):

        self.calcDate = cdate
        self.rebDate = rebdate
        self.isdIndex = isdIndex
        self.costFactor = costFactor
        self.rebCash = rebCash
        self.accruedCashFactor = accruedCashFactor
        self.calcCash = calcCash
        self.indexBMV = indexBMV
        self.indexMV = indexMV
        self.indexMTD = indexMTD

