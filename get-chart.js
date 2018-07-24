function search(tags) {

  var url = "https://research.stlouisfed.org/ssi/search.php?q=";
  var i;
  for(i=0; i < tags.length; i++) {
      url += tags[i]

      if (i < tags.length-1){
          url += "+"
      }
  }
  return url;
}

function getImage(url) {

  var request = require('request');
  var cheerio = require('cheerio');
  var url = search(["unemployment", "usa"]);


  request(url, function (error, response, html) {
    if (!error && response.statusCode == 200) {
      let $ = cheerio.load(html);
      var result = $('div[class=search-results]').html();
      console.log(result);
    }

  });


}

getImage()
