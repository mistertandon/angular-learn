import datetime


class Demo:

    @staticmethod
    def is_weekend(day) -> bool:

        _is_weekday: bool = True
        if day.weekday() == 5 or day.weekday() == 6:
            _is_weekday = False

        return _is_weekday


test_date = datetime.date(2020, 4, 25)
is_weekday = Demo.is_weekend(test_date)

if is_weekday:
    print('It is weekday')
else:
    print('It is not a weekday')