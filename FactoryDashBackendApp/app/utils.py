from datetime import datetime


def get_datetime_or_today(args, arg_name):
    arg_str = args.get(arg_name, default="", type=str)
    try:
        date = datetime.strptime(arg_str, "%Y%m%d")
        return date
    except ValueError:
        return datetime.today()
