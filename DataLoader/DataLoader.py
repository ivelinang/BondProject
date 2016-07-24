__author__ = 'ivelin.angelov'

#-------------------------------------------------------------------------------
# Author:       Ivelin Angelov
# Written:      23/03/2015
# Last Updated: 23/03/2015

# Filename:     DataLoader.py
# Python used:  2.7
#-------------------------------------------------------------------------------
# Description:  Serves as the main class for data querying. Different providers can be
# used, differing in the database pool data tables sourced
#-------------------------------------------------------------------------------
# Log of changes:
# ...
#-------------------------------------------------------------------------------

import os
from abc import ABCMeta, abstractmethod
import inspect

from DataGetter.ResultSet import ResultSet


#relative directory
SQLDir = os.path.join(os.path.dirname(__file__), "")

#----------------------------------------------------------------------------------------------------------------------
#               INTERFACE
#----------------------------------------------------------------------------------------------------------------------

class DataLoader(metaclass=ABCMeta):
    ''' Abstract Main class to retrieve data from SQL. Uses ResultSet class to get results in dict format.
        Has a number of methods to retrieve different types of data
        argument: database eg. xxx
        USED AS INTERFACE
    '''

    #CONSTANTS
    CONNECTION_STRING='DRIVER={SQL Server};SERVER=xxx'
    #Dictionary
    MethodMapper={}


    @abstractmethod
    def __init__(self):
        pass

    #@abstractmethod
    def getData(self, SQL_FILE, dataDate, dataKey):
        ''' universal method to get data from DB based on file, date, key
        :param SQL_FILE:
        :param dataDate:
        :param dataKey:
        :return:
        '''

        #create ResultSet object
        rs=ResultSet(SQL_FILE, self.CONNECTION_STRING)

        #get data
        rs.getData(dataDate, dataKey)

        return rs

    #@abstractmethod
    def getCalcDayRefData(self, dataDate, dataKey ):
        ''' get reference Data for a calculation day
        :param dataDate:
        :param dataKey:
        :return: dict of results, with keys as column names
        '''

        #CONSTANT for query file
        filename=inspect.stack()[0][3]  #the name of the method - used to map to sql file
        sqlname=self.MethodMapper[filename]
        SQL_FILE=os.path.join(SQLDir,sqlname)

        #use getData method
        rs= self.getData(SQL_FILE, dataDate, dataKey)

        return rs

    #@abstractmethod
    def getCalcDayAnalyticsData(self, dataDate, dataKey):
        ''' get analytics Data for a calc day
        :param dataDate:
        :param dataKey:
        :return:
        '''

        #CONSTANT for query file
        filename=inspect.stack()[0][3] #the name of the method - used to map to sql file
        sqlname=self.MethodMapper[filename]
        SQL_FILE=os.path.join(SQLDir,sqlname)

        #use getData method
        rs= self.getData(SQL_FILE, dataDate, dataKey)

        return rs

    #@abstractmethod
    def getRebDayRefData(self, dataDate, dataKey):
        ''' get reference data on reb day
        :param dataDate:
        :param dataKey:
        :return:
        '''

        #CONSTANT for query file
        filename=inspect.stack()[0][3] #the name of the method - used to map to sql file
        sqlname=self.MethodMapper[filename]
        SQL_FILE=os.path.join(SQLDir,sqlname)

        #use getData method
        rs= self.getData(SQL_FILE, dataDate, dataKey)

        return rs

    #@abstractmethod
    def getRebDayAnalyticsData(self, dataDate, dataKey):
        ''' get analytics data on reb day
        :param dataDate:
        :param dataKey:
        :return:
        '''

        #CONSTANT for query file
        filename=inspect.stack()[0][3] #the name of the method - used to map to sql file
        sqlname=self.MethodMapper[filename]
        SQL_FILE=os.path.join(SQLDir,sqlname)

        #use getData method
        rs= self.getData(SQL_FILE, dataDate, dataKey)

        return rs

#----------------------------------------------------------------------------------------------------------------------
#                   IMPLEMENTATION
#----------------------------------------------------------------------------------------------------------------------

class DataLoaderQA(DataLoader):
    ''' Load data from QA
    '''

    #override constant - conn string
    CONNECTION_STRING='DRIVER={SQL Server};SERVER=xxx'
    #Dict
    MethodMapper={}
    MethodMapper['getCalcDayRefData']='xxx1.sql'
    MethodMapper['getCalcDayAnalyticsData']='xxx2.sql'
    MethodMapper['getRebDayRefData']='xxx3.sql'
    MethodMapper['getRebDayAnalyticsData']='xxx4.sql'

    def __init__(self):
        super(DataLoaderQA, self).__init__()


#----------------------------------------------------------------------------------------------------------------------
#                   IMPLEMENTATION
#----------------------------------------------------------------------------------------------------------------------

class DataLoaderProd(DataLoaderQA):
    ''' Load data from PROD
    '''

    #override constant - conn string
    CONNECTION_STRING='DRIVER={SQL Server};SERVER=xxx'

    #Dict
    #same as QA - assume same tables an QA and PROD
    
    def __init__(self):
        super(DataLoaderProd, self).__init__()



def Main():

    dataload=DataLoaderProd()
    print(dataload.CONNECTION_STRING)
    CalcDate='2015-07-31'
    dataKey='xxx'
    result=dataload.getCalcDayRefData(CalcDate, dataKey)

    print(result.data[0]['column'])

    dataload=DataLoaderQA()
    print(dataload.CONNECTION_STRING)
    CalcDate='2015-06-30'
    dataKey='xxx'
    result=dataload.getRebDayRefData(CalcDate, dataKey)

    print(result.data[0]['column'])

'Run the Main function if the module is open(vs. imported)'
if __name__ == "__main__":
    Main()
