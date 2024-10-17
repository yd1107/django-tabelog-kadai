from django.shortcuts import render

# Create your views here.
from . import models
from django.views import generic

""" トップ画面=================================="""

class TopPageView(generic.ListView):
    template_name = "top_page.html"
    model = models.Restaurant
    queryset = models.Restaurant.objects.order_by('-rate')
    context_object_name = 'restaurant_list'

""" 会社概要=================================="""
class CompanyView(generic.TemplateView):
    template_name = "layout/company.html"

""" 利用規約=================================="""
class TermsView(generic.TemplateView):
    template_name = "layout/terms.html"


class TopPageView(generic.ListView):
    """ トップ画面=================================="""
    template_name = "top_page.html"
    model = models.Restaurant
    queryset = models.Restaurant.objects.order_by('-rate')
    context_object_name = 'restaurant_list'

    def get_context_data(self, **kwargs):
        if 'price_session' in self.request.session:
            self.request.session['price_session'] = 0
        if 'keyword_session' in self.request.session:
            self.request.session['keyword_session'] =''
        if 'category_session' in self.request.session:
            self.request.session['category_session'] =''
        if 'select_sort' in self.request.session:
            self.request.session['select_sort'] = '-created_at'
        context = super(TopPageView, self).get_context_data(**kwargs)
        category_list = models.Category.objects.all()
        new_restaurant_list = models.Restaurant.objects.all().order_by('-created_at')

        context.update({
            'category_list': category_list,
            'new_restaurant_list': new_restaurant_list,
        })
        return context