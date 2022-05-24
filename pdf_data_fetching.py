#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pdfplumber
import PyPDF2
import csv

file = open('104_Whimsical_Ct___Residential_Report.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(file)
pages = pdfReader.numPages
pdf = pdfplumber.open('104_Whimsical_Ct___Residential_Report.pdf')

for i in range(pages):
#     page = pdfReader.getPage(i)
#     print("Page no:",i)
    page = pdf.pages[i]
    text = page.extract_text()
    print(text)
pdf.close()

with open('sabaa.csv', 'w',newline="",encoding="UTF-8") as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(['Area', 'parts','Action','Inspection method','Roof Type/style','Coverings Material',
                    'Roof Drainage systems Gutter_Material','Flashings Material','Deficiencies','Recommendation'])     

rr=[]
first=[]
second =[]
area=[]
table_data=[]
action =[]
Inspection_method=[]
roof_type=[]
Coverings_Material=[]
Roof_Drainage=[]
Flashings_Material=[]
Deficiencie=[]
Recommendations=[]
arr=[]
for i in range(pages):
    page = pdf.pages[i]
    text = page.extract_text()
#     print(text)
    if '104 Whimsical Ct Keith Ramsey' in text:
        rr.append(text)
        if  'INSPECTION DETAILS' in text:
            first.append(text)
        if  'ROOF' in text:
            second=text.split('\n')
#             print(second)
            bejo=False
            for ch in second:
#                 print(ch)
                if "." in ch:
                    if '2.2.1 Roof Drainage Systems' not in ch and 'Extensions blocks should be under downspout to prevent erosion.' not in ch and 'Contact a quali\x00ed professional.' not in ch:
                        table_data.append(ch)
                        parts=table_data
#                         print(parts)
#                         for a in parts:
#                             print(a)
                if 'ROOF' in ch:
                    area.append('Roof')
                    Area=area
                if 'IN' in ch:
                    if 'IN = Inspected NI = Not Inspected NP = Not Present D = De\x00ciencies' not in ch and 'GET IT DONE HOME INSPECTIONS Page 5 of 26' not in ch:
                        action.append(ch.split())
                        Action=action
#                         for b in Action[0]:
#                             print(b)
                if "Inspection Method Roof Type/Style Coverings: Material" in ch:
                    bejo=True
                if bejo==True:
                    arr.append(ch)
            arr
            ss=arr[1].split(' ')
            Inspection_method.append(ss[0])
            Inspection_methods=Inspection_method
            roof_type.append(ss[1])
            Roof_Type=roof_type
            new=ss[2],ss[3]
            Coverings_Material.append(new)
            Coverings_Materials=Coverings_Material
            Roof_Drainage.append(arr[4])
            Roof_Drainage_systems_Gutter_Material=Roof_Drainage
            aa=arr[3].split( )
            Flashings_Material.append(aa[1])
            Flashings_Materials=Flashings_Material
            ww=arr[6],arr[8],arr[9]
            Deficiencie.append(ww)
            Deficiencies=Deficiencie
            Recommendations.append(arr[10])
            Recommendation=Recommendations
            for a,b in zip(parts,Action[0]):
                pt=a
                jj=a.split(" ")
                fd=""
                for ii in jj:
                    if len(ii)>3:
                        fd=fd+ii+" "
                print(fd,"kjkkkkk")
                with open('sabaa.csv', 'a+',newline="",encoding="UTF-8") as csvFile:
                    writer = csv.writer(csvFile)
                    writer.writerow([Area,fd,b,Inspection_methods,Roof_Type,Coverings_Materials,Roof_Drainage_systems_Gutter_Material,Flashings_Materials,Deficiencies,Recommendation])


# In[ ]:




