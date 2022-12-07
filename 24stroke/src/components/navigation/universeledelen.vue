<template>
    <div class="motordelennav">
        <div class="head">
                <div class="infohead row">
                    <div class="col-1">
                        <img class="img-fluid" src="img/icon/UniversalPartsNBG.png" alt="Engine" width="100%" height="auto">
                    </div>
                    <div class="col-11 g-0">
                        <div class="row">
                            <div class="infoheadtext col-10">
                                <h2>Universele onderdelen</h2>
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
                        <div class="item-1 col-11">
                            <div class="row">
                                <div class="col-4">
                                    <img class="product-image-photo" src="https://www.jmpbonderdelen.nl/media/catalog/category/Drawing_2__bolts_nuts_150x120_2.png" width="90px" height="72px" alt="Moeren">
                                </div>
                                <div class="col-8">
                                    <div class="headcatagory row">
                                        <p>Shop bouten, moeren & bevestiging materiaal</p>
                                    </div>
                                    <div class="infocatagory row">
                                        <p>{200} producten voor {selected}</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col-4">
                    <div class="row justify-content-center">
                        <div class="item-1 col-11">
                            <div class="row">
                                <div class="col-4">
                                    <img class="product-image-photo" src="https://www.jmpbonderdelen.nl/media/catalog/category/logo_electra.png" width="90px" height="72px" alt="Electra">
                                </div>
                                <div class="col-8">
                                    <div class="headcatagory row">
                                        <p>Shop electra</p>
                                    </div>
                                    <div class="infocatagory row">
                                        <p>{200} producten voor {selected}</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col-4">
                    <div class="row justify-content-end">
                        <div class="item-1 col-11">
                            <div class="row">
                                <div class="col-4">
                                    <img class="product-image-photo" src="https://www.jmpbonderdelen.nl/media/catalog/category/Drawing_4__Screwdriver_150x120.png" width="90px" height="72px" alt="Gereedschap">
                                </div>
                                <div class="col-8">
                                    <div class="headcatagory row">
                                        <p>Shop gereedschap</p>
                                    </div>
                                    <div class="infocatagory row">
                                        <p>{200} producten voor {selected}</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="rowdistance row g-0">
                <div class="col-4">
                    <div class="row justify-content-start g-0">
                        <div class="item-1 col-11">
                            <div class="row">
                                <div class="col-4">
                                    <img class="product-image-photo" src="https://www.jmpbonderdelen.nl/media/catalog/category/Drawing_2__Lock_150x120-1.png" width="90px" height="72px" alt="Sloten">
                                </div>
                                <div class="col-8">
                                    <div class="headcatagory row">
                                        <p>Shop sloten</p>
                                    </div>
                                    <div class="infocatagory row">
                                        <p>{200} producten voor {selected}</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col-4">
                    <div class="row justify-content-center">
                        <div class="item-1 col-11">
                            <div class="row">
                                <div class="col-4">
                                    <img class="product-image-photo" src="img/icon/motorolie.jpg" width="60px" height="72px" alt="Vloeistoffen">
                                </div>
                                <div class="col-8">
                                    <div class="headcatagory row">
                                        <p>Shop vloeistoffen</p>
                                    </div>
                                    <div class="infocatagory row">
                                        <p>{200} producten voor {selected}</p>
                                    </div>
                                </div>
                            </div>
                        </div>
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