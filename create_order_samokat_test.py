import sender_stand_request

# Барулина Анастасия 9-я когорта - Финальный проект. Инженер по тестированию плюс.
# Тест
def test_receive_correct_data_using_track_number():
    sender_stand_request.positive_assert(sender_stand_request.track_order_number)


