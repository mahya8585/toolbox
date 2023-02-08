import logging
import azure.functions as func
import requests
from bs4 import BeautifulSoup


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('start.')

    if req.method == 'GET':
        url = requests.get('https://azure.microsoft.com/ja-jp/services/')

        # とりあえずhtml_parserで回すよー
        page_soup = BeautifulSoup(url.text, 'html.parser')
        azure_services = page_soup.find_all('h3', class_='text-heading5')

        service_names = []
        for service_obj in azure_services:
            service_name = service_obj.find('span')
            result_name = service_name.text.replace('プレビュー', '')
            service_names.append(result_name)

        # print('全サービス数 : ' + str(len(service_names)))
        name_set = dict.fromkeys(service_names)
        logging.info('重複排除 : ' + str(len(name_set)))

        # 重複排除済み・プレビュー込みのazureサービス数
        return func.HttpResponse(str(len(name_set)))

    else:
        logging.warning('not arrowed method. ' + req.method)
        return func.HttpResponse(
            'not arrowed method. ' + req.method,
            status_code=403
        )
