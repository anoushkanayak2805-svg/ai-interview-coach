const Button = ({
    children,
    type = "button",
    onClick,
    className = "",
    disabled = false,
}) => {
    return (
        <button
            type={type}
            onClick={onClick}
            disabled={disabled}
            className={`w-full bg-blue-600 hover:bg-blue-700 transition text-white py-3 rounded-lg font-semibold disabled:opacity-50 ${className}`}
        >
            {children}
        </button>
    );
};

export default Button;