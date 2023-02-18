from django.contrib.auth.models import User
from django.core.mail import send_mail
from drf_wallet.celery import app
from wallet.models import Transaction
from datetime import timedelta, datetime


@app.task
def mass_send_mail():
    """
    Function for send email to all users
    in DB with detail statistic
    of transaction for yesterday
    :return: bash string-message
    """
      # list for stores all register users email
    yesterday = datetime.now() - timedelta(days=1)
    # yesterday in format DateTime
    for user in User.objects.all():
        recipients.append(user.email)  # add user's mail to list
        query_transaction = Transaction.objects.filter(
            user=user.id, date=yesterday.date()).values()
        # queryset conatains for each user his transactions for yesterday
        transactions = []
        for item in query_transaction:
            # create list with user's transactions
            one_row = 'Вид: {0} / Описание:{1}  /' \
                      '  Cумма: {2}  / Дата: {3}'.format(
                            item['kind'], item['description'],
                            item['amount'], item['date'])
            transactions.append(one_row)
        if len(transactions) == 0:
            # if there are no transactions,
            # the message contains an appropriate informational string
            message = "За {0} операций не произведено".format(yesterday.date())
        else:
            # bellow counters for store amount of transactions
            # for expenses and incomes
            ex_count = 0
            in_count = 0
            sum_expense = 0
            sum_income = 0
            for i in transactions:
                # sort each transaction and count
                # the amount of income and expenses for yesterday
                if i.find("Расход") != -1:
                    ex_count += 1
                    find = i.split("/")
                    s = str(find[2]).split(":")[1]
                    sum_expense += float(s)
                else:
                    in_count += 1
                    find = i.split("/")
                    s = str(find[2]).split(":")[1]
                    sum_income += float(s)
            message = "За {0} произведено {1} операций, из которых " \
                      "{2} операции расхода; " \
                      "{3} операции дохода. " \
                      "Сумма расходов: {4} BYN. " \
                      "Сумма доходов: {5} BYN".format(
                                yesterday.date(),
                                len(transactions),
                                ex_count,
                                in_count,
                                round(sum_expense, 3),
                                round(sum_income, 3)
                                )
        subject = "Рассылка статистики"
        from_email = "DjangoMarket@yandex.by"
        send_mail(subject,
                  message,
                  from_email,
                  user.email,
                  fail_silently=False)
    return "sending emails"
