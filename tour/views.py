from django.shortcuts import redirect, render

from .models import Place, Picture, Listing, Contact, Website_Image, Place_Wording, Regular_User

# Create your views here.

def home(request):
    Places = Place.objects.all()
    Pictures = Picture.objects.all()
    Listings = Listing.objects.all()
    Contacts = Contact.objects.all()
    Website_Images = Website_Image.objects.all()
    
    x = 0
    nights = 0
    
    for y in Places:
        x = y.day
        if y.day == x:
            nights = x-1
           
    
    if request.method == "POST":
        searchedInfo = request.POST.get('searched')
        if searchedInfo:
            search_finding = Place.objects.filter(name__contains=searchedInfo) 
            return render(request, 'search_result.html', {'search_finding' : search_finding, 'Website_Images': Website_Images, 'Contacts': Contacts, 'searchedInfo' :  searchedInfo})
        else:        
            return render(request, 'search_result.html', {'Places': Places, 'Pictures': Pictures, 'Listings' : Listings, 'Contacts': Contacts, 'Website_Images': Website_Images})

    
    return render(request, 'home.html',{'Places': Places, 'Pictures': Pictures, 'Listings' : Listings, 'Contacts': Contacts, 'Website_Images': Website_Images, 'nights': nights, 'x': x})  
    

def mombasa(request):
    Contacts = Contact.objects.all()
    Places = Place.objects.all()
    Pictures = Picture.objects.filter(place=1)
    Listings = Listing.objects.all()
    Website_Images = Website_Image.objects.all()
    Place_Wordings =Place_Wording.objects.all()
   
    return render(request, 'mombasa.html', {'Contacts': Contacts, 'Places': Places, 'Place_Wordings': Place_Wordings, 'Pictures': Pictures, 'Listings' : Listings, 'Website_Images': Website_Images,})


def diani(request):
    Contacts = Contact.objects.all()
    Places = Place.objects.all()
    Pictures = Picture.objects.filter(place=2)
    Listings = Listing.objects.all()
    Website_Images = Website_Image.objects.all()
    Place_Wordings =Place_Wording.objects.all()
    
    return render(request, 'diani.html', {'Contacts': Contacts, 'Places': Places, 'Place_Wordings': Place_Wordings, 'Pictures': Pictures, 'Listings' : Listings, 'Website_Images': Website_Images,})


def wasini(request):
    Contacts = Contact.objects.all()
    Places = Place.objects.all()
    Pictures = Picture.objects.filter(place=3)
    Listings = Listing.objects.all()
    Website_Images = Website_Image.objects.all()
    Place_Wordings =Place_Wording.objects.all()
    
    return render(request, 'wasini.html', {'Contacts': Contacts, 'Places': Places, 'Place_Wordings': Place_Wordings, 'Pictures': Pictures, 'Listings' : Listings, 'Website_Images': Website_Images,})

def watamu(request):
    Contacts = Contact.objects.all()
    Places = Place.objects.all()
    Pictures = Picture.objects.filter(place=6)
    Listings = Listing.objects.all()
    Website_Images = Website_Image.objects.all()
    Place_Wordings =Place_Wording.objects.all()
    
    return render(request, 'watamu.html', {'Contacts': Contacts, 'Places': Places, 'Place_Wordings': Place_Wordings, 'Pictures': Pictures, 'Listings' : Listings, 'Website_Images': Website_Images,})

def shimoni(request):
    Contacts = Contact.objects.all()
    Places = Place.objects.all()
    Pictures = Picture.objects.filter(place=5)
    Listings = Listing.objects.all()
    Website_Images = Website_Image.objects.all()
    Place_Wordings =Place_Wording.objects.all()
    
    return render(request, 'shimoni.html', {'Contacts': Contacts, 'Places': Places, 'Place_Wordings': Place_Wordings, 'Pictures': Pictures, 'Listings' : Listings, 'Website_Images': Website_Images,})

def mambrui(request):
    Contacts = Contact.objects.all()
    Places = Place.objects.all()
    Pictures = Picture.objects.filter(place=4)
    Listings = Listing.objects.all()
    Website_Images = Website_Image.objects.all()
    Place_Wordings =Place_Wording.objects.all()
    
    return render(request, 'mambrui.html', {'Contacts': Contacts, 'Places': Places, 'Place_Wordings': Place_Wordings, 'Pictures': Pictures, 'Listings' : Listings, 'Website_Images': Website_Images,})

