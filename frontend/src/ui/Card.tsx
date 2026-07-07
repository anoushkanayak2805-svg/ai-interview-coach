const Card = ({ children }) => {
    return (
        <div className="bg-white rounded-xl shadow-lg p-8">
            {children}
        </div>
    );
};

export default Card;