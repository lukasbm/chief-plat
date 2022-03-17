const baseUrl = import.meta.env.DEV ? "http://localhost:5000" : window.location.origin;

const getLogs = (projectName) => {
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

export { getProjects, getLogs };
