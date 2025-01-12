import uuid
from datetime import datetime
import pytz


def uid() -> str:
    return str(uuid.uuid4())


def date_string(datetime_value: datetime) -> str:
    est = pytz.timezone("US/Eastern")
    now_est = datetime_value.astimezone(est)
    # Format as a string compatible with PostgreSQL
    timestamp_str = now_est.strftime("%m-%d-%Y %H:%M:%S")
    return timestamp_str
