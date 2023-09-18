import tentaclio
import pandas as pd
from datetime import date

from cmescraper import cme

BASE_FTP = "ftp://ftp.cmegroup.com"
SETTLE_FTP = f'{BASE_FTP}/settle'


def fetch(market: cme.Markets = cme.Markets.NYMEX, settlement_date: date = None) -> pd.DataFrame:
    if settlement_date:
        settlement_date_str = settlement_date.strftime("%Y%m%d")
        file_name = f'{SETTLE_FTP}/{market.value.lower()}.settle.{settlement_date_str}.s.csv'
    else:
        file_name = f'{SETTLE_FTP}/{market.value.lower()}.settle.s.csv'
    with tentaclio.open(file_name) as reader:
        df = pd.read_csv(reader)
        return df.values
