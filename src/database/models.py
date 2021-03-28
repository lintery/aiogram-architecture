from tortoise import Model, fields


class User(Model):
    id = fields.IntField(pk=True)
    uid = fields.IntField()

    count_messages = fields.IntField(default=0)

    class Meta:
        table = "users"
