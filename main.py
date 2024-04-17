from web3 import Web3
from web3.middleware import geth_poa_middleware
from contact_info import abi, contract_address

w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

contract = w3.eth.contract(address=contract_address, abi=abi)

print(w3.eth.get_balance("0xd431A61361A275f6eE8814BFaae34CC0B34B9EE7"))
print(w3.eth.get_balance("0x86777B25e99D7d59Deb94860Ac57Dd1129AFC7d6"))
print(w3.eth.get_balance("0xDa005b7B842e72FCc608c9D21E287E6CD4AfDAF5"))
print(w3.eth.get_balance("0xD61CA8A3F68e5f2ACcDdf6427b40247EF39cB646"))
print(w3.eth.get_balance("0x42Ebe42605a037450675F38f554D7dd470053E32"))
# def auth():
#     public_key = input("Введите публичный ключ: ")
#     password = input("Введите пароль: ")
#     try:
#         w3.geth.personal.unlock_account(public_key, password)
#         print("Вы авторизованы")
#         return public_key
#     except Exception as e:
#         print(e)
#         return None


# def regisration():
#     password = input("Введите пароль: ")
#     address = w3.geth.personal.new_account(password)
#     print(f"Адрес нового аккаунта: {address}")


# def send_eth(account):
#     amount = int(input("Введите сумму: "))
#     try:
#         tx_hash = contract.function.sendEth().transact({
#             "from": account,
#             "value": amount
#         })
#         print("Транзакция успешно отправлена. Хеш транзакция:", tx_hash.hex())
#     except Exception as e:
#         print ("Ошибка при отправке эфира: ", e)

# def get_balance(account):
#     try:
#         balance_wei = contract.function.get_balance().call({
#             "from": account,
#         })
#         print("Баланс аккаунта:", balance_wei.hex, "WEI")
#     except Exception as e:
#         print ("Ошибка при получении баланса: ", e)

# def withdraw(account):
#     recipient = input("Введите адрес получателя: ")
#     amount = int(input("Введите сумму: "))
#     try:
#         tx_hash = contract.function.withdrawll(recipient, amount).transact({
#             "from": account,
#         })
#         print("Транзакция успешно отправлена. Хеш транзакция:", tx_hash.hex())
#     except Exception as e:
#         print ("Ошибка при отправке эфира: ", e)

# def get_balance_account():
#     pass

# def main():
#     account = ""
#     is_auth = False
#     while True:
#         if not is_auth:
#             choice = input("Выберите:\n1. Авторизация\n2. Регистрация\n")
#             match choice:
#                 case "1":
#                     account = auth()
#                 case "2":
#                     regisration()
#         else :
#             choice = input("Выберите:\n1. Отправить эфир\n2. Посмотреть баланс на смарт-контракт\n3. Вывести средства\n4. Посмотреть баланс аккаунта\n5. Выйти")
#             match choice:
#                 case "1":
#                     send_eth(account)
#                 case "2":
#                     get_balance(account)
#                 case "3":
#                     withdraw(account)
#                 case "4":
#                     get_balance_account()
#                 case "5":
#                     is_auth = False
#                 case _:
#                     print("Введите корректное слово")



# if __name__ == "__main__":
#     main()

