from typing import Any, Dict
from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from django.views.generic import CreateView, ListView
from .models import Review
from primary.models import *
# Create your views here.


class ReviewCreateView(View):
    model = Review
    template_name = 'review/review.html'

    def get(self, request):

        # categories
        categories = Category.objects.filter(is_active=True)
        # brands
        brands = Brand.objects.filter(is_active=True)
        # models
        models = Model.objects.filter(is_active=True)
        # questions
        question = Question.objects.get(id=1)
        # product_user
        product_user = ProductUser.objects.all()

        context = {
            'categories': categories,
            'brands': brands,
            'models': models,
            'question': question,
            'product_user': product_user
        }
        return render(request, self.template_name, context=context)

    def post(self, request):
        # Handle form submission
        # Access form data using request.POST dictionary

        # Example: Retrieve form fields
        category = request.POST.get('category')
        brand = request.POST.get('brand')
        model = request.POST.get('model')

        rating = request.POST.get('rating_input')
        # reviewed_by = request.POST.get('reviewed_by')
        review_of_user = request.POST.get('review_of_user')
        # opinion = request.POST.get('opinion')
        ques = request.POST.get('ques-1')
        files = request.POST.get('files')

        print(request.POST)
        # Example: Perform form validation or processing

        # Example: Save form data to database
        review_create = Review.objects.create(
            category=Category.objects.get(id=category),
            brand=Brand.objects.get(id=brand),
            model=Model.objects.get(id=model),
            rating=rating,
            price_of_review=500,
            review_of_user=ProductUser.objects.get(id=review_of_user)
        )

        # Redirect after successful form submission
        return redirect('review-list')

    # def put(self, request, *args, **kwargs):


class ReviewListView(ListView):
    model = Review
    template_name = 'review/review_list.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        reviews = Review.objects.all()
        context["reviews_list"] = reviews
        return context
