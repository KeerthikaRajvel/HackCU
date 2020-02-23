function showTweets(){
    console.log(ids)

     for (var i = 0; i < ids.length; i++){
      twttr.widgets.createTweet(
          ids[i],
          document.getElementById('tweets'),
          {
            theme: 'light'
          }
        );

  }
  }