/* ===============CLASE 14 - LUNES-16/08/2023=============== */

const shopContent = document.getElementById("shopContent");

productos.forEach((product) => {
    const content = document.createElement("div");
    content.innerHTML = `
    <img src="${product.img}">
    <h3>${product.productName}</h3>
    <p>${product.price} $</p>
    `;
    shopContent.append(content);
});
