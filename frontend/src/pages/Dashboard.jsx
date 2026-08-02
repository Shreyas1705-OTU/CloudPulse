import { useEffect, useState } from "react";

import {
    Thermometer,
    Droplets,
    Battery,
    Bell,
    Cpu,
    Database,
} from "lucide-react";

import Header from "../components/Header";
import MetricCard from "../components/MetricCard";
import SectionCard from "../components/SectionCard";

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

        }

        catch (err) {

            console.error(err);

        }

    }

    const latest = readings.length ? readings[0] : null;

    return (

        <div className="min-h-screen bg-slate-950">

            <Header />

            <div className="max-w-7xl mx-auto p-8">

                {/* KPI Cards */}

                <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-6 mb-8">

                    <MetricCard
                        title="Temperature"
                        value={latest ? latest.temperature : "--"}
                        unit="°C"
                        color="bg-red-500/20"
                        icon={<Thermometer className="text-red-400" />}
                    />

                    <MetricCard
                        title="Humidity"
                        value={latest ? latest.humidity : "--"}
                        unit="%"
                        color="bg-blue-500/20"
                        icon={<Droplets className="text-blue-400" />}
                    />

                    <MetricCard
                        title="Battery"
                        value={latest ? latest.battery : "--"}
                        unit="%"
                        color="bg-green-500/20"
                        icon={<Battery className="text-green-400" />}
                    />

                    <MetricCard
                        title="Devices"
                        value={devices.length}
                        unit=""
                        color="bg-cyan-500/20"
                        icon={<Cpu className="text-cyan-400" />}
                    />

                    <MetricCard
                        title="Readings"
                        value={readings.length}
                        unit=""
                        color="bg-purple-500/20"
                        icon={<Database className="text-purple-400" />}
                    />

                    <MetricCard
                        title="Alerts"
                        value={alerts.length}
                        unit=""
                        color="bg-yellow-500/20"
                        icon={<Bell className="text-yellow-400" />}
                    />

                </div>

                {/* Tables */}

                <div className="grid xl:grid-cols-2 gap-6">

                    <SectionCard title="Latest Readings">

                        <table className="w-full text-left">

                            <thead>

                                <tr className="border-b border-slate-700">

                                    <th className="pb-3">Device</th>
                                    <th>Temp</th>
                                    <th>Humidity</th>
                                    <th>Battery</th>

                                </tr>

                            </thead>

                            <tbody>

                                {readings.slice(0,8).map((reading)=>(

                                    <tr
                                        key={reading.id}
                                        className="border-b border-slate-800 hover:bg-slate-700/20"
                                    >

                                        <td className="py-3">
                                            {reading.device_id}
                                        </td>

                                        <td>
                                            {reading.temperature}°C
                                        </td>

                                        <td>
                                            {reading.humidity}%
                                        </td>

                                        <td>
                                            {reading.battery}%
                                        </td>

                                    </tr>

                                ))}

                            </tbody>

                        </table>

                    </SectionCard>

                    <SectionCard title="Recent Alerts">

                        {alerts.length===0 && (

                            <p className="text-slate-400">

                                No alerts.

                            </p>

                        )}

                        {alerts.slice(0,8).map((alert)=>(

                            <div
                                key={alert.id}
                                className="flex justify-between items-center border-b border-slate-700 py-4"
                            >

                                <div>

                                    <p className="font-semibold">

                                        {alert.message}

                                    </p>

                                    <p className="text-sm text-slate-400">

                                        Device {alert.device_id}

                                    </p>

                                </div>

                                <span
                                    className={`px-3 py-1 rounded-full text-sm font-semibold ${
                                        alert.severity==="HIGH"
                                            ? "bg-red-600"
                                            : "bg-yellow-600"
                                    }`}
                                >

                                    {alert.severity}

                                </span>

                            </div>

                        ))}

                    </SectionCard>

                </div>

            </div>

        </div>

    );

}