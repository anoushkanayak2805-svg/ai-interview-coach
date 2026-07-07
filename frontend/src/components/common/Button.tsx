type Props = {
  children: React.ReactNode;
  loading?: boolean;
} & React.ButtonHTMLAttributes<HTMLButtonElement>;

export default function Button({
  children,
  loading,
  ...props
}: Props) {
  return (
    <button
      {...props}
      disabled={loading}
      className="w-full rounded-lg bg-blue-600 py-3 text-white font-semibold hover:bg-blue-700 disabled:bg-gray-400"
    >
      {loading ? "Loading..." : children}
    </button>
  );
}