from utils import Utils
from os.path import isfile
from csv import reader, writer
from typing import Mapping, Union


class Transaction_IO:
    def __init__(self) -> None:
        self.file = './db/transactions.csv'
        self.utils = Utils()
    
    def import_data(self, data: Mapping[str, list[Mapping[str, Union[str, int, float]]]]) -> None:
        if isfile(self.file):
            # Fetching data from CSV
            imported_data: list[Mapping[str, str]] = list()
            
            try:        
                with open(self.file, 'r') as transactions:
                    transaction_reader = reader(transactions)
                    for row in transaction_reader:
                        if row == self.utils.transaction_headers(): continue
                        else:
                            temp_dict: Mapping[str, Union[str, int, float]] = dict(zip(
                                self.utils.transaction_headers(),
                                row
                            ))
                            imported_data.append(temp_dict)

                if imported_data:
                    transaction_keys: list[str] = list()
                    for transaction in data['transactions']:
                        transaction_keys.append(transaction['Description'])

                    # Preventing duplicate entries
                    for transaction in imported_data:
                        if transaction['Description'] in transaction_keys: continue
                        else:
                            data['transactions'].append(transaction)
            except PermissionError: print('Permission Denied: Unable to access the file!')

    def export_data(self, data: Mapping[str, list[Mapping[str, Union[str, int, float]]]]) -> None:
            # Writing data to CSV
            exported_data: list[list[str]] = list()
            exported_data.append(self.utils.transaction_headers())
            
            for transaction in data['transactions']:
                exported_data.append(list(transaction.values()))
            
            try:
                with open(self.file, 'w', newline='') as transactions:
                    transaction_writer = writer(transactions)
                    transaction_writer.writerows(exported_data)
            except PermissionError: print('Permission Denied: Unable to access the file!')

class Model_IO:
    def __init__(self) -> None:
        self.file = './db/models.csv'
        self.utils = Utils()
        
    def import_data(self, data: Mapping[str, list[Mapping[str, Union[str, int]]]]) -> None:
        if isfile(self.file):
            # Fetching data from CSV
            imported_data: list[Mapping[str, str]] = list()
            
            try:
                with open(self.file, 'r') as models:
                    model_reader = reader(models)
                    for row in model_reader:
                        if row == self.utils.model_headers(): continue
                        else:
                            temp_dict: Mapping[str, Union[str, int]] = dict(zip(
                                self.utils.model_headers(),
                                row
                            ))
                            imported_data.append(temp_dict)
                
                if imported_data:
                    model_keys: list[str] = list()
                    for model in data['models']:
                        model_keys.append(model['Account'])
                        
                    # Preventing duplicate entries
                    for model in imported_data:
                        if model['Account'] in model_keys: continue
                        else:
                            data['models'].append(model)
            except PermissionError: print('Permission Denied: Unable to access the file!')
    
    def export_data(self, data: Mapping[str, list[Mapping[str, Union[str, int]]]]) -> None:
        # Writing data to CSV
        exported_data: list[list['str']] = list()
        exported_data.append(self.utils.model_headers())
        
        for model in data['models']:
            exported_data.append(list(model.values()))
            
        try:
            with open(self.file, 'w', newline='') as models:
                model_writer = writer(models)
                model_writer.writerows(exported_data)
        except PermissionError: print('Permission Denied: Unable to access the file!')
