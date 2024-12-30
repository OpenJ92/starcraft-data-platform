from database.config import SessionLocal
from database.storage import LocalStorage
from database.inject import BatchInjector, InjectionManager

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

## def main():
##     # Initialize the database schema
##     print("Initializing database...")
##     init_db()
## 
##     # Load the replay
##     replay = sc2reader.load_replay("examples/example_5.SC2Replay", load_map=True)
## 
##     # Create the InjectionManager and inject the replay
##     print("Injecting replay data...")
##     manager = InjectionManager(Base)
##     with SessionLocal() as session:
##         manager.inject(replay, session)
## 
##     print("Injection complete!")

def main():
    # Initialize the database schema
    print("Initializing database...")
    init_db()

    batch = BatchInjector(Base, SessionLocal, LocalStorage('examples'))
    batch.inject()

if __name__ == "__main__":
    main()
