import { NextApiRequest, NextApiResponse } from 'next';
import { Answer } from '../../interfaces/answer';
import { company_sizes, creative_sizes, accounting_sizes, it_sizes } from "../../utils/sample-data";


const handler = (_req: NextApiRequest, res: NextApiResponse) => {
    const { method, body } = _req;

    const answer: Answer = body;

    console.log("Recevied request at /api/quantify")

    const QuantifyAnswer = (answer: Answer) => {
        const com = company_sizes.indexOf(answer.company_size) + 1
        const acc = accounting_sizes.indexOf(answer.accounting_size) + 1
        const cre = creative_sizes.indexOf(answer.creative_size) + 1
        const it = it_sizes.indexOf(answer.it_size) + 1

        const ans_value = (com * 90) + (acc * 20) + (cre * 20) + (it * 20)
        return ans_value;
    }

    res.status(200).send({
        answer: answer,
        value: QuantifyAnswer(answer)
    })

    return

}

export default handler;