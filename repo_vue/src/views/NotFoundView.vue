<template>
    <div class="text-is-light not-found-container">
        <h1 class="not-found-title">
            The page you are requesting does not exist :(
        </h1>
    </div>
    </template>
    
    <script>
    export default {
    
        data() {
            return {
            }
        },
    
        mounted() {
            document.title = '404 Not Found';
    
        },
    
    }
    </script>