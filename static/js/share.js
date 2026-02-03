(function () {
  function popup(url) {
    var w = 900, h = 700;
    var dualScreenLeft = window.screenLeft !== undefined ? window.screenLeft : screen.left;
    var dualScreenTop = window.screenTop !== undefined ? window.screenTop : screen.top;
    var width = window.innerWidth || document.documentElement.clientWidth || screen.width;
    var height = window.innerHeight || document.documentElement.clientHeight || screen.height;
    var left = ((width / 2) - (w / 2)) + dualScreenLeft;
    var top = ((height / 2) - (h / 2)) + dualScreenTop;
    window.open(url, '_blank', 'scrollbars=yes, width=' + w + ', height=' + h + ', top=' + top + ', left=' + left);
  }
  function setShareLinks() {
    var url = encodeURIComponent(window.location.href);
    var title = encodeURIComponent(document.title);
    var tw = document.getElementById('share-twitter');
    var li = document.getElementById('share-linkedin');
    var fb = document.getElementById('share-facebook');
    var em = document.getElementById('share-email');
    var twUrl = 'https://twitter.com/intent/tweet?url=' + url + '&text=' + title;
    var liUrl = 'https://www.linkedin.com/sharing/share-offsite/?url=' + url;
    var fbUrl = 'https://www.facebook.com/sharer/sharer.php?u=' + url;
    if (tw) {
      tw.setAttribute('href', twUrl);
      tw.onclick = function (e) { e.preventDefault(); popup(twUrl); };
    }
    if (li) {
      li.setAttribute('href', liUrl);
      li.onclick = function (e) { e.preventDefault(); popup(liUrl); };
    }
    if (fb) {
      fb.setAttribute('href', fbUrl);
      fb.onclick = function (e) { e.preventDefault(); popup(fbUrl); };
    }
    if (em) {
      var subject = 'GeoFly Lab: ' + document.title;
      var body = 'Original post: ' + window.location.href;
      var mailto = 'mailto:?subject=' + encodeURIComponent(subject) + '&body=' + encodeURIComponent(body);
      em.setAttribute('href', mailto);
      em.onclick = function (e) { e.preventDefault(); window.location.href = mailto; };
    }
  }
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', setShareLinks);
  } else {
    setShareLinks();
  }
})();
