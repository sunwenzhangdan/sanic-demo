from datetime import date, datetime
import json

from tortoise import Model, fields


class Users(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(50)
    password = fields.CharField(50)
    first_name = fields.CharField(50)

    def __str__(self):
        return


class OutboundStatistics(Model):
    id = fields.IntField(pk=True)
    sap_no = fields.BigIntField(null=True,pk=False)
    out_type = fields.CharField(null=True, max_length=255)
    out_category = fields.CharField(null=True, max_length=255)
    deliver_year = fields.BigIntField(null=True, pk=False)
    mark_month = fields.BigIntField(pk=False)
    out_month = fields.BigIntField(pk=False)
    # out_date = fields.DateField(null=True)
    province = fields.CharField(null=True, max_length=255)
    city = fields.CharField(null=True, max_length=255)
    area = fields.CharField(null=True, max_length=255)
    area_level = fields.CharField(null=True, max_length=255)
    bus_owner = fields.CharField(null=True, max_length=255)
    customer_name = fields.CharField(null=True, max_length=255)
    product_name = fields.CharField(null=True, max_length=255)
    package_form = fields.CharField(null=True, max_length=255)
    specifications = fields.CharField(null=True, max_length=255)
    out_num = fields.BigIntField(null=True, pk=False)
    single_price = fields.CharField(null=True, max_length=255)
    sale_num = fields.CharField(null=True, max_length=255)
    out_no = fields.CharField(null=True, max_length=255)
    deliver_no = fields.BigIntField(null=True, pk=False)
    comment = fields.CharField(null=True, max_length=255)
    batch_no = fields.CharField(null=True, max_length=255)
    # dead_line = fields.DateField(null=True, max_length=255)
    return_label = fields.CharField(null=True, max_length=255)
    invoice_pass = fields.CharField(null=True, max_length=255)
    invoice_type = fields.CharField(null=True, max_length=255)
    invoice_count = fields.BigIntField(null=True,pk=False)
    promoter_company_name = fields.CharField(null=True, max_length=255)
    foregin_money = fields.CharField(null=True, max_length=255)
    crm_client_code = fields.CharField(null=True, max_length=255)
    pass_one = fields.CharField(null=True, max_length=255)
    pass_two = fields.CharField(null=True, max_length=255)
    pass_unit = fields.CharField(null=True, max_length=255)
    out_num_discount = fields.BigIntField(null=True, pk=False)

    def __str__(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)


。。。。。。
