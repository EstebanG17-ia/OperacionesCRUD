// Confirmacion antes de eliminar un producto
document.querySelectorAll('.form-eliminar').forEach((form) => {
    form.addEventListener('submit', (event) => {
        const confirmar = confirm(
            '¿Estás seguro de que deseas eliminar este producto?'
        );

        if (!confirmar) {
            event.preventDefault();
        }
    });
});

// Validación adicional del formulario
const formulario = document.getElementById('formProducto');

if (formulario) {
    formulario.addEventListener('submit', (event) => {
        const nombre = document.getElementById('nombre').value.trim();
        const precio = document.getElementById('precio').value;
        const stock = document.getElementById('stock').value;

        if (
            nombre === '' ||
            precio === '' ||
            stock === '' ||
            Number(precio) < 0 ||
            Number(stock) < 0 ||
            !Number.isInteger(Number(stock))
        ) {
            event.preventDefault();
            alert('Verifica que todos los campos sean correctos.');
        }
    });
}