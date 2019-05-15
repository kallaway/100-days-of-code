from django.shortcuts import render
from django.views import View


class IndexView(View):
    template = 'index.html'

    def get(self, request):
        return render(request, self.template)
