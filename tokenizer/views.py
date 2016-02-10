from django.shortcuts import render
from django.http import HttpResponse
from models import Question
import base64
from Crypto.Cipher import AES
import sys
import re

keys_dict = {'standin' : '1234567890123456', 'mayfly' : '2345678901234567','authcapture':'3456789012345672','pymt':'4567890123456723','symphony':'5678901234567234','switch':'6789012345672345'
			,'settlement':'7890123456723456','iso8583':'8901234567234567','australia':'9012345672345670'}

# Create your views here.
def home(request):
	return render(request,'tokenizer/home.html',{})

def question(request):
	pname = request.POST['pname']
	no_of_qs = Question.objects.count()
	#if object count is 0
	print pname
	hname = hashName(pname,no_of_qs)
	print hname
	question = Question.objects.get(pk=hname)
	context ={}
	context['encoded_text'] = encode(question.answer.lower().strip().replace(' ',''),question.volunteer) 
	context['question_text'] = question.question_text	
	return render(request, 'tokenizer/question.html',context)

def answer(request):
	pattern = re.compile(r'[\s-]+')
	resp = re.sub(pattern, '', request.POST['resp'].lower().strip())
	print resp
	encoded_text = request.POST['encoded_text']

	decoded_text = decode(resp,encoded_text)
	print decoded_text
	context = {'decoded_text':decoded_text}
	return render(request,'tokenizer/answer.html',context)
	

def hashName(name,noq):
	name = name.lower()
	sum=0
	for alpha in name:
		sum = sum + (ord(alpha)-97)
	hash = sum % noq
	print hash
	return hash
	
def encode(key, string):
	secret_key = keys_dict[key] 
	cipher = AES.new(secret_key,AES.MODE_ECB) 
	return base64.b64encode(cipher.encrypt(string.rjust(32)))

def decode(key, string):
	try:
		secret_key = keys_dict[key] 
	except KeyError:
		return "Bummer! "
		#secret_key = '1111111111111111'
	cipher = AES.new(secret_key,AES.MODE_ECB)
	return cipher.decrypt(base64.b64decode(string))



