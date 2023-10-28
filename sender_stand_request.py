
import requests
import data
import configuration

#Выполняем запрос на создание нового заказа:
def create_order(new_order):
    return requests.post(configuration.URL + configuration.CREATE_NEW_ORDER,
                    json=new_order,
                    headers=data.headers)
response = create_order(data.new_order)


# Сохраняем номер трека заказа:
track_order_number = response.json()["track"]


# Выполняем запрос на получение заказа по его номеру:
def receive_order_track(track_order_number):
    return requests.get(configuration.URL + configuration.RECEIVE_TRACK_ORDER,
                        params={"t": track_order_number})

# Функция для проверки, что код ответа равен 200.
def positive_assert(track_order_number):
    answer = receive_order_track(track_order_number)
    assert answer.status_code == 200