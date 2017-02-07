function tweetQuote(){
  var quoteSpan     = document.getElementById("quoteText").innerHTML;
  var authorSpan    = document.getElementById("authorText").innerHTML;
  var url = "https://twitter.com/intent/tweet?text=" + quoteSpan + authorSpan;
  window.open(url, '_blank');
}

window.onload = function() {
    var quoteSpan     = document.getElementById("quoteText");
    var authorSpan    = document.getElementById("authorText");
    var submitTechButton  = document.getElementById('techButton');
  var submitSportButton  = document.getElementById('sportButton');
    var oldQuoteIndex = -1;
    var newQuoteIndex = -1;
    var techQuotes        = [
        {'text': '"Just because something doesn’t do what you planned it to do doesn’t mean it’s useless."', 'author': '– Thomas Edison'}, 
        {'text': '"It has become appallingly obvious that our technology has exceeded our humanity."', 'author': '– Albert Einstein'}, 
        {'text': '"Computers are useless. They can only give you answers."', 'author': '– Pablo Picasso'}, 
        {'text': '"Technology is nothing. What’s important is that you have a faith in people, that they’re basically good and smart, and if you give them tools, they’ll do wonderful things with them."', 'author': '– Steve Jobs'}, 
        {'text': '"Technology is teaching us to be human again."', 'author': '– Simon Mainwaring'}
    ];  
  
  var sportQuotes        = [
        {'text': '"If you aren’t going all the way, why go at all?"', 'author': '– Joe Namath'}, 
        {'text': '"Champions keep playing until they get it right."', 'author': '– Billie Jean King'}, 
        {'text': '"If you have everything under control, you’re not moving fast enough."', 'author': '– Mario Andretti'}, 
        {'text': '"Age is no barrier. It’s a limitation you put on your mind."', 'author': '– Jackie Joyner'}, 
        {'text': '"The more difficult the victory, the greater the happiness in winning."', 'author': '– Pele'}
    ];  

    function nextSportQuote() {
        while (newQuoteIndex == oldQuoteIndex) {
            newQuoteIndex = Math.floor(Math.random() * sportQuotes.length);
        }

        quoteSpan.innerHTML  = sportQuotes[newQuoteIndex].text; //make HTML's quoteText random quote
        authorSpan.innerHTML = sportQuotes[newQuoteIndex].author; //make HTML's authorText random author

        oldQuoteIndex = newQuoteIndex;
    }
  function nextTechQuote() {
        while (newQuoteIndex == oldQuoteIndex) {
            newQuoteIndex = Math.floor(Math.random() * techQuotes.length);
        }

        quoteSpan.innerHTML  = techQuotes[newQuoteIndex].text; //make HTML's quoteText random quote
        authorSpan.innerHTML = techQuotes[newQuoteIndex].author; //make HTML's authorText random author

        oldQuoteIndex = newQuoteIndex;
    }
    submitTechButton.onclick = nextTechQuote;
    submitSportButton.onclick = nextSportQuote;
}
