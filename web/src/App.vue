<script setup>
import ProjectVue from "./components/Project.vue";
import RestartDialogVue from "./components/RestartDialog.vue";
import LogsVue from "./components/Logs.vue";
import AuthVue from "./components/Auth.vue";
import { ref } from "vue";

let projects = ref([]);
const apiKey = localStorage.getItem("apiKey");

fetch("http://localhost:5000/projects", {
  method: "GET",
  headers: {
    Authorization: `Bearer ${apiKey}`,
  },
})
  .then((resp) => {
    console.log(resp);
    projects.value = resp.body();
  })
  .catch((err) => {
    console.error(err);
    projects.value = [
      {
        name: "Test-app",
        containers: [
          { name: "redis", status: "up", uptime: "2h" },
          { name: "nginx", status: "down", uptime: null },
        ],
      },
    ];
  });


console.log(projects.value);
</script>

<template>
  <h1 class="text-3xl font-bold">Chief-Plat</h1>
  <AuthVue></AuthVue>

  <main class="container">
    <div class="grid">
      <ProjectVue v-for="proj in projects" :key="proj.name" :project="proj"></ProjectVue>
    </div>
    <RestartDialogVue :open="false"></RestartDialogVue>
    <LogsVue></LogsVue>
  </main>
</template>
