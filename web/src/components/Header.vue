<script setup>
import AuthVue from "./Auth.vue";
import DarkModeVue from "./DarkMode.vue";
</script>

<template>
  <nav class="bg-gray-150 shadow-md border-gray-200 px-2 sm:px-4 py-2.5 dark:bg-gray-800 mb-4">
    <div class="container flex flex-wrap justify-between items-center mx-auto">
      <div class="flex items-center space-x-2">
        <img src="/favicon.ico" class="mr-3 h-6 sm:h-10" alt="Flowbite Logo" />
        <h1 class="text-2xl font-bold tracking-tight text-gray-900 dark:text-white">Chief-Plat</h1>
      </div>
      <div class="flex md:order-2 space-x-2">
        <AuthVue></AuthVue>
        <DarkModeVue></DarkModeVue>
      </div>
    </div>
  </nav>
</template>
