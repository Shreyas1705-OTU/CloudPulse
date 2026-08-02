export default function SectionCard({
    title,
    children,
}) {
    return (
        <div className="bg-slate-800 rounded-xl border border-slate-700 shadow-lg p-6">

            <h2 className="text-xl font-semibold text-white mb-5">
                {title}
            </h2>

            {children}

        </div>
    );
}