import {
    LineChart,
    Line,
    XAxis,
    YAxis,
    CartesianGrid,
    Tooltip,
    ResponsiveContainer,
} from "recharts";

export default function TemperatureChart({ readings }) {

    const data = [...readings]
        .slice(0, 15)
        .reverse()
        .map((reading) => ({
            time: reading.id,
            temperature: reading.temperature,
        }));

    return (

        <div className="h-80">

            <ResponsiveContainer width="100%" height="100%">

                <LineChart data={data}>

                    <CartesianGrid strokeDasharray="3 3" stroke="#334155"/>

                    <XAxis dataKey="time"/>

                    <YAxis/>

                    <Tooltip/>

                    <Line
                        type="monotone"
                        dataKey="temperature"
                        stroke="#06b6d4"
                        strokeWidth={3}
                        dot={false}
                    />

                </LineChart>

            </ResponsiveContainer>

        </div>

    );

}