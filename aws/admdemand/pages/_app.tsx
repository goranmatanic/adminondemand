import Link from 'next/link'
import Layout from '../components/Layout'
import Survey from '../components/Survey'
import { surveyQuestions } from '../utils/sample-data'
import '../styles/globals.css'
import 'tailwindcss/tailwind.css';


const IndexPage = () => (
    <Layout title="AdminOn Demand">
        <h1 className="text-3xl font-bold text-center">AdminOn Demand</h1>
        <Survey questions={surveyQuestions.questions} onSubmit={surveyQuestions.onSubmit} />
    </Layout>
)

export default IndexPage
