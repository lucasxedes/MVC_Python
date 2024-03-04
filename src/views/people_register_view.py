import os
from typing import Dict

class PeopleRegisterView:
    def register_person_view(self) -> Dict:
        os.system('cls||clear')

        print('Cadastrar Nova Pessoa \n\n')
        name = input('Dertermine o nome da pessoa: ')
        age = input('Dertermine a idade da pessoa: ')
        height = input('Determine a altura da pessoa: ')

        new_person_informations = {
            "name": name, "age": age, "height": height
        }

        return new_person_informations

    def register_person_success(self, message: Dict) -> None:
        os.system('cls||clear')

        success_message = f'''
            Usuario cadastrado com sucesso!

            Tipo: {message["type"]}
            Registro: {message["count"]}
            Infos:
                Nome: {message["attributes"]["name"]}
                idade: {message["attributes"]["age"]}
        '''
        print(success_message)

    def register_person_fail(self, error: str) -> None:
        os.system('cls||clear')

        fail_message = f'''
            Falha ao cadastrar usuario!

            Erro: {error}
        '''
        print(fail_message)
