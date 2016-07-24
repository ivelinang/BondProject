__author__ = 'ivelin.angelov'

#-------------------------------------------------------------------------------
# Author:       Ivelin Angelov
# Written:      23/03/2015
# Last Updated: 23/03/2015

# Filename:     ResultSet.py
# Python used:  2.7
#-------------------------------------------------------------------------------
# Description:  Class to read text file that contains SQL statemment,
# replace key variables, and retrieve data from SQL database
#-------------------------------------------------------------------------------
# Log of changes:
# ...
#-------------------------------------------------------------------------------

#import ODBC drivers (first need to install from: https://code.google.com/p/pyodbc/wiki/GettingStarted)
import pypyodbc
import os



#relative directory
SQLDir = os.path.join(os.path.dirname(__file__), "")

class ResultSet(object):
    ''' Class ResultSet to get data from sql
        sqlfile: file to contain sql query
        Connstr: connection string used to connect to sql DB (eg.:'DRIVER={SQL Server};SERVER=xxx;DATABASE=xxx')
    '''

    def __init__(self, sqlFile, connString):
        self.sql_file=sqlFile
        self.connection_string=connString
        self.data=None

    #getter
    @property
    def connection_string(self):
        return self.__connection_string

    #setter
    @connection_string.setter
    def connection_string(self, connString):
        if not isinstance(connString, str):
            raise TypeError('Expected a string')
        else:
            self.__connection_string=connString

    def readText(self):
        ''' method to get the text from a text file
            :return: string
        '''
        with open(self.sql_file) as file:
            text=file.read()

        return text

    def getData(self, *args):
        ''' main method to connect to DB and retrieve results
        :param args: arguments you want to replace in SQL statement
        :param symbol: symbol (string) you want to replace (usually "?") - hardcoded
        :return: SQL results
        '''

        #Read txt file
        SQLstr=self.readText()

        #List of variables to replace
        ReplaceSQL=[]
        for elem in args:
            ReplaceSQL.append(elem)

        #Replace ? with list values
        for var in ReplaceSQL:
            SQLstr=SQLstr.replace('?',str(var),1)

        #Execute SQL
        result=self.getSQLData(SQLstr)

        #return results
        self.data=result

    def getSQLData(self, sql_string, result_format=0):
        ''' method to connect to database via the pypyodbc package. Takes two inputs:
            SQLstr: SQL statement
            result_format: the format of the result
                0: list of dictionaries
                1: dictionary of lists

        :param sql_string: SQL query
        :return: sql results
        '''

        #lowercase
        pypyodbc.lowercase = False

        #make a connection to db
        cnxn = pypyodbc.connect(self.connection_string)

        #create a cursor
        cursor=cnxn.cursor()

        #execute string
        cursor.execute(sql_string)

        #fetch results
        rows=cursor.fetchall()

        #raise an error if empty results
        if len(rows)==0:
            raise RuntimeError('SQL return no results')

        #get column names
        columns = [column[0] for column in cursor.description]

        #Compile rows in a Dict
        if result_format==0:
            result=self.maptodict(rows, columns)
        else:
            result=self.compile(rows, columns)

        #Return results
        return result

    @staticmethod
    def compile(rows, columns):
        ''' static method to order the SQL results in a dictionary with keys being column names
        '''

        #Create Dict to store the results
        results={}

        #create key names in Dict with empty lists
        for nm in columns:
            results[nm]=[]

        #Fill the Dict with the SQL data
        for row in rows:
            for i in range(len(columns)):
                results[columns[i]].append(row[i])

        #return results, if no result, return dict with empty list
        return results

    @staticmethod
    def maptodict(rows, columns):
        ''' static method to transfor SQL results into list of dictionaries
        :param rows:
        :param columns:
        :return: list of dicts
        '''

        #create list to store results
        results=[]

        #map the rows and columns
        for row in rows:
            results.append(dict(zip(columns, row)))

        return results



def Main():

    sqlfile=os.path.join(SQLDir,"xxx.sql")
    Connstr='DRIVER={SQL Server};SERVER=xxx'
    rs=ResultSet(sqlfile, Connstr)
    cdate='2015-07-31'
    dataKey='xxx'
    rs.getData(cdate, dataKey)

    print(rs.data[0]['column'])
    #should get xxx

'Run the Main function if the module is open(vs. imported)'
if __name__ == "__main__":
    Main()
