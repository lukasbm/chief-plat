<script setup>
defineProps({
  project: Object,
});
</script>

<template>
  <div class="p-6 max-w-sm bg-white rounded-lg border border-gray-200 shadow-md dark:bg-gray-800 dark:border-gray-700">
    <a href="#">
      <h5 class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">
        {{ project.name }}
      </h5>
    </a>

    <button
      type="button"
      class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm p-2.5 text-center inline-flex items-center mr-2 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
    >
      <span class="material-icons">stop</span>
    </button>

    <button
      type="button"
      class="text-blue-700 border border-blue-700 hover:bg-blue-700 hover:text-white focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm p-2.5 text-center inline-flex items-center mr-2 dark:border-blue-500 dark:text-blue-500 dark:hover:text-white dark:focus:ring-blue-800"
    >
      <span class="material-icons w-full h-full">restart_alt</span>
    </button>

    <p class="mb-2 font-normal text-gray-700 dark:text-gray-400">Here are the biggest enterprise technology acquisitions of 2021 so far, in reverse chronological order.</p>

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

    <button
      class="inline-flex items-center py-2 px-3 text-sm font-medium text-center text-white bg-blue-700 rounded-lg hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
    >
      Logs
      <span class="material-icons scale-75">content_paste_go</span>
    </button>
  </div>
</template>
