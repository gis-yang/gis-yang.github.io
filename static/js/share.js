(function () {
  function absoluteUrl(src) {
    if (!src) return '';
    try { return new URL(src, window.location.href).href; } catch (e) { return src; }
  }
  function buildEmailBody() {
    var titleEl = document.querySelector('h1.main-heading');
    var title = titleEl ? titleEl.innerText : document.title;
    var container = document.querySelector('.blog .col-lg-8');
    var text = '';
    if (container) {
      var paragraphs = Array.from(container.querySelectorAll('p'))
        .map(function (p) { return p.innerText.trim(); })
        .filter(Boolean);
      text = paragraphs.join('\n\n');
    }
    var images = container ? Array.from(container.querySelectorAll('img')) : [];
    var imageUrls = images.map(function (img) { return absoluteUrl(img.getAttribute('src')); }).filter(Boolean);
    var bodyParts = [];
    if (title) bodyParts.push(title);
    if (text) bodyParts.push(text);
    if (imageUrls.length) bodyParts.push('Images:\n' + imageUrls.map(function (u) { return '• ' + u; }).join('\n'));
    bodyParts.push('Original post: ' + window.location.href);
    return bodyParts.join('\n\n');
  }
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
      var subjTitle = (document.querySelector('h1.main-heading') || {}).innerText || document.title;
      var subject = 'GeoFly Lab: ' + subjTitle;
      var body = buildEmailBody();
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
