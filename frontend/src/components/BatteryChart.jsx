import {
    BarChart,
    Bar,
    XAxis,
    YAxis,
    Tooltip,
    CartesianGrid,
    ResponsiveContainer,
} from "recharts";

export default function BatteryChart({ readings }) {

    const data=[...readings]
    .slice(0,15)
    .reverse()
    .map((reading)=>({

        time:reading.id,

        battery:reading.battery,

    }));

    return(

        <div className="h-80">

            <ResponsiveContainer>

                <BarChart data={data}>

                    <CartesianGrid stroke="#334155"/>

                    <XAxis dataKey="time"/>

                    <YAxis/>

                    <Tooltip/>

                    <Bar
                        dataKey="battery"
                        fill="#22c55e"
                    />

                </BarChart>

            </ResponsiveContainer>

        </div>

    );

}