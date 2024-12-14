from utils.http_method import Http_methods


"""Методы для тестирования Google maps api"""

base_url = "https://rahulshettyacademy.com"  # Базовое URL
key = "?key=qaclick123" # параметр


class Google_maps_api:
    """Метод для создания новой локации"""
    @staticmethod
    def create_new_place():
        json_for_create_new_location = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            }, "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"
        }

        post_resource = "/maps/api/place/add/json"  # Ресурс метода Пост
        post_url = base_url + post_resource + key
        print(post_url)
        result_post = Http_methods.post(post_url,json_for_create_new_location)
        print(result_post.json())
        print(result_post.status_code)
        return result_post

    @staticmethod
    def get_new_place(place_id):
        """Метод для изменения новой локации"""

        get_resource = "/maps/api/place/get/json"  # ресурс метода Get
        get_url = base_url + get_resource + key + "&place_id=" + place_id
        print(get_url)
        result_get = Http_methods.get(get_url)
        print(result_get.json())
        print(result_get.status_code)
        return result_get

    """Метод для проверки новой локации"""
    @staticmethod
    def put_new_place(place_id):

        put_resource = "/maps/api/place/update/json"
        put_url = base_url + put_resource + key
        print(put_url)
        json_for_update_new_location = {
            "place_id": place_id,
            "address":"100 Lenina street, RU",
            "key":"qaclick123"
        }

        result_put = Http_methods.put(put_url,json_for_update_new_location)
        print(result_put.json())
        return result_put

    """Метод для удаления новой локации"""
    @staticmethod # это декоратор, который используется для определения статического метода внутри класса.
    def delete_new_place(place_id):


        delete_resource = "/maps/api/place/delete/json"  # ресурс метода Delete
        delete_url = base_url + delete_resource + key
        print(delete_url)
        json_for_delete_new_location = {
            "place_id": place_id
        }
        result_delete = Http_methods.delete(delete_url,json_for_delete_new_location)
        print(result_delete.json())
        print(result_delete.status_code)
        return result_delete
















