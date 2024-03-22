from django.shortcuts import render, redirect,get_object_or_404,HttpResponse
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from .models import course, email_subscription, blog, Trainer,course_buy,Booking
from datetime import date, datetime
import pandas as pd
from .models import Itemcart

def home(request):
    latest_blogs = blog.objects.all()[:3]
    teachers = Trainer.objects.all()[:3]
    c=course.objects.all()[:3]

    return render(request,'index.html', {'latest_blog': latest_blogs, 'teacher_all': teachers,'courses':c})


def classes_details(request,id):
    c=get_object_or_404(course,id=id)
    teachers = Trainer.objects.all()
    return render(request,'classes.html',{'course':c,'teacher_all': teachers})

def blogs(request):
    b = blog.objects.all()
    latest_blog = blog.objects.order_by('Date')[:3]
    teachers = Trainer.objects.all()
    cart = request.session.get('cart', [])
    cart_count = len(cart)
    return render(request,'blog.html', {'blogs': b, 'latest': latest_blog,'teacher_all': teachers, 'count': cart_count})

def about(request):
    latest_blog = blog.objects.all()[:1]
    teacher = Trainer.objects.all()
    cart = request.session.get('cart', [])
    cart_count = len(cart)
    return render(request, 'about.html', {'latest': latest_blog, 'teacher_all': teacher, 'count': cart_count})

# def price(request):
#     return render(request, 'price.html')

def service(request):
    c=course.objects.all()
    return render(request, 'service.html',{'courses':c})

def therapist(request):
    trainers = Trainer.objects.all()
    return render(request,'team.html',{'teacher_all':trainers})

def therapist_details(request,id):
    experts = get_object_or_404(Trainer,id=id)
    trainers = Trainer.objects.all()
    return render(request,'expert.html',{'expert':experts,'teacher_all':trainers})


def blog_details(request,text):
    b = get_object_or_404(blog,title=text)
    blogs_by_date = blog.objects.order_by('Date')
    return render(request,'single.html',{'blog':b,'latest':blogs_by_date})

def add_cart(request, pk):
    product = get_object_or_404(course, pk=pk)
    cart = request.session.get('cart', [])
    cart.append({'id':product.id,'name': product.course_name, 'price': float(product.price),'title':product.title,'img':product.file_mainpic.url,'quantity':1})
    request.session['cart'] = cart
    return redirect('service')

def view_cart(request):
    cart = request.session.get('cart',[])
    if cart:
        df=pd.DataFrame(cart)
        df1=df.value_counts().reset_index()
        print(df1)
        df1['price']=df1['price']*df1['count']
        cart= df1.to_dict(orient='records')
        total_price = sum(item['price'] for item in cart)   
        return render(request,'cart.html', {'carts':cart, 'total_price': total_price})
    else:
        empty_cart_message = "Your cart is empty. Please add items before proceeding to book."
        return render(request, 'cart.html', {'carts': [], 'total_price': 0, 'empty_cart_message': empty_cart_message})

def remove_from_cart(request, product_id):
    cart = request.session.get('cart',[])
    cart = [item for item in cart if item['id'] != product_id]
    request.session['cart'] = cart    
    return redirect('view_cart') 


def contact(request,id):
    experts = get_object_or_404(Trainer,id=id)
    if request.method == "POST":
        Name = request.POST['user_name']
        Email = request.POST['user_email']
        Phone = request.POST['user_contact']
        message = request.POST['message']
        booking_date=request.POST['user_date']

        booking = Booking.objects.create(
            trainer=experts,
            user_name=Name,
            user_email=Email,
            user_contact=Phone,
            booking_date=datetime.strptime(booking_date, '%Y-%m-%d'),  # Convert string to datetime
            message=message
        )
        return render(request,'success.html',{'book':booking})
    else:
        return render(request,'contact.html',{'expert':experts})




