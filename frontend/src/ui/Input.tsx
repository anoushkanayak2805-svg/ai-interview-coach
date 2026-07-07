const Input = ({
    label,
    type = "text",
    placeholder,
    value,
    onChange,
}) => {
    return (
        <div className="mb-4">
            <label className="block mb-2 text-sm font-medium">
                {label}
            </label>

            <input
                type={type}
                placeholder={placeholder}
                value={value}
                onChange={onChange}
                className="w-full border rounded-lg px-4 py-3 focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
        </div>
    );
};

export default Input;