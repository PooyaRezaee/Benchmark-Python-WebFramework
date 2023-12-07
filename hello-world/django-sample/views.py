from django.views import View
from django.http import HttpResponse
import time
import asyncio


class IndexView(View):
    async def get(self, request):
        return HttpResponse("Hello World")
        