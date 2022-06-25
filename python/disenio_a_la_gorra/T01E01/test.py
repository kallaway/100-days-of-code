from timeclasses import Time, TimeDataclass
from timezone import TimeZone


class Example:

    def test(self):
        webminar_starting_time = Time(19, 0, 0)
        now = Time(20, 0, 0)

        assert (now.difference_in_hour(webminar_starting_time)) == 1, "El resultado debe ser 1"

    # Agregamos timezone al modelo
    def test_timezone(self):
        webminar_starting_time_cr = Time(16, 0, 0, TimeZone(-6, 'CR'))
        now_ar = Time(20, 0, 0, TimeZone(-3, 'AR'))


        assert (now_ar.difference_in_hour(webminar_starting_time_cr)) == 1, "El resultado debe ser 1"



class ExampleDataclass:

    def test(self):
        webminar_starting_time = TimeDataclass(19, 0, 0)
        now = TimeDataclass(20, 0, 0)

        assert (now.difference_in_hour(webminar_starting_time)) == 1, "El resultado debe ser 1"

    # Agregamos timezone al modelo
    def test_timezone(self):
        webminar_starting_time_cr = TimeDataclass(16, 0, 0, TimeZone(-6, 'CR'))
        now_ar = TimeDataclass(20, 0, 0, TimeZone(-3, 'AR'))


        assert (now_ar.difference_in_hour(webminar_starting_time_cr)) == 1, "El resultado debe ser 1"




if __name__ == "__main__":
    test = Example()
    test.test()
    test.test_timezone()
    testDC=ExampleDataclass()
    testDC.test()
    testDC.test_timezone()