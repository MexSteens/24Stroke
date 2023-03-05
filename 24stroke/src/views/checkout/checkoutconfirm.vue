<template>
    <div class="checkout-payment">
        <div class="row justify-content-center">
            <div class="col-10">
                <CheckoutBreadcrumbs activepage="sixth"/>
                <!-- Enter information here -->
                <div class="checkout-title text-center pt-4">
                    <h1>Uw bestelling is geplaatst!</h1>
                </div>
                <div class="text-center mt-3" v-if="this.$route.query.pending === 'true'">
                    <h1 class="h4">Uw betaling word nu in behandeling genomen. Als u met Sofort<br>heeft betaald kan dit 2 tot 14 dagen duren<br>voordat Sofort de betaling vrijgeeft.</h1>
                </div>
                <div class="text-center">
                    <font-awesome-icon icon="check-circle"
                                        :style="{ color: 'green', width: '10vw', height: '10vw'}" />
                </div>
                <div class="text-center mt-3">
                    <h1 class="h2">Dankuwel voor het kiezen van 24stroke</h1>
                </div>
            </div>
        </div>
    </div>                
</template>


<script>
import CheckoutBreadcrumbs from '@/components/checkoutBreadcrumbs.vue'

export default {
  name: 'checkoutconfirm',
  components: {
        CheckoutBreadcrumbs
  }
}
</script>