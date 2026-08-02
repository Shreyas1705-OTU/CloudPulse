export default function MetricCard({
    title,
    value,
    unit,
    icon,
    color,
}) {
    return (
        <div className="bg-slate-800 rounded-xl shadow-lg p-6 border border-slate-700 hover:border-cyan-500 transition-all">

            <div className="flex justify-between items-center">

                <div>

                    <p className="text-slate-400 text-sm">
                        {title}
                    </p>

                    <h2 className="text-3xl font-bold mt-2 text-white">
                        {value}
                        <span className="text-lg ml-1">
                            {unit}
                        </span>
                    </h2>

                </div>

                <div
                    className={`p-3 rounded-lg ${color}`}
                >
                    {icon}
                </div>

            </div>

        </div>
    );
}