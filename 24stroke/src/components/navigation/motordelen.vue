<template>
    <div class="motordelennav">
        <div class="head">
                <div class="infohead row">
                    <div class="col-1">
                        <img class="img-fluid" src="img/icon/Derbiengine-removebg-preview.png" alt="Engine" width="100%" height="auto">
                    </div>
                    <div class="col-11 g-0">
                        <div class="row">
                            <div class="infoheadtext col-10">
                                <h2>Motor onderdelen</h2>
                            </div>
                        </div>
                        <hr class="line-infohead">
                    </div>
                </div>
            </div>
        <div class="items">
            <div class="rowdistance row g-0">
                    <div class="col-4">
                        <div class="row justify-content-start g-0">
                            <router-link :to="'/cilinders'" class="routerlink"><div class="item-1 col-11">
                                <div class="row">
                                    <div class="col-4">
                                        <img class="product-image-photo" src="https://www.jmpbonderdelen.nl/media/catalog/category/logo_cilinder_yamaha.png" width="90px" height="72px" alt="Cilinders">
                                    </div>
                                    <div class="col-8">
                                        <div class="headcatagory row">
                                            <p>Shop cilinders</p>
                                        </div>
                                        <div class="infocatagory row">
                                            <p>{200} producten voor {selected}</p>
                                        </div>
                                    </div>
                                </div>
                            </div></router-link>
                        </div>
                    </div>
                <div class="col-4">
                    <div class="row justify-content-center">
                        <router-link :to="'/krukassen'" class="routerlink"><div class="item-1 col-11">
                            <div class="row">
                                <div class="col-4">
                                    <img class="product-image-photo" src="https://www.jmpbonderdelen.nl/media/catalog/category/crankshaft_tomos_small_2.jpg" width="90px" height="72px" alt="Krukassen">
                                </div>
                                <div class="col-8">
                                    <div class="headcatagory row">
                                        <p>Shop krukassen</p>
                                    </div>
                                    <div class="infocatagory row">
                                        <p>{200} producten voor {selected}</p>
                                    </div>
                                </div>
                            </div>
                        </div></router-link>
                    </div>
                </div>
                <div class="col-4">
                    <div class="row justify-content-end">
                        <router-link :to="'/uitlaten'" class="routerlink"><div class="item-1 col-11">
                            <div class="row">
                                <div class="col-4">
                                    <img class="product-image-photo" src="https://www.jmpbonderdelen.nl/media/catalog/category/Drawing_6__Exhaust_150x120_1.png" width="90px" height="72px" alt="Uitlaten">
                                </div>
                                <div class="col-8">
                                    <div class="headcatagory row">
                                        <p>Shop uitlaten</p>
                                    </div>
                                    <div class="infocatagory row">
                                        <p>{200} producten voor {selected}</p>
                                    </div>
                                </div>
                            </div>
                        </div></router-link>
                    </div>
                </div>
            </div>
            <div class="rowdistance row g-0">
                <div class="col-4">
                    <div class="row justify-content-start g-0">
                        <router-link :to="'/varburatueren-en-inlaten'" class="routerlink"><div class="item-1 col-11">
                            <div class="row">
                                <div class="col-4">
                                    <img class="product-image-photo" src="https://www.jmpbonderdelen.nl/media/catalog/category/logo_carb_yamaha.png" width="90px" height="72px" alt="Carburateuren">
                                </div>
                                <div class="col-8">
                                    <div class="headcatagory row">
                                        <p>Shop carburateuren & inlaten</p>
                                    </div>
                                    <div class="infocatagory row">
                                        <p>{200} producten voor {selected}</p>
                                    </div>
                                </div>
                            </div>
                        </div></router-link>
                    </div>
                </div>
                <div class="col-4">
                    <div class="row justify-content-center">
                        <router-link :to="'/koppelingen-en-variateurs'" class="routerlink"><div class="item-1 col-11">
                            <div class="row">
                                <div class="col-4">
                                    <img class="product-image-photo" src="https://www.jmpbonderdelen.nl/media/catalog/category/Drawing_4__Koppeling_Citta_150x120_1.png" width="90px" height="72px" alt="Koppelingen">
                                </div>
                                <div class="col-8">
                                    <div class="headcatagory row">
                                        <p>Shop koppelingen & variateurs</p>
                                    </div>
                                    <div class="infocatagory row">
                                        <p>{200} producten voor {selected}</p>
                                    </div>
                                </div>
                            </div>
                        </div></router-link>
                    </div>
                </div>
                <div class="col-4">
                    <div class="row justify-content-end">
                        <router-link :to="'/transmissies-en-vertandingen'" class="routerlink"><div class="item-1 col-11">
                            <div class="row">
                                <div class="col-4">
                                    <img class="product-image-photo" src="img/icon/vertanding.png" width="90px" height="72px" alt="Vertandingen">
                                </div>
                                <div class="col-8">
                                    <div class="headcatagory row">
                                        <p>Shop transmissies & vertandingen</p>
                                    </div>
                                    <div class="infocatagory row">
                                        <p>{200} producten voor {selected}</p>
                                    </div>
                                </div>
                            </div>
                        </div></router-link>
                    </div>
                </div>
            </div>
            <div class="rowdistance row g-0">
                <div class="col-4">
                    <div class="row justify-content-start g-0">
                        <router-link :to="'/ontsteking'" class="routerlink"><div class="item-1 col-11">
                            <div class="row">
                                <div class="col-4">
                                    <img class="product-image-photo" src="img/icon/ontsteking.png" width="72px" height="72px" alt="Ontsteking">
                                </div>
                                <div class="col-8">
                                    <div class="headcatagory row">
                                        <p>Shop ontsteking</p>
                                    </div>
                                    <div class="infocatagory row">
                                        <p>{200} producten voor {selected}</p>
                                    </div>
                                </div>
                            </div>
                        </div></router-link>
                    </div>
                </div>
                <div class="col-4">
                    <div class="row justify-content-center">
                        <router-link :to="'/lagers-en-keerringen'" class="routerlink"><div class="item-1 col-11">
                            <div class="row">
                                <div class="col-4">
                                    <img class="product-image-photo" src="https://www.jmpbonderdelen.nl/media/catalog/category/Drawing_1__bearings_150x120_3.png" width="90px" height="72px" alt="Lagers">
                                </div>
                                <div class="col-8">
                                    <div class="headcatagory row">
                                        <p>Shop lagers & keerringen</p>
                                    </div>
                                    <div class="infocatagory row">
                                        <p>{200} producten voor {selected}</p>
                                    </div>
                                </div>
                            </div>
                        </div></router-link>
                    </div>
                </div>
                <div class="col-4">
                    <div class="row justify-content-end">
                        <router-link :to="'/pakkingen'" class="routerlink"><div class="item-1 col-11">
                            <div class="row">
                                <div class="col-4">
                                    <img class="product-image-photo" src="https://www.jmpbonderdelen.nl/media/catalog/category/gasket_yamaha.png" width="90px" height="72px" alt="Pakkingen">
                                </div>
                                <div class="col-8">
                                    <div class="headcatagory row">
                                        <p>Shop pakkingen</p>
                                    </div>
                                    <div class="infocatagory row">
                                        <p>{200} producten voor {selected}</p>
                                    </div>
                                </div>
                            </div>
                        </div></router-link>
                    </div>
                </div>
            </div>
            <div class="rowdistance row g-0">
                <div class="col-4">
                    <div class="row justify-content-start g-0">
                        <router-link :to="'/blokdelen'" class="routerlink"><div class="item-1 col-11">
                            <div class="row">
                                <div class="col-4">
                                    <img class="product-image-photo" src="https://www.jmpbonderdelen.nl/media/catalog/category/logo_carter_yamaha.png" width="90px" height="72px" alt="Blokdelen">
                                </div>
                                <div class="col-8">
                                    <div class="headcatagory row">
                                        <p>Shop blokdelen</p>
                                    </div>
                                    <div class="infocatagory row">
                                        <p>{200} producten voor {selected}</p>
                                    </div>
                                </div>
                            </div>
                        </div></router-link>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
.infohead p {
    text-align: left;
    margin-bottom: 0;
    font-size: 15px;
}

.motordelennav {
    margin-top: 60px;
}

.line-infohead {
    height: 3px;
    border-width: 0;
    color: #FF2400;
    background-color: #FF2400;
    opacity: 1;
    margin: 0;
    margin-bottom: 30px;
}

.infoheadtext h2 {
    text-align: left;
    font-size: 2vw;
    font-weight: 600;
    margin-bottom: 0px;
    margin-top: 8px;
}

.infoheadtextsmall {
    margin-left: -2%;
}

.productamount {
    color: rgb(167, 167, 167);
}

.item-1 {
    background-color: white;
    border-radius: 2px;
}

.rowdistance {
    margin-bottom: 20px;
}

.headcatagory {
    text-align: left;
}

.headcatagory p {
    margin-top: 10px;
    margin-bottom: 0;
    font-size: 1vw;
    font-weight: 500;
}

.infocatagory {
    text-align: left;
    font-size: 0.8vw;
}

.infocatagory p {
    margin-bottom: 0;
}
</style>