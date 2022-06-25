from timeclasses import Time


class PhoneCallInProgress:
    endcall_time: int

    def __init__(self, origin_number: str, destination_number: int, startcall_time: Time):
        self.origin_number = origin_number
        self.destination_number = destination_number
        self.start_time = startcall_time

    # Acá ya hay un codesmell, si endcall_time esta definida pero no inicalizada, se puede crear otro objeto