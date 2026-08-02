export default function SectionCard({
    title,
    children,
}) {
    return (
        <div className="bg-slate-800 rounded-xl p-6 border border-slate-700 shadow-lg">

            <h2 className="text-xl font-semibold mb-5 text-white">
                {title}
            </h2>

            {children}

        </div>
    );
}