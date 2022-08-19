import xml.etree.ElementTree as ET
from dbhandler import DBHandler

class MainProcess(DBHandler):
    def __init__(self):
        self.book_list= []
        
    def getDataFromXml(self):
        self.tree = ET.parse('books.xml')
        root = self.tree.getroot()
        #print(root.tag)

        for child in root.findall("book"):
            #print(child.attrib['id'])
            if len(child):
                each_book_detail = {}
                each_book_detail.update(child.attrib)
                for subChild in child:
                    #print(subChild.text)
                    each_book_detail[subChild.tag] = subChild.text
                self.book_list.append(each_book_detail)
        #xprint(self.book_list)
    
    def putDataToTable(self):
        if len(self.book_list) == 0:
            print("book_list is empty. Exiting!!!")
            return 0
        
        
        
        for bookIter in self.book_list:
            columns=', '.join(bookIter.keys())
            placeholders = ', '.join(['%s'] * len(bookIter))
            sql = "insert into Books1 ({0}) values({1})".format(columns,placeholders)
            #print(sql)

            try:
                #print("establish connection")
                DBHandler.__init__(self)
                #self.__curosr.execute(sql, list(bookIter.values()))
                self.executeQuery(sql, list(bookIter.values()))
                #print("Insert ")

            except Exception as e:
                print('--------------------------------ERROR-----------------------')
                print('issue in execution. error:', e)
                return 0
            finally:
                #print('closing connection')
                self.close()
        return 1
    

        


if __name__ == "__main__":
    mpObj = MainProcess()
    mpObj.getDataFromXml()
    returnVal = mpObj.putDataToTable()
    if returnVal:
        print ("XML data successfully inserted to db")
    else:
        print ("XML data failed to insert to db")