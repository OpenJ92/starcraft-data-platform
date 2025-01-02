from starcraft_data_orm.warehouse.config import SessionLocal
from starcraft_data_orm.storage import LocalStorage
from starcraft_data_orm.inject import BatchInjector, InjectionManager

from starcraft_data_orm.warehouse import initialize_warehouse, WarehouseBase

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

def main():
    # Initialize the starcraft_data_orm schema
    print("Initializing starcraft_data_orm...")
    initialize_warehouse()

    batch = BatchInjector(WarehouseBase, SessionLocal, LocalStorage('examples'))
    batch.inject()

if __name__ == "__main__":
    main()
