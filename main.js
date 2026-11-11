(function(){
  document.documentElement.classList.add('js');

  // Mobile menu: toggles the rail (top bar on small screens, left rail on desktop).
  var btn=document.querySelector('.menu-btn'),rail=document.getElementById('rail');
  if(btn&&rail){btn.addEventListener('click',function(){
    var o=rail.classList.toggle('open');
    btn.setAttribute('aria-expanded',o);
    btn.setAttribute('aria-label',o?'Close menu':'Open menu');});
    document.addEventListener('keydown',function(e){
      if(e.key==='Escape'&&rail.classList.contains('open')){rail.classList.remove('open');btn.setAttribute('aria-expanded',false);btn.setAttribute('aria-label','Open menu');btn.focus();}});}

  // Reveal on scroll.
  if('IntersectionObserver' in window){
    var io=new IntersectionObserver(function(es){es.forEach(function(e){
      if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target);}});},{threshold:.12});
    document.querySelectorAll('.reveal').forEach(function(el){io.observe(el);});
  }else{document.querySelectorAll('.reveal').forEach(function(el){el.classList.add('in');});}

  // Knowledge Hub filters.
  var chips=document.querySelectorAll('.chip[data-filter]');
  chips.forEach(function(c){c.addEventListener('click',function(){
    chips.forEach(function(x){x.setAttribute('aria-pressed',x===c);});
    var f=c.dataset.filter;
    document.querySelectorAll('.post[data-cat]').forEach(function(p){
      p.hidden=!(f==='all'||p.dataset.cat===f);});});});

  // Glossary search.
  var s=document.getElementById('glossary-search');
  if(s){s.addEventListener('input',function(){
    var q=s.value.trim().toLowerCase(),n=0;
    document.querySelectorAll('.term').forEach(function(t){
      var m=t.textContent.toLowerCase().indexOf(q)>-1;t.hidden=!m;if(m)n++;});
    document.getElementById('glossary-empty').hidden=n>0;});}

  // Contact form: validates, then opens the visitor's email app (mailto).
  var f=document.getElementById('contact-form');
  if(f){f.addEventListener('submit',function(e){
    e.preventDefault();var ok=true;
    f.querySelectorAll('[required]').forEach(function(i){
      var err=i.parentElement.querySelector('.err'),bad=!i.value.trim()||(i.type==='email'&&!/^\S+@\S+\.\S+$/.test(i.value));
      err.textContent=bad?(i.type==='email'?'Please enter a valid email.':'This field is required.'):'';
      i.setAttribute('aria-invalid',bad);if(bad)ok=false;});
    if(ok){
      var v=function(id){var e=document.getElementById(id);return e?e.value.trim():'';};
      var subj='Website enquiry'+(v('topic')?': '+v('topic'):'');
      if(!f.dataset.mail||f.dataset.mail.charAt(0)==='['){console.warn('Contact email is still a placeholder in tools/identity.py');}
      var body='Name: '+v('name')+'\nEmail: '+v('email')+'\n\n'+v('msg');
      f.hidden=true;var okEl=document.getElementById('form-ok');okEl.hidden=false;okEl.focus();
      window.location.href='mailto:'+(f.dataset.mail||'')+'?subject='+encodeURIComponent(subj)+'&body='+encodeURIComponent(body);
    }
  });}

  // Hours calculator (runs in the browser only).
  var cf=document.getElementById('calc');
  if(cf){
    var t=document.getElementById('c-target'),r=document.getElementById('c-rate'),o=document.getElementById('c-out');
    var run=function(){var a=parseFloat(t.value),b=parseFloat(r.value);
      if(!(a>0)||!(b>0)){o.hidden=true;return;}
      var h=a/b/4.33;o.innerHTML='<b>Roughly '+(Math.round(h*10)/10)+' hours a week</b><br>to cover $'+a+' a month at $'+b+' an hour, before tax and costs. This is a rough planning figure only, not a promise of income.';o.hidden=false;};
    t.addEventListener('input',run);r.addEventListener('input',run);
  }

  // Job guides: highlight the current section in the contents rail.
  var toc=document.querySelectorAll('.toc a');
  if(toc.length&&'IntersectionObserver' in window){
    var map={};toc.forEach(function(a){map[a.getAttribute('href').slice(1)]=a;});
    var so=new IntersectionObserver(function(es){es.forEach(function(e){
      if(e.isIntersecting){toc.forEach(function(a){a.removeAttribute('aria-current');});
        var a=map[e.target.id];if(a)a.setAttribute('aria-current','true');}});},{rootMargin:'-20% 0px -70% 0px'});
    Object.keys(map).forEach(function(id){var el=document.getElementById(id);if(el)so.observe(el);});
  }
})();
