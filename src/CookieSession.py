class CookieSession(object):
    def __init__(self, cookie, ts):
        """
        <str> cookie : 16 length string from csv logs.
        <str> ts : Cookie logs from csv file.
        """

        self.cookie = cookie
        self.timestamp = {
            "year": int(ts[:4]),
            "month": int(ts[5:7]),
            "day": int(ts[8:10]),
            # "hour": int(ts[11:13]),
            # "minute": int(ts[14:16]),
            # "second": int(ts[17:19]),
            # "min_ofst": int(ts[20:22]),
            # "sec_ofst": int(ts[23:25])
        }

    def __repr__(self):
        return self.cookie