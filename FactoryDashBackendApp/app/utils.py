from datetime import datetime, timedelta


def get_datetime_or_today(args, arg_name, add_days=0):
    arg_str = args.get(arg_name, default="", type=str)
    try:
        date = datetime.strptime(arg_str, "%Y%m%d")
        return date
    except ValueError:
        return datetime(2021, 10, 7) + timedelta(add_days)


class Colors:
    GOOD = "#5ECD4C"
    MEDIUM = "#FFC121"
    BAD = "#FF2121"
