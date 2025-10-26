import { defineConfig } from "vite";

export default defineConfig({
    build: {
        outDir: "./static/dist",
        emptyOutDir: true,
        manifest: true,
        rollupOptions: {
            input: {
                main: "./static/scss/main.scss",
                main_js: "./static/js/main.js",
            },
        },
    },
});