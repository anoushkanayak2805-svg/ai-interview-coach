import type { ReactNode } from "react";

interface CardProps {
  children: ReactNode;
}

const Card = ({ children }: CardProps) => {
  return (
    <div className="rounded-xl bg-white p-8 shadow-lg">
      {children}
    </div>
  );
};

export default Card;