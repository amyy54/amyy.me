/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
        "src/**/*.{html,js}"
    ],
    theme: {
        extend: {
            colors: {
                'accent': '#bb8aff',
                'bg-primary': '#25222a',
                'bg-secondary': '#282828',
                'language-python': '#3572a5',
                'language-rust': '#dea584',
                'language-go': '#00add8',
                'language-typescript': '#3178c6',
                'language-csharp': '#178600',
                'language-cplusplus': '#f34b7d'
            }
        },
    },
    plugins: [],
}
