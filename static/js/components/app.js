import { init as initSidebar } from "./global/sidebar.js";

const pages = {
  files_browser: () => import("./pages/files_browser.js"),
  telegram_setup: () => import("./pages/telegram_setup.js"),
};

export async function initApp() {
  initSidebar();
  const load = pages[document.body.dataset.page];
  if (!load) return;
  const mod = await load();
  if (typeof mod.init === "function") mod.init();
}