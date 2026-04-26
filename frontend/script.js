const API_BASE_URL = "http://127.0.0.1:5000/api/v1/indexer";

const form = document.getElementById("search-form");
const meta = document.getElementById("meta");
const resultsContainer = document.getElementById("results");

function escapeHtml(str = "") {
  return str
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#039;");
}

function renderResults(data) {
  meta.innerHTML = `<p><strong>Final query:</strong> ${escapeHtml(data.query || "")}</p>`;
  resultsContainer.innerHTML = "";

  if (!data.query_results?.length) {
    resultsContainer.innerHTML = "<p>No results returned.</p>";
    return;
  }

  const fragment = document.createDocumentFragment();

  data.query_results.forEach((item) => {
    const card = document.createElement("article");
    card.className = "result-card";

    const title = document.createElement("h3");
    title.textContent = item.title || "Untitled";

    const link = document.createElement("a");
    const url = Array.isArray(item.url) ? item.url[0] : item.url;
    link.href = url || "#";
    link.textContent = url || "(missing URL)";
    link.target = "_blank";
    link.rel = "noopener noreferrer";

    const snippet = document.createElement("p");
    const content = Array.isArray(item.content) ? item.content[0] : item.content;
    snippet.textContent = (content || "").slice(0, 260);

    card.append(title, link, snippet);
    fragment.append(card);
  });

  resultsContainer.append(fragment);
}

form.addEventListener("submit", async (event) => {
  event.preventDefault();

  const query = document.getElementById("query-input").value.trim();
  const type = document.querySelector('input[name="type"]:checked').value;

  try {
    const url = new URL(API_BASE_URL);
    url.searchParams.set("query", query);
    url.searchParams.set("type", type);

    const response = await fetch(url);
    if (!response.ok) throw new Error(`Request failed: ${response.status}`);

    const data = await response.json();
    renderResults(data);
  } catch (error) {
    meta.innerHTML = `<p class="error">${escapeHtml(error.message)}</p>`;
    resultsContainer.innerHTML = "";
  }
});
