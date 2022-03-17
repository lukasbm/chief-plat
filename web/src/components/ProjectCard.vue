<script setup>
import Logs from "./Logs.vue";
import StopButton from "./StopButton.vue";
import RestartButton from "./RestartButton.vue";

defineProps({
  project: Object,
});
</script>

<template>
  <div class="p-6 max-w-sm bg-white rounded-lg border border-gray-200 shadow-md dark:bg-gray-800 dark:border-gray-700 space-y-2">
    <h5 class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">
      {{ project.name }}
    </h5>

    <StopButton :projectName="project.name"></StopButton>
    <RestartButton :projectName="project.name"></RestartButton>

    <p v-if="project.description" class="mb-2 font-normal text-gray-700 dark:text-gray-400">{{ project.description }}</p>
    <p v-if="project.url" class="mb-2 font-normal text-gray-700 dark:text-gray-400">URL: {{ project.url }}</p>

    <ul role="list" class="divide-y divide-gray-200 dark:divide-gray-700">
      <li class="py-3 sm:py-4" v-for="container in project.containers" :key="container.name">
        <div class="flex items-center space-x-4">
          <div class="flex-1 min-w-0">
            <p class="text-sm font-medium text-gray-900 truncate dark:text-white">{{ container.name }}</p>
            <p v-if="container.uptime" class="text-sm text-gray-500 truncate dark:text-gray-400">uptime: {{ container.uptime }}</p>
          </div>
          <div class="inline-flex items-center text-base font-semibold text-gray-900 dark:text-white">
            <span class="rounded-full w-6 h-6 bg-green-400"></span>
          </div>
        </div>
      </li>
    </ul>

    <Logs :projectName="project.name"></Logs>
  </div>
</template>
