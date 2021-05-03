from django.shortcuts import render, redirect
from . models import AllVendor
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from . models import Category_list
from .models import ImportProduct
from .models import Store
from .models import Customer_Detail
from .models import Sell

# Create your views here.
def businesswork(request):
    try:
            
        uobj=request.user
        Customer=Customer_Detail.objects.filter(added_by=request.user)
        return render(request,'index.html',{'data':uobj,'cust':Customer})
    except:
        return redirect('/login/')



    
    return render(request,'index.html',{'data':uobj,'cust':Customer})
@login_required(login_url='/login/') 
def searchCust(request):
    try:

        uobj=request.user
        try:
            q= request.GET.get('q')
        except:
            q=None
        if q:
            Customer=Customer_Detail.objects.filter(added_by=request.user,c_name__icontains=q)
            return render(request,'index.html',{'data':uobj,'cust':Customer})
        else:
            return redirect('/vendor/businesswork/')
    except:
        return redirect('/login/')
    return render(request,'index.html',{'data':uobj,'cust':Customer})
@login_required(login_url='/login/') 
def searchVendor(request):
    try:
        uobj=request.user
        try:
            q= request.GET.get('q')
        except:
            q=None
        if q:
            vobjs=AllVendor.objects.filter(addedby=uobj.id,vname__icontains=q)
            return render(request,'vendorslist.html',{'data':vobjs})
        else:
            return redirect('/vendor/ViewVendors/')
    except:
        return redirect('/login/')

    return render(request,'vendorslist.html',{'data':vobjs})
@login_required(login_url='/login/') 
def searchPro(request):
    try:


        uobj=request.user
        try:
            q= request.GET.get('q')
        except:
            q=None
        if q:
            CatObj=Category_list.objects.filter(category_by=uobj.id)
            ProObj=Store.objects.filter(ImportingUser=uobj,name__icontains=q)
            return render(request,'mystore.html',{'product':ProObj,'cat':CatObj})
    except:
        return redirect('/login/')
       
    return render(request,'mystore.html',{'product':ProObj,'cat':CatObj})





@login_required(login_url='/login/')
def about_customer(request,id):
    Customer=Customer_Detail.objects.filter(id=id)

    return render(request,'particularcustomer.html',{'cust':Customer})

@login_required(login_url='/login/')
def addvendor(request):
    if request.method=='POST':
        vname=request.POST['vname']
        vcompany=request.POST['vcompany']
        vcontact=request.POST['vcontact']
        vaddress=request.POST['vaddress']
        vpincode=request.POST['vpincode']
        vemail=request.POST['vemail']
        
        
        uObj=request.user
        url='/vendor/addvendor/'
        try:

            v=AllVendor(vname=vname,vcompany=vcompany,vcontact=vcontact,vaddress=vaddress,vpincode=vpincode,vemail=vemail,addedby=uObj)
            v.save()
            return HttpResponse('<script>alert("Vendor added.");\
                    window.location="%s"</script>'%url)
        except:
            return HttpResponse("Something went wrong.")
        return redirect('/vendor/addvendor/')

    return render(request,'addvendor.html')
@login_required(login_url='/login/')
def IProduct(request):
    uobj=request.user
    vObj=AllVendor.objects.filter(addedby=uobj.id)
    cObj=Category_list.objects.filter(category_by=uobj.id)

    if request.method=='POST':
        
        vendor=request.POST['vendor']
        proname=request.POST['proname']
        qty=request.POST['qty']
        rate=request.POST['rate']
        price=request.POST['price']
        
        qty=float(qty)
        rate=float(rate)
        totalprice=qty*rate
        
        title=request.POST['title']
        desc=request.POST['desc']
        brand=request.POST['brand']
        category=request.POST['category']
        model=request.POST['model']
        catObj=Category_list.objects.get(id=category)
        vObj=AllVendor.objects.get(id=vendor)
        uobj=request.user
        url='/vendor/import/'
        try:
            P=ImportProduct(name=proname,description=desc,title=title,price=price,brand=brand,model=model,pro_category=catObj,pro_vendor=vObj,qty=qty,rate=rate,total_price=totalprice,ImportingUser=uobj)
            P.save()
            S=Store(name=proname,description=desc,title=title,selling_price=price,cost_price=rate,brand=brand,model=model,pro_category=catObj,qty=qty,ImportingUser=uobj)
            S.save()
            return HttpResponse('<script>alert("Product added.");\
                    window.location="%s"</script>'%url)
        except:
            return HttpResponse("Something went wrong.")
        return redirect('/vendor/import/')
    return render(request,'import.html',{'cats':cObj,'vObj':vObj})

@login_required(login_url='/login/')
def ViewVendors(request):
    uobj=request.user

    vobjs=AllVendor.objects.filter(addedby=uobj.id)

    return render(request,'vendorslist.html',{'data':vobjs})
@login_required(login_url='/login/')
def Category(request):
    uobj=request.user
    CatObj=Category_list.objects.filter(category_by=uobj.id)
    return render(request,'category.html',{'data':CatObj})
