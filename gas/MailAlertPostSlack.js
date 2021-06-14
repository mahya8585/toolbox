//slackへポストする
function postSlackMessage(message_text, channel, name, emoji) {
    var payload = {
      'channel'    : channel,
      'text'       : message_text,
      'username'   : name,
      'icon_emoji' : emoji
    };
    
    var params = {
        'method' : 'post',
        'contentType' : 'application/json',
        'muteHttpExceptions' : true,
        'payload' : JSON.stringify(payload)
    };
  
    Logger.log(params);
    var send = UrlFetchApp.fetch('https://hooks.slack.com/services/TTTTTT/BBBBBBBB/4a4a4a4a4a4a4a4a4a4a', params);
    Logger.log("send.");
  }
  
  //未読のメールを検索しslackに情報を投げる
  function exec() {
    var mail_threads = GmailApp.search('label:inbox is:unread');
    Logger.log(mail_threads);
  
    if(mail_threads.length > 0){
      var cnt = 0;
      while(cnt < mail_threads.length){
        var mail_thread = mail_threads[cnt];   
        Logger.log(mail_thread);     
        var thread_messages = mail_thread.getMessages();
  
        //取得できた最新のメール情報を取得
        var message = thread_messages[0];
        var title = message.getSubject();
        var body = message.getPlainBody();
        var send_message = '【' + title + '】 \n ' + body;
  
        //slack送信
        postSlackMessage(send_message, 'チャンネル名', 'bot名', ':emoji:');
  
        Utilities.sleep(2000);
        cnt++;
      }
  
      //通知したメールを既読にする
      GmailApp.markThreadsRead(mail_threads);
    }
    
  }
  
  