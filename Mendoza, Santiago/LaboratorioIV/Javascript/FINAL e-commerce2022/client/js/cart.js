// const { error } = require("console");
// const e = require("express");

const modalContainer = document.getElementById("modal-container"); 
const modalOverlay = document.getElementById("modal-overlay");

const cartCounter = document.getElementById("cart-counter")
const cartBtn = document.getElementById("cart-btn");

const displayCart = () =>{
    modalContainer.innerHTML = "";
    modalContainer.style.display = "block";
    modalOverlay.style.display = "block";

    // modal header
    const modalHeader = document.createElement("div");

    
    const modalClose = document.createElement("div");
    modalClose.innerText = "❌";
    modalClose.className = "modal-close";
    modalHeader.append(modalClose);

    modalClose.addEventListener("click", ()=>{
        modalContainer.style.display = "none"
        modalOverlay.style.display = "none";
    
    })

    const modalTittle = document.createElement("div");
    modalTittle.innerText = "cart";
    modalTittle.className = "modal-tittle";
    modalHeader.append(modalTittle);


    modalContainer.append(modalHeader);

// Modal body
if(cart.length > 0){
cart.forEach((product) => {
    const modalBody = document.createElement("div");

    modalBody.className = "modal-body";
    modalBody.innerHTML = `
    <div class="product">

        <img class="product-img" src="${product.img}"/>
        <div class="product-info">
            <h4>${product.productName}
            </h4>
        </div>

        <div class="quantity">

        <span class="quantity-btn-decrase">-</span>

        <span class="quantity-input">${product.quanty}
        </span>
        
        <span class="quantity-btn-increse">+</span>

        </div>
        <div class="price">${product.price * product.quanty} $
        </div>
        <div class="delete-product">❌</div>
    </div>
    `;
    modalContainer.append(modalBody);

    const decrase = modalBody.querySelector(".quantity-btn-decrase");
    decrase.addEventListener("click",()=>{
        if(product.quanty != 1){
            product.quanty--;
            displayCart();
        }
        displayCartCounter();
    })

    const increse = modalBody.querySelector(".quantity-btn-increse");
    increse.addEventListener("click",()=>{
            product.quanty++;
            displayCart();
            displayCartCounter(); 
    })

    const deleteProduct = modalBody.querySelector(".delete-product");

    deleteProduct.addEventListener("click",() =>{
        deleteCartProduct(product.id);
    });
});


// Modal footer
const total = cart.reduce((acc,el) => acc + el.price * el.quanty, 0);

const modalFooter = document.createElement("div");
modalFooter.className = "modal-footer";
modalFooter.innerHTML = `
<div class="total-price">
Total: $ ${total}
</div>
<button class="btn-primary" id="checkout-btn">go to checkout</button>
<div id="button-checkout"></div>

`;
modalContainer.append(modalFooter);
// mp
const mercadopago = new MercadoPago("public_key",{
    locale: "es-AR", // The most common are: 'pt-BR', 'es-AR' and 'en-US'
});

const checkoutButton = modalFooter.querySelector("#checkout-btn");
checkoutButton.addEventListener("click", function(){
    checkoutButton.remove();

    const orderData = {
        quantity: 1,
        description: "Compra ecommerce",
        price: total,   
    };

    fetch("http://localhost:8080/create_preference",{
        method: "POST",
        headers:{
            "Content-Type":"application/json",
        },
        body: JSON.stringify(orderData),
    })
    .then(function(response){
        return response.json();
    })
    .then(function(preference){
        createCheckoutButton(preference.id);
    })
    .catch(function(){
        alert("Unexpected error");
    });
});

function createCheckoutButton(preferenceId){
    // Initialize the checkout

    const bricksBuilder = mercadopago.bricks();

    const renderComponent = async (bricksBuilder) =>{
        // if (windows.checkoutButton) checkoutButton.unmount();

        await bricksBuilder.create(
            "waller",
            "button-checkout", // class / id where the payment button will be displayed
            {
                initialization:{
                    preferenceId: preferenceId,

                },
                callbacks:{
                    onError: (error) => console.error(error),
                    onReady: () =>{},
                },
            }
        );
    };
    window.checkoutButton = renderComponent(bricksBuilder);
}

}else{
    const modalText = document.createElement("h2");
    modalText.className = ("modal-body");
    modalText.innerText = ("Your cart is empty!");
    modalContainer.append(modalText);
}
};

cartBtn.addEventListener("click", displayCart);


const deleteCartProduct = (id) => {
    const foundId = cart.findIndex((element)=> element.id === id);
    console.log(foundId)
    cart.splice(foundId,1);
    displayCart();
    displayCartCounter();
};

const displayCartCounter = () => {
    const cartLength = cart.reduce((acc,el) => acc + el.quanty, 0);

    if(cartLength > 0){
        cartCounter.style.display = "block";
        cartCounter.innerText = cartLength;
    }else{
        cart.style.display = "none";
    }


};