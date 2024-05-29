from io import BytesIO
from PIL import Image
import azure.functions as func
import logging


app = func.FunctionApp()

@app.route(route="", auth_level=func.AuthLevel.ANONYMOUS)
def color_changer(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    """
    {
  "$content-type": "image/jpeg",
  "$content": "/9j/4AAQSkZJRgABAQEAYAs/9k="
    }
    """

    if req.method == 'POST':
        req_body = req.get_body()

        im = Image.open(BytesIO(req_body))
        logging.info('get image.')

        # 画像を白黒にする
        im_gray = im.convert('L')

        # 画像を返却
        buffer = BytesIO()
        im_gray.save(buffer, format='JPEG')

        logging.info('response.')
        return func.HttpResponse(buffer.getvalue(), mimetype='image/jpeg')

    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )