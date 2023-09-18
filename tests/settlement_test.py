import datetime

import pytest
from pandas.tseries.offsets import BDay

import cmescraper.settlement as settlement


def test_settlement():
    df = settlement.fetch()
    assert len(df) != 0


def test_settlement_day():
    bday = datetime.datetime.today() - BDay(1)
    df = settlement.fetch(settlement_date=bday)
    assert len(df) != 0


def test_settlement_bad_day():
    bday = datetime.datetime.today() - datetime.timedelta(days=30)
    with pytest.raises(Exception):
        df = settlement.fetch(settlement_date=bday)
