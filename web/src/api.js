const baseUrl = import.meta.env.DEV ? "http://localhost:5000" : window.location.origin;

const getAuthHeader = () => {
  const apiKey = localStorage.getItem("apiKey") ?? "";
  return "Bearer " + apiKey;
};

const getProjectLogs = (projectName) => {
  return fetch(`${baseUrl}/project/${projectName}/logs`, {
    method: "GET",
    headers: {
      Authorization: getAuthHeader(),
    },
  });
};

const getProjects = () => {
  return fetch(`${baseUrl}/projects`, {
    method: "GET",
    headers: {
      Authorization: getAuthHeader(),
    },
  });
};

const startProject = (projectName) => {
  return fetch(`${baseUrl}/project/${projectName}/start`, {
    method: "GET",
    headers: {
      Authorization: getAuthHeader(),
    },
  });
};

const stopProject = (projectName) => {
  return fetch(`${baseUrl}/project/${projectName}/stop`, {
    method: "GET",
    headers: {
      Authorization: getAuthHeader(),
    },
  });
};

const restartProject = (projectName) => {
  return fetch(`${baseUrl}/project/${projectName}/restart`, {
    method: "GET",
    headers: {
      Authorization: getAuthHeader(),
    },
  });
};

export { getProjects, getProjectLogs, startProject, stopProject, restartProject };