def course_purchase(request,pk):
    course_details = course.objects.get(pk=pk)
    print(course_details)
    email_sub=email_subscription.objects.all()
    if request.method=="POST":
        
        Name1 = request.POST['name']
        country1 = request.POST['country']
        booking_date1 = request.POST['Therapy_date']
        email1 = request.POST['Email']
        Phone1 = request.POST['contact']
        payment1 = request.POST['payment']
        address1 = request.POST['address']
        
        booking_date_obj = date.fromisoformat(booking_date1)

        print("Name1:", Name1)
        print("Country1:", country1)
        print("booking_date_obj:",booking_date_obj)
        print("Email1:", email1)
        print("Phone1:", Phone1)
        print("Payment1:", payment1)
        print("Address1:", address1)
       

        print(type(course_details.course_name))
    
        cart1 = request.session.get('cart',[])
        
        cart_count=len(cart1)


        if payment1=='esewa':
            total=int(course_details.price)
            return render(request,'esewapayment.html',{'course':course_details,'t':total})
        elif payment1=='cod':
            try:
                print(course_details.course_name)
                save_product=course_buy(name=str(Name1),country=str(country1),
                                            Therpay_name=course_details,
                                            date=booking_date_obj,
                                            Email=email1,contact=str(Phone1),payment=str(payment1),
                                            address=str(address1),message='HEY How are you')
                print(str(save_product))
                print(save_product.save())

                email_sub = email_subscription.objects.filter(email=email1)

                if email_sub.exists():
                    pass
                else:
                    email_subscription.objects.create(email=email1)
                if save_product:
                     email_from = settings.EMAIL_HOST_USER
                     subject = 'Booking confirmation'
                     recipient_email=str(email1)
                     recipient_email1='anupthatal2@gmail.com'

                     context = {
                        'name':save_product.name,
                        'Therapy Name':course_details.course_name,
                        'country':save_product.country,
                        'address':save_product.address,
                        'payment':save_product.payment,
                        'courses':save_product.course_details,
                        'price':course_details.price,
                        'id':save_product.id,
                        'date':save_product.booking_date_obj
                        }
                     html_version = 'booking.html'
                     html_message = render_to_string(html_version, {'context': context})
                     message = EmailMessage(subject,html_message,email_from,[recipient_email,recipient_email1])
                     message.content_subtype = 'html'
                     try:
                         message.send()
                         return redirect('booked')  # Redirect to a success page
                     except Exception as e:
                         return HttpResponse("Error: " + str(e))  # Replace with your error handling logic
                    #  request.session['booking_successful'] = True
            except Exception as e:
                print(f"Error creating course_buy object: {e}")
    return render(request,'course_purchase.html',{'course':course_details})

def course_purchase_cart(request):
    cart = request.session.get('cart', [])
    df = pd.DataFrame(cart)
    df1 = df.value_counts().reset_index()
    df1['price'] = df1['price'] * df1['count']
    cart = df1.to_dict(orient='records')
    total_price = sum(item['price'] for item in cart)
    cart1 = request.session.get('cart', [])
    cart_count = len(cart1)
    if request.method == "POST":
        name = request.POST['name']
        country = request.POST['country']
        location = request.POST['country']
        email = request.POST['Email']
        contact = request.POST['contact']
        payment = request.POST['payment']
        try:
            any_special_request = request.POST['any_special_request']
        except KeyError:
            any_special_request = None
        if payment == 'esewa':
            total = int(total_price)
            return render(request,'esewapayment.html', {'t': total})
        elif payment == 'cod':
            item_cart = Itemcart.objects.create(
                name=name,
                country=country,
                location=location,
                Email=email,
                contact=contact,
                Any_sepcial_request=any_special_request,
                total_price=total_price,
            )
            auto_generated_id = item_cart.id
            selected_course_names = [item['name'] for item in cart]
            courses = course.objects.filter(course_name__in=selected_course_names)
            item_cart.items.set(courses)
            course_names = [course.course_name for course in courses]
            context = {
                'name': name,
                'country': country,
                'address': location,
                'payment': payment,
                'therapy_name': course_names,
                'price': total_price,
                'date': datetime.now().date(),
                'id': auto_generated_id
            }
            # html_version = 'booking.html'
            # html_message = render_to_string(html_version, {'context': context})
            # email_from = settings.EMAIL_HOST_USER
            # subject = 'Booking confirmation'
            # recipient_email = str(email)
            # recipient_email1 = 'anupthatal2@gmail.com'
            # message = EmailMessage(subject, html_message, email_from, [recipient_email, recipient_email1])
            # message.content_subtype = 'html'
            # message.send()
            request.session['cart'] = []
            return redirect('booked')
    return render(request, 'course_purchase_cart.html', {'carts': cart, 'total_p': total_price, 'cart': cart_count})


def booked(request):
    return render(request,'booked.html')