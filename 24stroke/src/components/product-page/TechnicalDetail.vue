<template>
    <div class="technical-detail col-12">
        <hr class="seperation-line-product">
        <div class="row">
            <div class="col-6 text-truncate">
                <h4 class="font-weight-bold">{{name}}</h4>
            </div>
            <div class="col-6">
                <p class="font-weight-light">{{nameValue}}</p>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "TechnicalDetail",
    props: ['name', 'nameValue']
}
</script>

<style>
    .technical-detail h4 {
        text-align: left;
        margin-bottom: 0.6rem;
    }

    .technical-detail p {
        margin-bottom: 0;
    }
</style>