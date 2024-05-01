from silantaccountsapp.models import SilantClients, SilantServiveCompanies
from django.db import models


#  ----reference tables
class MashineModel(models.Model):
    name = models.TextField(editable=True, null=False)
    description = models.TextField(editable=True, null=True)

    def __str__(self) -> str:
        return self.name


class EngineModel(models.Model):
    name = models.TextField(editable=True, null=False)
    description = models.TextField(editable=True, null=True)

    def __str__(self) -> str:
        return self.name


class TransmissionModel(models.Model):
    name = models.TextField(editable=True, null=False)
    description = models.TextField(editable=True, null=True)

    def __str__(self) -> str:
        return self.name


class DriveAxleModel(models.Model):
    name = models.TextField(editable=True, null=False)
    description = models.TextField(editable=True, null=True)

    def __str__(self) -> str:
        return self.name


class SteeringAxleModel(models.Model):
    name = models.TextField(editable=True, null=False)
    description = models.TextField(editable=True, null=True)

    def __str__(self) -> str:
        return self.name


class MaintenanceType(models.Model):
    name = models.TextField(editable=True, null=False)
    description = models.TextField(editable=True, null=True)

    def __str__(self) -> str:
        return self.name


class RefusalNode(models.Model):
    name = models.TextField(editable=True, null=False)
    description = models.TextField(editable=True, null=True)

    def __str__(self) -> str:
        return self.name


class RecoveryMethod(models.Model):
    name = models.TextField(editable=True, null=False)
    description = models.TextField(editable=True, null=True)

    def __str__(self) -> str:
        return self.name
#  reference tables----


class Mashine(models.Model):
    factory_mashine_number = models.TextField(editable=True, null=False, unique=True, help_text="Зав. № машины")
    mashine_model = models.ForeignKey(MashineModel, on_delete=models.CASCADE, help_text="Модель техники")
    engine_model = models.ForeignKey(EngineModel, on_delete=models.CASCADE, help_text="Модель двигателя")
    factory_engine_number = models.TextField(editable=True, null=False, help_text="Зав. № двигателя")
    transmission_model = models.ForeignKey(TransmissionModel, on_delete=models.CASCADE, help_text="Модель трансмиссии")
    factory_transmission_number = models.TextField(editable=True, null=False, help_text="Зав. № трансмиссии")
    drive_axle_model = models.ForeignKey(DriveAxleModel, on_delete=models.CASCADE, help_text="Модель ведущего моста")
    factory_drive_axle_number = models.TextField(editable=True, null=False, help_text="Зав. № ведущего моста")
    steering_axle_model = models.ForeignKey(SteeringAxleModel, on_delete=models.CASCADE, help_text="Модель управляемого моста")
    factory_steering_axle_number = models.TextField(editable=True, null=False, help_text="Зав. № управляемого моста")
    #####
    supply_agreement = models.TextField(editable=True,blank=True, null=True, help_text="Договор поставки №, дата")
    factory_shipment_date = models.DateField(editable=True, null=False, help_text="Дата отгрузки с завода")
    consignee = models.TextField(editable=True, null=False, help_text="Грузополучатель (конечный потребитель)")
    delivery_address = models.TextField(editable=True, null=False, help_text="Адрес поставки (эксплуатации)")
    equipment = models.TextField(editable=True, null=False, help_text="Комплектация (доп. опции)")
    client = models.ForeignKey(SilantClients, on_delete=models.CASCADE, null=True, help_text="Клиент")
    service_company = models.ForeignKey(SilantServiveCompanies, on_delete=models.CASCADE,  null=True, help_text="Сервисная компания")

    def __str__(self) -> str:
        return self.factory_mashine_number

    def get_base_mashine(self):
        return [
            self.factory_mashine_number, self.mashine_model.name, self.engine_model.name,
            self.factory_engine_number, self.transmission_model.name, self.factory_transmission_number,
            self.drive_axle_model.name, self.factory_drive_axle_number, self.steering_axle_model.name,
            self.factory_steering_axle_number
        ]

    def get_full_data(self):
        return [
            self.factory_mashine_number, self.mashine_model.name, self.engine_model.name,
            self.factory_engine_number, self.transmission_model.name, self.factory_transmission_number,
            self.drive_axle_model.name, self.factory_drive_axle_number, self.steering_axle_model.name,
            self.factory_steering_axle_number,
            self.supply_agreement, self.factory_shipment_date, self.consignee, self.delivery_address,
            self.equipment, self.client.user.company_name, self.service_company.user.company_name
        ]

class Maintence(models.Model):
    maintence_type = models.ForeignKey(MaintenanceType, on_delete=models.CASCADE, help_text="Вид ТО")
    maintence_date = models.DateField(editable=True, null=False, help_text="Дата проведения ТО")
    operating_time = models.IntegerField(editable=True, null=False, help_text="Наработка, м/час")
    work_order_number = models.TextField(editable=True, null=False, help_text="№ заказ-наряда")
    work_order_date = models.DateField(editable=True, null=False, help_text="Дата заказ-наряда")
    mashine = models.ForeignKey(Mashine, on_delete=models.CASCADE, help_text="Машина")
    # service_company = models.ForeignKey(ServiceCompany, on_delete=models.CASCADE, help_text="Сервисная компания")

    def __str__(self) -> str:
        return f"{self.mashine.factory_mashine_number}: {self.work_order_number}"

    def get_full_data(self):
        return [
            self.maintence_type.name, self.maintence_date, self.operating_time,
            self.work_order_number, self.work_order_date, self.mashine.factory_mashine_number
        ]


class Complaints(models.Model):
    refusal_date = models.DateField(editable=True, null=False, help_text="Дата отказа")
    operating_time = models.FloatField(editable=True, null=False, help_text="Наработка, м/час")
    refusal_node = models.ForeignKey(RefusalNode, on_delete=models.CASCADE, help_text="Узел отказа")
    refusal_description = models.TextField(editable=True, null=False, help_text="Описание отказа")
    recovery_method = models.ForeignKey(RecoveryMethod, on_delete=models.CASCADE, help_text="Способ восстановления")
    spare_parts_used = models.TextField(editable=True, blank=True, null=True, help_text="Используемые запасные части")
    recovery_date = models.DateField(editable=True, null=False, help_text="Дата восстановления")
    mashine_downtime = models.TextField(editable=True, null=False, help_text="Время простоя техники")
    mashine = models.ForeignKey(Mashine, on_delete=models.CASCADE, help_text="Mашина")
    # service_company = models.ForeignKey(ServiceCompany, on_delete=models.CASCADE, null=True, help_text="Cервисная компания") ##

    def __str__(self) -> str:
        return f"{self.mashine.factory_mashine_number}: {self.refusal_date.isoformat()}"

    def get_full_data(self):
        return [
            self.refusal_date, self.operating_time, self.refusal_node.name, self.refusal_description,
            self.recovery_method.name, self.spare_parts_used, self.recovery_date, self.mashine_downtime,
            self.mashine.factory_mashine_number
        ]