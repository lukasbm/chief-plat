<script setup>
import { ref, onMounted } from "vue";
import { getProjectLogs } from "../api";

const props = defineProps({
  projectName: {
    type: String,
    required: true,
  },
});

let logs = ref(null);
let error = ref(null);

onMounted(() => {
  getProjectLogs(props.projectName)
    .then((res) => (logs.value = res.data))
    .catch((err) => {
      console.error(err);
      error.value = err;
    });
});
</script>

<template>
  <!-- TODO extract button out of module -->
  <button
    class="inline-flex items-center py-2 px-3 text-sm font-medium text-center text-white bg-blue-700 rounded-lg hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
    data-modal-toggle="logs-modal"
    type="button"
  >
    Logs
    <span class="material-icons scale-75">content_paste_go</span>
  </button>

  <!-- 
  <div v-if="error">Error: {{ error }}</div>
  <div v-else-if="logs">TODO: show modal</div>
  <div v-else class="text-center">
    <svg role="status" class="inline mr-2 w-32 h-32 mt-10 text-gray-200 animate-spin dark:text-gray-600 fill-blue-600" viewBox="0 0 100 101" fill="none" xmlns="http://www.w3.org/2000/svg">
      <path
        d="M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z"
        fill="currentColor"
      />
      <path
        d="M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z"
        fill="currentFill"
      />
    </svg>
  </div> -->

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
          <div class="p-4 bg-gray-50 dark:bg-gray-800" :id="l.container" role="tabpanel" :class="{ hidden: i != 0 }" :aria-labelledby="`${l.container}-tab`" v-for="(l, i) in logs" :key="l.container">
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
