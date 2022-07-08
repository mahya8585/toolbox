/**
 * trigger: gmail box Polling
 * 1. 送ったメールに対してMDS@gmail からfailure通知があった場合、名簿にエラー表記を行う
 * 2. 見知らぬメールサーバ(postmaster)からの返信があった場合、要チェック表記を行う
 * 
 * 上記処理が発火した場合、システムログとしてmaayaさんプライベートslackチャネルへ通知をします
 */

//記入メッセージステータス
const statusFailure = "failure";
const statusTBC = "TBC";

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
  UrlFetchApp.fetch("https://hooks.slack.com/services/*********", params);
  Logger.log("end.");
}

//スプレッドシートに書き込む
function updateColumn(messageType, address){
  //スプレッドシートのメールアドレス(B列)をすべて取得
  var sheet = SpreadsheetApp.openById("******************************");
  var target = sheet.getSheetByName("memberList");
  var columnVals = target.getRange("B:B").getValues(); 
  Logger.log(columnVals);
  const lastRow = String((columnVals.filter(String).length + 1).toFixed(0));

  for(var i=1; i<=lastRow; i++){
    //名簿に存在するメールアドレスだった場合、メッセージタイプに合わせてエラーステータスを入力する
    if(address == columnVals[i]){
      var rangeCount = Math.round(i) + 1;
      Logger.log("rangeCount : " + rangeCount);

      if(messageType == statusFailure) {
        var targetCell = target.getRange("D"+rangeCount);
        targetCell.setValue("returned error");

      } else if (messageType == statusTBC) {
        var targetCell = target.getRange("D"+rangeCount);
        targetCell.setValue("TBC");
      } 
    }
  }
}


//googleMDSメッセージの検索及び情報取得
function searchAndNotifyForMDS(){
  var threads = GmailApp.search("label:inbox is:unread from:mailer-daemon@googlemail.com", 0, 200);
  Logger.log(threads);

  //エラー対象になっているメールアドレスが名簿に存在したら各所へ通知処理実施
  for (var t=0; t<threads.length; t++) {
    var mails = GmailApp.getMessagesForThread(threads[t]);
 
    for (var m=0; m<mails.length; m++) {
      //エラー対象のメールアドレスを取得
      const body = mails[m].getPlainBody();
      Logger.log(body);

      var bodySearch = body.match(/メールは(.*)に配信されませんでした。/g);
      Logger.log(bodySearch);
      if(bodySearch != null){
        var address = bodySearch[0].replace("メールは","").replace("に配信されませんでした。","").trim();
        Logger.log(address);

        //スプレッドシートへ書き込み
        updateColumn(statusFailure, address);
        //slackへ通知
        postSlackMessage(statusFailure + "  for GoogleMDS : " + address);

        //既読にする
        mails[m].markRead();
      }
    }

    Logger.log("thead search end.");
  }
}


//postmaster系メッセージの検索及び情報取得
function searchAndNotifyForPostMaster(){
  var threads = GmailApp.search('postmaster@ label:inbox is:unread', 0, 200);
  Logger.log(threads);

  //エラー対象になっているメールアドレスが名簿に存在したら各所へ通知処理実施
  for (var t=0; t<threads.length; t++) {
    var mails = GmailApp.getMessagesForThread(threads[t]);
 
    for (var m=0; m<mails.length; m++) {
      //エラー対象のメールアドレスを取得
      const body = mails[m].getPlainBody();
      Logger.log(body);

      var bodySearch = body.match(/(.*)@(.*)/g);
      Logger.log(bodySearch);
      if(bodySearch != null){
        var address = bodySearch[0].split("<")[0];
        Logger.log(address);

        //スプレッドシートへ書き込み
        updateColumn(statusTBC, address);
        //slackへ通知
        postSlackMessage(statusTBC + " : " + body);

        //既読にする
        mails[m].markRead();
      }
    }

    Logger.log("thead search end.");

  }
}


//実行メソッド
function exec() {
  //MDS@gmailからのメールをキャッチ
  searchAndNotifyForMDS();

  //postmasterからのメールをキャッチ
  searchAndNotifyForPostMaster();
  
}

