import logging
import azure.functions as func
import requests
from bs4 import BeautifulSoup


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('start.')

    if req.method == 'GET':
        url = requests.get('https://azure.microsoft.com/ja-jp/global-infrastructure/geographies/')

        # とりあえずhtml_parserで回すよー
        page_soup = BeautifulSoup(url.text, 'html.parser')
        target = page_soup.find(id='new-regions').find('div', class_='row row-size2 column')
        azure_region_body = target.find('p', class_='text-body5')

        regions = azure_region_body.text.split(sep=':')[1].split(sep='、')

        logging.info('リージョン数 : ' + str(len(regions)))
        logging.info(regions)
        logging.info(azure_region_body.text)

        # 重複排除済み・プレビュー込みのazureサービス数
        return func.HttpResponse(str(len(regions)))

    else:
        logging.warning('not arrowed method. ' + req.method)
        return func.HttpResponse(
            'not arrowed method. ' + req.method,
            status_code=403
        )
