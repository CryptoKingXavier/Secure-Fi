from datetime import datetime

class Utils:    
    def transaction_headers(self) -> list[str]:
        return ['Account', 'Amount', 'Description', 'Available Balance', 'Date']
    
    def model_headers(self) -> list[str]:
        return ['Name', 'Account', 'Pin', 'Password', 'Pin-Salt', 'Password-Salt']

    def get_datetime(self) -> str:
        date, time = datetime.now().__str__().split(' ')
        hour, minute, _ = time.split(':')
        return f'{date} {hour}:{minute}'
