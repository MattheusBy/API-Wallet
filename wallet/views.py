import requests
from rest_framework import generics, viewsets
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from wallet.models import UserBalance, Transaction
from wallet.serializer import UserBalanceSerializer, TransactionSerializer


# Create your views here.
class ActivateUser(GenericAPIView):

    def get(self, request, uid, token, format=None):
        payload = {'uid': uid, 'token': token}

        url = "http://localhost:8000/auth/users/activation/"
        response = requests.post(url, data=payload)

        if response.status_code == 204:
            return Response({}, response.status_code)
        else:
            return Response(response.json())


class UserBalanceAPIView(generics.CreateAPIView,
                         generics.UpdateAPIView):
    """
    Allows the user to set the balance,
    to get information the current balance and update it
    """
    queryset = UserBalance.objects.all()
    serializer_class = UserBalanceSerializer

    def get(self, request, *args, **kwargs):
        # to get current balance
        balance = UserBalance.objects.get(
            user=self.request.user)
        self.serializer = UserBalanceSerializer(balance)
        return Response(
            {"Ваш текущий баланс составляет": self.serializer.data['balance']}
        )

    def post(self, request, *args, **kwargs):
        # to set balance after register
        balance = UserBalance.objects.create(
            user=self.request.user, balance=self.request.data['balance'])
        self.serializer = UserBalanceSerializer(balance)
        return Response(
            {"Ваш баланс составляет": self.serializer.data['balance']}
            )

    def put(self, request, *args, **kwargs):
        # to update balance at any point in time
        current_balance = UserBalance.objects.get(
            user=self.request.user)
        current_balance.balance = self.request.data['balance']
        current_balance.save()
        self.serializer = UserBalanceSerializer(current_balance)
        return Response({"Ваш баланс обновлен и составляет":
                        self.serializer.data['balance']}
                        )


class TransactionViewSet(viewsets.ViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def create(self, request):
        change_balance = UserBalance.objects.get(
            user=request.user)
        if request.data['kind'] == "Доход":
            self.queryset = Transaction.objects.create(
                description=request.data['description'],
                category=request.data['category'],
                amount=request.data['amount'],
                user=request.user,
                kind=request.data['kind'])
            change_balance.balance += round(float(request.data['amount']), 2)
            change_balance.save()
        else:
            self.queryset = Transaction.objects.create(
                description=request.data['description'],
                category=request.data['category'],
                amount=request.data['amount'],
                user=request.user,
                kind=request.data['kind'])
            change_balance.balance -= round(float(request.data['amount']), 2)
            change_balance.save()
        serializer = TransactionSerializer(self.queryset)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        self.queryset = Transaction.objects.get(user=request.user, pk=pk)
        self.serializer = TransactionSerializer(self.queryset)
        return Response(self.serializer.data)

    def update(self, request, pk=None):
        self.queryset_update = Transaction.objects.filter(
            user=request.user, pk=pk).update(
            description=self.request.data['description'],
            category=self.request.data['category'],
            amount=self.request.data['amount'],
            user=self.request.user,
            kind=self.request.data['kind']
        )
        self.queryset = Transaction.objects.get(user=request.user, pk=pk)
        self.serializer = TransactionSerializer(self.queryset)
        return Response(self.serializer.data)

    def destroy(self, request, pk=None):
        self.queryset = Transaction.objects.filter(
            user=request.user, pk=pk).delete()
        return Response('Запись {0} удалена'.format(self.request.data))
