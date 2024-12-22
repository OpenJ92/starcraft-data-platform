from sqlalchemy.exc import  SQLAlchemyError, IntegrityError, OperationalError
from asyncio import gather, Event

from database.inject.Injectable import Injectable

class InjectionManager():
    def __init__(self, base):
        """
        Initialize the InjectionManager.
        :param metadata: SQLAlchemy metadata (Base.metadata).
        """
        self.base = base
        self.metadata = base.metadata
        ## self.sorted_relations = self._topological_sort()


    async def inject(self, replay, session):
        """
        Perform the injection process for a replay.
        :param replay: Parsed replay object to inject.
        :param session: Database session supporting flush, commit and rollback:
        """
        try:
            for relation in self.metadata.sorted_tables:
                name = f"{relation.schema}.{relation.name}"
                relation_cls = self.base.injectable.get(name)
                if relation_cls and issubclass(relation_cls, Injectable):
                    await relation_cls.process(replay, session)
                    await session.flush()  # Flush after each relation
            await session.commit()  # Commit transaction after all relations

        except Exception as e:
            await session.rollback()
            print(f"Unexpected error: {e}")
            # Gracefully handle all other exceptions

class EventInjectionManager:
    def __init__(self, base):
        """
        Initialize the EventInjectionManager.
        :param base: SQLAlchemy Base, providing metadata and injectable models.
        """
        self.base = base
        self.metadata = base.metadata
        self.events = {}  # Dictionary to track events for each table

    def _get_event(self, table_name):
        """
        Retrieve or create an asyncio.Event for a specific table.
        :param table_name: Fully qualified table name (e.g., schema.table).
        :return: asyncio.Event instance.
        """
        if table_name not in self.events:
            self.events[table_name] = Event()
        return self.events[table_name]

    async def inject(self, replay, session):
        """
        Perform the injection process using Event-based synchronization.
        :param replay: Parsed replay object to inject.
        :param session: Database session supporting flush, commit, and rollback.
        """
        tasks = []
        for relation in self.metadata.sorted_tables:
            name = f"{relation.schema}.{relation.name}"
            relation_cls = self.base.injectable.get(name)

            if relation_cls and issubclass(relation_cls, Injectable):
                # Define dependencies from the class relationships
                dependencies = []
                for dependency in relation.foreign_key_constraints:
                    fkey = f"{dependency.referred_table.schema}.{dependency.referred_table.name}"
                    dependencies.append(fkey)
                    breakpoint()

                # Inject the current relation
                tasks.append(self._inject_relation(relation_cls, replay, session, dependencies))

        # Run all tasks concurrently
        await gather(*tasks)
        await session.commit()

    async def _inject_relation(self, relation_cls, replay, session, dependencies):
        """
        Inject a single relation, waiting for dependencies to complete.
        :param relation_cls: The model class to process.
        :param replay: Parsed replay object.
        :param session: Database session.
        :param dependencies: List of dependent table names.
        """
        for dep in dependencies:
            await self._get_event(dep).wait()  # Wait for dependencies to complete

        try:
            # Process the current relation
            await relation_cls.process(replay, session)
            await session.flush()  # Flush after processing
        except Exception as e:
            await session.rollback()
            print(f"Error processing {relation_cls.__tablename__}: {e}")
        finally:
            # Signal that this relation is complete
            self._get_event(relation_cls.__tablename__).set()

## ## Consider Supplying a "Base" at each level of the database via __init__.py file
## class InjectionManagerFactory():
##     def __init__(self):
##         pass
## 
##     @classmethod
##     def WAREHOUSE(cls):
##         return InjectionManager(WareshouseBase)
## 
##     @classmethod
##     def ANALYTICS(cls):
##         return InjectionManager(AnalyticsBase)
## 
##     @classmethod
##     def MACHINE_LEARNING(cls):
##         return InjectionManager(MachineLearningBase)
