interface Props {
  message: string;
}

export default function ErrorCard({ message }: Props) {
  return (
    <div className="rounded-xl border border-red-200 bg-red-50 p-6 text-red-700">
      {message}
    </div>
  );
}