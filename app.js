const $=s=>document.querySelector(s);let D;
const esc=s=>String(s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
fetch('data/data.json').then(r=>r.json()).then(d=>{D=d;
 [...new Set(d.entries.map(e=>e.category))].sort().forEach(c=>$('#cat').add(new Option(c,c)));
 d.countries.forEach(c=>$('#country').add(new Option(c,c)));
 $('#meta').textContent=`${d.entries.length} entries · updated ${d.updated}`;
 ['#q','#cat','#country','#novc','#ver'].forEach(s=>$(s).addEventListener('input',render));render();});
function filtered(){const q=$('#q').value.toLowerCase(),c=$('#cat').value,co=$('#country').value;
 return D.entries.filter(e=>(!q||(e.name+e.provider+e.eligibility+e.value).toLowerCase().includes(q))&&(!c||e.category==c)&&(!co||e.countries.includes(co)||e.countries.includes('Global'))&&(!$('#novc').checked||!e.needs_vc)&&(!$('#ver').checked||e.verified))
 .sort((a,b)=>(b.featured-a.featured)||(b.verified-a.verified));}
function render(){const L=filtered();$('#count').textContent=`Showing ${L.length} of ${D.entries.length}`;
 $('#list').innerHTML=L.map(e=>`<article class="card">${e.featured?'<span class="tag feat">Featured</span>':''}<h3>${esc(e.name)} <span class="mut">· ${esc(e.provider)}</span></h3>
 <div class="val">${esc(e.value)}</div><div class="mut">${esc(e.eligibility)}</div>
 <div><span class="tag">${esc(e.category)}</span><span class="tag">${e.countries.map(esc).join(', ')}</span>${e.status&&e.status!='open'?'<span class="tag unv">'+esc(e.status)+'</span>':''}<span class="tag">${e.needs_vc?'VC/partner needed':'No VC needed'}</span>${e.verified?'<span class="tag ok">Verified '+e.date_checked+'</span>':'<span class="tag unv">Unverified, check source</span>'}</div>
 <div class="mut"><a href="${esc(e.apply_url)}" target="_blank" rel="noopener">Apply</a> · <a href="${esc(e.source_url)}" target="_blank" rel="noopener">Source</a> · checked ${e.date_checked}</div></article>`).join('');}
