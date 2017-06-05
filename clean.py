import csv
class Solution(object):
    #��csv
    def readCsv(self,csv_name):
        csv_reader = csv.reader(open(csv_name))
        return csv_reader
    
    def cleanData(self,csv_reader):
        out = open(r'E:\stock\data_new.csv', 'w', newline='')
        csv_writer = csv.writer(out, dialect='excel')
        for row in csv_reader:
            data=[]
            #��x_0��x_49��������ȱʧ�Ĵ���ȱʧ��������ǰһ���������x_0ȱʧ����������ҵĵ�һ�����ݲ�
            for i in range(3,53):
                if(row[i]=="" ):
                    #x_0ȱʧ
                    if(i==3):
                        for j in row[3:53]:
                            if j!="":
                                row[i]=j
                                break
                    #��ǰһ����
                    else:
                        row[i]=row[i-1]
            #ֻ����id,x_0,..x_49,y
            data.append(row[0])
            for j in row[3:53]:
                data.append(j)
            data.append (row[1])
            csv_writer.writerow(data)
    #дcsv
    def writeCsv(self,csv_name,data):
        out = open(csv_name, 'w', newline='')
        csv_writer = csv.writer(out, dialect='excel')
        csv_writer.writerow(data)

if __name__ =='__main__':
    s = Solution()
    csv_reader=s.readCsv(r'E:\stock\data.csv')
    s.cleanData(csv_reader)

