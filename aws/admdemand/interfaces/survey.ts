interface SurveyQuestion {
    id: number,
    question: string,
    answers: string[];
}

export interface Question {
    text: string;
    options: string[];
}

export interface SurveyProps {
    questions: Question[];
    onSubmit: (answers: string[]) => void;
}

export default SurveyQuestion;