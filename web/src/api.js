const baseUrl = import.meta.env.DEV ? "http://localhost:5000" : window.location.origin;

const getProjectLogs = (projectName) => {
  const apiKey = localStorage.getItem("apiKey");
  return fetch(`${baseUrl}/project/${projectName}/logs`, {
    method: "GET",
    headers: {
      Authorization: `Bearer ${apiKey}`,
    },
  });
};

const getProjects = () => {
  const apiKey = localStorage.getItem("apiKey");
  return fetch(`${baseUrl}/projects`, {
    method: "GET",
    headers: {
      Authorization: `Bearer ${apiKey}`,
    },
  });
};

const startProject = (projectName) => {
  const apiKey = localStorage.getItem("apiKey");
  return fetch(`${baseUrl}/project/${projectName}/start`, {
    method: "GET",
    headers: {
      Authorization: `Bearer ${apiKey}`,
    },
  });
};

const stopProject = (projectName) => {
  const apiKey = localStorage.getItem("apiKey");
  return fetch(`${baseUrl}/project/${projectName}/stop`, {
    method: "GET",
    headers: {
      Authorization: `Bearer ${apiKey}`,
    },
  });
};

const restartProject = (projectName) => {
  const apiKey = localStorage.getItem("apiKey");
  return fetch(`${baseUrl}/project/${projectName}/restart`, {
    method: "GET",
    headers: {
      Authorization: `Bearer ${apiKey}`,
    },
  });
};

export { getProjects, getProjectLogs, startProject, stopProject, restartProject };
