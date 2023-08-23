from django.shortcuts import render
from apps.transactions.models import Purchase, Sale
from django.contrib.humanize.templatetags.humanize import intcomma
import datetime

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

    sales = Sale.objects.get_monthly_income()
    expenses = Purchase.objects.get_monthly_expenses()
    month = datetime.date.today().month
    month = number_to_month(month)

    if sales > 0.00:
        profit = f"R$ {intcomma('{:0.2f}'.format(sales - expenses))}"
    elif expenses > 0.00:
        profit = f"R$ {intcomma('{:0.2f}'.format(-expenses))}"
    else:
        profit = f"R$ {intcomma('{:0.2f}'.format(0.00))}"

    sales = f"R$ {intcomma('{:0.2f}'.format(sales))}"
    expenses = f"R$ {intcomma('{:0.2f}'.format(expenses))}"
    

    return render(request, 'index.html', {'sales': sales, 'expenses': expenses, 'profit': profit, 'month': month})

def history(request):
    id = request.user.id
    earliest_sale = Sale.objects.filter(user=id).earliest('sale_date')
    earliest_purchase = Purchase.objects.filter(user=id).earliest('purchase_date')

    latest_sale = Sale.objects.filter(user=id).latest('sale_date')
    latest_purchase = Purchase.objects.filter(user=id).latest('purchase_date')

    if earliest_purchase.purchase_date > earliest_sale.sale_date:
        oldest_year = earliest_sale.sale_date.year
    else:
        oldest_year = earliest_purchase.purchase_date.year

    if latest_purchase.purchase_date > latest_sale.sale_date:
        newest_year = latest_sale.sale_date.year
    else:
        newest_year = latest_purchase.purchase_date.year

    years = list(range(oldest_year, newest_year+1))

    return render(request, 'history.html', {'years': years})

def month_history(request, month, year):
    id = request.user.id
    sales = Sale.objects.filter(user=id, sale_date__year=year ,sale_date__month=month)
    purchases = Purchase.objects.filter(user=id, purchase_date__year=year ,purchase_date__month=month)

    return render(request, 'month_history.html', {'sales': sales, 'purchases': purchases})

def handler404(request, exception, template_name="404.html"):
    response = render(request, template_name)
    response.status_code = 404
    return response