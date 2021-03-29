from tortoise import Model, fields


class User(Model):
    id = fields.IntField(pk=True)
    uid = fields.IntField()

    name = fields.CharField(max_length=30, null=True)
    age = fields.IntField(null=True)

    count_messages = fields.IntField(default=0)

    class Meta:
        table = "users"
