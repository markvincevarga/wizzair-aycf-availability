import { defineConfig } from "cf/config";

export default defineConfig({
  worker: {
    "name": "aycf",
    "domains": ["aycf.mvarga.dev"],
    "compatibilityDate": "2026-11-04",
    "observability": {
      "enabled": true
    }
  }
});
