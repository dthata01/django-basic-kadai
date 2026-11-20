from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Product
from django.urls import reverse_lazy



# トップページのビューを作成する
class TopView(TemplateView):
  template_name = "top.html"

# ListViewを継承したビューを作成する
class ProductListView(ListView):
  model = Product
  # ページネーション機能の追加
  paginate_by = 3

# 商品追加用のビューを追加する
class ProductCreateView(CreateView):
  model = Product
  fields = '__all__'

# 商品編集用のビューを追加
class ProductUpdateView(UpdateView):
  model = Product
  fields = '__all__'
  template_name_suffix = '_update_form'

# 商品削除用のビューを追加
class ProductDeleteView(DeleteView):
  model = Product
  success_url = reverse_lazy('list')
  
# 商品詳細用のビューを追加する
class ProductDetailView(DetailView):
  model = Product
  fields = '__all__'
