from rest_framework.decorators import api_view
from django.http import JsonResponse, HttpRequest
from rest_framework.views import Request


from rest_framework.authtoken.models import Token
from silantaccountsapp.models import (
    SilantUser, SilantClients, SilantManagers, SilantServiveCompanies
)


@api_view(["POST"])
def silant_login(request: Request):
    login = request.data["login"]
    password = request.data["password"]
    print(login, password)
    user = SilantUser.objects.filter(username=login)
    if user:
        print("do", user)
        user = user[0]
        if user.password == password:
            role_info = (
                SilantClients.objects.filter(user=user) or
                SilantManagers.objects.filter(user=user) or
                SilantServiveCompanies.objects.filter(user=user)
            )
            role_info = role_info[0]
            role = role_info.access.role_name or ""
            role_access = role_info.access.role_access

            token = user.login()
            expired_time = user.get_expired_time()

            return JsonResponse({
                "status": "ok",
                "companyName": user.company_name,
                "role": role,
                "access": role_access,
                "token": token,
                "expired_time": expired_time
            })

        return JsonResponse({
            "status": "error",
            "text": "This password does not exists"
        })

    return JsonResponse({
        "status": "error",
        "text": "This user does not exists"
    })


@api_view(["POST"])
def silant_logout(request: Request):
    token = request.data["token"]
    row = Token.objects.filter(key=token)
    if row:
        row = row[0]
        user = row.user
        user.logout()

        return JsonResponse({
            "status": "ok",
            "text": "logout"
        })
    return JsonResponse({
        "status": "error",
        "text": "token does not exists"
    })