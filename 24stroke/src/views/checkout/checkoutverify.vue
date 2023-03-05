<template>
    <div class="checkout-payment">
        <div class="row justify-content-center">
            <div class="col-10">
                <CheckoutBreadcrumbs activepage="fifth"/>
                <!-- Enter information here -->
                <div class="checkout-title text-center">
                    <h1>Verifiëren</h1>
                </div>
                <!-- <div class="loading-bar">
                    <div class="loading-spinner spinner-border text-danger"></div>
                </div> -->
                <div class="spinner-border loading-spinner text-danger" role="status">
                    <span class="sr-only">Loading...</span>
                </div>
            </div>
        </div>
    </div>                
</template>

<script>
import CheckoutBreadcrumbs from '@/components/checkoutBreadcrumbs.vue'

export default {
  name: 'verifieren',
  components: {
        CheckoutBreadcrumbs
  },
  methods: {
    async payment_status() {
        const stripe = Stripe('pk_test_51Kk6PTFE6zAlv2VHQhRTMCPyGYwlBGoNAd2QbJl5OHOgU87ErgzMeCWLIJVAo2HLSKVNTgfzD8gjBiPwFBZ1qch400cBR1sLzQ')
        const clientSecret = this.$route.query.payment_intent_client_secret
        console.log(clientSecret)
        const {paymentIntent, error} = await stripe.retrievePaymentIntent(clientSecret);
        if (error) {
            this.$router.push({ path: 'checkout-betaling', query: { failed: "true" } })
        } else if (paymentIntent && paymentIntent.status === 'succeeded') {
            this.$router.push({ path: 'checkout-bevestiging' })
        } else if (paymentIntent && paymentIntent.status === 'pending') {
            console.log("verifyings")
        }
        else {
            if (this.$route.query.redirect_status == "succeeded") {
                this.$router.push({ path: 'checkout-bevestiging' })
            }
            if (this.$route.query.redirect_status == "failed") {
                this.$router.push({ path: 'checkout-betaling', query: { failed: "true" } })
            }
            if (this.$route.query.redirect_status == "pending") {
                this.$router.push({ path: 'checkout-bevestiging', query: { pending: "true" } })
            }
        }
    }
  },
  mounted() {
    this.payment_status()
  }
}
</script>