class Query(object):
    def __init__(self, query, q_type, delimeter):
        """
        <str> query : Query in string format from command line.
        <str> q_type : Options from command line represents type of query.
        <str> delimeter : How query is formated.
        """

        if q_type == '-d':
            query = query.split(delimeter)
            self.query = {
                "year": int(query[0]),
                "month": int(query[1]),
                "day": int(query[2])
            }

    def items(self):
        return self.query.items()