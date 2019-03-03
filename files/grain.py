import nltk
import json
discuss=[]
final_data=[]
medicine_names=[]
x=set()
z=list()
count=0
#f1=open("SIH_keywords_test2.json","w")
import re  
import sys 
y,final=[],[]
if __name__ == '__main__':
    with open("temp/%s"%(sys.argv[1]),"r",encoding='utf8') as json_data:
    #with open("test3.txt","r") as json_data: 
        text = json_data.read()
        #print(text)
    with open('all_medical_terms.txt',"r") as f:
        dictionary=f.read().split("\n")
    with open('all_medicine_names.txt',"r") as f2:
        medical_dictionary=f2.read().split("\n")
        #mdeical_dictionary=list(medicine_dictionary)
        medicine_dictionary=[x.lower() for x in medical_dictionary]
    #print(dictionary)
    final_data=text.split("\n")
    scrap_list=(open("scrap_list.txt","r")).read().split("\n")
    #print(dictionary)
    final_data=text.split("\n")
    for i in final_data:
        i=str(re.sub(r"\n","",str(i)))
        for j in scrap_list:
            try:
                i=str(re.sub(r"%s"%(j),"",i))
            except:
                pass  
        
        #print(final_data)
    date=re.findall(r"\d{1,2}\s{0,1}\/\s{0,1}\d{1,2}\s{0,1}\/\s{0,1}\d{2,4}",text)
    time=re.findall(r"\d{1,2}\s{0,1}[:|.]\s{0,1}\d{1,2}\s{0,1}[:|.]\s{0,1}\d{2}\s{0,1}[AaPp]{0,1}[Mm]{0,1}",text)
    Doctor=re.findall(r"\bDr\b\s{0,1}\.\s{0,1}[A-Za-z]+[a-zA-Z]*\s[A-Za-z]+[a-zA-Z]*",text)
    weight=re.findall(r"(\d{2,3}\s{0,1})[Kk][gG]",text)
    age=re.findall(r"(\d{2,3}\s{0,1})[Yy][eE][aA][Rr][sS]{0,1}",text)
    speciality=re.findall(r"\s{0,1}\bSpeciality\b\s{0,1}:\s{0,1}([A-Za-z]+[a-zA-Z]*\s[A-Za-z]+[A-Z]*)",text)
    age2=re.findall(r"\bAge\b\s{0,2}:\s{0,1}(\d\d)",text)
    patient=re.findall(r"\bPatient Name\b\s{0,1}:\s{0,1}([A-Za-z]+[a-zA-Z]*\s[A-Za-z]+[a-zA-Z]*\s[A-Z]*\s)",text)
    data=" ".join(final_data)
    gender=re.findall(r"\bGender\b\s{0,2}:\s{0,2}([A-Za-z]+[a-zA-Z]*)",data)
    gender2=re.findall(r"[Ff]{0,1}[eE]{0,1}[Mm][aA][lL][Ee]",text)
    List=['Appointment','Date','Time', 'Gender', 'Age', 'Pain', 'Consultant', 'Female', 'Patient',
          'Speciality','Abdominal', 'Bloating', "Established", 'Burning', 'Appetite', 'Average', "Established", "National", "Health", "Education", "Society", "Maximum", "Midnight", "Hospital", "Medical", "Research", "Centre"]
    
    medicine=[]
    dictionary=list(set.union(set(dictionary),set(medicine_dictionary)))
    for i in nltk.word_tokenize(data):
        
        try:
            if str(i)[0].isupper() and str(i)[1].islower() and len(i)>5 and (str(i) not in List) and (str(i).lower() in dictionary):
                medicine.append(i)
        except:
            pass
    '''    
    print(medicine)
    print(date)
    print(time)
    print(Doctor)
    print(weight)
    print(age)
    print(patient)
    print(gender)
    print(final_data)
    '''
    k=str(re.sub(r"\s{1,2}G\s{0,1}/\s{0,1}E\s{1,2}"," General Expression ",str(data)))
    k1=str(re.sub(r"\s{1,2}c\s{0,1}/\s{0,1}o\s{1,2}"," complaint of ",str(k)))
    k2=str(re.sub(r"\s{1,2}B\s{0,1}/\s{0,1}L\s{1,2}"," bilateral ",str(k1)))
    k3=str(re.sub(r"\s{1,2}E\s{0,1}/\s{0,1}O\s{1,2}"," evidence of ",str(k2)))
    k4=str(re.sub(r"\s{1,2}F\s{0,1}/\s{0,1}H\s{1,2}"," Family history ",str(k3)))
    k5=str(re.sub(r"\s{1,2}F\s{0,1}/\s{0,1}[Uu]\s{1,2}"," Follow up ",str(k4)))
    k6=str(re.sub(r"\s{1,2}H\s{0,1}/\s{0,1}o\s{1,2}"," History of ",str(k5)))
    k7=str(re.sub(r"\s{1,2}B\s{0,1}E\s{1,2}"," both eyes ",str(k6)))
    k8=str(re.sub(r"\s{1,2}B\s{0,1}L\s{1,2}"," before lunch ",str(k7)))
    k9=str(re.sub(r"\s{1,2}B\s{0,1}P\s{1,2}"," blood pressure ",str(k8)))
    k10=str(re.sub(r"\s{1,2}Bs{0,1}s\s{1,2}"," Biopsy ",str(k9)))
    k11=str(re.sub(r"\s{1,2}C\s{0,1}[tT]\s{1,2}"," continue ",str(k10)))
    k12=str(re.sub(r"\s{1,2}D\s{0,1}N\s{1,2}"," Diabetic neuropathy ",str(k11)))
    k13=str(re.sub(r"\s{1,2}D\s{0,1}R\s{1,2}"," Diabetic retinopathy ",str(k12)))
    k14=str(re.sub(r"\s{1,2}G\s{0,1}A\s{1,2}"," general anesthesia ",str(k13)))
    k15=str(re.sub(r"\s{1,2}G\s{0,1}C\s{1,2}"," General Condition ",str(k14)))
    k16=str(re.sub(r"\s{1,2}H\s{0,1}S\s{1,2}"," at bedtime ",str(k15)))
    k17=str(re.sub(r"\s{1,2}S\s{0,1}A\s{1,2}"," Spinal anesthesia ",str(k16)))
    k18=str(re.sub(r"\s{1,2}R\s{0,1}R\s{1,2}"," Respiratory Rate ",str(k17)))
    k19=str(re.sub(r"\s{1,2}P\s{0,1}V\s{1,2}"," per vaginal ",str(k18)))
    k20=str(re.sub(r"\s{1,2}P\s{0,1}I\s{1,2}"," per rectum ",str(k19)))
    k21=str(re.sub(r"\s{1,2}P\s{0,1}O\s{1,2}"," per oral ",str(k20)))
    k22=str(re.sub(r"\s{1,2}O\s{0,1}U\s{1,2}"," both ears ",str(k21)))
    k23=str(re.sub(r"\s{1,2}O\s{0,1}H\s{1,2}"," past history ",str(k22)))
    k24=str(re.sub(r"\s{1,2}w\s{0,1}/\s{0,1}h\s{1,2}"," withold ",str(k23)))
    k25=str(re.sub(r"\s{1,2}w\s{0,1}/\s{0,1}c\s{1,2}"," without ",str(k24)))
    k26=str(re.sub(r"\s{1,2}T\s{0,1}/\s{0,1}T\s{1,2}"," treatment given ",str(k25)))
    k27=str(re.sub(r"\s{1,2}R\s{0,1}x\s{1,2}"," treatment given ",str(k26)))
    k28=str(re.sub(r"\s{1,2}s\s{0,1}/\s{0,1}p\s{1,2}"," status post ",str(k27)))
    k29=str(re.sub(r"\s{1,2}s\s{0,1}/\s{0,1}o\s{1,2}"," suggestive of ",str(k28)))
    k30=str(re.sub(r"\s{1,2}S\s{0,1}/\s{0,1}L\s{1,2}"," sublingual ",str(k29)))
    k31=str(re.sub(r"\s{1,2}S\s{0,1}/\s{0,1}E\s{1,2}"," Systematic Examination ",str(k30)))
    k32=str(re.sub(r"\s{1,2}s\s{0,1}/\s{0,1}c\s{1,2}"," subcutaneous ",str(k31)))
    k33=str(re.sub(r"\s{1,2}S\s{0,1}/\s{0,1}b\s{1,2}"," Seen by ",str(k32)))
    k34=str(re.sub(r"\s{1,2}r\s{0,1}/\s{0,1}o\s{1,2}"," Rule out ",str(k33)))
    k35=str(re.sub(r"\s{1,2}P\s{0,1}/\s{0,1}A\s{1,2}"," Per abdomen ",str(k34)))
    k36=str(re.sub(r"\s{1,2}O\s{0,1}/\s{0,1}H\s{1,2}"," Obstetric history ",str(k35)))
    k37=str(re.sub(r"\s{1,2}O\s{0,1}/\s{0,1}E\s{1,2}"," On examination ",str(k36)))
    k38=str(re.sub(r"\s{1,2}N\s{0,1}/\s{0,1}E\s{1,2}"," Local Examination ",str(k37)))
    k39=str(re.sub(r"\s{1,2}BBS\s{1,2}"," before breakfast ",str(k38)))
    k40=str(re.sub(r"\s{1,2}BID\s{1,2}"," two times a day ",str(k39)))
    k41=str(re.sub(r"\s{1,2}CNS\s{1,2}"," central nervous system ",str(k40)))
    k42=str(re.sub(r"\s{1,2}CVS\s{1,2}"," cardiovascular system ",str(k41)))
    k43=str(re.sub(r"\s{1,2}CXR\s{1,2}"," chest xray ",str(k42)))
    k44=str(re.sub(r"\s{1,2}DNB\s{1,2}"," diabetic neuropathy ",str(k43)))
    k45=str(re.sub(r"\s{1,2}DOR\s{1,2}"," discharge on request ",str(k44)))
    k46=str(re.sub(r"\s{1,2}Inv\s{1,2}"," investigation ",str(k45)))
    k47=str(re.sub(r"\s{1,2}NAD\s{1,2}"," no abnormality detected ",str(k46)))
    k48=str(re.sub(r"\s{1,2}NBA\s{1,2}"," nil by mouth ",str(k47)))
    k49=str(re.sub(r"\s{1,2}NED\s{1,2}"," no evidence of disease ",str(k48)))
    k50=str(re.sub(r"\s{1,2}POD\s{1,2}"," post operative day ",str(k49)))
    k51=str(re.sub(r"\s{1,2}SOS\s{1,2}"," as required ",str(k50)))
    k52=str(re.sub(r"\s{1,2}TID\s{1,2}"," thrice a day ",str(k51)))
    k53=str(re.sub(r"\s{1,2}TSR\s{1,2}"," to show report ",str(k52)))
    k54=str(re.sub(r"\s{1,2}WNL\s{1,2}"," within normal limits ",str(k53)))
    k55=str(re.sub(r"\s{1,2}DAMA\s{1,2}"," discharge against medical advice ",str(k54)))
    k56=str(re.sub(r"\s{1,2}a\s{0,1}/\s{0,1}w\s{1,2}"," associated with ",str(k55)))
    k57=str(re.sub(r"\s{1,2}HP\s{1,2}"," Histopathy ",str(k56)))
    k58=str(re.sub(r"\s{1,2}HPE\s{1,2}"," Histopathy ",str(k57)))
    k59=str(re.sub(r"\s{1,2}\u2191\s{1,2}"," increased value of tre ",str(k58)))
    k60=str(re.sub(r"\s{1,2}\u2193\s{1,2}"," decreased value of tre ",str(k59)))
    k61=str(re.sub(r"\s{1,2}#\s{1,2}"," present ",str(k60)))
    k62=str(re.sub(r"\s{1,2}a]\s{0,1}\.\s{0,1}c"," before meal (anti cibum) ",str(k61)))
    k63=str(re.sub(r"\s{1,2}act\s{0,1}\.\s{0,1}"," every other day ",str(k62)))
    k64=str(re.sub(r"\s{1,2}ap\s{1,2}"," before dinner ",str(k63)))
    k65=str(re.sub(r"\s{1,2}[bB][iI][dD]\s{1,2}"," twice a day (bis in die) ",str(k64)))
    k66=str(re.sub(r"\s{1,2}b\.i\.n."," twice a night (bis in night) ",str(k65)))
    k67=str(re.sub(r"\s{1,2}Bx\s{1,2}"," biospsy ",str(k66)))
    k68=str(re.sub(r"\s{1,2}h\.s\.\s{1,2}"," at bedtime ",str(k67)))
    k69=str(re.sub(r"\s{1,2}P\.O\.\s{1,2}"," orally (per oral) ",str(k68)))
    k70=str(re.sub(r"\s{1,2}t\.i\.d\s{1,2}"," three times a day (three in die) ",str(k69)))
    k71=str(re.sub(r"\s{1,2}top\s{1,2}"," topically (locally) ",str(k70)))
    k72=str(re.sub(r"\s{1,2}UTI\s{1,2}"," urinary tract infection ",str(k71)))
    k73=str(re.sub(r"\s{1,2}OD\s{1,2}"," once daily ",str(k72)))
    k74=str(re.sub(r"\s{1,2}OCD\s{1,2}"," obsessive compulsive disorder ",str(k73)))
    #k75=str(re.sub(r"\s{1,2}a.m\.\s{1,2}"," morning ",str(k74)))
    k76=str(re.sub(r"\s{1,2}a\s{0,1}\.\s{0,1}s\s{0,1}\.\s{1,2}"," left ear ",str(k74)))
    k77=str(re.sub(r"\s{1,2}cap\s{1,2}"," capsule ",str(k76)))
    k78=str(re.sub(r"\s{1,2}a\s{0,1}\.\s{0,1}u\s{0,1}\.\s{1,2}"," each ear ",str(k77)))
    k79=str(re.sub(r"\s{1,2}bis\s{1,2}"," twice ",str(k78)))
    k80=str(re.sub(r"\s{1,2}CBC\s{1,2}"," complete blood count ",str(k79)))
    k81=str(re.sub(r"\s{1,2}D\s{1,2}"," Dose ",str(k80)))
    k82=str(re.sub(r"\s{1,2}e\s{0,1}\.\s{0,1}m\s{0,1}\.\s{0,1}p\s{0,1}\.\s{1,2}"," as directed ",str(k81)))
    k83=str(re.sub(r"\s{1,2}HT\s{1,2}"," Hypertension ",str(k82)))
    k84=str(re.sub(r"\s{1,2}IM\s{1,2}"," Intramuscular ",str(k83)))
    k85=str(re.sub(r"\s{1,2}IV\s{1,2}"," Intravenous ",str(k84)))
    k86=str(re.sub(r"\s{1,2}liq\s{1,2}"," liquid ",str(k85)))
    k87=str(re.sub(r"\s{1,2}et\s{1,2}"," and ",str(k86)))
    k88=str(re.sub(r"\s{1,2}m\s{0,1}\.\s{0,1}t\s{0,1}\.\s{0,1}n\s{1,2}"," morning and night ",str(k87)))
    k89=str(re.sub(r"\s{1,2}N\s{0,1}\.\s{0,1}R\s{0,1}\.\s{1,2}"," do not repeat ",str(k88)))
    k90=str(re.sub(r"\s{1,2}NPO\s{1,2}"," nothing by mouth ",str(k89)))
    k91=str(re.sub(r"\s{1,2}P\s{0,1}\.\s{0,1}C\s{1,2}"," after meal (pose cibum) ",str(k90)))
    k92=str(re.sub(r"\s{1,2}q\s{1,2}"," every ",str(k91)))
    k93=str(re.sub(r"\s{1,2}qd\s{1,2}"," everyday ",str(k92)))
    k94=str(re.sub(r"\s{1,2}qid\s{1,2}"," four times a day (quadri in) ",str(k93)))
    k95=str(re.sub(r"\s{1,2}R\s{1,2}"," rectal ",str(k94)))
    k96=str(re.sub(r"\s{1,2}SOB\s{1,2}"," shortness of breath ",str(k95)))
    k97=str(re.sub(r"\s{1,2}sol\s{1,2}"," solution ",str(k96)))
    k98=str(re.sub(r"\s{1,2}ss\s{0,1}\.\s{1,2}"," one-half ",str(k97)))
    k99=str(re.sub(r"\s{1,2}stat\s{1,2}"," immediately ",str(k98)))
    k100=str(re.sub(r"\s{1,2}sup\s{1,2}"," suppository ",str(k99)))
    k101=str(re.sub(r"\s{1,2}susp\s{1,2}"," suspension ",str(k100)))
    k102=str(re.sub(r"\s{1,2}syr\s{1,2}"," syrup ",str(k101)))
    k103=str(re.sub(r"\s{1,2}tab\s{1,2}"," tablet ",str(k102)))
    k104=str(re.sub(r"\s{1,2}tbsp\s{1,2}"," tablespoon ",str(k103)))
    k105=str(re.sub(r"\s{1,2}tiw\s{1,2}"," three times a week ",str(k104)))
    k106=str(re.sub(r"\s{1,2}tsp\s{1,2}"," teaspoon ",str(k105)))
    k107=str(re.sub(r"\s{1,2}URI\s{1,2}"," upper respiratory infecction ",str(k106)))
    k108=str(re.sub(r"\s{1,2}w\s{0,1}/\s{1,2}"," with ",str(k107)))
    k109=str(re.sub(r"\s{1,2}w\s{0,1}/o\s{1,2}"," without ",str(k108)))
    k110=str(re.sub(r"\s{1,2}x\s{1,2}"," times ",str(k109)))
    k111=str(re.sub(r"\s{1,2}y\s{0,1}\.\s{0,1}o\s{1,2}"," year old ",str(k110)))
    k112=str(re.sub(r"\s{1,2}qh\s{1,2}"," every hour ",str(k111)))
    try:
        k113=re.sub(r"\s{1,2}\bPain Score\b\s{1,2}0\s{1,2}1\s{1,2}2\s{1,2}3\s{1,2}4\s{1,2}5\s{1,2}6\s{1,2}7\s{1,2}8\s{1,2}9\s{1,2}10\s{1,2}\bNo Pain\b\s{1,2}\bMaximum Pain\b\s{1,2}","",str(k112))
        count=1
        #print(k113)
    except:
        #print(k112)
        pass
#    final_data=nltk.sent_tokenize(text)
#    print(final_data)
    count,count1=0,0
    #final_data=[final_data[0]]
    #final_data=list(final_data)
    output=dict()
    output['date']=date
    output['time']=time
    output['Doctor']=Doctor
    if len(weight)>0:
        output['weight']=int(weight[0])
    else:
        output['weight']=0
    if len(age)>0:
        output['age']=int(age[0])
    else:
        output['age']=0
    output['patient']=list(set(patient))[0]
    if count==0:
        output['summary']=k112
    else:
        output['summary']=k112
    if len(gender)>0:
        output['gender']=gender
    else:
        output['gender']=gender2
    output['speciality']=speciality
    output['medicine-disease']=list(set(medicine))
    #with open("nlp%s"%(sys.argv[2]),"r") as f3:
    
    status=True
    if status:
        file=sys.argv[1]
        file1=re.sub(r"\b.txt\b",".json",file)
        with open("nlp/%s"%(file1),"w") as f3:
        #with open("Medicine_names_test2.json","w") as f3:
            json.dump(output,f3)
