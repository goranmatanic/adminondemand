import React from 'react';

interface int_Element {
    name: string;
    price: number;
    url: string;
}

const Element: React.FC<int_Element> = ({ name, price, url }) => {
    return (
        <div className="border rounded p-4">
            <h2 className="font-bold text-2xl">{name}</h2>
            <p className="text-xl font-bold">Price: ${price}</p>
            <a className="text-blue-500 underline" href={url}>View Service</a>
        </div>
    );
};

export default Element;
