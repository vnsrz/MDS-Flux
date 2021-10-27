from django.db.models.expressions import Exists
from django.shortcuts import render
from apps.transactions.models import Purchase, Sale
from django.contrib.humanize.templatetags.humanize import intcomma
import datetime
import decimal

def index(request):
    def number_to_month(argument):
        switcher = {
            1: "Janeiro",
            2: "Fevereiro",
            3: "Março",
            4: "Abril",
            5: "Maio",
            6: "Junho",
            7: "Julho",
            8: "Agosto",
            9: "Setembro",
            10: "Outubro",
            11: "Novembro",
            12: "Dezembro",
        }
        return switcher.get(argument, "Mês não encontrado")

    id = request.user.id

    sales = decimal.Decimal(Sale.objects.get_monthly_income(id))
    expenses = decimal.Decimal(Purchase.objects.get_monthly_expenses(id))
    month = datetime.date.today().month
    month = number_to_month(month)

    profit = f"R$ {intcomma('{:0.2f}'.format(sales - expenses))}"
    sales = f"R$ {intcomma('{:0.2f}'.format(sales))}"
    expenses = f"R$ {intcomma('{:0.2f}'.format(expenses))}"
    

    return render(request, 'index.html', {'sales': sales, 'expenses': expenses, 'profit': profit, 'month': month})

def history(request):
    id = request.user.id

    is_empty = 1
    newest_year = 0
    oldest_year = 3000

    if Sale.objects.filter(user=id):
        earliest_sale = Sale.objects.filter(user=id).earliest('sale_date')
        latest_sale = Sale.objects.filter(user=id).latest('sale_date')
        is_empty = 0

        oldest_year = earliest_sale.sale_date.year
        newest_year = latest_sale.sale_date.year

    if Purchase.objects.filter(user=id):
        earliest_purchase = Purchase.objects.filter(user=id).earliest('purchase_date')
        latest_purchase = Purchase.objects.filter(user=id).latest('purchase_date')
        is_empty = 0
        
        if earliest_purchase.purchase_date.year < oldest_year:
            oldest_year = earliest_purchase.purchase_date.year
        if latest_purchase.purchase_date.year > newest_year:
            newest_year = latest_purchase.purchase_date.year

    if is_empty:
        years = [1, 2]
    else:
        years = list(range(oldest_year, newest_year+1))

    return render(request, 'history.html', {'years': years, 'is_empty': is_empty})

def month_history(request, month, year):
    id = request.user.id
    sales = Sale.objects.filter(user=id, sale_date__year=year ,sale_date__month=month)
    purchases = Purchase.objects.filter(user=id, purchase_date__year=year ,purchase_date__month=month)

    return render(request, 'month_history.html', {'sales': sales, 'purchases': purchases})

def handler404(request, exception, template_name="404.html"):
    response = render(request, template_name)
    response.status_code = 404
    return response

def handler500(request):
    response = render(request, "500.html")
    response.status_code = 500
    return response