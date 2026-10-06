export function init() {
  const sidebar = document.getElementById("app_sidebar");

  document.querySelectorAll("[data-sidebar-toggle]").forEach((btn) => {
    btn.addEventListener("click", () => sidebar?.toggle?.());
  });

  document.addEventListener("keydown", (e) => {
    if (e.key !== "/" || e.ctrlKey || e.metaKey || e.altKey) return;
    if (e.target.matches("input, textarea, select, [contenteditable]")) return;
    e.preventDefault();
    document.getElementById("sidebar_search")?.focus();
  });
}