<template>
    <div class="cilinders-product-page">
        <div class="row justify-content-center">
            <div class="col-10">
                <div class="breadcrumbs">
                    <ul class="breadcrumb">
                        <li><a href="/"><font-awesome-icon icon="home" /></a></li>
                        <li><a href="#">{selected moped}</a></li>
                        <li><a href="/motordelen">Motordelen</a></li>
                        <li>Cilinders</li>
                    </ul>
                    <hr class="breadcrumbs-line">
                </div>
                <div class="row products-row">

                    <div class="col-md-3 col-sm-6" v-for="product in latestProducts" :key="product.id">
                        <div class="product-grid">
                            <div class="product-image">
                                <a href="#" class="image">
                                    <img class="img-1" v-bind:src="product.get_thumbnail">
                                </a>
                                <span class="product-brand-label">Motoforce</span>
                            </div>
                            <div class="product-content">
                                <ul class="rating">
                                    <li class=""><font-awesome-icon icon="star"/></li>
                                    <li class=""><font-awesome-icon icon="star"/></li>
                                    <li class=""><font-awesome-icon icon="star"/></li>
                                    <li class=""><font-awesome-icon icon="star"/></li>
                                    <li class="disable"><font-awesome-icon icon="star"/></li>
                                    <li class="disable">(1 reviews)</li>
                                </ul>
                                <div class="product-title">
                                    <div class="product-title">
                                    <h3 class="title"><a href="#">{{ product.name }}</a></h3>
                                </div>
                                </div>
                                <div class="price-stock">
                                    <div class="row">
                                        <div class="price col"><p>{{product.price}} €</p></div>
                                        <div class="stock col g-0">
                                            <hr class="stock-line">
                                            <p>Op voorraad</p>
                                        </div>
                                    </div>
                                </div>
                                <div class="shoppingcart-button"><router-link v-bind:to="product.get_absolute_url">
                                    <button type="button" class="shoppingcart-buttonbutton btn btn-success">
                                            <span class="button-cart-icon"><font-awesome-icon icon="shopping-cart" :style="{ color: 'white', width: '18px', height: '18px'}" /></span>
                                            <span class="button-cart-text">In winkelwagen</span>
                                    </button></router-link>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- <div class="col-md-3 col-sm-6">
                        <div class="product-grid">
                            <div class="product-image">
                                <a href="#" class="image">
                                    <img class="img-1" src="img/icon/cilinderkitproduct2.jpg">
                                </a>
                                <span class="product-brand-label">Motoforce</span>
                            </div>
                            <div class="product-content">
                                <ul class="rating">
                                    <li class=""></li>
                                    <li class=""></li>
                                    <li class=""></li>
                                    <li class=" disable"></li>
                                    <li class=" disable"></li>
                                    <li class="disable"></li>
                                </ul>
                                <div class="product-title">
                                    <div class="product-title">
                                    <h3 class="title"><a href="#">Cylinder Kit Black Series 50cc Minarelli horizontal LC (Yamaha Aerox)</a></h3>
                                </div>
                                </div>
                                <div class="price-stock">
                                    <div class="row">
                                        <div class="price col"><p>14,50 €</p></div>
                                        <div class="stock col g-0">
                                            <hr class="stock-line">
                                            <p>Op voorraad</p>
                                        </div>
                                    </div>
                                </div>
                                <div class="shoppingcart-button">
                                    <button type="button" class="shoppingcart-buttonbutton btn btn-success">
                                        <span class="button-cart-icon"><font-awesome-icon icon="shopping-cart" :style="{ color: 'white', width: '18px', height: '18px'}" /></span>
                                        <span class="button-cart-text">In winkelwagen</span>
                                    </button>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="col-md-3 col-sm-6">
                        <div class="product-grid">
                            <div class="product-image">
                                <a href="#" class="image">
                                    <img class="img-1" src="img/icon/Zuigerproduct.jpg">
                                </a>
                                <span class="product-brand-label">Motoforce</span>
                                <ul class="product-links">
                                    <li><a href="#"><i class="fa fa-heart"></i></a></li>
                                    <li><a href="#"><i class="fa fa-random"></i></a></li>
                                    <li><a href="#"><i class="fa fa-shopping-cart"></i></a></li>
                                </ul>
                                <a href="#" class="product-view"><i class="fa fa-search"></i></a>
                            </div>
                            <div class="product-content">
                                <ul class="rating">
                                    <li class=""><font-awesome-icon icon="star"/></li>
                                    <li class=""><font-awesome-icon icon="star"/></li>
                                    <li class=""><font-awesome-icon icon="star"/></li>
                                    <li class=""><font-awesome-icon icon="star"/></li>
                                    <li class="disable"><font-awesome-icon icon="star"/></li>
                                    <li class="disable">(1 reviews)</li>
                                </ul>
                                <div class="product-title">
                                    <h3 class="title"><a href="#">Piston original 50cc Minarelli horizontal / vertical</a></h3>
                                </div>
                                <div class="price-stock">
                                    <div class="row">
                                        <div class="price col"><p>14,50 €</p></div>
                                        <div class="stock col g-0">
                                            <hr class="stock-line">
                                            <p>Op voorraad</p>
                                        </div>
                                    </div>
                                </div>
                                <div class="shoppingcart-button">
                                    <button type="button" class="shoppingcart-buttonbutton btn btn-success">
                                        <span class="button-cart-icon"><font-awesome-icon icon="shopping-cart" :style="{ color: 'white', width: '18px', height: '18px'}" /></span>
                                        <span class="button-cart-text">In winkelwagen</span>
                                    </button>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="col-md-3 col-sm-6">
                        <div class="product-grid">
                            <div class="product-image">
                                <a href="#" class="image">
                                    <img class="img-1" src="img/icon/zuigerverenproduct.jpg">
                                </a>
                                <span class="product-brand-label">Motoforce</span>
                            </div>
                            <div class="product-content">
                                <ul class="rating">
                                    <li class=""></li>
                                    <li class=""></li>
                                    <li class=""></li>
                                    <li class=" disable"></li>
                                    <li class=" disable"></li>
                                    <li class="disable"></li>
                                </ul>
                                <div class="product-title">
                                    <h3 class="title"><a href="#">Cylinder Kit Black Series 50cc Minarelli horizontal LC (Yamaha Aerox)</a></h3>
                                </div>
                                <div class="price-stock">
                                    <div class="row">
                                        <div class="price col"><p>14,50 €</p></div>
                                        <div class="stock col g-0">
                                            <hr class="stock-line">
                                            <p>Op voorraad</p>
                                        </div>
                                    </div>
                                </div>
                                <div class="shoppingcart-button">
                                    <button type="button" class="shoppingcart-buttonbutton btn btn-success">
                                        <span class="button-cart-icon"><font-awesome-icon icon="shopping-cart" :style="{ color: 'white', width: '18px', height: '18px'}" /></span>
                                        <span class="button-cart-text">In winkelwagen</span>
                                    </button>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="row products-row">
                    <div class="col-md-3 col-sm-6">
                        <div class="product-grid">
                            <div class="product-image">
                                <a href="#" class="image">
                                    <img class="img-1" src="img/icon/Zuigerproduct.jpg">
                                </a>
                                <span class="product-brand-label">Motoforce</span>
                                <ul class="product-links">
                                    <li><a href="#"><i class="fa fa-heart"></i></a></li>
                                    <li><a href="#"><i class="fa fa-random"></i></a></li>
                                    <li><a href="#"><i class="fa fa-shopping-cart"></i></a></li>
                                </ul>
                                <a href="#" class="product-view"><i class="fa fa-search"></i></a>
                            </div>
                            <div class="product-content">
                                <ul class="rating">
                                    <li class=""><font-awesome-icon icon="star"/></li>
                                    <li class=""><font-awesome-icon icon="star"/></li>
                                    <li class=""><font-awesome-icon icon="star"/></li>
                                    <li class=""><font-awesome-icon icon="star"/></li>
                                    <li class="disable"><font-awesome-icon icon="star"/></li>
                                    <li class="disable">(1 reviews)</li>
                                </ul>
                                <div class="product-title">
                                    <h3 class="title"><a href="#">Piston original 50cc Minarelli horizontal / vertical</a></h3>
                                </div>
                                <div class="price-stock">
                                    <div class="row">
                                        <div class="price col"><p>14,50 €</p></div>
                                        <div class="stock col g-0">
                                            <hr class="stock-line">
                                            <p>Op voorraad</p>
                                        </div>
                                    </div>
                                </div>
                                <div class="shoppingcart-button">
                                    <button type="button" class="shoppingcart-buttonbutton btn btn-success">
                                        <span class="button-cart-icon"><font-awesome-icon icon="shopping-cart" :style="{ color: 'white', width: '18px', height: '18px'}" /></span>
                                        <span class="button-cart-text">In winkelwagen</span>
                                    </button>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="col-md-3 col-sm-6">
                        <div class="product-grid">
                            <div class="product-image">
                                <a href="#" class="image">
                                    <img class="img-1" src="img/icon/cilinderkitproduct2.jpg">
                                </a>
                                <span class="product-brand-label">Motoforce</span>
                            </div>
                            <div class="product-content">
                                <ul class="rating">
                                    <li class=""></li>
                                    <li class=""></li>
                                    <li class=""></li>
                                    <li class=" disable"></li>
                                    <li class=" disable"></li>
                                    <li class="disable"></li>
                                </ul>
                                <div class="product-title">
                                    <h3 class="title"><a href="#">Cylinder Kit Black Series 50cc Minarelli horizontal LC (Yamaha Aerox)</a></h3>
                                </div>
                                <div class="price-stock">
                                    <div class="row">
                                        <div class="price col"><p>14,50 €</p></div>
                                        <div class="stock col g-0">
                                            <hr class="stock-line">
                                            <p>Op voorraad</p>
                                        </div>
                                    </div>
                                </div>
                                <div class="shoppingcart-button">
                                    <button type="button" class="shoppingcart-buttonbutton btn btn-success">
                                        <span class="button-cart-icon"><font-awesome-icon icon="shopping-cart" :style="{ color: 'white', width: '18px', height: '18px'}" /></span>
                                        <span class="button-cart-text">In winkelwagen</span>
                                    </button>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="col-md-3 col-sm-6">
                        <div class="product-grid">
                            <div class="product-image">
                                <a href="#" class="image">
                                    <img class="img-1" src="img/icon/Zuigerproduct.jpg">
                                </a>
                                <span class="product-brand-label">Motoforce</span>
                                <ul class="product-links">
                                    <li><a href="#"><i class="fa fa-heart"></i></a></li>
                                    <li><a href="#"><i class="fa fa-random"></i></a></li>
                                    <li><a href="#"><i class="fa fa-shopping-cart"></i></a></li>
                                </ul>
                                <a href="#" class="product-view"><i class="fa fa-search"></i></a>
                            </div>
                            <div class="product-content">
                                <ul class="rating">
                                    <li class=""><font-awesome-icon icon="star"/></li>
                                    <li class=""><font-awesome-icon icon="star"/></li>
                                    <li class=""><font-awesome-icon icon="star"/></li>
                                    <li class=""><font-awesome-icon icon="star"/></li>
                                    <li class="disable"><font-awesome-icon icon="star"/></li>
                                    <li class="disable">(1 reviews)</li>
                                </ul>
                                <div class="product-title">
                                    <h3 class="title"><a href="#">Piston original 50cc Minarelli horizontal / vertical</a></h3>
                                </div>
                                <div class="price-stock">
                                    <div class="row">
                                        <div class="price col"><p>14,50 €</p></div>
                                        <div class="stock col g-0">
                                            <hr class="stock-line">
                                            <p>Op voorraad</p>
                                        </div>
                                    </div>
                                </div>
                                <div class="shoppingcart-button">
                                    <button type="button" class="shoppingcart-buttonbutton btn btn-success">
                                        <span class="button-cart-icon"><font-awesome-icon icon="shopping-cart" :style="{ color: 'white', width: '18px', height: '18px'}" /></span>
                                        <span class="button-cart-text">In winkelwagen</span>
                                    </button>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="col-md-3 col-sm-6">
                        <div class="product-grid">
                            <div class="product-image">
                                <a href="#" class="image">
                                    <img class="img-1" src="img/icon/cilinderkitproduct2.jpg">
                                </a>
                                <span class="product-brand-label">Motoforce</span>
                            </div>
                            <div class="product-content">
                                <ul class="rating">
                                    <li class=""></li>
                                    <li class=""></li>
                                    <li class=""></li>
                                    <li class=" disable"></li>
                                    <li class=" disable"></li>
                                    <li class="disable"></li>
                                </ul>
                                <div class="product-title">
                                    <h3 class="title"><a href="#">Cylinder Kit Black Series 50cc Minarelli horizontal LC (Yamaha Aerox)</a></h3>
                                </div>
                                <div class="price-stock">
                                    <div class="row">
                                        <div class="price col"><p>14,50 €</p></div>
                                        <div class="stock col g-0">
                                            <hr class="stock-line">
                                            <p>Op voorraad</p>
                                        </div>
                                    </div>
                                </div>
                                <div class="shoppingcart-button">
                                    <button type="button" class="shoppingcart-buttonbutton btn btn-success">
                                        <span class="button-cart-icon"><font-awesome-icon icon="shopping-cart" :style="{ color: 'white', width: '18px', height: '18px'}" /></span>
                                        <span class="button-cart-text">In winkelwagen</span>
                                    </button>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>                                 -->
                <!-- <div class="products">
                    <div class="row g-0">
                        <div class="total-product-1 col-3">
                            <div class="padding-product">
                                <div class="product-image-row row">
                                    <img class="img-fluid" src="img/icon/Zuigerproduct.jpg" alt="product" max-width="100%" height="auto">
                                </div>
                            </div>
                        </div>
                        <div class="total-product-2 col-3">
                            <p>test</p>
                        </div>
                        <div class="total-product-3 col-3">
                            <p>test</p>
                        </div>
                        <div class="total-product-4 col-3">
                            <p>test</p>
                        </div>
                    </div>-->
                </div>
            </div>
        </div>
    </div>
