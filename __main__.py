from database.config import SessionLocal
from database.inject import *
from database.init import *

import sc2reader
from sc2reader.engine.plugins import (
    SelectionTracker,
    APMTracker,
    ContextLoader,
    GameHeartNormalizer,
)

sc2reader.engine.register_plugin(SelectionTracker())
sc2reader.engine.register_plugin(APMTracker())
sc2reader.engine.register_plugin(ContextLoader())
sc2reader.engine.register_plugin(GameHeartNormalizer())

async def main():
    # Initialize the database schema
    print("Initializing database...")
    await init_db()

    # Load the replay
    replay = sc2reader.load_replay("examples/example_5.SC2Replay")

    # Create the InjectionManager and inject the replay
    print("Injecting replay data...")
    ## manager = InjectionManager(Base)
    manager = EventInjectionManager(Base)

    async with SessionLocal() as session:
        await manager.inject(replay, session)

    print("Injection complete!")

if __name__ == "__main__":
    asyncio.run(main())
