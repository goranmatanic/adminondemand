import React, { useState } from 'react';
import { Question } from '../interfaces/survey';

const Survey = () => {
    const [currentPage, setCurrentPage] = useState(0);
    const [answers, setAnswers] = useState([]);
    var questions: Question[] = [
        {
            text: "Kaj ima",
            choices: ["Nema nis", "Ima svasta"]
        }
    ];

    const getQuestions = async () => {
        // Query /api/questions
    }

    const handleAnswer = (answer) => {
        setAnswers([...answers, answer]);
    };

    const handlePrevPage = () => {
        setCurrentPage(currentPage - 1);
    };

    const handleSubmit = () => {
        // Submit answers to server or save to local storage
        if (currentPage + 1 == questions.length) {
            console.log("Submit to backend: " + JSON.stringify(answers, null, 4))
        } else {
            setCurrentPage(currentPage + 1);
        }
    };

    const currentQuestion = questions[currentPage];
    return (
        <div className="w-full max-w-lg mx-auto mt-8 p-4 text-center">
            <h1 className="mb-4 font-bold text-2xl">{currentQuestion.text}</h1>
            <div className="column">
                {currentQuestion.choices.map((choice) => (
                    <div key={choice} className="mb-4">
                        <input
                            type="radio"
                            name="choice"
                            id={choice}
                            value={choice}
                            onChange={() => handleAnswer(choice)}
                        />
                        <label className="font-bold text-lg" htmlFor={choice}>
                            {choice}
                        </label>
                    </div>
                ))}
                <div className="mb-4 flex justify-between">
                    {currentPage > 0 && (
                        <button onClick={handlePrevPage} className="font-bold text-lg">
                            Prev
                        </button>
                    )}
                    {currentPage <= questions.length - 1 && (
                        <button
                            onClick={handleSubmit}
                            className="font-bold text-lg px-4 py-2 rounded-full bg-blue-500 text-white float-right"
                        >
                            Submit
                        </button>
                    )}
                </div>
            </div>
        </div>
    );
};

export default Survey;
