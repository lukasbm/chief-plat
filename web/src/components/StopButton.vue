<script setup>
import { stopProject } from "../api";

const props = defineProps({
  projectName: {
    type: String,
    required: true,
  },
});

function stop() {
  stopProject(props.projectName).catch((err) => {
    console.error(err);
  });
}
</script>

<template>
  <button
    @click="stop()"
    type="button"
    class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm p-2.5 text-center inline-flex items-center mr-2 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
  >
    <span class="material-icons">stop</span>
  </button>
</template>
