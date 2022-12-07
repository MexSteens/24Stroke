<template>
    <div class="error-message-container">
        <span><font-awesome-icon icon="times-circle" :style="{ marginRight: '7px'}"/>{{ message }}</span>
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
.error-message-container {
    background-color: #FF2400;
    border-radius: 5px;
    padding: 5px;
    color: white;
    font-weight: 600;
    margin-bottom: 5px;
}
</style>