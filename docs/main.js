const AIRPORT_COORDS = {
  "Aalesund": [62.5625, 6.1194], "Aberdeen": [57.2019, -2.1977], "Abu Dhabi": [24.433, 54.6511],
  "Agadir": [30.3281, -9.4131], "Alexandria": [31.1884, 29.9489], "Alghero": [40.6322, 8.2908],
  "Alicante": [38.2822, -0.5581], "Almaty": [43.3517, 77.04], "Amman": [31.7225, 35.9928],
  "Ancona": [43.6161, 13.3619], "Antalya": [36.8986, 30.8008], "Asyut": [27.0467, 31.0119],
  "Athens": [37.9364, 23.9475], "Bacau": [46.5211, 26.9103], "Baku": [40.4675, 50.0467],
  "Banja Luka": [44.9411, 17.2975], "Barcelona": [41.2974, 2.0833], "Bari": [41.1389, 16.7606],
  "Basel/Mulhouse": [47.5897, 7.5294], "Beirut": [33.8206, 35.4883], "Belgrade": [44.8184, 20.3092],
  "Bergen": [60.2934, 5.2181], "Berlin": [52.3512, 13.4936], "Bilbao": [43.3011, -2.9106],
  "Billund": [55.7403, 9.1522], "Birmingham": [52.4539, -1.7481], "Bishkek": [43.0611, 74.4761],
  "Bologna": [44.5353, 11.2889], "Brasov": [45.595, 25.5156], "Bratislava": [48.1703, 17.2128],
  "Brussels": [50.9014, 4.4844], "Bucharest": [44.5711, 26.085], "Budapest": [47.4381, 19.2556],
  "Burgas": [42.5697, 27.5153], "Castellon": [40.2097, 0.0703], "Catania": [37.4669, 15.0664],
  "Chania": [35.5317, 24.1497], "Chisinau": [46.9275, 28.9308], "Cluj": [46.7853, 23.6864],
  "Comiso": [36.9947, 14.6072], "Constanta": [44.3442, 28.4883], "Copenhagen": [55.6181, 12.6508],
  "Craiova": [44.3181, 23.8886], "Dalaman": [36.7133, 28.7925], "Dammam": [26.4711, 49.7978],
  "Debrecen": [47.4889, 21.6153], "Dortmund": [51.5178, 7.6122], "Dubai": [25.2522, 55.3644],
  "Dubrovnik": [42.5614, 18.2681], "Eindhoven": [51.45, 5.3747], "Faro": [37.0144, -7.9658],
  "Frankfurt": [50.0379, 8.5622], "Friedrichshafen": [47.6719, 9.5114], "Fuerteventura": [28.4528, -13.8639],
  "Gabala": [40.8267, 47.7125], "Gdansk": [54.3775, 18.4661], "Genoa": [44.4133, 8.8375],
  "Girona": [41.9011, 2.7608], "Giza": [30.1203, 30.8067], "Glasgow": [55.8719, -4.4331],
  "Gothenburg": [57.6628, 12.2797], "Gran Canaria": [27.9319, -15.3867], "Gyumri": [40.75, 43.8514],
  "Hamburg": [53.6304, 10.0067], "Haugesund": [59.3453, 5.2081], "Heraklion": [35.3387, 25.1803],
  "Hurghada": [27.1783, 33.7994], "Iasi": [47.1781, 27.6206], "Ibiza": [38.8728, 1.3731],
  "Istanbul": [41.2754, 28.7519], "Jeddah": [21.6796, 39.1564], "Karlsruhe/Baden-Baden": [48.7794, 8.0806],
  "Katowice": [50.4742, 19.08], "Kaunas": [54.9639, 24.0844], "Kerkyra": [39.6017, 19.9119],
  "Kosice": [48.6631, 21.2411], "Krakow": [50.0778, 19.7847], "Kutaisi": [42.1761, 42.4825],
  "Larnaca": [34.875, 33.6249], "Leeds/Bradford": [53.8658, -1.6603], "Leipzig/Halle": [51.4239, 12.2361],
  "Lisbon": [38.7813, -9.1361], "Liverpool": [53.3356, -2.8497], "Ljubljana": [46.2237, 14.4581],
  "London": [51.47, -0.4543], "Lublin": [51.7225, 23.1714], "Lyon": [45.7256, 5.0811],
  "Madeira": [32.6978, -16.7745], "Madinah": [24.5536, 39.705], "Madrid": [40.4936, -3.5667],
  "Malaga": [36.675, -4.4992], "Male": [4.1917, 73.5289], "Malmo": [55.5361, 13.3675],
  "Malta": [35.8575, 14.4775], "Marrakech": [31.6067, -8.0361], "Marsa Alam": [25.5572, 34.5836],
  "Memmingen": [47.9881, 10.2394], "Milan": [45.6306, 8.7281], "Mykonos": [37.435, 25.3483],
  "Naples": [40.886, 14.2908], "Nice": [43.6653, 7.215], "Nis": [43.3372, 21.8536],
  "Nur-Sultan": [51.0219, 71.4669], "Nuremberg": [49.4986, 11.0669], "Ohrid": [41.18, 20.7428],
  "Olbia": [40.8986, 9.5181], "Oslo": [60.1939, 11.1003], "Palma De Mallorca": [39.5517, 2.7386],
  "Paphos": [34.7181, 32.4856], "Paris": [49.0097, 2.5478], "Perugia": [43.0956, 12.5133],
  "Pescara": [42.4317, 14.1811], "Pisa": [43.6839, 10.3928], "Plovdiv": [42.0678, 24.8508],
  "Podgorica": [42.3597, 19.2519], "Poprad/Tatry": [49.0736, 20.2406], "Porto": [41.2481, -8.6814],
  "Poznan": [52.4214, 16.8269], "Prague": [50.1008, 14.26], "Pristina": [42.5728, 21.0361],
  "Radom": [51.3889, 21.2133], "Reykjavik": [63.985, -22.6056], "Rhodes": [36.4054, 28.0864],
  "Riga": [56.9236, 23.9711], "Rimini": [44.0203, 12.6114], "Riyadh": [24.9578, 46.6983],
  "Rome": [41.8003, 12.2389], "Rzeszow": [50.11, 22.0192], "Salalah": [17.0386, 54.0914],
  "Salerno": [40.6203, 14.9114], "Salzburg": [47.7931, 13.0044], "Samarkand": [39.7006, 66.9844],
  "Santorini": [36.3992, 25.4794], "Sarajevo": [43.8247, 18.3314], "Satu Mare": [47.7031, 22.8856],
  "Sevilla": [37.4181, -5.8931], "Sharm el-Sheikh": [27.9772, 34.3947], "Sibiu": [45.7856, 24.0914],
  "Skiathos": [39.1769, 23.5036], "Skopje": [41.9617, 21.6214], "Sofia": [42.6947, 23.4114],
  "Sohag": [26.3428, 31.7428], "Split": [43.5389, 16.2981], "Stavanger": [58.8767, 5.6378],
  "Stockholm": [59.6519, 17.9186], "Stuttgart": [48.6897, 9.2219], "Suceava": [47.6875, 26.3544],
  "Szczecin": [53.5847, 14.9019], "Tallinn": [59.4133, 24.8328], "Targu-Mures": [46.4681, 24.4119],
  "Tashkent": [41.2578, 69.2811], "Tel Aviv": [32.0114, 34.8867], "Tenerife": [28.0828, -16.5725],
  "Thessaloniki": [40.5197, 22.9706], "Timisoara": [45.8103, 21.3378], "Tirana": [41.4147, 19.7206],
  "Trieste": [45.8275, 13.4719], "Tromso": [69.6833, 18.9189], "Trondheim": [63.4578, 10.9242],
  "Turin": [45.2006, 7.6494], "Turkistan": [43.2733, 68.3072], "Turku": [60.5142, 22.2628],
  "Tuzla": [44.4586, 18.725], "Valencia": [39.4894, -0.4814], "Varna": [43.2322, 27.8253],
  "Venice": [45.5053, 12.3519], "Verona": [45.3956, 10.8883], "Vienna": [48.1103, 16.5697],
  "Vilnius": [54.6342, 25.2858], "Warsaw": [52.1658, 20.9675], "Wroclaw": [51.1025, 16.8858],
  "Yerevan": [40.1475, 44.3956], "Zakinthos Island": [37.7508, 20.8828], "Zaragoza": [41.6661, -1.0406],
  "Ankara": [40.1281, 32.9951], "Bordeaux": [44.8283, -0.7156], "Brindisi": [40.6576, 17.9470],
  "Cologne/Bonn": [50.8659, 7.1427], "Klaipeda/Palanga": [55.9733, 21.0939], "Lamezia Terme": [38.9054, 16.2422],
  "Maastricht": [50.9117, 5.7700], "Menorca": [39.8626, 4.2186], "Oradea": [47.0253, 21.9028],
  "Palermo": [38.1759, 13.0910], "Sandefjord": [59.1867, 10.2586],
  "Santander": [43.4267, -3.8200], "Szczytno": [53.4783, 20.9378]
};

const WEEKDAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'];
const MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];

const PLOT_CONFIG = { displaylogo: false, displayModeBar: false, responsive: true };
const COLORS = {
  text: '#0a0a0a',
  textSoft: '#525252',
  textMuted: '#737373',
  textFaint: '#a3a3a3',
  border: '#e7e7e7',
  surface: '#ffffff',
  accent: '#e6007e',
  slate: '#404040',
  hub: '#e6007e',
  dest: '#404040',
  other: '#a3a3a3',
};
const FONT_SANS = "'Geist', -apple-system, BlinkMacSystemFont, sans-serif";
const FONT_MONO = "'Geist Mono', ui-monospace, monospace";
const FONT = { family: FONT_MONO, size: 11, color: COLORS.textMuted };
const BASE_LAYOUT = {
  paper_bgcolor: 'rgba(0,0,0,0)',
  plot_bgcolor: 'rgba(0,0,0,0)',
  font: FONT,
  hoverlabel: {
    font: { family: FONT_SANS, size: 13, color: COLORS.text },
    bgcolor: COLORS.surface,
    bordercolor: COLORS.border,
  },
  margin: { l: 56, r: 16, t: 12, b: 48 },
};
const AXIS_BASE = {
  showline: false,
  linecolor: COLORS.border,
  linewidth: 1,
  ticks: 'outside',
  tickcolor: COLORS.border,
  ticklen: 4,
  tickfont: { family: FONT_MONO, size: 11, color: COLORS.textMuted },
  gridcolor: COLORS.border,
  zeroline: false,
  title: { font: { family: FONT_MONO, size: 11, color: COLORS.textMuted }, standoff: 12 },
};

