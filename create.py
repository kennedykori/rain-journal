class Journal(object):
    """Journal class"""

    journal = {}
    last = {}

    def __init__(self):
        super(Journal, self).__init__()

    def create_journal(self, title):
        self.journal[title] = {}

    def get_journal(self):
        return self.journal

    def create_entry(self, title, subtitle, entry):
        if title in self.journal:
            # prompt user to create an entry
            entries = self.journal[title]
            entries[subtitle] = entry
            last = {subtitle: entry}
        else:
            print("Journal does not exist. Enter cmd to create a new journal")

