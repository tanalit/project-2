class exfile:
    def __init__(self, mcode, mname, mno, mtype, pcode, pname, acode, aname, tcode, tname, orgcode, orgname, orgtype, remark, lastupdate, time, lat, long, log):  # Constructor
        self.mcode = mcode 
        self.mname = mname
        self.mno = mno
        self.mtype = mtype
        self.pcode = pcode
        self.pname = pname
        self.acode = acode
        self.aname = aname
        self.tcode = tcode
        self.tname = tname
        self.orgcode = orgcode
        self.orgname = orgname
        self.orgtype = orgtype
        self.remark = remark
        self.lastupdate = lastupdate 
        self.time = time
        self.lat = lat 
        self.long = long 
        self.log = log
    def __str__(self):
        return f'{self.mcode:9} {self.mname:20} {self.mno:2} {self.mtype:2} {self.pcode:2} {self.pname:16} {self.acode:5} {self.aname:19} {self.tcode:9} {self.tname:11} {self.orgcode:5} {self.orgname:10} {self.orgtype:16} {self.remark:6} {self.lastupdate:11} {self.time:9} {self.lat:5} {self.long:5} {self.log:5}'

# เปิดไฟล์ อ่านข้อมูล
with open('mm.txt', 'r', encoding='utf-8') as file:
    content = file.readlines()  # อ่านข้อความทั้งหมดในไฟล์

    textlist = []
    for line in content:
        data1, data2, data3 = line.split('S')
        NewData = data3.replace("(", "").replace(")", "").replace("'", "").replace(",", "").replace(";", "")
        mcode, mname, mno, mtype, pcode, pname, acode, aname, tcode, tname, orgcode, orgname, orgtype, remark, lastupdate, time, lat, long, log = NewData.split()
        textlist.append(exfile(mcode, mname, mno, mtype, pcode, pname, acode, aname, tcode, tname, orgcode, orgname, orgtype, remark, lastupdate, time, lat, long, log))
    
with open("mmHomework.txt", "w", encoding="utf-8") as file:
    for output in textlist:
        file.write(output.__str__() + "\n")
