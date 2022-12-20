<template>
    <div class="technical-details-box p-1 row">
        <div class="title-technical col-12">
            <h1 class="font-weight-bold">Technical Details</h1>
        </div>
        <div class="product-name-technival col-12">
            <h4 class="font-weight-bold">{{product.name}}</h4>
        </div>
        <TechnicalDetail name="Artikel nr." :nameValue="product.technical_details.article_number" />
        <TechnicalDetail name="EAN" :nameValue="product.technical_details.ean" />
        <TechnicalDetail name="Merk" :nameValue="product.technical_details.brand" />
        <TechnicalDetail name="Kleur" :nameValue="product.technical_details.colour" />
        <TechnicalDetail v-if="product.technical_details.material" name="Materiaal" :nameValue="product.technical_details.material" />
        <TechnicalDetail v-if="product.technical_details.tuning_level" name="Tuning level" :nameValue="product.technical_details.tuning_level" />
        <TechnicalDetail v-if="product.technical_details.moped" name="Brommer" :nameValue="product.technical_details.moped" />
        <TechnicalDetail v-if="product.technical_details.cylinder_displacement" name="Cilinder inhoud" :nameValue="product.technical_details.cylinder_displacement" />
        <TechnicalDetail v-if="product.technical_details.cylinder_piston_pin" name="Zuiger pen" :nameValue="product.technical_details.cylinder_piston_pin" />
        <TechnicalDetail v-if="product.technical_details.cylinder_bore" name="Cilinder Boring" :nameValue="product.technical_details.cylinder_bore" />
        <TechnicalDetail v-if="product.technical_details.cylinder_stroke" name="Slag" :nameValue="product.technical_details.cylinder_stroke" />
        <TechnicalDetail v-if="product.technical_details.cylinder_conrod_length" name="Krukas lengte" :nameValue="product.technical_details.cylinder_conrod_length" />
        <TechnicalDetail v-if="product.technical_details.bougie_thread" name="Draad" :nameValue="product.technical_details.bougie_thread" />
        <TechnicalDetail v-if="product.technical_details.carburetor_type" name="Carb type" :nameValue="product.technical_details.carburetor_type" />
        <TechnicalDetail v-if="product.technical_details.carburetor_diameter" name="Carb diameter" :nameValue="product.technical_details.carburetor_diameter" />
        <TechnicalDetail v-if="product.technical_details.carburetor_airfilter_connection" name="Luchtfilter dia..." :nameValue="product.technical_details.carburetor_airfilter_connection" />
        <TechnicalDetail v-if="product.technical_details.carburetor_manifold_connection" name="Spruitstuk dia..." :nameValue="product.technical_details.carburetor_manifold_connection" />
        <TechnicalDetail v-if="product.technical_details.carburetor_choke" name="Carb choke" :nameValue="product.technical_details.carburetor_choke" />
        <TechnicalDetail v-if="product.technical_details.carburetor_ports" name="Carb poorten" :nameValue="product.technical_details.carburetor_ports" />
        <TechnicalDetail v-if="product.technical_details.variator_roller_size" name="Afmetingen rollen" :nameValue="product.technical_details.variator_roller_size" />
        <TechnicalDetail v-if="product.technical_details.variator_roller_weight" name="Rollen gewicht" :nameValue="product.technical_details.variator_roller_weight" />
        <TechnicalDetail v-if="product.technical_details.variator_range" name="Variateur maat" :nameValue="product.technical_details.variator_range" />
        <TechnicalDetail v-if="product.technical_details.clutch_diameter" name="Koppeling maat" :nameValue="product.technical_details.clutch_diameter" />
        <TechnicalDetail v-if="product.technical_details.transmission_type" name="Transmissie type" :nameValue="product.technical_details.transmission_type" />
        <TechnicalDetail v-if="product.technical_details.ignition_lighting_supply" name="Lichtspoel" :nameValue="product.technical_details.ignition_lighting_supply" />
        <TechnicalDetail v-if="product.technical_details.light_style" name="Type licht" :nameValue="product.technical_details.light_style" />
        <TechnicalDetail v-if="product.technical_details.light_voltage" name="Voltage licht" :nameValue="product.technical_details.light_voltage" />
        <TechnicalDetail v-if="product.technical_details.tire_width" name="Band breedte" :nameValue="product.technical_details.tire_width" />
        <TechnicalDetail v-if="product.technical_details.tire_height" name="Band hoogte" :nameValue="product.technical_details.tire_height" />
        <TechnicalDetail v-if="product.technical_details.tire_rim_diameter" name="Band diameter" :nameValue="product.technical_details.tire_rim_diameter" />
        <TechnicalDetail v-if="product.technical_details.tire_code" name="Band code" :nameValue="product.technical_details.tire_code" />
        <TechnicalDetail v-if="product.technical_details.tire_application" name="Band type" :nameValue="product.technical_details.tire_application" />


    </div>
</template>

<style>
.technical-details-box {
    background-color: #F0F1F2;
    border: 1px solid #cacaca;
}

.title-technical h1 {
    font-size: 2.1rem;
}

.technical-details-box h4 {
    font-size: 1rem;
}

.technical-details-box p {
    font-size: 1rem;
}

</style>

<script>
import TechnicalDetail from './TechnicalDetail.vue';

export default {
    name: "TechnicalDetails",
    props: ['product'],
    components: {
        TechnicalDetail
    },
    mounted () {
        this.test()
    },
    methods: {
        test() {
            console.log(this.product)
        }
    }
}
</script>