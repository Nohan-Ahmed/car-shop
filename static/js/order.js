document.addEventListener('DOMContentLoaded', function() {
    const quantityInput = document.getElementById('id_quantity');
    const totalPriceElement = document.getElementById('total-price');
    const pricePerUnit = parseFloat(totalPriceElement.textContent.replace(/[^0-9.-]+/g, ""));  // Get the initial price

    // Set default value for quantity
    quantityInput.value = 1;

    function updateTotalPrice() {
        let quantity = parseInt(quantityInput.value) || 0;
        let totalPrice = quantity * pricePerUnit;
        totalPriceElement.textContent = totalPrice.toLocaleString();
    }

    quantityInput.addEventListener('input', updateTotalPrice);

    // Initialize total price on page load
    updateTotalPrice();
});
