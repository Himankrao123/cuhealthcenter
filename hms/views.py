import email
from pydoc import Doc
from time import time
from turtle import title
from unicodedata import name
from django.shortcuts import redirect, render
from django.shortcuts import render
import datetime
from django.contrib.auth import login, logout,authenticate
from numpy import double
from hms.models import Appointment, Contact_us, UserProfile, User, Document,UpdateNew,Doctor
import random
import yagmail
yag = yagmail.SMTP('Email please','Password please')
def index(request):
    if request.user.is_anonymous:
        return render(request, "index.html")

    listofup = []
    updates = UpdateNew.objects.all()
    for i in updates:
        a = i.title.replace(" ","_")
        listofup.append(f"<a href='/update/{a}'><button class='updatebut'>{i.title}</button></a>")
    return render(request, "userindex.html",context={"listofup":listofup})  

def service(request):
    return render(request,"service.html",{"page":"base.html" if request.user.is_anonymous else "base2.html",})

def contactus(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        desc = request.POST.get('desc')
        dat = datetime.datetime.today()
        subject = request.POST.get('subject')
        contacting = Contact_us(name = name, emailid = email, desc = desc, dateofcontact = dat,contactnumber = number,subjecttocontact = subject)
        contacting.save()
    return render(request,"contact_us.html",{"page":("base.html" if request.user.is_anonymous else "base2.html"),})

def update(request, slug):
    l = slug.replace("_"," ")
    updatedict = {}
    update = UpdateNew.objects.filter(title = l)
    for i in update:
        updatedict["title"] = i.title
        updatedict["messageis"] = i.messageis
        updatedict["messageby"] = i.messageby
        updatedict["messageon"] = i.messageon
    return render(request,"update.html",updatedict)

def docinfo(request,slug):
    page = "base2.html"
    if request.user.is_anonymous:
        page = "base.html"
    docdict = {"page":page}
    try:
        doc = Doctor.objects.filter(name = slug.replace("_"," "))
    except:
        redirect("/")
    for i in doc:
        docdict["name"]=i.name
        docdict["desc"]=i.docdesc
        docdict["special"]=i.specialization
        docdict["exp"]=i.experience
        docdict["st"]=i.start_time
        docdict["et"]=i.end_time
        docdict["timestate"]=f"on {i.current_date} after {i.current_time}"

    return render(request,"doctors.html",docdict)

def accounts(request,slug):
    def accountsfunc():
        if slug=="signin":
            if request.method == "POST":
                username = request.POST.get("username")
                password = request.POST.get("password")
                userserv = authenticate(request, username=username, password=password)
                if userserv is not None:
                    login(request, userserv)
                    return redirect('/')
                else:
                    message = {"message":"Invalid username or password!","status":"Try again","nextsteplink":"/accounts/signin","nextstep":"Sign in"}
                    return render(request, 'message.html', message)
            message = {"what":""}
            return render(request, "signin.html",message)
        elif slug=="signup":
            if request.method == "POST":
                fname = request.POST.get("fname")
                lname = request.POST.get("lname")
                username = request.POST.get("username")
                password = request.POST.get("password")
                email = request.POST.get("email")
                mobile = int(request.POST.get("phone"))
                dob = request.POST.get("dob")
                age = int(request.POST.get("age"))
                gender = request.POST.get("gender")
                try:
                    newuser = User.objects.create_user(username = username,password = password,email = email,first_name = fname,last_name = lname)
                    dob = (datetime.datetime.strptime(dob,'%Y-%m-%d'))
                    newuserprofile = UserProfile(userz = newuser,dateofbirth = dob,contactnumber = mobile,age = age,gender = gender)
                    newuser.save()
                    newuserprofile.save()
                    var = {"status":"Success","message":"New account created successfuly!","nextsteplink":"/accounts/signin","nextstep":"Sign in"}
                    return render(request, "message.html",context = var)
                except:
                    var = {"status":"Failed","message":"We are sorry! Due to some issue account creation failed.","nextsteplink":"/accounts/signup","nextstep":"Sign up"}
                    return render(request, "message.html",context=var)
            return render(request,"signup.html")
        else:
            return redirect("/accounts/signin")
    
    if request.user.is_anonymous:
        return accountsfunc()
    else:
        logout(request)
        return accountsfunc()

def logoutacc(request):
    if request.user.is_anonymous:
        return redirect("/")
    logout(request)
    return redirect("/")
def profile(request):
    if request.user.is_anonymous:
        return redirect("/accounts/signin")
    detailsdict = {}
    try:
        whois = UserProfile.objects.get(userz = request.user)
        detailsdict = {"username":request.user.username,"email":request.user.email,"fname":request.user.first_name,"lname":request.user.last_name,"age":whois.age,"DOB":whois.dateofbirth,"gender":whois.gender,"contactnumber":whois.contactnumber}
    except:
        pass
    return render(request, "profile.html",detailsdict)

def profileedit(request):
    if request.user.is_anonymous:
        return redirect("/accounts/signin")

    if request.method == "POST":
        try:
            fname = request.POST.get("fname")
            lname = request.POST.get("lname")
            emaila = request.POST.get("email")
            contactnumber = request.POST.get("contactnumber")
            dob = request.POST.get("dob")
            age = request.POST.get("age")
            gender = request.POST.get("gender")
            whois = UserProfile.objects.get(userz = request.user)
            request.user.email = emaila
            request.user.first_name = fname
            request.user.last_name = lname
            whois.age = age
            whois.dateofbirth = dob
            whois.gender = gender
            whois.contactnumber = contactnumber
            request.user.save()
            whois.save()
            var = {"status":"Success","message":"Profile saved Successfully","nextsteplink":"/","nextstep":"Home"}
            return render(request, "message.html",context=var)
        except:
            var = {"status":"Failed","message":"We are sorry! Due to some issue we are unable to save profile.","nextsteplink":"/","nextstep":"Home"}
            return render(request, "message.html",context=var)
        
    detailsdict = {}
    
    try:
        whois = UserProfile.objects.get(userz = request.user)
        detailsdict = {"email":request.user.email,"fname":request.user.first_name,"lname":request.user.last_name,"age":whois.age,"DOB":whois.dateofbirth.strftime('%Y-%m-%d'),"gender":whois.gender,"contactnumber":whois.contactnumber}
        
    except:
        pass
    return render(request, "profileedit.html",detailsdict)

def documents(request):
    if request.user.is_anonymous:
        return redirect("/accounts/signin")
    
    listofdoc = Document.objects.all().filter(user = request.user)
    listofuserdoc = []
    for i in listofdoc:
        a = str(i.file)
        a = a[10:]
        listofuserdoc.append(f"<td>{a}</td><td>{i.docexp}</td><td><a href='/media/{i.file}' download>Download</a></td></p>")
    docdict = {"objects":listofuserdoc}
    return render(request,"documents.html",docdict)

def newappointment(request):
    if request.user.is_anonymous:
        return redirect("/accounts/signin")
    if request.method == "POST":
        try:
            withwhom = request.POST.get("withwho")
            appid = random.randint(1000000000,9999999999)
            appdesc = request.POST.get("appdesc")
            try:
                doc  = Doctor.objects.get(name = withwhom)
            except:
                var = {"status":"Failed","message":"Your appointment request is failed.","nextsteplink":"/","nextstep":"Home"}
                return render(request, "message.html",context=var)
            if doc.current_date<datetime.date.today()+datetime.timedelta(days=1):
                doc.current_date = datetime.date.today()+datetime.timedelta(days=1)
                doc.current_time = datetime.time(9,0,0)
            if doc.current_time == datetime.time(12,0,0):
                doc.current_time = datetime.time(13,0,0)
            if doc.current_time==datetime.time(18,0,0):
                doc.current_date = doc.current_date + datetime.timedelta(days=1)
                doc.current_time = datetime.time(9,0,0)
            apptime = doc.current_time
            appdate = doc.current_date
            if doc.current_time.minute ==40 :
                doc.current_time = doc.current_time.replace(hour=doc.current_time.hour+1)
                doc.current_time = doc.current_time.replace(minute=00)
            else:
                doc.current_time = doc.current_time.replace(minute=doc.current_time.minute+20)
            messageformail = f"<h2>Dear {request.user.first_name},</h2><br>Your request for appointment with {withwhom} is booked on {appdate} at {apptime}.Your time of appointment is 20 minutes. If there is any change in your appointment time or date you will be informed. you appointment id is {appid}. Please be on time.<br>Thankyou!!<br>Regards CU Health Centre"
            newappointment = Appointment(of_whom = request.user.username,with_whom = withwhom,active = False,appointmentid = appid,appointmentdesc = appdesc,appointmentdate=appdate,appointmenttime = apptime)
            doc.save()
            newappointment.save()
            yag.send(request.user.email,"Appointment booking successful", messageformail)
            var = {"status":"Success","message":"Your appointment request is submited. You will be notified soon with further details via email","nextsteplink":"/","nextstep":"Home"}
            return render(request, "message.html",context=var)
        except:
            var = {"status":"Failed","message":"We are sorry! Due to some issue appointment booking failed.","nextsteplink":"/contact_us","nextstep":"Contact us"}
            return render(request, "message.html",context=var)


    doctorsdict = ["Dr Nandini Khurana","Dr Himank Yadav","Dr Suraj Rana","Dr Khushi Sangal","Dr Sagar Dandapat"]
    maindict = {"page":("base.html" if request.user.is_anonymous else "base2.html"),"options":doctorsdict}
    return render(request,"newappointment.html",maindict)