let DATA = null;
const STATE = { hub: null, destination: null };

async function init() {
  try {
    const r = await fetch('aggregated-data.json', { cache: 'no-cache' });
    if (!r.ok) throw new Error(`HTTP ${r.status}`);
    DATA = await r.json();
    preprocess(DATA);
    setupCombos();
    setupMeta();
    render();
    document.getElementById('loading').classList.add('hidden');
  } catch (e) {
    document.getElementById('loading').textContent = 'Failed to load data: ' + e.message;
    console.error(e);
  }
}

function preprocess(d) {
  d.dates = Object.keys(d.availability).sort();
  d.airportIdx = {};
  d.airports.forEach((n, i) => { d.airportIdx[n] = i; });
  d.dateAvailSet = {};
  for (const dt of d.dates) d.dateAvailSet[dt] = new Set(d.availability[dt]);
  d.routeIdx = {};
  d.routes.forEach(([o, dst], i) => {
    if (!d.routeIdx[o]) d.routeIdx[o] = {};
    d.routeIdx[o][dst] = i;
  });
  d.continuousDates = fillRange(d.dates[0], d.dates[d.dates.length - 1]);
  d.dateSet = new Set(d.dates);
  d.weekdayOfDate = {};
  for (const dt of d.continuousDates) d.weekdayOfDate[dt] = (new Date(dt + 'T00:00:00Z').getUTCDay() + 6) % 7;
}

function fillRange(start, end) {
  const out = [];
  let cur = new Date(start + 'T00:00:00Z');
  const stop = new Date(end + 'T00:00:00Z');
  while (cur <= stop) {
    out.push(cur.toISOString().slice(0, 10));
    cur.setUTCDate(cur.getUTCDate() + 1);
  }
  return out;
}

function setupMeta() {
  const lastDate = DATA.dates[DATA.dates.length - 1];
  const fmt = (iso) => new Date(iso + 'T00:00:00Z').toLocaleDateString('en-GB', {
    day: 'numeric', month: 'long', year: 'numeric', timeZone: 'UTC',
  });
  const el = document.getElementById('pub-date');
  if (el) {
    el.textContent = fmt(lastDate);
    el.setAttribute('datetime', lastDate);
  }
}

function setupCombos() {
  setupCombo('hub-input', 'hub-list', () => STATE.hub, v => { STATE.hub = v; render(); });
  setupCombo('dest-input', 'dest-list', () => STATE.destination, v => { STATE.destination = v; render(); });
  document.querySelectorAll('.combo-clear').forEach(btn => {
    btn.addEventListener('mousedown', e => e.preventDefault());
    btn.addEventListener('click', () => {
      const t = btn.dataset.target;
      const inp = document.getElementById(`${t}-input`);
      inp.value = '';
      if (t === 'hub') STATE.hub = null; else STATE.destination = null;
      render();
    });
  });
}

function setupCombo(inputId, listId, getValue, setValue) {
  const inp = document.getElementById(inputId);
  const list = document.getElementById(listId);
  let activeIdx = -1;
  let visible = [];

  inp.setAttribute('role', 'combobox');
  inp.setAttribute('aria-autocomplete', 'list');
  inp.setAttribute('aria-controls', listId);
  inp.setAttribute('aria-expanded', 'false');

  const renderList = (filter) => {
    const f = filter.trim().toLowerCase();
    visible = DATA.airports.filter(a => a.toLowerCase().includes(f));
    if (!visible.length) {
      list.innerHTML = '<li class="empty">No airports match</li>';
      return;
    }
    list.innerHTML = visible.map((a, i) => `<li role="option" data-idx="${i}">${esc(a)}</li>`).join('');
    if (activeIdx >= visible.length) activeIdx = -1;
    if (activeIdx >= 0) list.children[activeIdx].classList.add('active');
  };

  const open = () => { list.hidden = false; inp.setAttribute('aria-expanded', 'true'); renderList(inp.value); };
  const close = () => { list.hidden = true; inp.setAttribute('aria-expanded', 'false'); activeIdx = -1; };
  const updateActive = () => {
    [...list.children].forEach((c, i) => c.classList.toggle('active', i === activeIdx));
    const el = list.children[activeIdx];
    if (el && el.scrollIntoView) el.scrollIntoView({ block: 'nearest' });
  };
  const select = (v) => { inp.value = v; setValue(v); close(); };

  inp.addEventListener('focus', open);
  inp.addEventListener('input', () => { activeIdx = -1; renderList(inp.value); list.hidden = false; });
  inp.addEventListener('blur', () => {
    setTimeout(() => {
      close();
      const cur = getValue();
      if (inp.value !== (cur || '')) inp.value = cur || '';
    }, 150);
  });
  inp.addEventListener('keydown', e => {
    if (list.hidden) {
      if (e.key === 'ArrowDown') open();
      return;
    }
    if (e.key === 'ArrowDown') { activeIdx = Math.min(visible.length - 1, activeIdx + 1); updateActive(); e.preventDefault(); }
    else if (e.key === 'ArrowUp') { activeIdx = Math.max(0, activeIdx - 1); updateActive(); e.preventDefault(); }
    else if (e.key === 'Enter') {
      if (activeIdx >= 0 && visible[activeIdx]) { select(visible[activeIdx]); e.preventDefault(); }
      else if (visible.length === 1) { select(visible[0]); e.preventDefault(); }
    } else if (e.key === 'Escape') { close(); inp.blur(); }
  });
  list.addEventListener('mousedown', e => {
    e.preventDefault();
    const li = e.target.closest('li[data-idx]');
    if (!li) return;
    select(visible[+li.dataset.idx]);
  });
}

