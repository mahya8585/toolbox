import json
import requests


def create_analyze_response(image_url):
    """
    https://westus.dev.cognitive.microsoft.com/docs/services/5adf991815e1060e6355ad44/operations/56f91f2e778daf14a499e1fa
    :param image_url:
    :return:
    """
    base_url = 'https://japaneast.api.cognitive.microsoft.com/vision/v2.0/analyze'
    # request_computer_vision(image_url, base_url+'?visualFeatures=ImageType')
    # request_computer_vision(image_url, base_url + '?visualFeatures=Faces')
    # request_computer_vision(image_url, base_url + '?visualFeatures=Adult')
    # request_computer_vision(image_url, base_url + '?visualFeatures=Categories')
    # request_computer_vision(image_url, base_url + '?visualFeatures=Color')
    request_computer_vision(image_url, base_url + '?visualFeatures=Tags')
    # request_computer_vision(image_url, base_url + '?visualFeatures=Description')


def request_computer_vision(image_url, endpoint):
    """
    computer visionにデータ送信する
    :param image_url: url
    :param endpoint: APIエンドポイント名(
    :return: json
    """
    post_body = {
        'url': image_url
    }
    header = {
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': '3869dd1a50a944c6a8b7c1e3cd109537'
    }

    res = requests.post(endpoint, headers=header, data=json.dumps(post_body))

    print(res.text)


if __name__ == '__main__':
    image = 'http://imgs.u-note.me/note/uploadimage/1457354180034.jpg'

    # その他APIもあるので、同じ感じで作っていけばOKです
    # https://japaneast.dev.cognitive.microsoft.com/docs/services/5adf991815e1060e6355ad44/operations/56f91f2e778daf14a499e1fa
    create_analyze_response(image)
