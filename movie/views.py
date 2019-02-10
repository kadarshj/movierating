from django.shortcuts import render
from movie.models import User
from .models import MoviesList,Subscribe
from  django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse


# Create your views here.
@login_required
def home(request):
    movie_list = MoviesList.objects.all()
    user = request.user
    user_obj = User.objects.get(email = user)
    user_id = user_obj.id

    page = request.GET.get('page', 1)
    paginator = Paginator(movie_list, 200)
    try:
        movielist = paginator.page(page)
    except PageNotAnInteger:
        movielist = paginator.page(1)
    except EmptyPage:
        movielist = paginator.page(paginator.num_pages)

    return render(request,"rating/dashboard.html",{'movielist': movielist, 'user_id': user_id})

@login_required
def SubscribeMovie(request,movie_id,user_id):
    subcount = Subscribe.objects.filter(user_id=user_id, movielist_id=movie_id).count()
    sub = Subscribe.objects.filter(user_id=user_id, movielist_id=movie_id).first()
    if not sub:
        Subscribe.objects.create(user_id=user_id, movielist_id=movie_id)
    else:
        if sub.is_subscribed:
            sub.is_subscribed = False
        else:
            sub.is_subscribed = True
        sub.save()
    if not sub:
        if subcount == 0:
            subsave = Subscribe.objects.filter(user_id=user_id, movielist_id=movie_id).first()
            subsave.is_subscribed = True
            subsave.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False})
    else:
        return JsonResponse({'success': True})


@login_required
def Mymovie(request):
    user = request.user
    user_obj = User.objects.get(email=user)
    user_id = user_obj.id
    mymovielist = Subscribe.objects.select_related('movielist').filter(user_id = user_id, is_subscribed = True)

    page = request.GET.get('page', 1)
    paginator = Paginator(mymovielist, 5)
    try:
        movielist = paginator.page(page)
    except PageNotAnInteger:
        movielist = paginator.page(1)
    except EmptyPage:
        movielist = paginator.page(paginator.num_pages)

    return render(request, "rating/mymovie.html", {'movielist': movielist, 'user_id': user_id})

@login_required
def Ranking(request):
    user_id = request.GET.get('user_id', None)
    movielist_id = request.GET.get('movielist_id', None)
    rating = request.GET.get('rating', None)
    star = Subscribe.objects.filter(user_id=user_id, movielist_id=movielist_id).first()
    star.rating = rating
    star.save()
    return JsonResponse({'success': True})


