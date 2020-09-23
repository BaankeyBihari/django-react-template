from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_GET
import json

def core_index(request):
    return render(request, "build/index.html")

def core_book(request):
    return render(request, "build/book.html")

def core_asset_manifest(request):
    with open('frontend/build/asset-manifest.json', 'r') as amf:
        assetManifestData = json.load(amf)
    return JsonResponse(assetManifestData, safe=False)

@require_GET
def robots_txt(request):
    lines = [
        "User-Agent: *",
        "Disallow: ",
        # "Disallow: /private/",
        # "Disallow: /junk/",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")
