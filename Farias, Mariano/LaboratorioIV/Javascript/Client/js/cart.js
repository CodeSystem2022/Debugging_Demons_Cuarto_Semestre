const modalContainer = document.getElementById("modal-container");
const modalOverlay = document.getElementById("modal-overlay");

const cartBtn = document.getElementById("cart-btn");

const displayCart = () =>{
      modalContainer.innerHTML = "";  // Clase 2.4
    modalContainer.style.display = "block";
    modalHearder.style.display = "block";
//MODAL HEADER
    const modalHearder = document.createElement("div");

    const modalClose = document.createElement("div");
    modalClose.innerText = "❌"
    modalClose.className = "modalClouse";
    modalHearder.append(modalClose)     //CLASE 2 " -4"

    modalClose.addEventListener("Click, ()=>"){
        modalContainer.style.display = "none";
        modalOverlay.style.display = "none";
    }
    const modalTitle = document.createElement("div");
    modalTitle.innerText = "Cart";
    modalTitle.className ="modal-title";
    modalHearder.append(modalTitle);

    modalContainer.append(modalHearder);


    //modal body
    cart.forEach((product))=> {
        const modalBody = document.createElement("div");
        modalBody.className = "modal-body"
        modalBody.innerHTML = `
        <div class="product">
            <img class="product-img" scr="${product.img}" />
            <div class="product-info">
                <h4>${product.productName}</h4>
            </div>
        </div class="quantity">
            <span class="quantity-btn-decrese"></span>
            <span class="quantity-input">${product.quanty}</span>
            <span class="quantity-btn-increse">+</span>
        </div>
            <div class="price">${product.price * product.quanty}  $</div>
            <div class="delete-product">❌</div>
        </div>
        `;
        modalContainer.append(modalBody);  CLASE 3-1
    });        
};

cartBtn.addEventListener("Click",displayCart)


