from ast import AsyncFunctionDef
import wfdb
import numpy as np
from pymongo import MongoClient

test = False

class Metadata:
    def __init__(self, name = '', desc = '', num = 0, unit = '', link = ''):
        #4 metadata values
        self.metadata = {'Database': name,
                         'Description': desc,
                         'Amount': num,
                         'Unit': unit,
                         'Link': link}
    
    def getMetadata(self):
        return self.metadata
    
    def setDownload(self, link):
        self.metadata.update({'Link': link})

# class Record:
#     def __init__(self, db = None, rec = None):
#         if (rec is not None) and (db is not None):
#             self.rec = wfdb.io.get_record_list(db, records='all')

class Dataset:
    def __init__(self):
        self.client = MongoClient("mongodb+srv://avengineers461L:MwycDXNBxKObOc3I@cluster0.s12ua.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
        self.db = np.array(wfdb.io.get_dbs())
        self.__db = self.client.Project461L
        if(test):
            print("Init", np.shape(self.db))

    def getDatasetDBList(self):
        # Returns a list of all database names
        dataset = self.db[:,0]
        if (test):
            print(len(dataset))
            # print(dataset)
        return dataset
    
    def getRecordList(self, db):
        #Gets a list of all the records in daatabase
        rec = wfdb.io.get_record_list(db, records='all')
        if (test):
            print(db, rec)
        return rec

    # def getRecordMetadata(self, db, record):
    #     #Gets predetermined metadata values for a record
    #     #Currently abandoned
    #     #Suggestion: separate into dictionary/individual value
    #     rec = wfdb.rdrecord(record, pn_dir=(db+""))
    #     metadata = [rec.record_name, rec.comments, rec.sig_name, rec.sig_len, rec.units, rec.samps_per_frame]
    #     for i in range(0, len(metadata)):
    #         if isinstance(metadata[i], list):
    #             metadata[i] = metadata[i][0]
                
    #     if (test):
    #         print("\ngetRecordMetadata", metadata)
    #     return metadata
    
    def getDBMetadata(self, db):
        location = np.where(self.db == db)
        desc = self.db[location[0][0]][1]
        recList = self.getRecordList(db)
        num = len(recList)
        rec = recList[0]
        folder = ""
        split = rec.split("/")
        if (len(split) > 1):
            folder = "/" + split[0]
            rec = split[1]
        rec = wfdb.rdrecord(rec, pn_dir=(db+folder))
        unit = rec.units[0]
        metadata = Metadata(db, desc, num, unit)
        if (test):
            print("\nDB Metadata:", metadata.getMetadata())
        return metadata

    # def updateFive(self):
    #     #Hard coded 5 records from 5 datasets, 25 values total
    #     #1) aami-ec13: aami3a, aami3b, aami3c, aami3d, aami4a
    #     db = 'aami-ec13'
    #     record = 'aami3a'
    #     metadata = self.getRecordMetadata(db, record)
    #     if (test):
    #         print ("\nupdateFive", metadata)

    # def getFive(self):
    #     ds = []
    #     for i in range(0, 5):
    #         ds.append()
    
    #Five dbs:
    def getFirst(self):
        #Hard coded dataset:
        #
        db = 'aami-ec13'
        dl = 'https://physionet.org/static/published-projects/aami-ec13/ansiaami-ec13-test-waveforms-1.0.0.zip'
        metadata = self.getDBMetadata(db)
        metadata.setDownload(dl)
        return metadata.getMetadata()

    def getSecond(self):
        #Hard coded dataset:
        #
        db = 'ahadb'
        dl = 'https://physionet.org/static/published-projects/ahadb/aha-database-sample-excluded-record-1.0.0.zip'
        metadata = self.getDBMetadata(db)
        metadata.setDownload(dl)
        return metadata.getMetadata()

    def getThird(self):
        #Hard coded dataset:
        #https://physionet.org/content/iafdb/1.0.0/
        db = 'iafdb'
        dl = 'https://physionet.org/static/published-projects/iafdb/intracardiac-atrial-fibrillation-database-1.0.0.zip'
        metadata = self.getDBMetadata(db)
        metadata.setDownload(dl)
        return metadata.getMetadata()


    def getFourth(self):
        #Hard coded dataset:
        #
        db = 'ltstdb'
        dl = 'https://physionet.org/static/published-projects/ltstdb/long-term-st-database-1.0.0.zip'
        metadata = self.getDBMetadata(db)
        metadata.setDownload(dl)
        return metadata.getMetadata()


    def getFifth(self):
        #Hard coded dataset:
        #https://physionet.org/content/taichidb/1.0.2/
        db = 'taichidb'
        dl = 'https://physionet.org/static/published-projects/taichidb/tai-chi-physiological-complexity-and-healthy-aging-gait-1.0.2.zip'
        metadata = self.getDBMetadata(db)
        metadata.setDownload(dl)
        return metadata.getMetadata()

# ds = Dataset()
# print("\n\n")
# # print(ds.getDatasetDBList())
# db1 = ds.getDatasetDBList()[0]
# # print(ds.getRecordList(db1))
# rec1 = ds.getRecordList(db1)[0]
# # print(ds.getRecordMetadata(db1,rec1))
# # ds.updateFive()
# ds.getDBMetadata(db1)

# db1 = ds.getFirst()
# print("1", db1)
# db2 = ds.getSecond()
# print("2", db2)
# db3 = ds.getThird()
# print("3", db3)
# db4 = ds.getFourth()
# print("4", db4)
# db5 = ds.getFifth()
# print("5", db5)