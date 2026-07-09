import type {
  ChangeEventHandler,
  HTMLInputTypeAttribute,
} from "react";

interface InputProps {
  label: string;
  type?: HTMLInputTypeAttribute;
  placeholder?: string;
  value?: string | number;
  onChange?: ChangeEventHandler<HTMLInputElement>;
}

const Input = ({
  label,
  type = "text",
  placeholder = "",
  value = "",
  onChange,
}: InputProps) => {
  return (
    <div className="mb-4">
      <label className="mb-2 block text-sm font-medium">
        {label}
      </label>

      <input
        type={type}
        placeholder={placeholder}
        value={value}
        onChange={onChange}
        className="w-full rounded-lg border px-4 py-3 focus:outline-none focus:ring-2 focus:ring-blue-500"
      />
    </div>
  );
};

export default Input;