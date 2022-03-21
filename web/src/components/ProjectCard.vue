<script setup>
import Logs from "./Logs.vue";
import StopButton from "./StopButton.vue";
import RestartButton from "./RestartButton.vue";
import StartButton from "./StartButton.vue";

const props = defineProps({
  project: Object,
});
</script>

<template>
  <div class="p-6 max-w-sm bg-white rounded-lg border border-gray-200 shadow-md dark:bg-gray-800 dark:border-gray-700 space-y-2">
    <h5 class="text-2xl font-bold tracking-tight text-gray-900 dark:text-white">
      {{ project.name }}
    </h5>

    <StopButton :projectName="project.name"></StopButton>
    <RestartButton :projectName="project.name"></RestartButton>
    <StartButton :projectName="project.name"></StartButton>

    <p v-if="project.description" class="font-normal text-gray-700 dark:text-gray-400">{{ project.description }}</p>
    <ul v-if="project.urls" class="font-normal text-gray-700 dark:text-gray-400 list-disc list-inside">
      <li v-for="url in project.urls" :key="url">
        <a :href="url" target="_blank">{{ url }}</a>
      </li>
    </ul>

    <ul role="list" class="divide-y divide-gray-200 dark:divide-gray-700">
      <li class="py-3 sm:py-4" v-for="container in project.status" :key="container">
        <div class="flex">
          <div class="flex-1 min-w-0">
            <p class="font-medium text-gray-900 truncate dark:text-white">{{ container.name }}</p>
            <p class="text-sm text-gray-500 truncate dark:text-gray-400">status: {{ container.status }}</p>
          </div>
          <div class="inline-flex items-center text-base font-semibold text-gray-900 dark:text-white">
            <span v-if="container.status == 'running'" class="rounded-full w-6 h-6 bg-green-400"></span>
            <span v-else-if="container.status == 'exited'" class="rounded-full w-6 h-6 bg-yellow-300 dark:bg-yellow-200"></span>
            <span v-else class="rounded-full w-6 h-6 bg-red-500"></span>
          </div>
        </div>
      </li>
    </ul>

    <Logs :projectName="project.name"></Logs>
  </div>
</template>
