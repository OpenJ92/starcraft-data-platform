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

replay = sc2reader.load_replay("examples/example_5.SC2Replay")

manager = InjectionManager(Base)
manager.inject(replay, SessionLocal())
