class operation:
    def __init__(self, date, description, source, destination, amount, currency):
        self.date = date
        self.description = description
        self.source = source
        self.destination = destination
        self.amount = amount
        self.currency = currency


    def prepare_source(self, source):
        if source[:4] == 'Счет':
            return f"Счет **{source[-4:]}"
        if not source:
            return ''
        return f"{source[:-12]} {source[-12:-10]}** **** {source[-4:]}"
    

    def prepare_destination(self, destination):
        return f"{destination[:4]} **{destination[-4:]}"


    def prepare_date(self, date):
        return f"{date[8:10]}.{date[5:7]}.{date[:4]}"
                

    def __str__(self):
        if self.source:
            return f"""{self.prepare_date(self.date)} {self.description}
{self.prepare_source(self.source)} -> {self.prepare_destination(self.destination)}
{self.amount} {self.currency}"""
        else:
            return f"""{self.prepare_date(self.date)} {self.description}
{self.prepare_destination(self.destination)}
{self.amount} {self.currency}"""
