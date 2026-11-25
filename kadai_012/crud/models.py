from django.db import models
from django.urls import reverse

# カテゴリモデルを追加
class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
# サンプルモデルの追加
class Product(models.Model):
    # 商品名を格納するフィールド(文字列200文字)
    name = models.CharField(max_length=200)
    # 商品の価格を格納するフィールド(正の整数のみ)
    price = models.PositiveIntegerField()
    # カテゴリを外部キーとして追加
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # 画像を格納するフィールド(空白可、デフォルト画像を指定)
    img = models.ImageField(blank=True, default='noImage.png')
    # 商品の詳細を格納するフィールドを追加(空白可)
    detail = models.TextField(blank=True, null=True)

    # 文字列として商品名を返すようにする。
    def __str__(self):
        return self.name
    
    # 新規作成・編集完了時のリダイレクト先
    def get_absolute_url(self):
        return reverse('list')