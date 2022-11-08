import random
import time

#https://stackoverflow.com/questions/553303/generate-a-random-date-between-two-other-dates
def str_time_prop(start, end, time_format, prop):
    """Get a time at a proportion of a range of two formatted times.

    start and end should be strings specifying times formatted in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    """

    stime = time.mktime(time.strptime(start, time_format))
    etime = time.mktime(time.strptime(end, time_format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(time_format, time.localtime(ptime))


def random_date(start, end, prop):
    return str_time_prop(start, end, '%Y-%m-%d', prop)

def fuckEndLine(str):
    str1=''
    for c in str:
        if (c!='\n'):
            str1=str1+c
    return str1

def fuckEndLineforListOfStr(ListStr):
    for i in range(0,len(ListStr)):
        ListStr[i]=fuckEndLine(ListStr[i])
    return ListStr


def GenerateName():
    f1 = open('ten1.txt','r', encoding='utf-8')
    f2 = open('ten2.txt','r', encoding='utf-8')
    f3 = open('ten3.txt','r', encoding='utf-8')

    ListTen1=f1.readlines()
    ListTen2=f2.readlines()
    ListTen3=f3.readlines()

    ListTen1 = fuckEndLineforListOfStr(ListTen1)
    ListTen2 = fuckEndLineforListOfStr(ListTen2)
    ListTen3 = fuckEndLineforListOfStr(ListTen3)

    pos1 = random.randint(0,len(ListTen1)-1)
    ten1=ListTen1[pos1]
    pos2 = random.randint(0,len(ListTen2)-1)
    ten2=ListTen2[pos2]
    pos3 = random.randint(0,len(ListTen3)-1)
    ten3=ListTen3[pos3]


    f1.close()
    f2.close()
    f3.close()
    
    return ten1+' '+ten2+' '+ten3

def randomTinhThanh():
    f = open('tinhthanh.txt','r',encoding='utf-8')

    listTinh = f.readlines()
    listTinh = fuckEndLineforListOfStr(listTinh)

    f.close()

    return(listTinh[random.randint(0,len(listTinh)-1)])


#https://gist.github.com/J2TEAM/9992744f15187ba51d46aecab21fd469
s1 = u'ÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚÝàáâãèéêìíòóôõùúýĂăĐđĨĩŨũƠơƯưẠạẢảẤấẦầẨẩẪẫẬậẮắẰằẲẳẴẵẶặẸẹẺẻẼẽẾếỀềỂểỄễỆệỈỉỊịỌọỎỏỐốỒồỔổỖỗỘộỚớỜờỞởỠỡỢợỤụỦủỨứỪừỬửỮữỰựỲỳỴỵỶỷỸỹ'
s0 = u'AAAAEEEIIOOOOUUYaaaaeeeiioooouuyAaDdIiUuOoUuAaAaAaAaAaAaAaAaAaAaAaAaEeEeEeEeEeEeEeEeIiIiOoOoOoOoOoOoOoOoOoOoOoOoUuUuUuUuUuUuUuYyYyYyYy'
def remove_accents(input_str):
	s = ''
	#print(input_str.encode('utf-8'))
	for c in input_str:
		if c in s1:
			s += s0[s1.index(c)]
		else:
			s += c

	return s

def remove_space(input_str):
    s=''
    for c in input_str:
        if c!=' ':
            s=s+c
    return s

def nameToEmail(input_str):
    s = input_str
    s = remove_accents(s)
    s = remove_space(s)

    return s + '@gulamail.com'


print(random_date("2008-1-1", "2009-1-1", random.random()))

#randomTinhThanh() -> string tinh thanh

#remove_accents(input_str) -> string but have no accents

#INSERT INTO `student_management`.`students` (`id`, `name`, `gender`, `date`, `address`, `email`, `classId`, `createdAt`, `updatedAt`) VALUES ('1', 'Võ Anh Kiệt', '1', '2022-08-11 00:00:00', 'Tân Hồng', 'kietgula@gmail.com', '1', '2022-08-11 00:00:00', '2022-08-11 00:00:00');

fi = open('studentInsert.txt','w',encoding='utf-8')

ID=0
for classID in range(1,4):
    for i in range(1,21):
        ID=ID+1
        name = GenerateName()
        gender = random.randint(0,1)
        
        date = random_date("2006-1-1", "2008-1-1", random.random()) + ' 00:00:00'
        
        address = randomTinhThanh()
        email = nameToEmail(name)


        fi.write("INSERT INTO `student_management`.`students` (`id`, `name`, `gender`, `date`, `address`, `email`, `classId`, `createdAt`, `updatedAt`) VALUES ('"+ str(ID) + "', '"+ name +"', '"+ str(gender) + "', '"+ date +"', '"+ address  +"', '"+ email +"', '"+ str(classID) +"', '2022-08-11 00:00:00', '2022-08-11 00:00:00');\n")

for classID in range(4,7):
    for i in range(1,21):
        ID=ID+1
        name = GenerateName()
        gender = random.randint(0,1)
        
        date = random_date("2005-1-1", "2007-1-1", random.random()) + ' 00:00:00'
        
        address = randomTinhThanh()
        email = nameToEmail(name)


        fi.write("INSERT INTO `student_management`.`students` (`id`, `name`, `gender`, `date`, `address`, `email`, `classId`, `createdAt`, `updatedAt`) VALUES ('"+ str(ID) + "', '"+ name +"', '"+ str(gender) + "', '"+ date +"', '"+ address  +"', '"+ email +"', '"+ str(classID) +"', '2022-08-11 00:00:00', '2022-08-11 00:00:00');\n")

for classID in range(7,10):
    for i in range(1,21):
        ID=ID+1
        name = GenerateName()
        gender = random.randint(0,1)
        
        date = random_date("2004-1-1", "2006-1-1", random.random()) + ' 00:00:00'
        
        address = randomTinhThanh()
        email = nameToEmail(name)


        fi.write("INSERT INTO `student_management`.`students` (`id`, `name`, `gender`, `date`, `address`, `email`, `classId`, `createdAt`, `updatedAt`) VALUES ('"+ str(ID) + "', '"+ name +"', '"+ str(gender) + "', '"+ date +"', '"+ address  +"', '"+ email +"', '"+ str(classID) +"', '2022-08-11 00:00:00', '2022-08-11 00:00:00');\n")


fi.close()