function getRouteIdx(originIdx, destIdx) {
  const m = DATA.routeIdx[originIdx];
  if (!m) return -1;
  const v = m[destIdx];
  return v == null ? -1 : v;
}

function render() {
  const dc = dailyMatchCounts();
  updateFilterHint();
  renderMetrics(dc);
  renderDailyChart(dc);
  renderMonthlyChart(dc);
  renderWeekdayChart(dc);
  renderMap();
}

function updateFilterHint() {
  const { hub, destination } = STATE;
  const el = document.getElementById('filter-hint');
  if (hub && destination) el.textContent = `${hub} ↔ ${destination} — both directions.`;
  else if (hub) el.textContent = `Departures from ${hub}.`;
  else if (destination) el.textContent = `Arrivals in ${destination}.`;
  else el.textContent = `All ${DATA.routes.length.toLocaleString()} routes shown.`;
}

function dailyMatchCounts() {
  const hi = STATE.hub != null ? DATA.airportIdx[STATE.hub] : null;
  const di = STATE.destination != null ? DATA.airportIdx[STATE.destination] : null;
  return DATA.dates.map(date => {
    const ids = DATA.availability[date];
    let count = 0;
    if (hi != null && di != null) {
      const ab = getRouteIdx(hi, di);
      const ba = getRouteIdx(di, hi);
      const set = DATA.dateAvailSet[date];
      const abv = ab >= 0 && set.has(ab) ? 1 : 0;
      const bav = ba >= 0 && set.has(ba) ? 1 : 0;
      return { date, ab: abv, ba: bav };
    }
    for (const rid of ids) {
      const [o, d] = DATA.routes[rid];
      if (hi != null) { if (o === hi) count++; }
      else if (di != null) { if (d === di) count++; }
      else count++;
    }
    return { date, count };
  });
}

function renderMetrics(dc) {
  const { hub, destination } = STATE;
  const el = document.getElementById('metrics');
  const prev = new Map();
  el.querySelectorAll('[data-key]').forEach(n => prev.set(n.dataset.key, n.textContent));

  el.classList.toggle('headline-dual', !!(hub && destination));

  if (hub && destination) {
    const total = dc.length;
    const ab = dc.filter(x => x.ab).length;
    const ba = dc.filter(x => x.ba).length;
    const pct = (n) => total ? (n / total * 100).toFixed(1) : '—';
    el.innerHTML = `
      <div class="col">
        <p class="pct" data-key="ab">${pct(ab)}<span class="unit">%</span></p>
        <p class="label">${esc(hub)} → ${esc(destination)}</p>
      </div>
      <div class="col">
        <p class="pct" data-key="ba">${pct(ba)}<span class="unit">%</span></p>
        <p class="label">${esc(destination)} → ${esc(hub)}</p>
      </div>
    `;
  } else {
    const counts = dc.map(d => d.count);
    const avg = counts.length ? counts.reduce((a, b) => a + b, 0) / counts.length : 0;
    let label;
    if (hub) label = `Average flights per day departing ${esc(hub)}`;
    else if (destination) label = `Average flights per day arriving in ${esc(destination)}`;
    else label = 'Average flights bookable on a typical day';
    el.innerHTML = `
      <p class="headline-label">${label}</p>
      <p class="headline-figure" data-key="avg">${avg.toFixed(2)}</p>
    `;
  }

  el.querySelectorAll('[data-key]').forEach(n => {
    const before = prev.get(n.dataset.key);
    if (before != null && before !== n.textContent) {
      n.classList.add('flip');
      setTimeout(() => n.classList.remove('flip'), 500);
    }
  });

  updateCoverageLine(dc);
}

