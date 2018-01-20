//フォームが送信されたら本スクリプトを実行する
function onFormSubmit(e) {
  postSlackMessage();
}

//slackへポストする
function postSlackMessage() {
    var payload = {
      'token'      : 'xoxp-xxxxxxx',
      'channel'    : 'CHANNELNAME',
      'text'       : createMessage(),
      'username'   : 'なかまに なりたそうに こちらをみている',
      'icon_emoji' : ':king:'
  };
  
  var params = {
      'method' : 'post',
      'payload' : payload
  };

  Logger.log(params);
  var send = UrlFetchApp.fetch('https://slack.com/api/chat.postMessage', params);
  Logger.log(send);
}

//送信メッセージの作成(解答スプレッドシートから)
function createMessage(){
  var form = FormApp.getActiveForm();
  var formResponses = form.getResponses();
  
  //解答情報の収集
  for (var resCount = 0; resCount < formResponses.length; resCount++) {
    var formResponse = formResponses[resCount];
    var message = '';
    
    message = '【Email】' + formResponse.getRespondentEmail() + '\n';
    
    var itemResponses = formResponse.getItemResponses();
    for (var itemCount = 0; itemCount < itemResponses.length; itemCount++) {
      var itemResponse = itemResponses[itemCount];
      var questionTitle = itemResponse.getItem().getTitle();
      var answer = itemResponse.getResponse();
      
      message += '【' + questionTitle + '】\n　　' + answer + '\n';
    }
  }

  return message;
}
