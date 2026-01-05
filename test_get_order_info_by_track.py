# Лоншаков Владислав, 39-я когорта — Финальный проект. Инженер по тестированию плюс
import data
import request


def test_get_order_info_by_track() -> None:
    track = request.create_order(data.order_body).json()['track']
    response = request.get_order_info_by_track(track)
    assert response.status_code == 200