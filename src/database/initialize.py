from tortoise import Tortoise

async def setup_db():
    await Tortoise.init(
        db_url='sqlite://database/db.sqlite3',
        modules={'models': ['src.database.models']}
    )
    await Tortoise.generate_schemas()
