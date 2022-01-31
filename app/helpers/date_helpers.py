from datetime import timedelta, datetime


def clean_day(days_as_text: str):
    if "يوم" in days_as_text:
        today = datetime.today()
        last_day = today - timedelta(days=1)
        return last_day.strftime("%Y-%m-%d")

    if "يومين" in days_as_text:
        today = datetime.today()
        last_2_days = today - timedelta(days=1)
        return last_2_days.strftime("%Y-%m-%d")

    if "ايام" in days_as_text:
        number_of_days = [int(number) for number in days_as_text if number.isdigit()]
        today = datetime.today()
        last_n_days = today - timedelta(days=number_of_days[0])
        return last_n_days.strftime("%Y-%m-%d")

    return "unknown day"


def clean_week(weeks_as_text: str):

    if "اسبوع" in weeks_as_text:
        today = datetime.today()
        last_week = today - timedelta(days=7)
        return last_week.strftime("%Y-%m-%d")

    if "اسبوعين" in weeks_as_text:
        today = datetime.today()
        last_2_weeks = today - timedelta(days=14)
        return last_2_weeks.strftime("%Y-%m-%d")

    if "اسابيع" in weeks_as_text:
        number_of_weeks = [int(number) for number in weeks_as_text if number.isdigit()]
        today = datetime.today()
        last_n_weeks = today - timedelta(days=number_of_weeks[0] * 7)
        return last_n_weeks.strftime("%Y-%m-%d")

    return "unknown week"


def clean_month(months_as_text: str):
    if "شهر" in months_as_text:
        today = datetime.today()
        first = today.replace(day=30)
        last_month = first - timedelta(days=1)
        return last_month.strftime("%Y-%m-%d")

    if "شهرين" in months_as_text:
        today = datetime.today()
        first = today.replace(day=60)
        last_2_month = first - timedelta(days=1)
        return last_2_month.strftime("%Y-%m-%d")

    if "شهور" in months_as_text:
        number_of_months = [
            int(number) for number in months_as_text if number.isdigit()
        ]
        today = datetime.today()
        first = today.replace(day=number_of_months[0] * 30)
        last_n_month = first - timedelta(days=1)
        return last_n_month.strftime("%Y-%m-%d")

    return "unknown month"
