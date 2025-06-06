import azure.functions as func
import azure.durable_functions as df

app = df.DFApp(http_auth_level=func.AuthLevel.ANONYMOUS)

# An HTTP-triggered function with a Durable Functions client binding
@app.route(route="orchestrators/start")
@app.durable_client_input(client_name="client")
async def http_start(req: func.HttpRequest, client):

    # オーケストレータの呼び出し
    instance_id = await client.start_new("hello_orchestrator")
    response = client.create_check_status_response(req, instance_id)

    return response


# Orchestrator 
@app.orchestration_trigger(context_name="context")
def hello_orchestrator(context):

    # 関数チェーン型
    result1 = yield context.call_activity("noon", "Seattle")
    result2 = yield context.call_activity("morning", "Tokyo")
    result3 = yield context.call_activity("evening", "London")
    result4 = yield context.call_activity("noon", "San Francisco")

    return [result1, result2, result3, result4]


# Activity
@app.activity_trigger(input_name="city")
def noon(city: str):
    return f"Hello, {city}"

@app.activity_trigger(input_name="city")
def morning(city: str):
    return f"Good morning, {city}"

@app.activity_trigger(input_name="city")
def evening(city: str):
    return f"Good evening, {city}"