</template>

<style>

/*----- test -----*/

.product-grid .product-image {
    overflow: hidden;
    position: relative;
    z-index: 1;
}

.product-grid .product-image a.image {
    display: block; 
}

.product-grid .product-image img{
    width: 100%;
    height: auto;
}

/* .product-grid .product-image .img-1 {
    transition: all 0.3s ease 0s;
} */

/* .product-grid:hover .product-image .img-1 { 
    opacity: 0; 
} */

/* .product-grid .product-image .img-2 {
    width: 100%;
    height: 100%;
    opacity: 0;
    backface-visibility: hidden;
    position: absolute;
    left: 0;
    top: 0;
    z-index: -1;
    transition: all 0.3s ease 0s;
} */
/* .product-grid:hover .product-image .img-2 { 
    opacity: 1; 
} */

.product-grid .product-brand-label,
.product-grid .product-discount-label {
    color: #6b6b6b;
    background: #fff;
    font-size: 12px;
    font-weight: 600;
    text-transform: uppercase;
    padding: 3px 10px;
    position: absolute;
    top: 10px;
    left: 10px;
    box-shadow: 0 0 5px rgba(0, 0, 0, 0.3);
    opacity: 0.8;
}

.product-grid .product-discount-label {
    background: #ff3939;
    left: auto;
    right: 10px;
}

