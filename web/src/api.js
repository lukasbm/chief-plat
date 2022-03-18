import axios from "axios";

const baseUrl = import.meta.env.DEV ? "http://localhost:5000" : window.location.origin;

const getAuthHeader = () => {
  const apiKey = localStorage.getItem("apiKey") ?? "";
  return "Bearer " + apiKey;
};

const getProjectLogs = (projectName) => {
  return axios.get(`${baseUrl}/project/${projectName}/logs`, {
    headers: {
      Authorization: getAuthHeader(),
    },
  });
};

const getProjects = () => {
  return axios.get(`${baseUrl}/projects`, {
    headers: {
      Authorization: getAuthHeader(),
    },
  });
};

const startProject = (projectName) => {
  return axios.get(`${baseUrl}/project/${projectName}/start`, {
    headers: {
      Authorization: getAuthHeader(),
    },
  });
};

const stopProject = (projectName) => {
  return axios.get(`${baseUrl}/project/${projectName}/stop`, {
    headers: {
      Authorization: getAuthHeader(),
    },
  });
};

const restartProject = (projectName) => {
  return axios.get(`${baseUrl}/project/${projectName}/restart`, {
    headers: {
      Authorization: getAuthHeader(),
    },
  });
};

export { getProjects, getProjectLogs, startProject, stopProject, restartProject };
