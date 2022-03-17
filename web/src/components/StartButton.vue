<script setup>
import { startProject } from "../api";

const props = defineProps({
  projectName: {
    type: String,
    required: true,
  },
});

function start() {
  startProject(props.projectName).catch((err) => {
    console.error(err);
  });
}
</script>

<template>
  <button
    @click="start()"
    type="button"
    class="text-blue-700 border border-blue-700 hover:bg-blue-700 hover:text-white focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm p-2.5 text-center inline-flex items-center mr-2 dark:border-blue-500 dark:text-blue-500 dark:hover:text-white dark:focus:ring-blue-800"
  >
    <span class="material-icons">play_arrow</span>
  </button>
</template>
