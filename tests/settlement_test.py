import datetime
from pandas.tseries.offsets import BDay
import cmescraper.settlement as settlement


def test_settlement():
    df = settlement.fetch()
    print(df)


def test_settlement_day():
    bday = datetime.datetime.today() - BDay(1)
    df = settlement.fetch(settlement_date=bday)
    print(df)