"""birinci alıştırma"""
x=8; y=3.2; z=8j+18; a="Hello World"; b=True;c=23<22; l=[1,2,3,4];
d={ "Name":"Jake","Age":27,"Adress":"Downtown"}
t=("Machine Learning", "Data Science")
s={"Python","Machine Learning","Data Science"}
##print(type(s))
"""ikinci alıştırma
Verilen string ifadenin tüm harflerini büyük harfe çeviriniz. Virgül ve nokta yerine space koyunuz, 
kelime kelime ayırınız
"""
text="The goal is to turn data into information, and information into insight."
a=text.replace(",","")
e=a.replace(".","")
new_string=e.split(" ")
b=[ind.upper() for ind in new_string]
##print(b)
"""3. soru """
lst=["D","A","T","A","S","C","I","E","N","C","E"]
##print(len(lst))
##print(lst[0],lst[10])
new=lst[0:4]
lst.pop(8)
lst.append(2)
lst.insert(8,"N")
""" 4. SORU """
dict={'Christian':["America",18],
'Daisy':["England",12],
'Antonio':["Spain",22],
'Dante':["Italy",25]}
##print(dict.keys())
#print(dict.values())
dict["Daisy"][1]=13
dict["Ahmet"]=["Turkey",24]
del dict['Antonio']
"""5. Soru """
l=[2,13,18,93,22]
def func(list):
    even=[] ;odd=[]
    [even.append(index) if index%2==0 else odd.append(index) for index in list ]
    return even,odd
even_list, odd_list=func(l)
"""6. soru"""
ogrenciler=["Ali","Veli","Ayşe","Talat","Zeynep","Ece"]
for index, stu in enumerate(ogrenciler):
    metin=f'Mühendislik Fakültesi {index+1} . öğrenci: {stu}'
    if index>2:
        metin=f'Tıp Fakültesi {index-2} . öğrenci: {stu}'
    #print(metin)
"""7. Soru"""
ders_kodu=["CMP1005","PSY1001","HUK1005","SEN2204"]
kredi=[3,4,2,4]
kontenjan=[30,75,150,25]
a=list(zip(ders_kodu,kredi,kontenjan))
for index, deger in enumerate(a):
    metin=f'Kredisi {deger[1]} olan {deger[0]} kodlu dersin kontenjanı {deger[2]} kişidir.'
    #print (metin)
"""8.soru"""
kume1=set(["data","python"])
kume2=set(["data","function","qcut","lambda","python","miuul"])
def function1(set1,set2):
    if set1.issuperset(set2):
        return set1.intersection(set2)
    else:
        return(set2-set1)
function1(kume1,kume2)
