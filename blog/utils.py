from django.db.models import Q
from .models import Blog, Comments, Tags, Categories
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from random import shuffle

def blogimgnames():
    blog_images=['salvation', 'jesus', 'good']
    return blog_images
    
def searchStuff(request):
    q=''
    if request.GET.get('q'):
        q= request.GET.get('q')

    # query= q.split()
    tags= Tags.objects.filter(name__icontains=q)
    categories= Categories.objects.filter(name__icontains=q)
    blog= Blog.objects.distinct().filter(
        
            Q(title__icontains= q) |
            Q(body__icontains=q) |
            Q(tags__in=tags) |
            Q(categories__in=categories) |
            Q(addtag__icontains=q) |
            Q(addcategory__icontains=q)
    )

    
    return blog, q

def paginateQuery(request, query_set, result):
    page=request.GET.get('page')
    
    paginator= Paginator(query_set, result)

    try:
        blogs= paginator.page(page)
    except PageNotAnInteger:
        page = 1
        blogs=paginator.page(page)
    except EmptyPage:
        page= paginator.num_pages
        blogs=paginator.page(page)

    blogs=paginator.page(page)
    # disorder the objects in the page
    # reoder=[]
    # for i in blogs:
    #     reoder.append(i)
    # shuffle(reoder)
    # disorder_blog=reoder
    # end of disoerder
    leftIndex= (int(page)-1)
    if leftIndex<1:
        leftIndex=1

    RightIndex=(int(page)+10)

    if RightIndex>paginator.num_pages:
        RightIndex=paginator.num_pages+1


    customRange= range(leftIndex,RightIndex)

    return blogs, customRange

def sideBlog(blog, no):
    bl=[]
    x=0
    for b in blog:
        if x>=no:
            break
        bl.append(b)
        x+=1

    return bl

def disorder_Blog(blog):
    disorder_blog = blog.order_by("?")
    return disorder_blog