.product-grid .product-view {
    color: #fff;
    background:#000;
    font-size: 16px;
    text-align: right;
    line-height: 50px;
    width: 60px;
    height: 60px;
    padding: 0 16px 0 0;
    border-radius: 50px;
    opacity: 0;
    transform: scale(0);
    position: absolute;
    bottom: -40px;
    left: -40px;
    transition: all .3s ease;
}

/* .product-grid:hover .product-view { 
    opacity: 1;
    transform: scale(1);
    bottom: -20px;
    left: -20px;
} */

/* .product-grid .product-view:hover { 
    background: #ff6f00; 
} */

.product-grid .product-links {
    padding: 0;
    margin: 0;
    list-style: none;
    transform: translateY(50%);
    position: absolute;
    bottom: 50%;
    right: 10px;
    z-index: 1;
}

/* .product-grid .product-links li {
    margin: 5px 0;
    opacity: 0;
    transform: translateX(100%);
    transition: all .3s ease;
}

.product-grid .product-links li:nth-child(2) { 
    transition-delay: .1s; 
}

.product-grid .product-links li:nth-child(3) { 
    transition-delay: .2s; 
}

.product-grid:hover .product-links li{
    opacity: 1;
    transform: translateX(0); 
} */

/* .product-grid .product-links li a {
    color: #000;
    background: #fff;
    font-size: 18px;
    text-align: center;
    line-height: 33px;
    width: 35px;
    height: 35px;
    border: 1px solid #000;
    display: block;
    transition: all .3s ease;
}

.product-grid .product-links li a:hover {
    color: #fff;
    background:#ff6f00; 
    border-color: #ff6f00;
} */