function updateCoverageLine(dc) {
  const el = document.getElementById('coverage-line');
  if (!el) return;
  const { hub, destination } = STATE;
  const matched = dc.filter(d => (d.count || 0) > 0 || d.ab > 0 || d.ba > 0).map(d => d.date);
  if (!matched.length) {
    el.textContent = '— no observations match the current filter —';
    return;
  }
  const first = matched[0];
  const last = matched[matched.length - 1];
  const span = `${longDate(first)} → ${longDate(last)}`;
  const daysWith = matched.length;
  const totalDays = DATA.dates.length;
  if (hub && destination) {
    el.textContent = `${hub} ↔ ${destination} · observed on ${daysWith.toLocaleString()} of ${totalDays.toLocaleString()} days · ${span}`;
  } else if (hub || destination) {
    el.textContent = `Coverage · ${daysWith.toLocaleString()} of ${totalDays.toLocaleString()} days · ${span}`;
  } else {
    el.textContent = `Coverage · ${totalDays.toLocaleString()} days collected · ${span}`;
  }
}

function longDate(iso) {
  return new Date(iso + 'T00:00:00Z').toLocaleDateString('en-GB', { day: '2-digit', month: 'short', year: 'numeric', timeZone: 'UTC' });
}

function renderDailyChart(dc) {
  const { hub, destination } = STATE;
  const wrap = document.getElementById('daily-chart');
  const legend = document.getElementById('daily-legend');

  if (hub && destination) {
    legend.classList.add('is-visible');
    renderRouteTimeline(wrap, hub, destination);
  } else {
    legend.classList.remove('is-visible');
    renderDailyLine(wrap, dc);
  }
}

function renderDailyLine(wrap, dc) {
  const observed = Object.fromEntries(dc.map(d => [d.date, d.count]));
  const x = DATA.continuousDates;
  const y = x.map(d => DATA.dateSet.has(d) ? observed[d] : null);
  const observedY = dc.map(d => d.count);
  const avg = observedY.length ? observedY.reduce((a, b) => a + b, 0) / observedY.length : 0;

  const data = [{
    x, y, type: 'scatter', mode: 'lines',
    line: { color: COLORS.accent, width: 1.6 },
    connectgaps: false,
    fill: 'tozeroy',
    fillcolor: 'rgba(230, 0, 126, 0.06)',
    name: 'Flights',
    hovertemplate: '<b>%{x|%a, %d %b %Y}</b><br>%{y} flights<extra></extra>',
  }];

  const layout = {
    ...BASE_LAYOUT,
    margin: { l: 48, r: 16, t: 16, b: 44 },
    height: 300,
    xaxis: { ...AXIS_BASE, title: undefined },
    yaxis: { ...AXIS_BASE, title: undefined, rangemode: 'tozero', gridcolor: COLORS.border },
    shapes: [{
      type: 'line', xref: 'paper', x0: 0, x1: 1,
      y0: avg, y1: avg,
      line: { color: COLORS.textFaint, dash: 'dot', width: 1 },
    }],
    annotations: [{
      xref: 'paper', x: 1, xanchor: 'right',
      y: avg, yanchor: 'bottom',
      text: `mean ${avg.toFixed(1)}`,
      showarrow: false,
      font: { family: FONT_MONO, size: 11, color: COLORS.textMuted },
      bgcolor: '#fafafa',
      borderpad: 4,
    }],
    hovermode: 'x unified',
  };
  Plotly.react(wrap, data, layout, PLOT_CONFIG);
}

function renderRouteTimeline(wrap, hub, dest) {
  const hi = DATA.airportIdx[hub];
  const di = DATA.airportIdx[dest];
  const ab = getRouteIdx(hi, di);
  const ba = getRouteIdx(di, hi);
  const dates = DATA.continuousDates;
  const haveData = new Set(DATA.dates);

  const cell = (date, rid) => {
    if (!haveData.has(date)) return null;
    if (rid < 0) return 0;
    return DATA.dateAvailSet[date].has(rid) ? 1 : 0;
  };

  const abRow = dates.map(d => cell(d, ab));
  const baRow = dates.map(d => cell(d, ba));
  const bothRow = abRow.map((v, i) => {
    const w = baRow[i];
    if (v == null || w == null) return null;
    return v === 1 && w === 1 ? 1 : 0;
  });

  const hover = (label) => (v, i) => {
    const date = dates[i];
    const wd = new Date(date + 'T00:00:00Z').toLocaleDateString('en-US', { weekday: 'short', timeZone: 'UTC' });
    const state = v == null ? 'No data collected' : v === 1 ? '✈️ Flight available' : 'No flight';
    return `<b>${esc(label)}</b><br>${date} (${wd})<br>${state}`;
  };

  const narrow = window.innerWidth < 720;
  const abbr = (s) => s.replace(/[\/\s].*$/, '').slice(0, 3).toUpperCase();
  const yLabels = narrow
    ? ['Both', `${abbr(hub)} → ${abbr(dest)}`, `${abbr(dest)} → ${abbr(hub)}`]
    : ['Both', `${hub} → ${dest}`, `${dest} → ${hub}`];
  const z = [bothRow, abRow, baRow];
  const customdata = [
    bothRow.map(hover('Both directions')),
    abRow.map(hover(`${hub} → ${dest}`)),
    baRow.map(hover(`${dest} → ${hub}`)),
  ];

  const data = [{
    type: 'heatmap',
    x: dates, y: yLabels, z,
    customdata,
    hovertemplate: '%{customdata}<extra></extra>',
    colorscale: [[0, '#f0f0f0'], [1, COLORS.accent]],
    zmin: 0, zmax: 1,
    showscale: false,
    xgap: narrow ? 0 : 1,
    ygap: narrow ? 3 : 6,
  }];
  const layout = {
    ...BASE_LAYOUT,
    margin: { l: narrow ? 90 : 180, r: 16, t: 12, b: 40 },
    height: narrow ? 180 : 220,
    xaxis: { ...AXIS_BASE, showgrid: false, title: undefined },
    yaxis: {
      ...AXIS_BASE,
      autorange: 'reversed',
      showgrid: false,
      showline: false,
      ticks: '',
      tickfont: { family: FONT_SANS, size: narrow ? 11 : 13, color: COLORS.text },
    },
  };
  Plotly.react(wrap, data, layout, PLOT_CONFIG);
}

