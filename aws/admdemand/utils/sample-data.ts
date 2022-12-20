import { User } from '../interfaces'
import { SurveyProps } from '../interfaces/survey'

/** Dummy user data. */
export const sampleUserData: User[] = [
  { id: 101, name: 'Alice' },
  { id: 102, name: 'Bob' },
  { id: 103, name: 'Caroline' },
  { id: 104, name: 'Dave' },
]

export var http_host;

if (process.env.ENVIRONMENT == "dev") {
  http_host = "http://localhost:3000"
} else if (process.env.ENVIRONMENT == "prod") {
  http_host = "https://adminon-demand.vercel.app"
}

export const ENV_VARIABLE = process.env.ENVIRONMENT

export const surveyQuestions: SurveyProps = {
  questions: [{
    text: "What is the size of your company",
    options: ["1-5", "6 - 50", "51 - 250", ">250",],
  }, {
    text: "How many people do you have working in accounting?",
    options: ["0", "1-5", "6 - 50", "51 - 250", ">250"],
  }, {
    text: "How many people do you have working in creative?",
    options: ["0", "1-5", "6 - 50", "51 - 250", ">250"],
  }, {
    text: "How many people do you have working in IT?",
    options: ["0", "1-5", "6 - 50", "51 - 250", ">250"],
  }
  ],
  onSubmit: ((answers) => { console.log(answers) })
}

export const company_sizes: string[] = ["1-5", "6 - 50", "51 - 250", ">250"]
export const accounting_sizes: string[] = ["0", "1-5", "6 - 50", "51 - 250", ">250"]
export const creative_sizes: string[] = ["0", "1-5", "6 - 50", "51 - 250", ">250"]
export const it_sizes: string[] = ["0", "1-5", "6 - 50", "51 - 250", ">250"]