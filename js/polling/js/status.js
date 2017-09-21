//JSON取得処理
function getJSON(url) {
    var result;
    var req = new XMLHttpRequest();
    req.onreadystatechange = function() {
        if (req.readyState == 4 && req.status == 200) {
            result = JSON.parse(req.responseText);
        }
    };
    req.open('GET', url, false);
    req.send(null);

    return result;
}


//各種値更新チェックエントリポイント
function statusUpdate(targetJson) {
    if (targetJson && targetJson.status) {
        //書き換え処理 
        $('#gs').text(targetJson.status);
    } else {
        console.log('対象のJSONデータが存在しません');
    }
}


//初期実行処理
$(window).on('load', function() {
    const jsonUrl = '../json/status.json';
    console.log(jsonUrl);

    //最初のJSON読み込み
    let operateJson = getJSON(jsonUrl);
    console.log(operateJson);

    //設定値の更新
    statusUpdate(operateJson);

    //ポーリング
    $.PeriodicalUpdater('/path/to/service', {
            url: jsonUrl,
            minTimeout: 10000,
            maxTimeout: 10000,
            multiplier: 1, //リクエスト間隔の変更
            maxCalls: 0, //リクエスト回数(0:制限なし)
            type: 'json'
        },
        function(resultJson) {
            console.log(resultJson);

            //設定値の更新
            statusUpdate(resultJson);

        });
});