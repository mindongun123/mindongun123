const GAMES = [
  { id: "matchkit", name: "Match Kit", cat: "Match-3", img: "assets/games/matchkit.png", url: "https://github.com/mindongun123/MJGame_APK/releases/tag/MatchKit", apk: true },
  { id: "merge", name: "Merge Restaurant", cat: "Merge", img: "https://github.com/mindongun123/MergeRestaurant/blob/main/MJGame-MergeRestaurant_2.gif?raw=true", url: "https://github.com/mindongun123/MergeRestaurant" },
  { id: "tapmusic", name: "Tap Music", cat: "Music / Tap", img: "assets/games/tapmusic.png", url: "https://github.com/mindongun123/2024GB" },
  { id: "block", name: "Block", cat: "Puzzle", img: "assets/games/block.png", url: "https://github.com/mindongun123/MJGame_APK/releases/tag/MJGame_Block", apk: true },
  { id: "emoji", name: "Emoji", cat: "Puzzle", img: "assets/games/emoji.png", url: "https://github.com/mindongun123/MJGame_APK/releases/tag/%23mjgameEmoji", apk: true },
  { id: "runner", name: "Runner 3D", cat: "Hyper-casual", img: "assets/games/runner3d.png", url: "https://github.com/mindongun123" },
  { id: "connect", name: "Connect", cat: "Puzzle", img: "assets/games/gconnect.png", url: "https://github.com/mindongun123" },
  { id: "jump", name: "Jump Adventure", cat: "Casual", img: "assets/games/mario.png", url: "https://github.com/mindongun123/MJGame_APK/releases/tag/MJGame_Mario", apk: true }
];

const $ = (s, el = document) => el.querySelector(s);
const $$ = (s, el = document) => [...el.querySelectorAll(s)];
const store = {
  get(k) { try { return localStorage.getItem(k); } catch (e) { return null; } },
  set(k, v) { try { localStorage.setItem(k, v); } catch (e) {} }
};

let dict = {};
let filter = "all";
const t = (path) => path.split(".").reduce((o, k) => (o ? o[k] : undefined), dict) ?? "";

/* ---------- i18n ---------- */
async function setLang(lang) {
  try {
    dict = await (await fetch(`i18n/${lang}.json`)).json();
  } catch (e) {
    return;
  }
  document.documentElement.lang = lang;
  store.set("lang", lang);
  $("#lang-toggle").textContent = lang === "en" ? "VI" : "EN";
  $$("[data-i18n]").forEach((el) => (el.textContent = t(el.dataset.i18n)));
  $$("[data-i18n-html]").forEach((el) => (el.innerHTML = t(el.dataset.i18nHtml)));
  $$("[data-i18n-ph]").forEach((el) => (el.placeholder = t(el.dataset.i18nPh)));
  renderFilters();
  renderGames();
  renderLists();
}

/* ---------- Games ---------- */
function renderFilters() {
  const cats = ["all", ...new Set(GAMES.map((g) => g.cat))];
  $("#filters").innerHTML = cats
    .map((c) => `<button class="chip ${c === filter ? "active" : ""}" data-cat="${c}">${c === "all" ? t("games.all") : c}</button>`)
    .join("");
}

function renderGames() {
  const list = GAMES.filter((g) => filter === "all" || g.cat === filter);
  $("#game-grid").innerHTML = list
    .map(
      (g) => `<article class="game" data-id="${g.id}" tabindex="0">
        <img src="${g.img}" alt="${g.name}" loading="lazy" />
        <div class="info"><h3>${g.name}</h3>
          <p class="tags"><span class="tag">${g.cat}</span>${g.apk ? '<span class="tag sand">Android</span>' : ""}</p>
        </div></article>`
    )
    .join("");
  $$(".game").forEach(tilt);
}