def hotels(request):
    Contacts = Contact.objects.all()
    Places = Place.objects.all()
    Pictures = Picture.objects.all()
    Listings = Listing.objects.all()
    Website_Images = Website_Image.objects.all()
    
    return render(request, 'listings.html', {'Contacts': Contacts, 'Places': Places, 'Pictures': Pictures, 'Listings' : Listings, 'Website_Images': Website_Images,})
 
def restaurants(request):
    Contacts = Contact.objects.all()
    Places = Place.objects.all()
    Pictures = Picture.objects.all()
    Listings = Listing.objects.all()
    Website_Images = Website_Image.objects.all()
    
    return render(request, 'listings.html', {'Contacts': Contacts, 'Places': Places, 'Pictures': Pictures, 'Listings' : Listings,'Website_Images': Website_Images, })
 
def destinations(request):
    Contacts = Contact.objects.all()
    Places = Place.objects.all()
    Pictures = Picture.objects.all()
    Listings = Listing.objects.all()
    Website_Images = Website_Image.objects.all()
    
    return render(request, 'listings.html', {'Contacts': Contacts, 'Places': Places, 'Pictures': Pictures, 'Listings' : Listings, 'Website_Images': Website_Images,})
 
def travels(request):
    Contacts = Contact.objects.all()
    Places = Place.objects.all()
    Pictures = Picture.objects.all()
    Listings = Listing.objects.all()
    Website_Images = Website_Image.objects.all()
    
    return render(request, 'listings.html', {'Contacts': Contacts, 'Places': Places, 'Pictures': Pictures, 'Listings' : Listings, 'Website_Images': Website_Images,})

    
def register(request):
    Contacts = Contact.objects.all()
    Places = Place.objects.all()
    Pictures = Picture.objects.all()
    Listings = Listing.objects.all()
    Website_Images = Website_Image.objects.all()
    Regular_Users = Regular_User.objects.all()

    if request.method == "POST":       
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        con_password = request.POST.get('con_password')         

        form = 0   # 1 2 3 - username  4 5 - email  6 7 - password  8 9 - confirm password
        if username=='' or email=='' or password=='' or con_password=='':
            form = 0 # fill in all the required details
        else:    
            if len(username) < 4:
                form = 1 # enter a complete username of atleast 4 characters
            else: # name should not be matching another in the db
                for user in  Regular_Users:
                    if username == user.username:
                        form = 2 # username is taken try another username
                    else:
                        form = 3 # username is okay continue
                
            if '@' in email:
                form = 4 # email is okay continue
            else:
                form = 5 # email requires @
            
            if len(password) < 5:
                form = 6 # enter a complete password of atleast 5 characters
            else:
                form = 7 # password is okay continue
                
            if con_password != password:
                form = 8 # con_password is not same to password
            else:
                form = 9 # confirmation password is okay continue to save
        
        if form != 0 or form != 1 or form != 2 or form != 5 or form != 6 or form != 8:        
            new_user = Regular_User(username=username, email=email, password=password, con_password=con_password)
            new_user.save() 
               
        return render(request, 'register.html', {'form' : form, 'Places': Places, 'Pictures': Pictures, 'Listings' : Listings, 'Contacts': Contacts, 'Website_Images': Website_Images})          
    
    return render(request, 'register.html', {'Places': Places, ' Regular_Users':  Regular_Users, 'Pictures': Pictures, 'Listings' : Listings, 'Contacts': Contacts, 'Website_Images': Website_Images})   


def unregister(request):
    Contacts = Contact.objects.all()
    Places = Place.objects.all()
    Pictures = Picture.objects.all()
    Listings = Listing.objects.all()
    Website_Images = Website_Image.objects.all()
    Regular_Users = Regular_User.objects.all()

    if request.method == "POST":       
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        con_password = request.POST.get('con_password')         

        form = 0   # 1 2 3 - username  4 5 - email  6 7 - password  8 9 - confirm password
        if username=='' or email=='' or password=='' or con_password=='':
            form = 0
        else:    
            if len(username) < 4:
                form = 1 # username is short
            else: # name should not be matching another in the db
                for user in  Regular_Users:
                    if username == user.username:
                        form = 2 # username is taken
                                  
            
        

               
        return render(request, 'unregister.html', {'form' : form, 'Places': Places, 'Pictures': Pictures, 'Listings' : Listings, 'Contacts': Contacts, 'Website_Images': Website_Images})          
    
    return render(request, 'unregister.html', {'Places': Places, ' Regular_Users':  Regular_Users, 'Pictures': Pictures, 'Listings' : Listings, 'Contacts': Contacts, 'Website_Images': Website_Images})   


        
            