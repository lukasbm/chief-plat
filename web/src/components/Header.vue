<script setup>
import AuthVue from './Auth.vue';
</script>

<template>
  <nav class="bg-gray-150 shadow-md border-gray-200 px-2 sm:px-4 py-2.5 rounded dark:bg-gray-800 mb-4">
    <div class="container flex flex-wrap justify-between items-center mx-auto">
      <a href="#" class="flex items-center">
        <img src="/favicon.ico" class="mr-3 h-6 sm:h-10" alt="Flowbite Logo" />
        <h1 class="text-2xl font-bold">Chief-Plat</h1>
      </a>
      <div class="flex md:order-2">
        <AuthVue></AuthVue>
      </div>
    </div>
  </nav>
</template>
