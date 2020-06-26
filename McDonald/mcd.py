import os, sys
import mechanize

amt1 = 2
amt2 = 33
age_ver = 1
visit_date = '08%2f24%2f2015'
store_id = '29853'
format_Date = '20150824'
day = 24
hour=11
minute = 22
month = '08'
reg_Num=2
transaction_Num=275
year=2015
url = 'https://www.mcdvoice.com'
#c=313419

url_build = url + '/Index.apsx?AmountSpent1='+ str(amt1) + '&AmountSpent2='+str(amt2) +'&CN1=&CN2=&CN3=&CN4=&CN5=&CN6=&Index_AgeVerification=1'
url_build +='&Index_VisitDateDatePicker=' +visit_date+'&Index_VisitDateFormattedDate='+format_Date+'&InputDay='+str(day)
url_build += '&InputHour='+str(hour)+'&InputMinute='+str(minute)+'&InputMonth='+str(month)+'&InputRegisterNum='+str(reg_Num)
url_build += '&InputStoreID='+store_id+'&InputTransactionNum='+str(transaction_Num)+'&InputYear='+str(year)





def submit_Info():
	br = Browser()
	br.open(url)
	br.select_form(name='surveyEntryForm')
	print br
	#br['AmountSpent1']= str(amt1)
	#br['AmountSpent2']= str(amt2)
	#br['Index_VisitDateDatePicker']= visit_date  #One that gives options
	#br['Index_VisitDateFormattedDate'] = format_date #One that doesn't give options
	#br['Index_AgeVerification'] = 1
	#br['InputStoreID'] = store_id
	#br['InputTransactionNum'] = str(transaction_Num)
	#br['InputRegisterNum']=str(reg_Num)  
	#br['InputHour']=str(hour)
	#br['InputMinute']=str(minute)
	#response = br.submit()
	print response

submit_Info()	