function renderMonthlyChart(dc) {
  const { hub, destination } = STATE;
  const wrap = document.getElementById('monthly-chart');
  const isRoute = !!(hub && destination);

  const months = MONTHS.map(m => m.slice(0, 3));
  if (isRoute) {
    const ab = monthlyDirectionPct(STATE.hub, STATE.destination);
    const ba = monthlyDirectionPct(STATE.destination, STATE.hub);
    const data = [
      bar(months, ab, `${hub} → ${destination}`, COLORS.accent, true),
      bar(months, ba, `${destination} → ${hub}`, COLORS.slate, true),
    ];
    const layout = {
      ...BASE_LAYOUT,
      barmode: 'group',
      bargap: 0.4,
      xaxis: { ...AXIS_BASE, title: undefined },
      yaxis: { ...AXIS_BASE, title: undefined, range: [0, 108], ticksuffix: '%' },
      margin: { l: 48, r: 16, t: 16, b: 56 },
      height: 300,
      legend: legendCfg(),
    };
    Plotly.react(wrap, data, layout, PLOT_CONFIG);
  } else {
    const vals = monthlyDailyAvg(dc);
    const data = [bar(months, vals, 'Avg flights / day', COLORS.text, false)];
    const layout = {
      ...BASE_LAYOUT,
      bargap: 0.5,
      xaxis: { ...AXIS_BASE, title: undefined },
      yaxis: { ...AXIS_BASE, title: undefined, rangemode: 'tozero' },
      margin: { l: 56, r: 16, t: 16, b: 40 },
      height: 300,
      showlegend: false,
    };
    Plotly.react(wrap, data, layout, PLOT_CONFIG);
  }
}

function legendCfg() {
  return {
    orientation: 'h',
    y: -0.18, x: 0, xanchor: 'left',
    bgcolor: 'rgba(0,0,0,0)',
    font: { family: FONT_MONO, size: 12, color: COLORS.textSoft },
    itemsizing: 'constant',
  };
}

function bar(x, y, name, color, asPercent) {
  return {
    type: 'bar', x, y, name,
    marker: { color },
    hovertemplate: `<b>${esc(name)}</b><br>%{x}: %{y:.1f}${asPercent ? '%' : ''}<extra></extra>`,
    cliponaxis: false,
  };
}

function monthlyDailyAvg(dc) {
  const dateCount = Object.fromEntries(dc.map(d => [d.date, d.count]));
  const ymSum = {};
  const ymDays = {};
  for (const date of DATA.dates) {
    const ym = date.slice(0, 7);
    ymSum[ym] = (ymSum[ym] || 0) + (dateCount[date] || 0);
    ymDays[ym] = (ymDays[ym] || 0) + 1;
  }
  const byMonth = Array.from({ length: 12 }, () => []);
  for (const ym of Object.keys(ymSum)) {
    const dailyAvg = ymDays[ym] > 0 ? ymSum[ym] / ymDays[ym] : 0;
    const m = parseInt(ym.slice(5), 10) - 1;
    byMonth[m].push(dailyAvg);
  }
  return byMonth.map(arr => arr.length ? arr.reduce((a, b) => a + b, 0) / arr.length : 0);
}

function monthlyDirectionPct(originName, destName) {
  const oi = DATA.airportIdx[originName];
  const di = DATA.airportIdx[destName];
  const rid = getRouteIdx(oi, di);
  const ymDays = {};
  const ymHits = {};
  for (const date of DATA.dates) {
    const ym = date.slice(0, 7);
    ymDays[ym] = (ymDays[ym] || 0) + 1;
    if (rid >= 0 && DATA.dateAvailSet[date].has(rid)) {
      ymHits[ym] = (ymHits[ym] || 0) + 1;
    }
  }
  const byMonth = Array.from({ length: 12 }, () => []);
  for (const ym of Object.keys(ymDays)) {
    const frac = (ymHits[ym] || 0) / ymDays[ym];
    const m = parseInt(ym.slice(5), 10) - 1;
    byMonth[m].push(frac);
  }
  return byMonth.map(arr => arr.length ? (arr.reduce((a, b) => a + b, 0) / arr.length) * 100 : 0);
}

