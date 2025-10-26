import { defineConfig } from "vite";

export default defineConfig({
    // Мы убираем 'root', чтобы Vite работал из корня проекта. Это ключевое исправление.
    build: {
        // Путь для скомпилированных файлов, относительно корня проекта
        outDir: "./static/dist",
        emptyOutDir: true,
        manifest: true,
        rollupOptions: {
            // Пути к исходникам, относительно корня проекта
            input: {
                main: "./static/scss/main.scss",
                main_js: "./static/js/main.js",
            },
        },
    },
});