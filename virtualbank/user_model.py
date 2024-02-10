from typing import Union
from random import randint

class User_Model:
    def __init__(self) -> None:
        self.__balance: float = float()
        self.__is_connected: bool = False
        self.__pin: Union[str, None] = None
        self.__password: Union[str, None] = None
        self.__account_name: Union[str, None] = None
        self.__pin_salt: Union[bytes, str, None] = None
        self.__trans_msg: Union[list[str], None] = None
        self.__passwd_salt: Union[bytes, str, None] = None
        self.__account_number: str = f'07{randint(11_111_111, 99_999_999)}'
    
    # Account number getter and setter
    @property
    def account_number(self) -> str: return self.__account_number
    
    @account_number.setter
    def account_number(self, acc_num: str) -> None: self.__account_number = acc_num
    
    # Account name getter and setter
    @property
    def account_name(self) -> Union[str, None]: return self.__account_name
    
    @account_name.setter
    def account_name(self, acc_name: str) -> None: self.__account_name = acc_name
    
    # Account password getter and setter
    @property
    def password(self) -> Union[str, None]: return self.__password
    
    @password.setter
    def password(self, passwd: str) -> None: self.__password = passwd.encode()
    
    # Account pin getter and setter
    @property
    def pin(self) -> Union[str, None]: return self.__pin
    
    @pin.setter
    def pin(self, pin: str) -> None: self.__pin = pin.encode()
    
    # Password salt getter and setter
    @property
    def password_salt(self) -> Union[bytes, str, None]: return self.__passwd_salt
    
    @password_salt.setter
    def password_salt(self, salt: str) -> None: self.__passwd_salt = salt.encode()
    
    # Pin salt getter and setter
    @property
    def pin_salt(self) -> Union[bytes, str, None] : return self.__pin_salt
    
    @pin_salt.setter
    def pin_salt(self, salt: str) -> None: self.__pin_salt = salt.encode()
    
    # Account balance getter and setter
    @property
    def balance(self) -> Union[float, None]: return self.__balance
    
    @balance.setter
    def balance(self, bal: float) -> None: self.__balance += bal
    
    # Authenticated getter and setter
    @property
    def is_connected(self) -> bool: return self.__is_connected
    
    @is_connected.setter
    def is_connected(self, auth: bool) -> None: self.__is_connected = auth
    
    @property
    def trans_msg(self) -> Union[list[str], None]: 
        return f'\nLatest Transaction Details...\nAcct: {self.__account_number}\nAmt: {self.__trans_msg[0]}\nDesc: {self.__trans_msg[1]}\nAvail Bal: {self.__balance}\nDate: {self.__trans_msg[2]}'
    
    @trans_msg.setter
    def trans_msg(self, msg: list[str]) -> None: self.__trans_msg = msg
    
    def get_details(self) -> str:
        return f"\nFetching Details...\nName: {self.__account_name}\nNumber: {self.__account_number}\nBalance: {self.__balance}"
