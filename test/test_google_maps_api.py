import json
import allure
from utils.api import Google_maps_api
from utils.cheking import Checking
"""Создание, изменение и удаление новой локации """
# python -m pytest -s -v  python -m pytest --alluredir=test_results/ test/test_google_maps_api.py
"""Класс содержащий тест по работе с локацией"""
@allure.epic("Test create place")
class Test_create_place:

    @allure.description("Test create, update, delete. create new place")
    def test_create_new_place(self):

        print("Метод Post")
        result_post = Google_maps_api.create_new_place()
        check_post = result_post.json()
        place_id = check_post.get("place_id")
        Checking.check_status_code(result_post,200)
        Checking.check_json_token(result_post, ['status', 'place_id', 'scope', 'reference', 'id']  )
        print(result_post.status_code)
        token = json.loads(result_post.text)
        Checking.check_json_value(result_post,'status','OK')

        print("Метод GET Post")
        result_get = Google_maps_api.get_new_place(place_id)
        Checking.check_status_code(result_get, 200)
        Checking.check_json_token(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])
        Checking.check_json_value(result_get,'address','29, side layout, cohen 09')


        print("Метод PUT")
        result_put = Google_maps_api.put_new_place(place_id)
        Checking.check_status_code(result_put, 200)
        Checking.check_json_token(result_put, ['msg'])
        Checking.check_json_value(result_put, 'msg', 'Address successfully updated')

        print("Метод GET Put")
        result_get = Google_maps_api.get_new_place(place_id)
        Checking.check_status_code(result_get, 200)
        Checking.check_json_token(result_get,['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])
        Checking.check_json_value(result_get, 'address', '100 Lenina street, RU')


        print("Метод Delete")
        result_delete = Google_maps_api.delete_new_place(place_id)
        Checking.check_status_code(result_delete, 200)
        Checking.check_json_token(result_delete, ['status'])
        Checking.check_json_value(result_delete, 'status', 'OK')

        print("Метод GET Delete")
        result_get = Google_maps_api.get_new_place(place_id)
        Checking.check_status_code(result_get, 404)
        Checking.check_json_token(result_get, ['msg'])
        Checking.check_json_search_word_in_value(result_get,'msg','failed')

        print("Тестирование создания, изменения и удаления новой локации прошло успешно")


