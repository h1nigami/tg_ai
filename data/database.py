import aiosqlite
import time
import asyncio

class DB:
    def __init__(self, database_name) -> None:
        self.db_name = database_name
        
    async def create_tables(self) -> None:
        async with aiosqlite.connect(self.db_name) as db:
            await db.execute('CREATE TABLE IF NOT EXISTS users (tg_id INTEGER PRIMARY KEY, is_admin INTEGER DEFAULT 0, first_name VARCHAR(200))') 