.product-grid .product-content {
    background: #fff;
    text-align: left;
    padding-left: 15px;
    padding-right: 15px;
}

.product-grid .rating {
    color: #f7bc3d;
    font-size: 11px;
    padding: 0;
    margin: 0 0 8px;
    list-style: none;
}

.product-grid .rating li { 
    display: inline-block; 
}
.product-grid .rating .disable { 
    color: #a3a3a3; 
}

.product-grid .title {
    font-size: 15px;
    font-weight: 500;
    text-transform: capitalize;
    margin: 0 0 8px;
}
.product-grid .title a {
    color: #333;
    transition: all 0.3s ease 0s;
}
.product-grid .title a:hover { 
    color: #ca1b00; 
}

.product-grid .price {
    color: #2c3e50;
    font-size: 20px;
    font-weight: 500;
}

.product-grid .stock {
    text-align: right;
    color: #2c3e50;
    font-weight: 400;
}

.product-grid .stock-line {
    height: 3px;
    border-width: 0;
    color: #00AA00;
    background-color: #00AA00;
    opacity: 1;
    margin: 0px;
    width: 50%;
    margin-left: 51%;
    margin-top: 4px;
}

.shoppingcart-button {
    padding-bottom: 20px;
    padding-top: 15px;
}

.shoppingcart-buttonbutton {
    width: 100%;
    background-color: #1cad00 !important;
    border-color: #1cad00 !important;
}

