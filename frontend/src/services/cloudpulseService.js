import api from "./api";

export async function getDevices() {
    const response = await api.get("/devices/");
    return response.data;
}

export async function getReadings() {
    const response = await api.get("/readings");
    return response.data;
}

export async function getAlerts() {
    const response = await api.get("/alerts");
    return response.data;
}