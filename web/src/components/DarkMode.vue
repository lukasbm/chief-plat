<script setup>
import { ref } from "vue";

let isDark = ref(false);
if (localStorage.getItem("theme") === "dark") {
  isDark.value = true;
  setDarkMode();
} else {
  setLightMode();
}

function toggleDarkMode() {
  if (isDark.value) {
    setLightMode();
  } else {
    setDarkMode();
  }
}

function setLightMode() {
  isDark.value = false;
  localStorage.setItem("theme", "light");
  document.body.classList.remove("dark");
}

function setDarkMode() {
  isDark.value = true;
  localStorage.setItem("theme", "dark");
  document.body.classList.add("dark");
}
</script>

<template>
  <button
    @click="toggleDarkMode()"
    type="button"
    class="text-gray-500 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-700 focus:outline-none focus:ring-4 focus:ring-gray-200 dark:focus:ring-gray-700 rounded-lg text-sm p-2"
  >
    <span class="material-icons align-middle" v-if="isDark">light_mode</span>
    <span class="material-icons align-middle" v-else>dark_mode</span>
  </button>
</template>