.product-title {
    height: 60px;
}

.button-cart-text {
    font-size: 20px;
    font-weight: 500;
    margin-left: 10px;
}

.product-grid .price span {
    color: #999;
    font-size: 14px;
    font-weight: 400;
    text-decoration: line-through;
    margin-right: 5px;
}

.products-row {
    margin-bottom: 25px;
}

@media screen and (max-width: 990px) {
    .product-grid{ margin-bottom: 30px; }
}

/*----- test -----*/


.cilinders-product-page {
    background-color: #F0F1F2;
}

.total-product-1, .total-product-2, .total-product-3, .total-product-4 {
    padding: 0px;
    height: 250px;
    background-color: white;
}

.total-product-1 {
    border-right: 8px solid #F0F1F2;
}

.total-product-2 {
    border-right: 6px solid #F0F1F2;
    border-left: 4px solid #F0F1F2;
}

.total-product-3 {
    border-right: 4px solid #F0F1F2;
    border-left: 6px solid #F0F1F2;
}

.total-product-4 {
    border-left: 8px solid #F0F1F2;
}

.product-image-row {
    height: 100px;
}

</style>

<script>
import axios from 'axios'

import Navbar from "/src/components/navigationbar.vue"
import Footer from "/src/components/footerbar.vue"

export default {
  name: 'Home',
  components: {
    Navbar,
    Footer
  },
  data() {
    return {
      latestProducts: []
    }
  },
  mounted() {
      this.getLatestProducts()
  },
  methods: {
      getLatestProducts() {
          axios
            .get('api/v1/latest-products/')
            .then(response => {
                this.latestProducts = response.data
            })
            .catch(error => {
                console.log(error)
            })
      }
  }
}
</script>