import api from "../api/api";

export const getDevices = async () => {
  const response = await api.get("/devices/");
  return response.data;
};

export const getReadings = async () => {
  const response = await api.get("/readings");
  return response.data;
};

export const getAlerts = async () => {
  const response = await api.get("/alerts");
  return response.data;
};
