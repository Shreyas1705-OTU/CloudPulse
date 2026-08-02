import {
    AreaChart,
    Area,
    XAxis,
    YAxis,
    CartesianGrid,
    Tooltip,
    ResponsiveContainer,
} from "recharts";

export default function HumidityChart({ readings }) {

    const data = [...readings]
        .slice(0,15)
        .reverse()
        .map((reading)=>({

            time:reading.id,

            humidity:reading.humidity,

        }));

    return(

        <div className="h-80">

            <ResponsiveContainer>

                <AreaChart data={data}>

                    <CartesianGrid stroke="#334155"/>

                    <XAxis dataKey="time"/>

                    <YAxis/>

                    <Tooltip/>

                    <Area
                        dataKey="humidity"
                        stroke="#3b82f6"
                        fill="#2563eb"
                    />

                </AreaChart>

            </ResponsiveContainer>

        </div>

    );

}