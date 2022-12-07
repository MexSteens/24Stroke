<template>
    <div class="template">
        <div class="row justify-content-center">
            <div class="col-10">
                <!-- Enter information here -->
                <div class="register">
                    <div class="row">
                        <div class="col-3"></div>
                        <div class="login-section col-6">
                            <form @submit.prevent="submitForm">
                                <div class="login-title">
                                    <h2>Wachtwoord resetten</h2>
                                </div>
                                <div class="login-subtitle">
                                    <h4>Van bestaand account</h4>
                                </div>
                                <div class="email-title">
                                    <p>Voer hier het e-mail adres in van uw account</p>
                                </div>
                                <div class="email-form">
                                    <input type="email" class="form-control" placeholder="E-mail adres">
                                </div>
                                <div class="login-buttonpart">
                                    <div class="row">
                                        <div class="login-button col-5">
                                            <div class="shoppingcart-button">
                                                <button type="submit" class="shoppingcart-buttonbutton btn btn-success" @click="modal.show()">
                                                    <span class="button-cart-text">reset wachtwoord</span>
                                                </button>
                                            </div>
                                            <!-- Modal -->
                                            <div class="modal fade" ref="resetModal" tabindex="-1" aria-hidden="true">
                                                <div class="modal-dialog">
                                                    <div class="modal-content">
                                                    <div class="modal-body">
                                                        <p>Er is een link gestuurd naar uw email indien u al een account heeft om uw wachtwoord te resetten.</p>
                                                        <p>Als u op deze link klikt kan u uw wachtwoord veranderen.</p>
                                                        <p>Vervolgens kunt u weer inloggen met uw account.</p>
                                                        <div class="row">
                                                            <div class="col-4"><button type="button" class="modal-button1 btn btn-success" @click="modal.hide(), $router.push('login')">Ga naar login</button></div>
                                                            <div class="col-2"><button type="button" class="modal-reset-button btn btn-dangerr" @click="modal.hide()">Sluiten</button></div>
                                                        </div> 
                                                    </div>
                                                    </div>
                                                </div>
                                            </div>
                                            <!-- einde modal -->
                                        </div>
                                    </div>
                                </div>
                            </form>
                        </div>
                        <div class="col-3"></div>
                    </div>
                </div>  
            </div>  
        </div>
    </div>  
</template>

<script>
import { Modal } from 'bootstrap'

export default {
    data() {
        return {
            modal: null
        }
    },
    mounted() {
        this.modal = new Modal(this.$refs.resetModal)
    },
}

</script>

<style>
.modal-reset-button {
    color: #FF2400;
}

.modal-reset-button:hover {
    transition: all 0.3s ease 0s;
    color: #ca1b00;
}
</style>