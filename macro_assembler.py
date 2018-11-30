templ=0
dp=open("nihal.asm",'w')
m_name=[]
m_label=[]
m_data={}


	
def letschange(m_data,flag):
 fp=open("macro.asm",'r')
 fp1=fp.readlines()
 for i in range(len(fp1)):
	 if '.text' in fp1[i]:
		 flag=1
	 if (flag==1):
		print fp1[i]
	
		jj=fp1[i].split()
       		if str(jj[0]) in m_data:
                        jjj=jj[1].split(',')
                        temp=(jjj[0],jjj[1])
                        templ=m_data[jj[0]]
                #       print templ

                        for k in templ:
                                dp.write('\n\t')
                                for kk in k:
                                        if "%1"==kk:
                                                dp.write(","+jjj[0])


                                        elif "%2"==kk:
                                                dp.write(","+jjj[1])
                                                dp.write('\n')
                                        else:
                                                dp.write(kk+" ")
        	else:
                	dp.write(fp1[i])

	
def macrostart(line,mline,fp1,m_data0,man):
# print m_data0
 #print line
 #print mline
 for i in range(line+1,mline):
	if '%%' in fp1[i]:
		m_name.append([fp1[i]])
		#print fp1[i]
	else:
		jj=fp1[i].split()
		if len(jj)>1:
			jjj=jj[1].split(',')			
			m_data0.append([jj[0],jjj[0],jjj[1]])
			#print m_data0
 m_data[man]=m_data0
 #print m_data	
 return m_data

def macrotable(fp,mline):
  man=0
  dd={}
  fp1=fp.readlines()
  for i in fp1:
	mline+=1
	jj=i.split()
	for j in range(len(jj)):
		if jj[j]=='%macro':
			if len(i)>2:
				m_label.append(jj[1])
				start=mline
				man=jj[1]
		if jj[j]=='%endmacro':
			m_data0=[]
			dd=macrostart(start,mline,fp1,m_data0,man)
  return dd
def main():
	dk={}
	fp=open("macro.asm",'r')
	mline=-1
	dk=macrotable(fp,mline)
 	flag=0
 	letschange(dk,flag)

main()

