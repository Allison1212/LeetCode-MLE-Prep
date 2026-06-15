class Logger:

    def __init__(self):
        self.message_dict = dict()

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.message_dict.keys():
            self.message_dict[message] = timestamp
            return True
        else:
            if timestamp >= self.message_dict.get(message) + 10:
                self.message_dict[message] = timestamp
                return True
            else:
                return False