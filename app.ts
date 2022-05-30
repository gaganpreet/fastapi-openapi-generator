import { defaultApi } from "./env";

window.onload = async () => {
  const node = document.querySelector("#api-result");
  const items = await defaultApi.getItems();

  node.innerHTML = `<pre>${JSON.stringify(items.data, null, 4)}</pre>`;
};
