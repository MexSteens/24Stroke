<template>
    <div class="succes-message-container">
        <span><font-awesome-icon icon="check-circle" :style="{ marginRight: '7px'}"/>{{ message }}</span>
    </div>
</template>

<script>
export default {
    props: {
        message: String
    }
}
</script>

<style>
.succes-message-container {
    background-color: #1cad00 ;
    border-radius: 5px;
    padding: 5px;
    color: white;
    font-weight: 600;
}
</style>