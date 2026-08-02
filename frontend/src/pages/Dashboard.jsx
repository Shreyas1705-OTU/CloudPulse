import { useEffect, useState } from "react";
import {
  getDevices,
  getReadings,
  getAlerts,
} from "../services/cloudpulseService";

export default function Dashboard() {
  const [devices, setDevices] = useState([]);
  const [readings, setReadings] = useState([]);
  const [alerts, setAlerts] = useState([]);

  useEffect(() => {
    loadData();

    const interval = setInterval(loadData, 5000);

    return () => clearInterval(interval);
  }, []);

  async function loadData() {
    try {
      const deviceData = await getDevices();
      const readingData = await getReadings();
      const alertData = await getAlerts();

      setDevices(deviceData);
      setReadings(readingData);
      setAlerts(alertData);
    } catch (err) {
      console.error(err);
    }
  }

  const latest = readings.length ? readings[0] : null;

  return (
    <div
      style={{
        background: "#111827",
        minHeight: "100vh",
        color: "white",
        padding: "30px",
        fontFamily: "Arial",
      }}
    >
      <h1>CloudPulse Dashboard</h1>

      <hr />

      <h2>System Overview</h2>

      <p>Devices : {devices.length}</p>

      <p>Total Readings : {readings.length}</p>

      <p>Total Alerts : {alerts.length}</p>

      {latest && (
        <>
          <h2>Latest Reading</h2>

          <p>🌡 Temperature : {latest.temperature} °C</p>

          <p>💧 Humidity : {latest.humidity} %</p>

          <p>🔋 Battery : {latest.battery} %</p>
        </>
      )}

      <hr />

      <h2>Recent Alerts</h2>

      {alerts.slice(0, 5).map((alert) => (
        <div
          key={alert.id}
          style={{
            background: "#1F2937",
            marginBottom: "10px",
            padding: "10px",
            borderRadius: "8px",
          }}
        >
          <strong>{alert.severity}</strong>

          <br />

          {alert.message}
        </div>
      ))}
    </div>
  );
}