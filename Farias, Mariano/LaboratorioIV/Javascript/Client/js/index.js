const shopContent = document.getElementById("shopContent");

productos.forEach((product) =>{
    const content = document.createElement("div");
    content.innerHTML = `
    <img scr="${product.img}">
    <h3>${product.peoductName}</h3>
    <p>${product.price} </p>
    `;
    shopContent.append(content);
    
    const buyButton = document.createElement("button");
    buyButton.innerText = "Comprar";

    content.append(buyButton);

    buyButton.addEventListener("clik", ()=>{
        cart.push({
            id: product.id,
            productName: product.productName,
            price: product.price,
            quanty: product.quanty,
            img: product.img,
        })
        console.log(cart)
    })

});