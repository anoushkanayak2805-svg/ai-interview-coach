export default function LoadingSkeleton() {
  return (
    <div className="animate-pulse">

      <div className="h-64 rounded-3xl bg-slate-200"></div>

      <div className="mt-8 grid grid-cols-4 gap-6">

        {[1,2,3,4].map((i)=>(
          <div
            key={i}
            className="h-36 rounded-2xl bg-slate-200"
          />
        ))}

      </div>

    </div>
  );
}