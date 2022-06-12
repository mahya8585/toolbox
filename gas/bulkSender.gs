/**
 * trigger: なし
 * 0. Google docsにメール文章書いてね。docsのIDをconst doc(13行目)に記載してください
 * ※IDとは：https://docs.google.com/document/d/1vqglFckEI/edit の 「/d/【ここです(1vqglFckEI)】/edit」
 * 
 * 1. 名簿からメールアドレス取得
 * 2. メール送信
 * 
 * 上記処理が発火した場合、システムログとしてmaayaさんプライベートslackチャネルへ通知をします
 */
//件名
const subject = "【テスト】メール送信テスト";
//メール本文
const doc = DocumentApp.openById("メール文章を書いたgoogleDocのIDをいれる");
const body = doc.getBody().getText();
//TOで送る宛先(管理者アドレス)
const recipient = "TOに設定したいメールアドレスを入れる";


//slackへポストする
function postSlackMessage(message_text) {
    var payload = {
      'channel'    : "abks-management",
      'text'       : message_text
  };
  
  var params = {
      "method" : "post",
      "contentType" : "application/json",
      "muteHttpExceptions" : true,
      "payload" : JSON.stringify(payload)
  };

  Logger.log(params);
  UrlFetchApp.fetch("https://hooks.slack.com/services/**********************", params);
  Logger.log("end.");
}


//スプレッドシートからメール送付先取得
function gerAddress(){
  //スプレッドシートのメールアドレス(B列)をすべて取得
  var sheet = SpreadsheetApp.openById("*******************************************");
  var target = sheet.getSheetByName("test");
  var columnVals = target.getRange("B:B").getValues(); 
  Logger.log(columnVals);
  const lastRow = String((columnVals.filter(String).length + 1).toFixed(0));

  var addressList = "";
  for(var i=1; i<=lastRow; i++){
    if(i == 1){
      addressList = columnVals[i];
    } else {
      addressList = addressList + ',' + columnVals[i];
    }
  }

  return addressList;
}


//実行メソッド
function exec(){
  const bcc = gerAddress();
  const options = { bcc: bcc };
  GmailApp.sendEmail(recipient, subject, body, options);

  postSlackMessage("【メーリングリストへ一斉送信を行いました。】");
}
