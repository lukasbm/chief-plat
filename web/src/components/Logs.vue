<script setup>
defineProps({
  logs: {
    type: Array,
    required: true,
  },
});
</script>

<template>
  <button
    class="block w-full md:w-auto text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
    type="button"
    data-modal-toggle="logs-modal"
  >
    Extra large modal
  </button>

  <!-- Logs Modal -->
  <div class="hidden overflow-y-auto overflow-x-hidden fixed right-0 left-0 top-4 z-50 justify-center items-center md:inset-0 h-modal sm:h-full" id="logs-modal">
    <div class="relative px-4 w-full max-w-7xl h-full md:h-auto">
      <!-- Modal content -->
      <div class="relative bg-white rounded-lg shadow dark:bg-gray-700">
        <!-- Modal Header-->
        <div class="border-b border-gray-200 dark:border-gray-700">
          <ul class="flex flex-wrap -mb-px" id="logs-tabs" data-tabs-toggle="#logs-content" role="tablist">
            <li v-for="(l, i) in logs" :key="l.container" class="mr-2" role="presentation">
              <button
                class="inline-block py-4 px-4 text-sm font-medium text-center text-gray-500 rounded-t-lg border-b-2 border-transparent hover:text-gray-600 hover:border-gray-300 dark:text-gray-400 dark:hover:text-gray-300"
                :class="{ active: i == 0 }"
                :id="`${l.container}-tab`"
                :data-tabs-target="`#${l.container}`"
                type="button"
                role="tab"
                :aria-controls="l.container"
                :aria-selected="i == 0"
              >
                {{ l.container }}
              </button>
            </li>
            <button
              type="button"
              class="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm px-3 ml-auto inline-flex items-center dark:hover:bg-gray-600 dark:hover:text-white"
              data-modal-toggle="logs-modal"
            >
              <span class="material-icons">close</span>
            </button>
          </ul>
        </div>
        <!-- Modal Content -->
        <div id="logs-content">
          <div
            class="p-4 bg-gray-50 rounded-lg dark:bg-gray-800"
            :id="l.container"
            role="tabpanel"
            :class="{ hidden: i != 0 }"
            :aria-labelledby="`${l.container}-tab`"
            v-for="(l, i) in logs"
            :key="l.container"
          >
            <p class="text-xs font-mono text-gray-500 dark:text-gray-400 whitespace-pre-wrap">
              {{ l.text }}
            </p>
          </div>
        </div>
        <!-- Modal Footer -->
        <!-- TODO search function -->
      </div>
    </div>
  </div>
</template>
