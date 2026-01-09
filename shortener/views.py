from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Link
from django.http import HttpResponseRedirect # Still used for redirect_url if preferred, but redirect is cleaner

def index(request):
    short_url = None
    long_url = ""
    error = None
    
    if request.method == 'POST':
        long_url = request.POST.get('long_url')
        if long_url:
            # Simple validation, Django's URLField in model handles more strict validation if using Forms
            if not long_url.startswith(('http://', 'https://')):
                 long_url = 'http://' + long_url
            
            try:
                link, created = Link.objects.get_or_create(long_url=long_url)
                # Construct full short URL
                short_url = request.build_absolute_uri('/') + link.short_code
            except Exception as e:
                error = "Something went wrong. Please try again."
        else:
            error = "Please enter a URL"

    return render(request, 'shortener/main.html', {
        'display_url': short_url, 
        'long_url': long_url,
        'error': error
    })

def redirect_url(request, short_code):
    link = get_object_or_404(Link, short_code=short_code)
    return redirect(link.long_url)

@api_view(['POST'])
def api_shorten(request):
    long_url = request.data.get('long_url')
    if not long_url:
        return Response({'error': 'long_url is required'}, status=status.HTTP_400_BAD_REQUEST)
    
    # Validation logic same as above
    if not long_url.startswith(('http://', 'https://')):
        long_url = 'http://' + long_url

    try:
        link, created = Link.objects.get_or_create(long_url=long_url)
        full_short_url = request.build_absolute_uri('/') + link.short_code
        
        return Response({
            'short_code': link.short_code,
            'long_url': link.long_url,
            'short_url': full_short_url,
            'created_at': link.created_at
        })
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
