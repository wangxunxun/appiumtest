'''
Created on 2015年8月23日

@author: wangxun
'''
import httplib2
from urllib.parse import urlencode
import json
import xlwt
import sqlite3
import xlrd
from dominate.tags import table
import datetime
import pymysql


class ReadSelectData():
    def __init__(self,excelpath,tablename):
        self.excelpath = excelpath        
        self.data = xlrd.open_workbook(self.excelpath)
        self.table = self.data.sheet_by_name(tablename)
        
    def readTable(self):
        nrows = self.table.nrows
        header = self.table.row_values(0)
        tabledata = []
        pages = []
        elements = []
        i = 1        
        while i < nrows:
            rdata = self.table.row_values(i)
            element = []
            if rdata[0] and rdata[1]:
                location = {}                       
                location.setdefault(header[2],rdata[2])
                location.setdefault(header[3],rdata[3])
                element.append(rdata[1])
                element.append(location)
                elements.append(element)
                pages.append(rdata[0])
            if not rdata[0] and rdata[1]:
                location = {}                       
                location.setdefault(header[2],rdata[2])
                location.setdefault(header[3],rdata[3])
                element.append(rdata[1])
                element.append(location)
                elements.append(element)               
            i=i+1
        tabledata.append(pages)
        tabledata.append(elements)
        return tabledata
    
    def getPagedis(self):

        nrows = self.table.nrows
        i = 1        
        dis = []
        while i < nrows:
            rdata = self.table.row_values(i)
            if rdata[0]:
                dis.append(i)
            i = i+1
        dis.append(nrows)
        return dis
    
    def count(self,start,end):

        i = 1
        j = 1
        first = 0
        second = 0
        while i <start:
            if self.table.cell(i,1).value:
                first = first+1
            i = i+1
        while j < end:
            if self.table.cell(j,1).value:
                second = second+1
            j = j+1
        return second - first
    
    def realPage(self):
        dis = self.getPagedis()
        pagecount = []
        i = 0
        while i <len(dis)-1:
            count = self.count(dis[i], dis[i+1])
            pagecount.append(count)
            i = i+1            
        return pagecount
    
    def real(self):
        data = self.realPage()
        new = [0]
        i = 0        
        while i <len(data):
            c = 0
            j = 0
            while j<=i:
                c = c +data[j]
                j = j +1
            new.append(c)
            i = i+1
        return new
        
    
    def getdata(self):
        tabledata = self.readTable()
        real = self.real()
        i = 0
        data = []
        while i <len(real)-1:
            data.append(tabledata[1][real[i]:real[i+1]])
            i = i+1
        d = {}
        j = 0
        while j <len(real)-1:
            a = {}
            for l in data[j]:
                a.setdefault(l[0],l[1])
                d.setdefault(tabledata[0][j],a)
            j = j+1
        return d
        

class ReadTestCaseData():
    def __init__(self,excelpath,tablename):
        self.excelpath = excelpath        
        self.data = xlrd.open_workbook(self.excelpath)
        self.table = self.data.sheet_by_name(tablename)                
        
    def readTable(self):
        nrows = self.table.nrows
        header = self.table.row_values(0)
        data = []
        i = 1        
        while i < nrows:
            rdata = self.table.row_values(i)
            if rdata[0]:
                if isinstance(rdata[0],float):
                    rdata[0] = int(rdata[0])
                j = 0
                row = {}
                while j <len(header):
                    row.setdefault(header[j],rdata[j])
                    j = j+1
                data.append(row)
            i = i+1
        return data
                    