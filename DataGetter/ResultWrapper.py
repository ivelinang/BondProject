__author__ = 'ivelin.angelov'

#-------------------------------------------------------------------------------
# Author:       Ivelin Angelov
# Written:      23/03/2015
# Last Updated: 23/03/2015

# Filename:     ResultSet.py
# Python used:  2.7
#-------------------------------------------------------------------------------
# Description:  Wrapper class that uses ResultSet from SQL to return result in
# a desired format - int, float, string, bool
#-------------------------------------------------------------------------------
# Log of changes:
# ...
#-------------------------------------------------------------------------------

from DataGetter.ResultSet import ResultSet
import datetime


class ResultSetWrapper(object):

    def __init__(self, resultSet):
        self.resultSet=resultSet

    #getter
    @property
    def resultSet(self):
        return self.__resultSet

    #setter
    @resultSet.setter
    def resultSet(self, rs):
        if not isinstance(rs, ResultSet):
            raise TypeError('Expected an object of class ResultSet')
        else:
            self.__resultSet=rs


    def getInteger(self, name, rowNum):
        ''' get SQL result in Integer format
        :param name:
        :param rowNum:
        :return:
        '''

        #get the value
        value=self.resultSet.data[rowNum][name]
        #check if Null + return int
        if value is None:
            return None
        else:
            return int(value)

    def getFloat(self, name, rowNum):
        ''' get SQL result in float format
        :param name:
        :param rowNum:
        :return:
        '''

        #get the value
        value=self.resultSet.data[rowNum][name]
        #check if Null + return float
        if value is None:
            return None
        else:
            return float(value)

    def getString(self, name, rowNum):
        ''' get SQL result in string format
        :param name:
        :param rowNum:
        :return:
        '''

        #get value
        value=self.resultSet.data[rowNum][name]
        #check if Null + return string
        if value is None:
            return None
        else:
            return str(value)

    def getBoolen(self, name, rowNum):
        ''' get SQL result in Boolen format
        :param name:
        :param rowNum:
        :return:
        '''

        #get value
        value=self.resultSet.data[rowNum][name]
        #check if Null + return boolen
        if value is None:
            return None
        else:
            return bool(value)

    def getDatetime(self, name, rowNum):
        ''' get SQL result in datetime.datetime format
        :param name:
        :param rowNum:
        :return:
        '''

        #get value
        value=self.resultSet.data[rowNum][name]
        #check if Null + return boolen
        if value is None:
            return None
        else:
            return value

def Main():

    import os
    #relative directory
    SQLDir = os.path.join(os.path.dirname(__file__), "")

    sqlfile=os.path.join(SQLDir,"xxx.sql")
    Connstr='DRIVER={SQL Server};SERVER=xxx'
    rs=ResultSet(sqlfile, Connstr)
    cdate='2015-07-31'
    dataKEy='xxx'
    rs.getData(cdate, dataKEy)

    newWrapper=ResultSetWrapper(rs)
    res = newWrapper.getString('column',0)
    print(res)
    #should get xxx

'Run the Main function if the module is open(vs. imported)'
if __name__ == "__main__":
    Main()