function openGame(id) {
  const g = GAMES.find((x) => x.id === id);
  if (!g) return;
  $("#modal-img").src = g.img;
  $("#modal-img").alt = g.name;
  $("#modal-title").textContent = g.name;
  $("#modal-tags").innerHTML = `<span class="tag">${g.cat}</span>${g.apk ? '<span class="tag sand">Android</span>' : ""}`;
  $("#modal-desc").textContent = t(`games.items.${g.id}`);
  $("#modal-link").href = g.url;
  $("#modal-link").textContent = g.apk ? t("games.download") : t("games.repo");
  $("#game-modal").showModal();
}

function tilt(el) {
  if (matchMedia("(hover: none)").matches) return;
  el.addEventListener("mousemove", (e) => {
    const r = el.getBoundingClientRect();
    const x = (e.clientX - r.left) / r.width - 0.5;
    const y = (e.clientY - r.top) / r.height - 0.5;
    el.style.transform = `perspective(700px) rotateY(${x * 10}deg) rotateX(${-y * 10}deg) translateY(-4px)`;
  });
  el.addEventListener("mouseleave", () => (el.style.transform = ""));
}

/* ---------- Lists ---------- */
function renderLists() {
  $("#services-grid").innerHTML = (t("services.items") || [])
    .map((s) => `<div class="card"><div class="ico">${s.ico}</div><h3>${s.t}</h3><p>${s.d}</p></div>`)
    .join("");
  $("#process").innerHTML = (t("process.items") || []).map((p) => `<li><b>${p.t}</b><span>${p.d}</span></li>`).join("");
  $("#timeline").innerHTML = (t("about.timeline") || []).map((i) => `<li><b>${i.y}</b>${i.t}</li>`).join("");
}

/* ---------- Theme ---------- */
function currentTheme() {
  return document.documentElement.dataset.theme || (matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light");
}
function syncThemeIcon() {
  $("#theme-toggle").textContent = currentTheme() === "dark" ? "☀️" : "🌙";
}

/* ---------- Effects ---------- */
function countUp(el) {
  const end = +el.dataset.count;
  const start = performance.now();
  const step = (now) => {
    const p = Math.min((now - start) / 1200, 1);
    el.textContent = Math.round(end * (1 - Math.pow(1 - p, 3)));
    if (p < 1) requestAnimationFrame(step);
  };
  requestAnimationFrame(step);
}

const io = new IntersectionObserver(
  (entries) =>
    entries.forEach((e) => {
      if (!e.isIntersecting) return;
      e.target.classList.add("in");
      $$("[data-count]", e.target).forEach(countUp);
      io.unobserve(e.target);
    }),
  { threshold: 0.15 }
);

/* ---------- Init ---------- */
document.addEventListener("DOMContentLoaded", () => {
  $("#year").textContent = new Date().getFullYear();
  $$(".reveal").forEach((el) => io.observe(el));
  syncThemeIcon();

  const saved = store.get("lang");
  setLang(saved || (navigator.language.toLowerCase().startsWith("vi") ? "vi" : "en"));

  $("#lang-toggle").addEventListener("click", () => setLang(document.documentElement.lang === "en" ? "vi" : "en"));
  $("#theme-toggle").addEventListener("click", () => {
    const next = currentTheme() === "dark" ? "light" : "dark";
    document.documentElement.dataset.theme = next;
    store.set("theme", next);
    syncThemeIcon();
  });
  $("#menu-btn").addEventListener("click", () => $("#links").classList.toggle("open"));
  $$("#links a").forEach((a) => a.addEventListener("click", () => $("#links").classList.remove("open")));

  $("#filters").addEventListener("click", (e) => {
    const b = e.target.closest("[data-cat]");
    if (!b) return;
    filter = b.dataset.cat;
    renderFilters();
    renderGames();
  });
  $("#game-grid").addEventListener("click", (e) => {
    const card = e.target.closest(".game");
    if (card) openGame(card.dataset.id);
  });
  $("#game-grid").addEventListener("keydown", (e) => {
    const card = e.target.closest(".game");
    if (card && e.key === "Enter") openGame(card.dataset.id);
  });
  $("#modal-close").addEventListener("click", () => $("#game-modal").close());
  $("#game-modal").addEventListener("click", (e) => {
    if (e.target.id === "game-modal") e.target.close();
  });
});
