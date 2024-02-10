from user import User
from utils import Utils
from data_io import Model_IO
from bank_model import Bank_Model
from typing import Mapping, Union


class Bank:
    def __init__(self) -> None:
        self.utils = Utils()
        self.model = Bank_Model()
        self.model_io = Model_IO()
        self.data: Mapping[str, list[Mapping[str, Union[str, int]]]] = {
            'models': list()
        }
        self.model_io.import_data(self.data)
        self.sort_models()
        
    def sort_models(self) -> None: 
        self.data['models'] = sorted(self.data['models'], key=lambda model: model['Name'])
        
    def get_model(self, acc_num: str) -> Mapping[str, Union[str, int]]:
        if self.data['models']:
            for model in self.data['models']:
                if acc_num in model.values():
                    return model
            
    def new_model(self, name: str, acc_num: str, pin: int, password: int, pin_salt: str, password_salt: str) -> None:
        model: Mapping[str, Union[str, int]] = dict(zip(
            self.utils.model_headers(),
            [
                name,
                acc_num,
                pin,
                password,
                pin_salt.decode(),
                password_salt.decode()
            ]
        ))
        self.data['models'].append(model)
        self.sort_models()
        self.model_io.export_data(self.data)
        
    def get_currency(self) -> str: return self.model.currency
        
    def register(self, user: User) -> None:
        print(f'\nRegistering {user.get_account_name()} in {self.model.name}...')
        self.model.users = user
        
    def login(self, user: User) -> None:
        if user.auth():
            print(f'\nLogging {user.get_account_name()} in {self.model.name}...')
            self.model.auth_users = user
            
    def get_users(self) -> None: self.model.users
        
    def get_auth_users(self) -> None: self.model.auth_users
            
    def validate(self, user: User) -> bool:
        return self.model.validate(user)
    
    # def transfer(self, sender: User, receiver: User, amount: float) -> None:
    #     sender.transfer(amount=float(amount), callback=False)
    #     receiver.transfer(amount=float(amount), callback=True)
    