import { CheckCircle } from "lucide-react";

export default function DeviceStatus({ devices }) {
    return (
        <div className="space-y-4">

            {devices.map((device) => (

                <div
                    key={device.id}
                    className="flex justify-between items-center bg-slate-800 rounded-lg p-4 border border-slate-700"
                >

                    <div>

                        <h3 className="font-semibold text-white">
                            {device.name}
                        </h3>

                        <p className="text-sm text-slate-400">
                            Device ID: {device.id}
                        </p>

                    </div>

                    <div className="flex items-center gap-2">

                        <CheckCircle
                            size={18}
                            className="text-green-400"
                        />

                        <span className="text-green-400 font-medium">
                            Online
                        </span>

                    </div>

                </div>

            ))}

        </div>
    );
}