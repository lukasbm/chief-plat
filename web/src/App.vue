<script setup>
import ProjectVue from "./components/Project.vue";
import RestartDialogVue from "./components/RestartDialog.vue";
import LogsVue from "./components/Logs.vue";

const proj = {
  name: "Test-app",
  containers: [
    { name: "redis", status: "up", uptime: "2h" },
    { name: "nginx", status: "down", uptime: null },
  ],
};

const logs = [
  {
    container: "redis",
    text: `
1:C 05 Mar 2022 17:58:55.865 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
1:C 05 Mar 2022 17:58:55.865 # Redis version=6.2.6, bits=64, commit=00000000, modified=0, pid=1, just started
1:C 05 Mar 2022 17:58:55.865 # Warning: no config file specified, using the default config. In order to specify a config file use redis-server /path/to/redis.conf
1:M 05 Mar 2022 17:58:55.865 * monotonic clock: POSIX clock_gettime
1:M 05 Mar 2022 17:58:55.866 * Running mode=standalone, port=6379.
1:M 05 Mar 2022 17:58:55.866 # Server initialized
1:M 05 Mar 2022 17:58:55.866 # WARNING overcommit_memory is set to 0! Background save may fail under low memory condition. To fix this issue add 'vm.overcommit_memory = 1' to /etc/sysctl.conf and then reboot or run the command 'sysctl vm.overcommit_memory=1' for this to take effect.
1:M 05 Mar 2022 17:58:55.866 * Ready to accept connections
`,
  },
  {
    container: "nginx",
    text: `
hallo
lol
    `,
  },
];
</script>

<template>
  <h1 class="text-3xl font-bold">Chief-Plat</h1>

  <main class="container">
    <ProjectVue :project="proj"></ProjectVue>
    <RestartDialogVue></RestartDialogVue>
    <LogsVue :logs="logs"></LogsVue>
  </main>
</template>
