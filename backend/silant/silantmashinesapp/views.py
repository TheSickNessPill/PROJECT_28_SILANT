from rest_framework.decorators import api_view
from django.http import JsonResponse, HttpRequest
from rest_framework.views import Request

from rest_framework.authtoken.models import Token
from silantmashinesapp.models import Mashine, Maintence, Complaints
from silantaccountsapp.models import SilantClients, SilantManagers, SilantServiveCompanies


@api_view(["POST"])
def base_mashines(request: Request):
    fartory_number = request.data.get("factoryNumber", "")
    if not fartory_number:
        return JsonResponse({
            "status": "error",
            "text": "empty factory mashine number"
        })

    fields_name = [
        "Зав. № машины", "Модель техники", "Модель двигателя", "Зав. № двигателя",
        "Модель трансмиссии", "Зав. № трансмиссии", "Модель ведущего моста",
        "Зав. № ведущего моста", "Модель управляемого моста", "Зав. № управляемого моста"
    ]

    mashines = Mashine.objects.filter(factory_mashine_number=fartory_number)
    if not mashines:
        return JsonResponse({
            "status": "error",
            "text": "Машины с таким заводским номером не найдено."
        })

    mashines = list(map(lambda x: x.get_base_mashine(), mashines))
    print(mashines)
    return JsonResponse({
        "status": "ok",
        "header": fields_name,
        "baseMashineData": mashines
    })


