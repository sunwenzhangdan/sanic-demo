from tortoise import Model, fields


class Users(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(50)
    password=fields.CharField(50)
    first_name=fields.CharField(50)

    def __str__(self):
        return f"User {self.id}: {self.username}:{self.first_name}"


class OutboundStatistics(Model):
    id = fields.IntField(pk=True)
    sap_no = fields.BigIntField(100)
    out_type = fields.CharField(100)
    out_category = fields.CharField(100)
    deliver_year = fields.BigIntField(100)
    mark_month = fields.BigIntField(100)
    out_month = fields.BigIntField(100)
    out_date = fields.DateField
    province = fields.CharField(100)
    city = fields.CharField(100)
    county = fields.CharField(100)
    area = fields.CharField(100)
    area_level = fields.CharField(100)
    bus_owner = fields.CharField(100)
    customer_name = fields.CharField(100)
    product_name = fields.CharField(100)
    package_form = fields.CharField(100)
    specifications = fields.CharField(100)
    out_num = fields.BigIntField(100)
    single_price = fields.CharField(100)
    sale_num = fields.CharField(100)
    out_no = fields.CharField(100)
    deliver_no = fields.BigIntField(100)
    comment = fields.CharField(100)
    batch_no = fields.CharField(100)
    dead_line = fields.DateField
    return_label = fields.CharField(100)
    invoice_pass = fields.CharField(100)
    invoice_type = fields.CharField(100)
    invoice_count = fields.BigIntField(100)
    promoter_company_name = fields.CharField(100)
    foregin_money = fields.CharField(100)
    crm_client_code = fields.CharField(100)
    pass_one = fields.CharField(100)
    pass_two = fields.CharField(100)
    pass_unit = fields.CharField(100)
    out_num_discount = fields.BigIntField(100)