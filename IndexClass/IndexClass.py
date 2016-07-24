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
# 26/03/2015    Ivelin Angelov
#-------------------------------------------------------------------------------

from abc import ABCMeta
import datetime

from dateutil.relativedelta import relativedelta


#---------------------------------------------------------------------------------
# ABSTRACT BOND CLASS
#---------------------------------------------------------------------------------


class Index(metaclass=ABCMeta):
    """
    interface for index classes
    """

    #Constants
    REB_FREQ=1  #months

    #@abstractmethod
    def __init__(self, rebBonds, calcBonds, startdate=0):
        """
        :param bonds: list of bond objects
        :param startdate:
        """
        self.rebBondSet={} #dictionary with keys as rebalance dates and values as list of bonds
        self.calcBondSet={} #dict with keys are calc days and values as list of bonds
        self.analytics=None #holds object of index analytics
        #create bond membership using private methods
        self.__createRebMembership(rebBonds)    #arrange bonds in bondSet
        self.__createCalcMembership(calcBonds)  #arrange bond in bondSet

    def __createRebMembership(self, bonds):
        ''' create rebalance bond membership in index class by using reb dates as keys in a dict that relate to a list of bonds
        :param bonds:
        :return: self.rebBondSet
        '''
        alldates=[]
        for bond in bonds:
            alldates.append(bond.rebDate)
        dates=set(alldates)
        for date in dates:
            self.rebBondSet[date]=[]
        for key in self.rebBondSet.keys():
            for bond in bonds:
                if bond.rebDate==key:
                    self.rebBondSet[key].append(bond)

    def __createCalcMembership(self, bonds):
        ''' create calc bond members with keys being calc dates of bonds
        :param bonds:
        :return:
        '''
        alldates=[]
        for bond in bonds:
            alldates.append(bond.calcDate)
        dates=set(alldates)
        for date in dates:
            self.calcBondSet[date]=[]
        for key in self.calcBondSet.keys():
            for bond in bonds:
                if bond.calcDate==key:
                    self.calcBondSet[key].append(bond)

    def calcMTDreturn(self, calcDate):
        ''' calculate bond MTD returns
        :param calcDate:
        :return:
        '''

        #find rebdate for the calcDate
        rebDate=calcDate-relativedelta(days=calcDate.day)

        #error checker
        if rebDate not in self.rebBondSet.keys():
            raise RuntimeError('Bond Data for rebalance date '+self.dateTostring(rebDate)+' is not available')

        #match bond in calc + reb date
        for xbond in self.calcBondSet[calcDate]:
            for ybond in self.rebBondSet[rebDate]:
                if xbond.isdBond==ybond.isdBond:
                    xbond.MTDreturn=(xbond.calcMarketValue() + xbond.calcCashPayment()) / ybond.calcBaseMarketValue() - 1

    @staticmethod
    def dateTostring(cdate):
        return cdate.strftime("%Y-%m-%d") #format for SQL input

    @staticmethod
    def stringTodate(cdate):
        return datetime.datetime.strptime(cdate, "%Y-%m-%d")



def Main():

    from Mapper.BondMapper import BondMapper
    from Mapper.AnalyticsMapper import AnalyticsMapper
    from DataLoader.DataLoader import DataLoaderProd

    #create dataloader object
    dataload=DataLoaderProd()

    #get calc bond data
    CalcDate='2015-07-31'
    IndexID='MKT.DE0007931974.GBP.L.3396'
    calcData=dataload.getCalcDayRefData(CalcDate, IndexID)

    #get calc analytics data
    calcAnalyticsData=dataload.getCalcDayAnalyticsData(CalcDate, IndexID)

    #get reb bond data
    RebDate='2015-06-30'
    IndexID='MKT.DE0007931974.GBP.L.3396'
    rebData=dataload.getRebDayRefData(RebDate, IndexID)

    #get reb analytics data
    rebAnalyticsData=dataload.getRebDayAnalyticsData(RebDate, IndexID)

    #create bond mapper
    mapper=BondMapper()
    reb_bond_lst=[]
    calc_bond_lst=[]
    #create bonds from each row
    for row in range(len(rebData.data)):
        #rebbond
        bond=mapper.createBond(rebData,row)
        reb_bond_lst.append(bond)
        #calc bond
        bond=mapper.createBond(calcData, row)
        calc_bond_lst.append(bond)

    #create analytics mapper
    analyticMapper=AnalyticsMapper()
    reb_analytics_lst=[]
    calc_analytics_lst=[]
    #create analytics object
    for row in range(len(rebAnalyticsData.data)):
        #reb
        analytics=analyticMapper.createAnalytics(rebAnalyticsData, row)
        reb_analytics_lst.append(analytics)
        #calc
        analytics=analyticMapper.createAnalytics(calcAnalyticsData, row)
        calc_analytics_lst.append(analytics)

    #map calc bonds to calc analytics
    for bond in calc_bond_lst:
        for analytics in calc_analytics_lst:
            if bond.isdBond==analytics.isdBond and bond.calcDate==analytics.calcDate:
                bond.analytics=analytics

    #map reb bonds to reb analytics
    for bond in reb_bond_lst:
        for analytics in reb_analytics_lst:
            if bond.isdBond==analytics.isdBond and bond.rebDate==analytics.rebDate:
                bond.analytics=analytics



    #create Index object
    myIndex=Index(reb_bond_lst, calc_bond_lst)

    for date in myIndex.calcBondSet.keys():
        myIndex.calcMTDreturn(date)

    for date in myIndex.calcBondSet.keys():
        for bond in myIndex.calcBondSet[date]:
            print(bond.MTDreturn, bond.analytics.annualYield)



'Run the Main function if the module is open(vs. imported)'
if __name__ == "__main__":
    Main()
