import React, { useState } from 'react';
import { SurveyProps } from '../interfaces/survey';
import Element from './Recommendation';
import Recommendation from '../interfaces/recommendation';

const Survey: React.FC<SurveyProps> = ({ questions, onSubmit }) => {
    const [answers, setAnswers] = useState<string[]>([]);
    const [name, setName] = useState('');
    const [recommendations, setRecommendations] = useState<Recommendation[]>([]);
    var renderedRecommendations;

    const handleOptionChange = (index: number) => (event: React.ChangeEvent<HTMLInputElement>) => {
        const updatedAnswers = [...answers];
        updatedAnswers[index] = event.target.value;
        setAnswers(updatedAnswers);
    };

    const handleNameChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        setName(event.target.value);
    };

    const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
        event.preventDefault();

        const submitToSurvey = async () => {
            const response = await fetch('/api/survey', {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ name, answers })
            });

            const data = await response.json()

            const rcmds: Recommendation[] = []

            data['recommendation'].forEach(rcmd => {
                const newRecom: Recommendation = {
                    name: rcmd.name,
                    url: rcmd.url,
                    price: rcmd.price,
                    abs: rcmd.abs
                }
                rcmds.push(newRecom)
            });
            setRecommendations((vals) => {
                return [...rcmds];
            })
        }

        submitToSurvey()
    };

    if (recommendations.length > 0) {
        renderedRecommendations = Object.values(recommendations).map(rcm => {
            return (
                <>
                    <>Recommendations</>
                    <Element name={rcm.name} url={rcm.url} price={rcm.price} />
                </>
            )
        })
    };

    return (
        <form className="w-full max-w-lg bg-gray-200 rounded-lg p-4 mx-auto mt-8" onSubmit={handleSubmit}>
            <div className="mb-4 flex items-center">
                <label htmlFor="name" className="mr-2 font-bold text-lg">
                    Please state your name:
                </label>
                <input
                    id="name"
                    className="border py-2 px-3 leading-tight"
                    type="text"
                    value={name}
                    onChange={handleNameChange}
                />
            </div>
            <div className="flex">
                <div className="mx-auto mt-8 w-full max-w-lg ml-12">
                    {questions.map((question, index) => (
                        <div key={question.text} className="mb-4">
                            <p className="text-lg font-bold mb-2 text-center">{question.text}</p>
                            {question.options.map(option => (
                                <div key={option} className="mb-2">
                                    <label className="block cursor-pointer">
                                        <input
                                            className="mr-2 leading-tight ml-6"
                                            type="radio"
                                            value={option}
                                            checked={answers[index] === option}
                                            onChange={handleOptionChange(index)}
                                        />
                                        <span className="text-sm">{option}</span>
                                    </label>
                                </div>
                            ))}
                        </div>
                    ))}
                </div>
                <div className="w-1/2 pl-4">
                    <div className="mb-4 flex items-right">
                        {renderedRecommendations}
                    </div>
                </div>
            </div>
            <button className="ml-16 px-4 py-2 font-bold text-white bg-blue-500 rounded-full hover:bg-blue-700 focus:outline-none focus:shadow-outline-blue active:bg-blue-800" type="submit">
                Submit
            </button>
        </form >
    );
}

export default Survey;