@login_required(login_url='/login/')
def AddCategory(request):
    if request.method=='POST':
        catname=request.POST['catname']
        desc=request.POST['description']
        uObj=request.user
        url='/vendor/addcategory/'
        try:

            c=Category_list(catname=catname,desc=desc,category_by=uObj)
            c.save()
            return HttpResponse('<script>alert("Category added.");\
                    window.location="%s"</script>'%url)
        except:
            return HttpResponse("Something went wrong.")
        return redirect('/vendor/addcategory/')
    return render(request,'addcategory.html')
@login_required(login_url='/login/')
def ViewImport(request):
    uobj=request.user
    CatObj=Category_list.objects.filter(category_by=uobj.id)

    vobjs=AllVendor.objects.filter(addedby=uobj.id)

    ProObj=ImportProduct.objects.filter(ImportingUser=uobj)
    
    return render(request,'importlist.html',{'product':ProObj,'data':vobjs,'cat':CatObj,'order':vobjs})
@login_required(login_url='/login/')

def sortbyvendor(request,id):
    uobj=request.user
    CatObj=Category_list.objects.filter(category_by=uobj.id)
    vobjs=AllVendor.objects.filter(addedby=uobj.id)
    ProObj=ImportProduct.objects.filter(pro_vendor_id=id)
    #ProObj_normal=ImportProduct.objects.filter(ImportingUser=uobj)
    return render(request,'importlist.html',{'product':ProObj,'data':vobjs,'cat':CatObj,'order':vobjs})
@login_required(login_url='/login/')

def mystore(request):
    uobj=request.user
    CatObj=Category_list.objects.filter(category_by=uobj.id)
    ProObj=Store.objects.filter(ImportingUser=uobj)
    return render(request,'mystore.html',{'product':ProObj,'cat':CatObj})
@login_required(login_url='/login/')

def bycategory(request,id):
    uobj=request.user
    CatObj=Category_list.objects.filter(category_by=uobj.id)

    ProObj=Store.objects.filter(pro_category=id)
    return render(request,'mystore.html',{'product':ProObj,'cat':CatObj})
@login_required(login_url='/login/')
def customer_detail(request):
    if request.method=='POST':
        name=request.POST['c_name']
        mobile1=request.POST['mobile']
        mobile2=request.POST['mobile_']
        address=request.POST['address']
        addedby=request.user
        customer_db=Customer_Detail(c_name=name,c_mobile=mobile1,c_mobile_optional=mobile2,c_address=address,added_by=addedby)
        customer_db.save()
        return redirect('/vendor/export/')
    return render(request,'customer.html')
@login_required(login_url='/login/')    
def EProduct(request):
    uobj=request.user
    cObj=Category_list.objects.filter(category_by=uobj.id)
    c_d=Customer_Detail.objects.filter(added_by=request.user).order_by('-id')
    pro=Store.objects.filter(ImportingUser=request.user)
    if request.method=='POST':
        customer=request.POST['customer']
        pro_name=request.POST['pro']
        brand=request.POST['brand']
        qty=request.POST['qty']
        rate=request.POST['rate']
        desc=request.POST['desc']
        model=request.POST['model']
        title=request.POST['title']
        category=request.POST['category']
        uobj=request.user
        catObj=Category_list.objects.get(id=category)
        Cust_obj=Customer_Detail.objects.get(id=customer)
        pro_obj=Store.objects.get(id=pro_name)
        rate=float(rate)
        qty=float(qty)
        totalprice=float(rate*qty)
        
        
        updateStore=Store.objects.filter(id=pro_name)
        updateQty=updateStore[0].qty-int(qty)
        url='/vendor/export/'
        if updateQty<=-1:
            return HttpResponse('<script>alert("Wrong quantity or product unavailable.");\
                    window.location="%s"</script>'%url)
        
        else:

            updateStore.update(qty=updateQty)
            S=Sell(name=pro_obj.name,description=desc,title=title,totalprice=totalprice,brand=brand,model=model,qty=qty,rate=rate,ExportingUser=uobj,customer_detail=Cust_obj,pro_category=catObj)
            S.save()
        
		

        return redirect('/vendor/export/')



    return render(request,'export.html',{'cust':c_d,'pro':pro,'cats':cObj})
@login_required(login_url='/login/') 
def billing(request):
    proObj=Sell.objects.filter(ExportingUser=request.user)
    Customer=Customer_Detail.objects.filter(added_by=request.user).order_by('-id')

    return render(request,'bill.html',{'product':proObj,'cust':Customer,})
@login_required(login_url='/login/') 
def customer_bill(request,id):
    Customer=Customer_Detail.objects.filter(added_by=request.user).order_by('-id')
    proObj=Sell.objects.filter(ExportingUser=request.user)
    pro_by_cust=Sell.objects.filter(customer_detail_id=id)

    return render(request,'bill.html',{'product':pro_by_cust,'cust':Customer})
@login_required(login_url='/login/') 
def view_export(request):
    proObj=Sell.objects.filter(ExportingUser=request.user)
    Customer=Customer_Detail.objects.filter(added_by=request.user).order_by('-id')
    return render(request,'exportlist.html',{'product':proObj,'cust':Customer,})
def export_by_date(request,id):
    pass

@login_required(login_url='/login/') 
def about(request):
    return render(request,'about.html')