from sqlalchemy.orm import sessionmaker

from .models import Parliament
from .models import create_table
from .models import db_connect


# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# useful for handling different item types with a single interface


class ParliamentbgPipeline(object):
    """Livingsocial pipeline for storing scraped items in the database"""

    def __init__(self):
        """
        Initializes database connection and sessionmaker.
        Creates deals table.
        """
        engine = db_connect()
        create_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        """Save deals in the database.

        This method is called for every item pipeline component.

        """
        session = self.Session()
        deal = Parliament(**item)

        try:
            session.add(deal)
            session.commit()
        except Exception as ex:
            print(ex)
            session.rollback()
            raise
        finally:
            session.close()

        return item
