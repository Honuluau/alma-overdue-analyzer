document.addEventListener('DOMContentLoaded', () => {
    const btn = document.getElementById('update_button');
    btn.addEventListener('click', () => {
        // Call Python function exposed via js_api
        pywebview.api.change_text();
    });
});