import re
from helpers.date_helpers import clean_day, clean_week, clean_month
from datetime import date


def numbers_from_text(text_lst: list) -> list:
    """
    extract numbers from text and convert it to number instead of string
    """
    numbers_arr: list = []
    for text in text_lst:
        digits = re.findall(r"\d+", text)
        numbers_arr.append(int("".join(digits)))
    return numbers_arr


def clean_time(text: list) -> list:
    times_list: list = []
    for time in text:

        if (
            "ساعة" in time
            or "ساعتين" in time
            or "الان" in text
            or "دقيقة" in text
            or "ثانية" in text
            or "ساعات" in time
            or "دقائق" in text
        ):
            times_list.append(str(date.today()))

        elif "يوم" in text or "يومين" in text or "ايام" in text:
            times_list.append(str(clean_day(time)))

        elif "اسبوع" in time or "اسبوعين" in time or "اسابيع" in time:
            times_list.append(str(clean_week(time)))

        elif "شهر" in time or "شهرين" in time or "شهور" in time:
            times_list.append(str(clean_month(time)))
        else:
            times_list.append("unknown")
    return times_list
