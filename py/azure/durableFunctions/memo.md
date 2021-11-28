https://docs.microsoft.com/ja-jp/azure/azure-functions/durable/quickstart-python-vscode    
requrements.txt -> azure-functions-durable 追加

func init    
func new -> Durable Functions orchestrator    

func new -> Durable Functions activity 
- オーケストレータのActivity呼び出しを書き換える
-  context.call_activity([Activity名], "Tokyo")

func new -> Durable Functions HTTP starter    

az login
func azure functionapp publish [try-durable]
https://xxxxx.azurewebsites.net/api/orchestrators/funcOrchestrator?code=xupCI/2g==
    
-> URI 最期をオーケストレータfunctionの名前に変換する

{
name: "funcOrchestrator",
instanceId: "7875f24",
runtimeStatus: "Completed",
input: null,
customStatus: null,
output: [
"Hello Tokyo!",
"Hello Seattle!",
"Hello London!"
],
createdTime: "2021-11-28T05:54:09Z",
lastUpdatedTime: "2021-11-28T05:54:10Z"
}