@api_view(["POST"])
def full_data_by_user(request: Request):
    print('full_data_by_user')
    token = request.data["token"]
    role = request.data["role"]

    print(token, role)

    token_obj = Token.objects.filter(pk=token)
    if token_obj:
        user = token_obj[0].user
        if role == "client":
            client = SilantClients.objects.filter(user=user)
            if not client:
                return JsonResponse({
                    "status": "error",
                    "text": f"This user is not {role}"
                })
            client = client[0]
            mashine_fields_name = [
                "Зав. № машины", "Модель техники", "Модель двигателя", "Зав. № двигателя",
                "Модель трансмиссии", "Зав. № трансмиссии", "Модель ведущего моста",
                "Зав. № ведущего моста", "Модель управляемого моста", "Зав. № управляемого моста",
                "Договор поставки №, дата", "Дата отгрузки с завода", "Грузополучатель (конечный потребитель)",
                "Адрес поставки (эксплуатации)", "Комплектация (доп. опции)", "Клиент", "Сервисная компания"
            ]
            mashines = Mashine.objects.filter(client=client)
            mashines_data = list(map(lambda x: x.get_full_data(), mashines))
            mashines_data_ids = list(map(lambda x: x.id, mashines))

            maintance_fields_name = [
                "Вид ТО", "Дата проведения ТО", "Наработка, м/час",
                "№ заказ-наряда", "Дата заказ-наряда", "Машина"
            ]

            maintance = Maintence.objects.filter(mashine__in=mashines)
            maintance_data = list(map(lambda x: x.get_full_data(), maintance))
            maintance_data_ids = list(map(lambda x: x.id, maintance))

            complaints_fields_name = [
                "Дата отказа", "Наработка, м/час", "Узел отказа",
                "Описание отказа", "Способ восстановления", "Используемые запасные части",
                "Дата восстановления", "Время простоя техники", "Mашина"
            ]
            complaints = Complaints.objects.filter(mashine__in=mashines)
            complaints_data = list(map(lambda x: x.get_full_data(), complaints))
            complaints_data_ids = list(map(lambda x: x.id, complaints))

            return JsonResponse({
                "status": "ok",
                "mashineFieldsName": mashine_fields_name,
                "mashinesData": mashines_data,
                "maintanceFieldsName": maintance_fields_name,
                "maintanceData": maintance_data,
                "complaintsFieldsName": complaints_fields_name,
                "complaintsData": complaints_data
            })

        elif role == "service_company":
            client = SilantServiveCompanies.objects.filter(user=user)
            if not client:
                return JsonResponse({
                    "status": "error",
                    "text": f"This user is not {role}"
                })
            client = client[0]
            mashine_fields_name = [
                "Зав. № машины", "Модель техники", "Модель двигателя", "Зав. № двигателя",
                "Модель трансмиссии", "Зав. № трансмиссии", "Модель ведущего моста",
                "Зав. № ведущего моста", "Модель управляемого моста", "Зав. № управляемого моста",
                "Договор поставки №, дата", "Дата отгрузки с завода", "Грузополучатель (конечный потребитель)",
                "Адрес поставки (эксплуатации)", "Комплектация (доп. опции)", "Клиент", "Сервисная компания"
            ]
            mashines = Mashine.objects.filter(service_company=client)
            mashines_data = list(map(lambda x: x.get_full_data(), mashines))
            mashines_data_ids = list(map(lambda x: x.id, mashines))

            maintance_fields_name = [
                "Вид ТО", "Дата проведения ТО", "Наработка, м/час",
                "№ заказ-наряда", "Дата заказ-наряда", "Машина"
            ]

            maintance = Maintence.objects.filter(mashine__in=mashines)
            maintance_data = list(map(lambda x: x.get_full_data(), maintance))
            maintance_data_ids = list(map(lambda x: x.id, maintance))

            complaints_fields_name = [
                "Дата отказа", "Наработка, м/час", "Узел отказа",
                "Описание отказа", "Способ восстановления", "Используемые запасные части",
                "Дата восстановления", "Время простоя техники", "Mашина"
            ]
            complaints = Complaints.objects.filter(mashine__in=mashines)
            complaints_data = list(
                map(lambda x: x.get_full_data(), complaints))
            complaints_data_ids = list(map(lambda x: x.id, complaints))

            return JsonResponse({
                "status": "ok",
                "mashineFieldsName": mashine_fields_name,
                "mashinesData": mashines_data,
                "mashinesDataIds": mashines_data_ids,
                "maintanceFieldsName": maintance_fields_name,
                "maintanceData": maintance_data,
                "maintanceDataIds": maintance_data_ids,
                "complaintsFieldsName": complaints_fields_name,
                "complaintsData": complaints_data,
                "complaintsDataIds": complaints_data_ids
            })
        elif role == "manager":
            print("MANAGERS")
            client = SilantManagers.objects.filter(user=user)
            if not client:
                return JsonResponse({
                    "status": "error",
                    "text": f"This user is not {role}"
                })
            client = client[0]
            mashine_fields_name = [
                "Зав. № машины", "Модель техники", "Модель двигателя", "Зав. № двигателя",
                "Модель трансмиссии", "Зав. № трансмиссии", "Модель ведущего моста",
                "Зав. № ведущего моста", "Модель управляемого моста", "Зав. № управляемого моста",
                "Договор поставки №, дата", "Дата отгрузки с завода", "Грузополучатель (конечный потребитель)",
                "Адрес поставки (эксплуатации)", "Комплектация (доп. опции)", "Клиент", "Сервисная компания"
            ]
            mashines = Mashine.objects.all()
            mashines_data = list(map(lambda x: x.get_full_data(), mashines))
            mashines_data_ids = list(map(lambda x: x.id, mashines))

            maintance_fields_name = [
                "Вид ТО", "Дата проведения ТО", "Наработка, м/час",
                "№ заказ-наряда", "Дата заказ-наряда", "Машина"
            ]

            maintance = Maintence.objects.filter(mashine__in=mashines)
            maintance_data = list(map(lambda x: x.get_full_data(), maintance))
            maintance_data_ids = list(map(lambda x: x.id, maintance))

            complaints_fields_name = [
                "Дата отказа", "Наработка, м/час", "Узел отказа",
                "Описание отказа", "Способ восстановления", "Используемые запасные части",
                "Дата восстановления", "Время простоя техники", "Mашина"
            ]
            complaints = Complaints.objects.filter(mashine__in=mashines)
            complaints_data = list(
                map(lambda x: x.get_full_data(), complaints))
            complaints_data_ids = list(map(lambda x: x.id, complaints))

            return JsonResponse({
                "status": "ok",
                "mashineFieldsName": mashine_fields_name,
                "mashinesData": mashines_data,
                "mashinesDataIds": mashines_data_ids,
                "maintanceFieldsName": maintance_fields_name,
                "maintanceData": maintance_data,
                "maintanceDataIds": maintance_data_ids,
                "complaintsFieldsName": complaints_fields_name,
                "complaintsData": complaints_data,
                "complaintsDataIds": complaints_data_ids
            })
        else:
            return JsonResponse({
                "status": "error",
                "text": "role do not exists"
            })

    return JsonResponse({
        "status": "error",
        "text": "That Token do not exists"
    })
