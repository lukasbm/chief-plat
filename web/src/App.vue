<script setup>
import ProjectVue from "./components/Project.vue";
import HeaderVue from "./components/Header.vue";
import { ref } from "vue";

let projects = ref([]);
const apiKey = localStorage.getItem("apiKey");

fetch(`${import.meta.env.BASE_URL}/projects`, {
  method: "GET",
  headers: {
    Authorization: `Bearer ${apiKey}`,
  },
})
  .then((resp) => {
    console.log(resp);
    projects.value = resp.json();
  })
  .catch((err) => {
    console.error(err);
  });

projects.value = [
  {
    name: "Test-app",
    containers: [
      { name: "redis", status: "up", uptime: "2h" },
      { name: "nginx", status: "down", uptime: null },
    ],
  },
  {
    name: "Test-app2",
    containers: [
      { name: "test", status: "up", uptime: "4d 11h" },
      { name: "nginx", status: "down", uptime: null },
    ],
  },
  {
    name: "Test-app3",
    containers: [
      { name: "test", status: "up", uptime: "4d 11h" },
      { name: "nginx", status: "down", uptime: null },
    ],
  },
  {
    name: "Test-app4",
    containers: [
      { name: "test", status: "up", uptime: "4d 11h" },
      { name: "nginx", status: "down", uptime: null },
    ],
  },
  {
    name: "Test-app5",
    containers: [
      { name: "test", status: "up", uptime: "4d 11h" },
      { name: "nginx", status: "down", uptime: null },
    ],
  },
];
</script>

<template>
  <HeaderVue></HeaderVue>
  <main class="container flex flex-wrap justify-between items-center mx-auto">
    <div class="grid gap-4 xl:grid-cols-4 lg:grid-cols-3 md:grid-cols-2 sm:grid-cols-1">
      <ProjectVue v-for="proj in projects" :key="proj.name" :project="proj"></ProjectVue>
    </div>
  </main>
</template>
