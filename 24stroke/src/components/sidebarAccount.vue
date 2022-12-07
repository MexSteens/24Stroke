<template>
    <div class="row">
        <div class="my-account-sidebar col-11">
            <div class="my-account-title">
                <h1>Mijn account</h1>
            </div>
            <hr class="my-account-seperation-line">
            <div class="my-account-overview">
                <span><font-awesome-icon class="my-account-icon-first" icon="info"/>Account overzicht</span>
            </div>
            <hr class="my-account-seperation-line">
            <div class="my-account-information">
                <span><font-awesome-icon class="my-account-icon-second" icon="user"/>Mijn gegevens</span>
            </div>
            <hr class="my-account-seperation-line">
            <div class="my-account-overview">
                <span><font-awesome-icon class="my-account-icon-third" icon="box"/>Mijn bestellingen</span>
            </div>
            <hr class="my-account-seperation-line">
            <div class="my-account-overview">
                <span><font-awesome-icon class="my-account-icon-fourth" icon="warehouse"/>Mijn garage</span>
            </div>
            <hr class="my-account-seperation-line">
            <div class="my-account-overview">
                <span><font-awesome-icon class="my-account-icon-fifth" icon="heart"/>Mijn verlanglijst</span>
            </div>
            <hr class="my-account-seperation-line">
            <div class="my-account-overview">
                <span><font-awesome-icon class="my-account-icon-sixth" icon="lock"/>Wachtwoord wijzigen</span>
            </div>
            <hr class="my-account-seperation-line">
            <div class="my-account-overview">
                <span><font-awesome-icon class="my-account-icon-seventh" icon="sign-out-alt"/>Uitloggen</span>
            </div>
        </div>
    </div>
</template>

<style>
.my-account-sidebar {
    background-color: white;
    text-align: left;
    padding: 20px !important;
    font-size: 1.0vw;
    border: 1px solid #ddd;
}

.my-account-seperation-line {
    margin-top: 15px !important;
    margin-bottom: 15px !important;
    width: 95%;
    height: 1px !important;
}

.my-account-icon {
    margin-right: 12px;
}

.my-account-icon-first {
    margin-right: 1.125em;
    margin-left: 0.4rem;
}

.my-account-icon-second {
    margin-right: 1.025rem;
}

.my-account-icon-third {
    margin-right: 0.9rem;
}

.my-account-icon-fourth {
    margin-right: 0.65rem;
}

.my-account-icon-fifth {
    margin-right: 0.9rem;
}

.my-account-icon-sixth {
    margin-right: 1.025rem;
}

.my-account-icon-seventh {
    margin-right: 0.9rem;
}
</style>