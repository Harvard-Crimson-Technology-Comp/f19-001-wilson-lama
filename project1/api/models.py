from django.db import models

# TODO: you'll need to fill in the models that you create here!

# a class containing what happened in a purchase (who made it, when it was made, what it traded)
class PurchaseModel(models.Model):
    class Meta:
        app_label = 'api'
        timestamp = models.DateTimeField(auto_add_now=True)
        user = models.UserModel()
        symbol = models.CharField()
        price = models.FloatField()
        quantity = models.IntegerField()

# the class containing your user information (including their api token and password, etc)
class UserModel(models.Model):
    class Meta:
        app_label = 'api'
        first_name = models.CharField()
        last_name = models.CharField()
        api_token = models.TextField()
        password = models.TextField()
        username = models.CharField()
        portfolio = models.PortfolioModel()

# the class containing a portfolio of stocks
class PortfolioModel(models.Model):
    class Meta:
        app_label = 'api'
        cash = models.FloatField()

# a class containing a simple set of data on a stock within a portfolio
class StockModel(models.Model):
    class Meta:
        app_label = 'api'
        portfolio = models.PortfolioModel()
        symbol = models.CharField()
        quantity = models.IntegerField()