function renderWeekdayChart(dc) {
  const { hub, destination } = STATE;
  const wrap = document.getElementById('weekday-chart');
  const isRoute = !!(hub && destination);

  const wdShort = WEEKDAYS.map(d => d.slice(0, 3));
  if (isRoute) {
    const ab = weekdayDirectionPct(hub, destination);
    const ba = weekdayDirectionPct(destination, hub);
    const data = [
      bar(wdShort, ab, `${hub} → ${destination}`, COLORS.accent, true),
      bar(wdShort, ba, `${destination} → ${hub}`, COLORS.slate, true),
    ];
    const layout = {
      ...BASE_LAYOUT,
      barmode: 'group',
      bargap: 0.4,
      xaxis: { ...AXIS_BASE, title: undefined },
      yaxis: { ...AXIS_BASE, title: undefined, range: [0, 108], ticksuffix: '%' },
      margin: { l: 48, r: 16, t: 16, b: 56 },
      height: 280,
      legend: legendCfg(),
    };
    Plotly.react(wrap, data, layout, PLOT_CONFIG);
  } else {
    const totalsByWd = Array.from({ length: 7 }, () => ({ sum: 0, n: 0 }));
    for (const d of dc) {
      const wd = DATA.weekdayOfDate[d.date];
      totalsByWd[wd].sum += d.count;
      totalsByWd[wd].n += 1;
    }
    const vals = totalsByWd.map(x => x.n ? x.sum / x.n : 0);
    const data = [bar(wdShort, vals, 'Avg flights', COLORS.text, false)];
    const layout = {
      ...BASE_LAYOUT,
      bargap: 0.5,
      xaxis: { ...AXIS_BASE, title: undefined },
      yaxis: { ...AXIS_BASE, title: undefined, rangemode: 'tozero' },
      margin: { l: 56, r: 16, t: 16, b: 40 },
      height: 280,
      showlegend: false,
    };
    Plotly.react(wrap, data, layout, PLOT_CONFIG);
  }
}

function weekdayDirectionPct(originName, destName) {
  const oi = DATA.airportIdx[originName];
  const di = DATA.airportIdx[destName];
  const rid = getRouteIdx(oi, di);
  const totals = Array.from({ length: 7 }, () => ({ days: 0, hits: 0 }));
  for (const date of DATA.dates) {
    const wd = DATA.weekdayOfDate[date];
    totals[wd].days += 1;
    if (rid >= 0 && DATA.dateAvailSet[date].has(rid)) totals[wd].hits += 1;
  }
  return totals.map(t => t.days ? (t.hits / t.days) * 100 : 0);
}

function renderMap() {
  const { hub, destination } = STATE;
  const card = document.getElementById('map-section');
  if (hub && destination) { card.classList.add('is-hidden'); return; }
  card.classList.remove('is-hidden');

  const wrap = document.getElementById('map-chart');
  const totalDays = DATA.dates.length;
  const points = collectMapPoints(hub, destination, totalDays);

  const grouped = groupBy(points, p => p.color);
  const traces = [];
  const orderedColors = [COLORS.other, COLORS.dest, COLORS.hub];
  const showLabel = !!(hub || destination);
  for (const color of orderedColors) {
    const group = grouped.get(color);
    if (!group || !group.length) continue;
    const isFocus = color === COLORS.hub || color === COLORS.dest;
    traces.push({
      type: 'scattermap',
      lat: group.map(p => p.lat),
      lon: group.map(p => p.lon),
      mode: showLabel && isFocus ? 'markers+text' : 'markers',
      marker: {
        size: group.map(p => isFocus ? p.size + 4 : p.size),
        color,
        opacity: isFocus ? 1 : 0.7,
      },
      text: group.map(p => p.name),
      hovertext: group.map(p => p.hover),
      hovertemplate: '%{hovertext}<extra></extra>',
      textposition: 'top center',
      textfont: { family: FONT_SANS, size: 12, color: COLORS.text },
      showlegend: false,
    });
  }

  const center = mapCenter(hub, destination);
  const layout = {
    ...BASE_LAYOUT,
    map: { style: 'carto-positron', center, zoom: center.zoom },
    margin: { l: 0, r: 0, t: 0, b: 0 },
    height: 440,
  };
  Plotly.react(wrap, traces, layout, PLOT_CONFIG);
}

function mapCenter(hub, destination) {
  const c = (name) => AIRPORT_COORDS[name];
  if (hub && c(hub)) return { lat: c(hub)[0], lon: c(hub)[1], zoom: 4 };
  if (destination && c(destination)) return { lat: c(destination)[0], lon: c(destination)[1], zoom: 4 };
  return { lat: 48, lon: 14, zoom: 3.2 };
}

