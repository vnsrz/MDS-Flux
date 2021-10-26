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

def historico(request):
    return render(request, 'historico.html')

def clientes(request):
    return render(request, 'clientes.html')

def inventario(request):
    return render(request, 'inventario.html')