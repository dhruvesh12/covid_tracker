from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
import requests
from bs4 import BeautifulSoup 
import time
# Create your views here.
URL = "https://visalist.io/emergency/coronavirus/india-country/maharashtra"

r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html.parser')



def home(request):
	global total_c
	############For Nashik
	for i in soup.find_all(class_='v-list-item v-list-item--link theme--dark'):
		a=i.find_all(class_='body-2 text-truncate')
		for new_i in a:
			if new_i.text.replace('\n','')=="Nashik":
				s=i.find(class_='v-list-item__action-text subtitle-1 bolder font-weight-bold pink--text text--accent-3')
				con=s.text.replace('\n','')
			
				confirmed=i.find(class_='pink--text text--accent-3').text.replace('\n','')
				#grey--text

				recovered=i.find(class_='green--text text--accent-3').text.replace('\n','')

				death=i.find(class_='grey--text').text.replace('\n','')


	###########For Maharashtra
	for i in soup.find_all(class_='v-item-group theme--dark v-list-item-group blue--text'):
    

	    a=i.find_all(class_='v-list-item__content py-1')
	    for new_i in a:
	        state=new_i.find_all(class_='nuxt-link-exact-active nuxt-link-active')
	        for s in state:
	            if s.text.replace('\n','') == 'Maharashtra':
	                
	                total=new_i.find(class_='pink--text text--accent-3').text
	                total_recovered=new_i.find(class_='green--text text--accent-3').text
	                sick=new_i.find(class_='orange--text text--accent-3').text
	                dead=new_i.find(class_='grey--text').text



	##############For India

	for i in soup.find_all(class_='v-list-item v-list-item--link theme--dark'):
	    a=i.find_all(class_='layout row ma-0 pa-0')
	    for s in a:
	        aa=s.find_all(class_='nuxt-link-active')

	        for d in aa:
	            if d.text.replace('\n','') =='India':
	                total_c=i.find(class_='pink--text text--accent-3').text
	                sicks=i.find(class_='orange--text text--accent-3').text
	                total_r=i.find(class_='green--text text--accent-3').text
	                total_death=i.find(class_='grey--text').text


	return render(request,'home.html',{'con':con,'confirmed':confirmed,'recovered':recovered,'death':death,
		'total':total,'total_recovered':total_recovered,'sick':sick,'dead':dead,'total_c':total_c,'sicks':sicks,
		'total_r':total_r,'total_death':total_death})