function collectMapPoints(hub, destination, totalDays) {
  const out = [];
  if (hub && !destination) {
    const hi = DATA.airportIdx[hub];
    const dests = new Set();
    for (const date of DATA.dates) for (const rid of DATA.availability[date]) {
      const [o, d] = DATA.routes[rid];
      if (o === hi) dests.add(d);
    }
    pushAirport(out, hub, COLORS.hub, hubHover(hub, [...dests].map(i => DATA.airports[i]).sort()), 12);
    for (const di of dests) {
      const name = DATA.airports[di];
      const ob = routeProb(hi, di, totalDays);
      const ib = routeProb(di, hi, totalDays);
      const lines = [`<b>${esc(name)}</b>`];
      if (ob) lines.push(`From ${esc(hub)}: ${ob.pct.toFixed(1)}% (${ob.days}/${totalDays} days)`);
      if (ib) lines.push(`To ${esc(hub)}: ${ib.pct.toFixed(1)}% (${ib.days}/${totalDays} days)`);
      pushAirport(out, name, COLORS.other, lines.join('<br>'));
    }
  } else if (destination && !hub) {
    const di = DATA.airportIdx[destination];
    const origins = new Set();
    for (const date of DATA.dates) for (const rid of DATA.availability[date]) {
      const [o, d] = DATA.routes[rid];
      if (d === di) origins.add(o);
    }
    pushAirport(out, destination, COLORS.dest, destHover(destination, [...origins].map(i => DATA.airports[i]).sort()), 13);
    for (const oi of origins) {
      const name = DATA.airports[oi];
      const ib = routeProb(oi, di, totalDays);
      const ob = routeProb(di, oi, totalDays);
      const lines = [`<b>${esc(name)}</b>`];
      if (ib) lines.push(`To ${esc(destination)}: ${ib.pct.toFixed(1)}% (${ib.days}/${totalDays} days)`);
      if (ob) lines.push(`From ${esc(destination)}: ${ob.pct.toFixed(1)}% (${ob.days}/${totalDays} days)`);
      pushAirport(out, name, COLORS.other, lines.join('<br>'));
    }
  } else {
    const stats = computeAllAirportStats();
    for (const [ai, s] of stats) {
      const name = DATA.airports[ai];
      const lines = [`<b>${esc(name)}</b>`];
      if (s.outDays) lines.push(`Outbound: ${(s.outDays / totalDays * 100).toFixed(1)}% of days (${s.outRoutes.size} routes)`);
      if (s.inDays) lines.push(`Inbound: ${(s.inDays / totalDays * 100).toFixed(1)}% of days (${s.inRoutes.size} routes)`);
      pushAirport(out, name, COLORS.other, lines.join('<br>'));
    }
  }
  return out;
}

function pushAirport(out, name, color, hover, size = 9) {
  const c = AIRPORT_COORDS[name];
  if (!c) return;
  out.push({ name, lat: c[0], lon: c[1], color, hover, size });
}

function hubHover(hub, destinations) {
  const dl = formatList(destinations.map(esc), 12);
  return `<b>${esc(hub)}</b> (Hub)<br>Destinations: ${destinations.length}<br>${dl}`;
}

function destHover(dest, origins) {
  const dl = formatList(origins.map(esc), 12);
  return `<b>${esc(dest)}</b> (Destination)<br>Origins: ${origins.length}<br>${dl}`;
}

function formatList(items, max) {
  if (items.length <= max) return items.join(', ');
  return items.slice(0, max).join(', ') + `, … (+${items.length - max} more)`;
}

function routeProb(originIdx, destIdx, totalDays) {
  const rid = getRouteIdx(originIdx, destIdx);
  if (rid < 0) return null;
  let days = 0;
  for (const date of DATA.dates) if (DATA.dateAvailSet[date].has(rid)) days++;
  if (!days) return null;
  return { days, pct: (days / totalDays) * 100 };
}

function computeAllAirportStats() {
  const stats = new Map();
  const get = (ai) => {
    let s = stats.get(ai);
    if (!s) { s = { outDays: 0, inDays: 0, outRoutes: new Set(), inRoutes: new Set() }; stats.set(ai, s); }
    return s;
  };
  for (const date of DATA.dates) {
    const seenOut = new Set();
    const seenIn = new Set();
    for (const rid of DATA.availability[date]) {
      const [o, d] = DATA.routes[rid];
      get(o).outRoutes.add(rid);
      get(d).inRoutes.add(rid);
      seenOut.add(o);
      seenIn.add(d);
    }
    for (const o of seenOut) get(o).outDays++;
    for (const d of seenIn) get(d).inDays++;
  }
  return stats;
}

function groupBy(items, fn) {
  const m = new Map();
  for (const x of items) {
    const k = fn(x);
    if (!m.has(k)) m.set(k, []);
    m.get(k).push(x);
  }
  return m;
}

function esc(s) {
  return String(s).replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
}

window.addEventListener('DOMContentLoaded', init);

let resizeTimer;
window.addEventListener('resize', () => {
  clearTimeout(resizeTimer);
  resizeTimer = setTimeout(() => { if (DATA) render(); }, 200);
});
