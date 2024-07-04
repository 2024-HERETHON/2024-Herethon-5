from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import JsonResponse
from .models import PopupStore, Review, Location, Category
from .forms import ReviewForm, SearchForm, ReservationForm

# Create your views here.
def splash(request):
    return render(request, 'frontend/splash.html')

def main(request):
    return render(request, 'frontend/main.html')

def search(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data.get('query')  
            results = PopupStore.objects.filter(name__icontains=query)
        else:
            results = PopupStore.objects.none()
    else:
        form = SearchForm()
        results = PopupStore.objects.none()
    
    context = {
        'form': form,
        'results': results,
    }
    return render(request, 'frontend/search.html', context)

def map(request):
    stores = PopupStore.objects.all()
    categories= Category.objects.all()
    locations = Location.objects.all()
    context = {
        'stores': stores,
        'categories':categories,
        'locations': locations,
    }
    return render(request, 'frontend/map.html', context)
    # return render(request, 'frontend/map.html',{'stores':stores})

def magazine(request, magazine_id):
    magazine= get_object_or_404(PopupStore,pk=magazine_id)
    return render(request, 'frontend/magazine.html',{'magazine':magazine})

def magazine(request):
    return render(request, 'frontend/magazine.html')

def mypage(request):
    return render(request, 'frontend/mypage.html')

def login(request):
    return render(request, 'frontend/login.html')

def signup(request):
    return render(request, 'frontend/signup.html')

def signdone(request):
    return render(request, 'frontend/signdone.html')

# def popupstore_list(request):
#     popups = PopupStore.objects.all()
#     context = {
#         'popups': popups,
#     }
#     return render(request, 'frontend/popupstore.html', context)

def popupstore(request, popup_id):
    popup = get_object_or_404(PopupStore, id = popup_id)
    reviews = popup.review_set.all()
    context= {
        'popup':popup,
        'reviews':reviews,
    }
    return render(request, 'frontend/popupstore.html',context)

# @login_required
def popupreserv(request,popup_id):
    popup = get_object_or_404(PopupStore, id=popup_id)
    
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.popup_store = popup  # assuming Reservation model has a ForeignKey to PopupStore
            reservation.save()
            return redirect('popplace:popupreserved', popup_id=popup_id)
    else:
        form = ReservationForm()
    
    context = {
        'popup': popup,
        'form': form,
    }
    return render(request, 'frontend/popupreserv.html', context)

def popupreserved(request,popup_id):
    popup = get_object_or_404(PopupStore, id=popup_id)
    context = {'popup': popup,}
    return render(request, 'frontend/popupreserved.html', context)

def popupreview(request, popup_id):

    popup = get_object_or_404(PopupStore, id=popup_id)
    reviews = Review.objects.filter(popup_store=popup)

    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.popup_store = popup
            # review.user = request.user
            review.save()
            return redirect('popplace:popupstore', popup_id=popup_id)
    else:
        form = ReviewForm()

    context = {
        'popup': popup,
        'reviews': reviews,
        'form': form,
    }
    return render(request, 'frontend/popupreview.html', context)

def category(request):
    category = request.GET.get('category')  # URL에서 카테고리 파라미터 받아오기
    popup_stores = PopupStore.objects.all()

    if category:
        popup_stores = popup_stores.filter(category=category)

    context = {
        'popup_stores': popup_stores,
        'selected_category': category,  # 선택된 카테고리를 템플릿에 전달
    }
    return render(request, 'frontend/category.html', context)



# def category(request, category):
#     # 작은 카테고리에 따라 해당하는 팝업들을 가져와 JSON 형태로 반환
#     popups = PopupStore.objects.filter(category__iexact=category)  # 대소문자 구분 없이 필터링
#     data = list(popups.values('name', 'description'))  # 필요한 필드만 JSON으로 변환
    
#     return JsonResponse(data, safe=False)