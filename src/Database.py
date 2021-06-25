class Database(object):
    def __init__(self, cookie_sessions=[]):
        """
        <list<CookieSession>> cookie_sessions
        """

        self.trie = Node()
        for cookie_session in cookie_sessions:
            self.insert(cookie_session)

    def insert(self, cookie_session):
        """
        <CookieSession> cookie_session
        <None> return
        """

        # Traverse down trie and update each node
        # by storing the cookie session.
        temp = self.trie
        queries = cookie_session.timestamp
        for _, v in queries.items():
            if v not in temp.childrens:
                temp.childrens[v] = Node()
            temp = temp.childrens[v]
            temp.insert(cookie_session)

    def get_most_active(self, query):
        """
        <Query> query
        <list<str>> return
        """

        # Traverse down trie to get active cookies
        # on a particular day.
        temp = self.trie
        for _, v in query.items():
            # If a timestamp isn't present, then no
            # cookies were active in the particular
            # year/month/day.
            if v in temp.childrens:
                temp = temp.childrens[v]
            else:
                return []

        data, highest_freq = temp.data, temp.highest_freq
        # Get most frequent cookies on a particular day.
        return [id for id, cookies in data.items() if len(cookies) == highest_freq]


class Node(object):
    def __init__(self):
        # Maps int to Node
        self.childrens = {}
        # Maps str to list of cookie sessions
        self.data = {}
        self.highest_freq = 0

    def insert(self, cookie_session):
        """
        <CookieSession> cookie_session
        <None> return
        """

        # Stores cookie session by mapping the cookie
        # to it. Keeps track of highest count for each
        # insertion.
        if cookie_session.cookie not in self.data:
            self.data[cookie_session.cookie] = []
        self.data[cookie_session.cookie].append(cookie_session)
        x = len(self.data[cookie_session.cookie])
        self.highest_freq = max(self.highest_freq, x)